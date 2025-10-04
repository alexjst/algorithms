from flask import Flask, render_template, request, redirect, url_for, jsonify
import yaml
import json
from datetime import datetime, timedelta
import os
import random
import requests

app = Flask(__name__)

# Add JSON filter for templates
def tojsonfilter(value):
    return json.dumps(value)

app.jinja_env.filters['tojsonfilter'] = tojsonfilter

# LeetCode API Configuration
LEETCODE_API_BASE = "https://alfa-leetcode-api.onrender.com"

# Mapping from curriculum topics to LeetCode tags
TOPIC_TO_LEETCODE_TAGS = {
    "Two Pointers": ["two-pointers"],
    "Sliding Window": ["sliding-window"],
    "Binary Search": ["binary-search"],
    "DFS Fundamentals": ["depth-first-search", "tree", "binary-tree"],
    "BFS Fundamentals": ["breadth-first-search", "tree", "binary-tree"],
    "Dynamic Programming": ["dynamic-programming"],
    "Advanced DFS": ["depth-first-search", "tree", "graph"],
    "Advanced DP": ["dynamic-programming"],
    "Greedy Algorithms": ["greedy"],
    "Backtracking": ["backtracking"],
    "Advanced Backtracking": ["backtracking"],
    "Interval Problems": ["array", "sorting"],
    "Heap Operations": ["heap-priority-queue"],
    "Priority Queues": ["heap-priority-queue"],
    "Union-Find": ["union-find"],
    "Trie Operations": ["trie"],
    "Advanced Trie": ["trie"],
    "Matrix Traversal": ["matrix", "array"],
    "Special Algorithms": ["math", "bit-manipulation"],
    "Monotonic Stack": ["stack", "monotonic-stack"],
    "Topological Sort": ["topological-sort", "graph"],
    "Graph Algorithms": ["graph"],
    "Advanced Graph": ["graph"]
}

# Configuration
DATA_DIR = "data"
CURRICULUM_DIR = f"{DATA_DIR}/curriculum"
PROGRESS_FILE = f"{DATA_DIR}/progress.json"
REVIEWS_FILE = f"{DATA_DIR}/reviews.json"
CONFIG_FILE = f"{DATA_DIR}/config.json"
TIMER_FILE = f"{DATA_DIR}/timer_state.json"

def load_config():
    """Load configuration from config.json"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default configuration
        default_config = {
            "study_plan": {
                "coding": {"start_date": datetime.now().strftime('%Y-%m-%d'), "active": True},
                "system_design": {"start_date": datetime.now().strftime('%Y-%m-%d'), "active": True}
            },
            "settings": {"review_intervals": [1, 3, 7, 14], "timezone": "UTC"}
        }
        save_json_data(CONFIG_FILE, default_config)
        return default_config

# Load configuration
config = load_config()
REVIEW_INTERVALS = config['settings']['review_intervals']

def load_curriculum(track):
    """Load curriculum from YAML file"""
    with open(f"{CURRICULUM_DIR}/{track}.yaml", 'r') as f:
        return yaml.safe_load(f)

def load_json_data(filename):
    """Load data from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_json_data(filename, data):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def get_day_number(track):
    """Calculate current day number (1-28) based on configured start date for track and acceleration"""
    config = load_config()
    track_config = config['study_plan'][track]
    start_date_str = track_config['start_date']
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()

    # Get acceleration offset (defaults to 0 for backward compatibility)
    acceleration_days = track_config.get('acceleration_days', 0)

    today = datetime.now().date()
    days_elapsed = (today - start_date).days + 1 + acceleration_days
    return max(1, min(28, days_elapsed))

def get_topic_for_day(track, day):
    """Get the topic scheduled for a specific day"""
    curriculum = load_curriculum(track)

    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            if day_info['day'] == day:
                return day_info
    return None

def get_due_reviews(date_str):
    """Get all reviews due on a specific date"""
    reviews_data = load_json_data(REVIEWS_FILE)
    due_reviews = []

    for review in reviews_data.get('scheduled_reviews', []):
        if review['due_date'] == date_str and not review.get('completed_date'):
            due_reviews.append(review)

    return due_reviews

def get_topic_problems(topic, track):
    """Get practice problems for a specific topic"""
    curriculum = load_curriculum(track)

    # Search through all weeks and days to find the matching topic
    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            if day_info.get('topic') == topic:
                return day_info.get('problems', [])

    return []

def get_system_design_practice_questions(topic, track):
    """Get practice questions for a system design topic"""
    if track != 'system_design':
        return {}

    curriculum = load_curriculum(track)

    # Search through all weeks and days to find the matching topic
    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            if day_info.get('topic') == topic:
                practice_questions = day_info.get('practice_questions', {})

                # Handle both old and new question formats
                return {
                    'estimation': practice_questions.get('estimation', practice_questions.get('capacity_estimation', [])),
                    'concepts': practice_questions.get('concepts', practice_questions.get('conceptual', [])),
                    'tradeoffs': practice_questions.get('tradeoffs', practice_questions.get('architecture_decisions', [])),
                    'scenarios': practice_questions.get('scenarios', [])
                }

    return {}

def select_review_questions(topic, track, review_type):
    """Select appropriate questions for a review session based on type and difficulty"""
    if track != 'system_design':
        return []

    all_questions = get_system_design_practice_questions(topic, track)

    # Define question counts based on review type
    question_counts = {
        '1-day': {'estimation': 1, 'concepts': 1, 'scenarios': 1},   # 3 questions, quick review
        '3-day': {'estimation': 2, 'concepts': 2, 'tradeoffs': 1},  # 5 questions, moderate review
        '7-day': {'estimation': 2, 'concepts': 2, 'tradeoffs': 1, 'scenarios': 1},  # 6 questions, comprehensive
        '14-day': {'estimation': 3, 'concepts': 3, 'tradeoffs': 2, 'scenarios': 2}  # 10 questions, full assessment
    }

    import random
    selected_questions = []
    counts = question_counts.get(review_type, question_counts['3-day'])

    for question_type, count in counts.items():
        available_questions = all_questions.get(question_type, [])
        if available_questions:
            # Randomly select questions of this type
            selected = random.sample(available_questions, min(count, len(available_questions)))
            for question_text in selected:
                selected_questions.append({
                    'type': question_type,
                    'question': question_text,
                    'id': f"{question_type}_{len(selected_questions)}"
                })

    return selected_questions

def get_time_benchmarks(problems):
    """Calculate time benchmarks for problems based on difficulty"""
    # Base time expectations in minutes
    base_times = {
        'Easy': 17.5,    # 15-20 minutes
        'Medium': 30,    # 25-35 minutes
        'Hard': 50,      # 40-60 minutes
        'Mixed': 35      # Average for mixed problems
    }

    total_base_time = 0
    for problem in problems:
        difficulty = problem.get('difficulty', 'Medium')
        total_base_time += base_times.get(difficulty, base_times['Medium'])

    # Rating performance multipliers
    return {
        'total_base_minutes': total_base_time,
        'rating_benchmarks': {
            5: {'max_minutes': total_base_time * 0.7, 'description': 'Perfect (60-70% of base time)'},
            4: {'max_minutes': total_base_time * 1.0, 'description': 'Good (80-100% of base time)'},
            3: {'max_minutes': total_base_time * 1.5, 'description': 'Okay (100-150% of base time)'},
            2: {'max_minutes': total_base_time * 2.5, 'description': 'Poor (150-250% of base time)'},
            1: {'max_minutes': 999999, 'description': 'Forgot (250%+ or unable to solve)'}
        }
    }

def calculate_performance_rating(actual_minutes, benchmarks):
    """Calculate suggested rating based on performance time"""
    for rating in [5, 4, 3, 2, 1]:
        if actual_minutes <= benchmarks['rating_benchmarks'][rating]['max_minutes']:
            return rating
    return 1  # Fallback

def get_system_design_benchmarks(questions, review_type):
    """Calculate time benchmarks for system design questions"""
    # Base time per question type (minutes)
    base_times = {
        'estimation': 5,    # Quick calculations
        'concepts': 8,      # Thoughtful explanations
        'tradeoffs': 10,    # Comparative analysis
        'scenarios': 15     # System design scenarios
    }

    total_base_time = 0
    for question in questions:
        question_type = question.get('type', 'concepts')
        total_base_time += base_times.get(question_type, base_times['concepts'])

    # Adjust total time based on review type complexity
    complexity_multipliers = {
        '1-day': 0.8,   # Quick refresher
        '3-day': 1.0,   # Standard pace
        '7-day': 1.2,   # More thorough
        '14-day': 1.5   # Comprehensive review
    }

    multiplier = complexity_multipliers.get(review_type, 1.0)
    total_base_time = total_base_time * multiplier

    # Rating performance thresholds
    return {
        'total_base_minutes': total_base_time,
        'question_count': len(questions),
        'rating_benchmarks': {
            5: {'max_minutes': total_base_time * 0.7, 'description': 'Expert (≤70% of base time)'},
            4: {'max_minutes': total_base_time * 1.0, 'description': 'Good (≤100% of base time)'},
            3: {'max_minutes': total_base_time * 1.5, 'description': 'Moderate (≤150% of base time)'},
            2: {'max_minutes': total_base_time * 2.0, 'description': 'Struggled (≤200% of base time)'},
            1: {'max_minutes': 999999, 'description': 'Incomplete (200%+ or unable to complete)'}
        }
    }

def calculate_system_design_rating(session_data, benchmarks):
    """Calculate suggested rating based on system design practice performance"""
    time_minutes = session_data.get('total_time', 0)
    answers = session_data.get('answers', {})
    questions = session_data.get('questions', [])

    # Time performance score (0-1)
    time_score = 1.0
    for rating in [5, 4, 3, 2, 1]:
        if time_minutes <= benchmarks['rating_benchmarks'][rating]['max_minutes']:
            time_score = rating / 5.0
            break

    # Answer completeness score (0-1)
    completeness_score = 0.0
    if questions:
        answered_count = len([q for q in questions if answers.get(q['id'], '').strip()])
        completeness_score = answered_count / len(questions)

    # Self-assessment modifier from user's own evaluation
    self_assessment = session_data.get('self_assessment', {})
    coverage_score = 0.0
    if self_assessment:
        covered_concepts = len([k for k, v in self_assessment.items() if v])
        total_concepts = len(self_assessment)
        coverage_score = covered_concepts / total_concepts if total_concepts > 0 else 0.5

    # Combined score with weights
    final_score = (
        time_score * 0.3 +           # 30% time performance
        completeness_score * 0.4 +   # 40% answer completeness
        coverage_score * 0.3         # 30% concept coverage
    )

    # Convert to 1-5 rating
    if final_score >= 0.9: return 5
    elif final_score >= 0.75: return 4
    elif final_score >= 0.6: return 3
    elif final_score >= 0.4: return 2
    else: return 1

def schedule_reviews(topic, track, completed_date):
    """Schedule spaced repetition reviews for a completed topic"""
    reviews_data = load_json_data(REVIEWS_FILE)
    if 'scheduled_reviews' not in reviews_data:
        reviews_data['scheduled_reviews'] = []

    base_date = datetime.strptime(completed_date, '%Y-%m-%d').date()

    for interval in REVIEW_INTERVALS:
        review_date = base_date + timedelta(days=interval)
        review = {
            'topic': topic,
            'track': track,
            'review_type': f'{interval}-day',
            'due_date': review_date.strftime('%Y-%m-%d'),
            'scheduled_date': completed_date,
            'completed_date': None
        }
        reviews_data['scheduled_reviews'].append(review)

    save_json_data(REVIEWS_FILE, reviews_data)

def load_timer_state():
    """Load timer state from JSON file"""
    try:
        with open(TIMER_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            'active': False,
            'paused': False,
            'start_time': None,
            'pause_time': None,
            'duration': None,
            'remaining': None,
            'track': None,
            'topic': None,
            'last_updated': None,
            'total_pause_duration': 0
        }

def save_timer_state(timer_state):
    """Save timer state to JSON file"""
    timer_state['last_updated'] = datetime.now().isoformat()
    with open(TIMER_FILE, 'w') as f:
        json.dump(timer_state, f, indent=2)

def get_current_timer_state():
    """Get current timer state with real-time calculations"""
    timer_state = load_timer_state()

    # Migrate old timer states to include total_pause_duration
    if 'total_pause_duration' not in timer_state:
        timer_state['total_pause_duration'] = 0

    if not timer_state['active']:
        return timer_state

    now = datetime.now()

    if timer_state['paused'] and timer_state['pause_time']:
        # Timer is paused - return last known remaining time
        return timer_state
    elif timer_state['start_time']:
        # Timer is running - calculate remaining time
        start_time = datetime.fromisoformat(timer_state['start_time'])
        elapsed = (now - start_time).total_seconds()

        # Subtract any pause duration if timer was paused
        if timer_state.get('total_pause_duration'):
            elapsed -= timer_state['total_pause_duration']

        remaining = max(0, timer_state['duration'] - elapsed)
        timer_state['remaining'] = remaining

        # Auto-complete if time is up
        if remaining <= 0:
            timer_state['active'] = False
            timer_state['completed'] = True
            save_timer_state(timer_state)

    return timer_state

@app.route('/')
def dashboard():
    """Main dashboard showing today's agenda"""
    today = datetime.now().date().strftime('%Y-%m-%d')

    # Get current day for each track (they can have different start dates)
    coding_day = get_day_number('coding')
    system_design_day = get_day_number('system_design')

    # Get today's new learning
    coding_topic = get_topic_for_day('coding', coding_day)
    system_design_topic = get_topic_for_day('system_design', system_design_day)

    # Check if topics are already completed today
    progress_data = load_json_data(PROGRESS_FILE)
    coding_topic_completed = False
    system_design_topic_completed = False
    coding_completion_data = None
    system_design_completion_data = None

    for completion in progress_data.get('completions', []):
        if completion['date'] == today:
            if completion['track'] == 'coding' and coding_topic and completion['topic'] == coding_topic['topic']:
                coding_topic_completed = True
                coding_completion_data = completion
            elif completion['track'] == 'system_design' and system_design_topic and completion['topic'] == system_design_topic['topic']:
                system_design_topic_completed = True
                system_design_completion_data = completion

    # Get due reviews and enhance with problems and benchmarks
    due_reviews = get_due_reviews(today)

    # Enhance each review with practice problems and time benchmarks
    for review in due_reviews:
        if review['track'] == 'coding':
            # Coding reviews: use LeetCode problems
            problems = get_topic_problems(review['topic'], review['track'])
            review['problems'] = problems
            review['practice_questions'] = None
            if problems:
                review['benchmarks'] = get_time_benchmarks(problems)
            else:
                review['benchmarks'] = None
        elif review['track'] == 'system_design':
            # System design reviews: use practice questions
            practice_questions = select_review_questions(review['topic'], review['track'], review['review_type'])
            review['practice_questions'] = practice_questions
            review['problems'] = None
            if practice_questions:
                review['benchmarks'] = get_system_design_benchmarks(practice_questions, review['review_type'])
            else:
                review['benchmarks'] = None
        else:
            review['problems'] = None
            review['practice_questions'] = None
            review['benchmarks'] = None

    # Calculate total time estimate
    total_time = 0
    if coding_topic and not coding_topic_completed:
        total_time += coding_topic.get('time_estimate', 45)
    if system_design_topic and not system_design_topic_completed:
        total_time += system_design_topic.get('time_estimate', 45)

    # Add review time (estimated 10 min per review)
    total_time += len(due_reviews) * 10

    return render_template('dashboard.html',
                         today=today,
                         current_day=max(coding_day, system_design_day),
                         coding_topic=coding_topic,
                         system_design_topic=system_design_topic,
                         coding_topic_completed=coding_topic_completed,
                         system_design_topic_completed=system_design_topic_completed,
                         coding_completion_data=coding_completion_data,
                         system_design_completion_data=system_design_completion_data,
                         due_reviews=due_reviews,
                         total_time=total_time,
                         active_page='dashboard')

@app.route('/complete', methods=['POST'])
def mark_complete():
    """Mark a topic or review as complete"""
    data = request.get_json()
    topic = data['topic']
    track = data['track']
    item_type = data.get('type', 'topic')  # 'topic' or 'review'
    rating = data.get('rating', 3)
    notes = data.get('notes', '')
    completed_on_time = data.get('completed_on_time', None)  # New field for timer tracking

    today = datetime.now().date().strftime('%Y-%m-%d')

    if item_type == 'topic':
        # Save completion to progress
        progress_data = load_json_data(PROGRESS_FILE)
        if 'completions' not in progress_data:
            progress_data['completions'] = []

        completion = {
            'date': today,
            'track': track,
            'topic': topic,
            'rating': rating,
            'notes': notes,
            'completed_on_time': completed_on_time,  # Add timer tracking
            'timestamp': datetime.now().isoformat()
        }
        progress_data['completions'].append(completion)
        save_json_data(PROGRESS_FILE, progress_data)

        # Schedule reviews
        schedule_reviews(topic, track, today)

    elif item_type == 'review':
        # Mark review as complete with optional timing data
        practice_time = data.get('practice_time')  # Total practice time in minutes
        problem_times = data.get('problem_times', [])  # Individual problem solve times
        suggested_rating = data.get('suggested_rating')  # Auto-calculated rating

        reviews_data = load_json_data(REVIEWS_FILE)
        for review in reviews_data.get('scheduled_reviews', []):
            if (review['topic'] == topic and
                review['track'] == track and
                review['due_date'] == today and
                not review.get('completed_date')):
                review['completed_date'] = today
                review['rating'] = rating
                review['notes'] = notes

                # Add performance timing data if available
                if practice_time:
                    review['practice_time'] = practice_time
                if problem_times:
                    review['problem_times'] = problem_times
                if suggested_rating:
                    review['suggested_rating'] = suggested_rating

                # Add system design specific data
                session_data = data.get('session_data')
                if session_data:
                    review['session_data'] = session_data
                break
        save_json_data(REVIEWS_FILE, reviews_data)

    return jsonify({'status': 'success'})

@app.route('/api/review-practice', methods=['POST'])
def get_review_practice_data():
    """Get practice problems and benchmarks for a review topic"""
    data = request.get_json()
    topic = data.get('topic')
    track = data.get('track')

    if not topic or not track:
        return jsonify({'error': 'Topic and track are required'}), 400

    problems = get_topic_problems(topic, track)
    if not problems:
        return jsonify({'error': 'No problems found for this topic'}), 404

    benchmarks = get_time_benchmarks(problems)

    return jsonify({
        'topic': topic,
        'track': track,
        'problems': problems,
        'benchmarks': benchmarks
    })

@app.route('/api/system-design-practice', methods=['POST'])
def get_system_design_practice_data():
    """Get practice questions and benchmarks for a system design review topic"""
    data = request.get_json()
    topic = data.get('topic')
    track = data.get('track')
    review_type = data.get('review_type', '3-day')
    use_cached = data.get('use_cached', False)  # Whether to use cached questions if available

    if not topic or track != 'system_design':
        return jsonify({'error': 'Valid system design topic required'}), 400

    # Create a unique key for this practice session
    session_key = f"{track}_{topic}_{review_type}".replace(' ', '_')

    practice_questions = None

    # If use_cached is True, try to get cached questions first
    if use_cached:
        practice_questions = data.get('cached_questions')

    # If no cached questions, generate new ones
    if not practice_questions:
        practice_questions = select_review_questions(topic, track, review_type)
        if not practice_questions:
            return jsonify({'error': 'No practice questions found for this topic'}), 404

    benchmarks = get_system_design_benchmarks(practice_questions, review_type)

    return jsonify({
        'topic': topic,
        'track': track,
        'review_type': review_type,
        'questions': practice_questions,
        'benchmarks': benchmarks,
        'session_key': session_key
    })

@app.route('/api/calculate-system-design-rating', methods=['POST'])
def calculate_sd_rating():
    """Calculate suggested rating based on system design practice session"""
    data = request.get_json()
    session_data = data.get('session_data', {})
    benchmarks = data.get('benchmarks', {})

    if not session_data or not benchmarks:
        return jsonify({'error': 'Session data and benchmarks required'}), 400

    suggested_rating = calculate_system_design_rating(session_data, benchmarks)

    return jsonify({
        'suggested_rating': suggested_rating,
        'performance_summary': {
            'total_time': session_data.get('total_time', 0),
            'questions_answered': len([q for q in session_data.get('questions', [])
                                     if session_data.get('answers', {}).get(q['id'], '').strip()]),
            'total_questions': len(session_data.get('questions', [])),
            'benchmark_time': benchmarks.get('total_base_minutes', 0)
        }
    })

@app.route('/history')
def history():
    """Show completion history and stats"""
    progress_data = load_json_data(PROGRESS_FILE)
    reviews_data = load_json_data(REVIEWS_FILE)

    # Get recent completions
    recent_completions = sorted(
        progress_data.get('completions', []),
        key=lambda x: x['date'],
        reverse=True
    )[:10]

    # Get completed reviews
    completed_reviews = [
        r for r in reviews_data.get('scheduled_reviews', [])
        if r.get('completed_date')
    ]

    # Calculate basic stats
    total_topics = len(progress_data.get('completions', []))
    total_reviews = len(completed_reviews)

    # Calculate streak (consecutive days with completions)
    streak = calculate_streak(progress_data.get('completions', []))

    return render_template('history.html',
                         recent_completions=recent_completions,
                         completed_reviews=completed_reviews[:10],
                         total_topics=total_topics,
                         total_reviews=total_reviews,
                         streak=streak,
                         active_page='history')

def calculate_streak(completions):
    """Calculate current completion streak"""
    if not completions:
        return 0

    # Group completions by date
    dates = set()
    for completion in completions:
        dates.add(completion['date'])

    # Count consecutive days, allowing for today to be missed
    # (since you might not have studied today yet)
    today = datetime.now().date()
    streak = 0
    current_date = today

    # If there's no activity today, start from yesterday
    if today.strftime('%Y-%m-%d') not in dates:
        current_date = today - timedelta(days=1)

    # Count backwards from the starting date
    while current_date.strftime('%Y-%m-%d') in dates:
        streak += 1
        current_date -= timedelta(days=1)

    return streak

@app.route('/config')
def config_page():
    """Configuration page for study plan settings"""
    config = load_config()
    return render_template('config.html', config=config, active_page='config')

@app.route('/update_config', methods=['POST'])
def update_config():
    """Update configuration settings"""
    config = load_config()

    # Update start dates
    if 'coding_start_date' in request.form:
        config['study_plan']['coding']['start_date'] = request.form['coding_start_date']
    if 'system_design_start_date' in request.form:
        config['study_plan']['system_design']['start_date'] = request.form['system_design_start_date']

    # Update active status
    config['study_plan']['coding']['active'] = 'coding_active' in request.form
    config['study_plan']['system_design']['active'] = 'system_design_active' in request.form

    save_json_data(CONFIG_FILE, config)
    return redirect(url_for('config_page'))

@app.route('/preview')
def preview():
    """Preview next few days"""
    coding_day = get_day_number('coding')
    system_design_day = get_day_number('system_design')
    preview_days = []

    for i in range(1, 4):  # Next 3 days
        coding_day_preview = coding_day + i
        system_design_day_preview = system_design_day + i

        coding_topic = get_topic_for_day('coding', coding_day_preview) if coding_day_preview <= 28 else None
        system_design_topic = get_topic_for_day('system_design', system_design_day_preview) if system_design_day_preview <= 28 else None

        if coding_topic or system_design_topic:
            preview_days.append({
                'day': max(coding_day_preview, system_design_day_preview),
                'date': (datetime.now().date() + timedelta(days=i)).strftime('%Y-%m-%d'),
                'coding': coding_topic,
                'system_design': system_design_topic
            })

    return render_template('preview.html', preview_days=preview_days, active_page='preview')

@app.route('/analytics')
def analytics():
    """Analytics dashboard with visualizations and insights"""
    progress_data = load_json_data(PROGRESS_FILE)
    reviews_data = load_json_data(REVIEWS_FILE)

    # Calculate analytics data
    analytics_data = calculate_analytics(progress_data, reviews_data)

    return render_template('analytics.html', **analytics_data, active_page='analytics')

@app.route('/curriculum')
def curriculum_editor():
    """Curriculum customization and editing page"""
    coding_curriculum = load_curriculum('coding')
    system_design_curriculum = load_curriculum('system_design')

    return render_template('curriculum.html',
                         coding_curriculum=coding_curriculum,
                         system_design_curriculum=system_design_curriculum,
                         active_page='curriculum')

@app.route('/api/curriculum/<track>', methods=['GET'])
def get_curriculum(track):
    """Get curriculum data for a specific track"""
    try:
        curriculum = load_curriculum(track)
        return jsonify(curriculum)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/curriculum/<track>/topic', methods=['POST'])
def add_topic(track):
    """Add a new topic to the curriculum"""
    try:
        data = request.get_json()
        curriculum = load_curriculum(track)

        # Find the appropriate week or create a new one
        week_name = data.get('week', 'week_5')  # Default to week 5 for custom content
        if week_name not in curriculum['weeks']:
            curriculum['weeks'][week_name] = []

        # Find next available day number
        all_days = []
        for week_days in curriculum['weeks'].values():
            all_days.extend([day.get('day', 0) for day in week_days])
        next_day = max(all_days, default=28) + 1

        # Create new topic
        new_topic = {
            'day': next_day,
            'topic': data['topic'],
            'activity': data['activity'],
            'time_estimate': int(data.get('time_estimate', 45)),
            'detailed_content': data.get('detailed_content', ''),
        }

        # Add track-specific fields
        if track == 'coding':
            new_topic['problems'] = data.get('problems', [])
        else:  # system_design
            new_topic['resources'] = data.get('resources', [])
            new_topic['concepts'] = data.get('concepts', [])

        curriculum['weeks'][week_name].append(new_topic)
        save_curriculum(track, curriculum)

        return jsonify({'success': True, 'topic': new_topic})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/curriculum/<track>/topic/<int:day>', methods=['PUT'])
def update_topic(track, day):
    """Update an existing topic"""
    try:
        data = request.get_json()
        curriculum = load_curriculum(track)

        # Check for duplicate day numbers if day is being changed
        new_day = data.get('day', day)
        if new_day != day:
            # Check if the new day number already exists
            existing_days = []
            for week_days in curriculum['weeks'].values():
                existing_days.extend([d.get('day') for d in week_days if d.get('day') != day])

            if new_day in existing_days:
                return jsonify({'error': f'Day {new_day} already exists. Please choose a different day number.'}), 400

        # Find and update the topic
        topic_found = False
        for week_name, days in curriculum['weeks'].items():
            for i, topic in enumerate(days):
                if topic.get('day') == day:
                    # Update topic fields
                    topic['topic'] = data.get('topic', topic.get('topic'))
                    topic['activity'] = data.get('activity', topic.get('activity'))
                    topic['time_estimate'] = int(data.get('time_estimate', topic.get('time_estimate', 45)))
                    topic['detailed_content'] = data.get('detailed_content', topic.get('detailed_content', ''))

                    # Update day number if provided
                    if 'day' in data:
                        topic['day'] = int(data['day'])

                    # Update track-specific fields
                    if track == 'coding':
                        topic['problems'] = data.get('problems', topic.get('problems', []))
                    else:  # system_design
                        topic['resources'] = data.get('resources', topic.get('resources', []))
                        topic['concepts'] = data.get('concepts', topic.get('concepts', []))

                    topic_found = True
                    break
            if topic_found:
                break

        if not topic_found:
            return jsonify({'error': 'Topic not found'}), 404

        save_curriculum(track, curriculum)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/curriculum/<track>/topic/<int:day>', methods=['DELETE'])
def delete_topic(track, day):
    """Delete a topic from the curriculum"""
    try:
        curriculum = load_curriculum(track)

        # Find and remove the topic
        topic_found = False
        for week_name, days in curriculum['weeks'].items():
            for i, topic in enumerate(days):
                if topic.get('day') == day:
                    days.pop(i)
                    topic_found = True
                    break
            if topic_found:
                break

        if not topic_found:
            return jsonify({'error': 'Topic not found'}), 404

        save_curriculum(track, curriculum)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def save_curriculum(track, curriculum_data):
    """Safely save curriculum data to YAML file"""
    filename = f"{CURRICULUM_DIR}/{track}.yaml"

    # Create backup
    backup_filename = f"{filename}.backup"
    if os.path.exists(filename):
        import shutil
        shutil.copy2(filename, backup_filename)

    # Save new data
    with open(filename, 'w') as f:
        yaml.dump(curriculum_data, f, default_flow_style=False, sort_keys=False, indent=2)

def calculate_analytics(progress_data, reviews_data):
    """Calculate comprehensive analytics from progress and review data"""
    completions = progress_data.get('completions', [])
    reviews = reviews_data.get('scheduled_reviews', [])

    # 1. Calendar Heatmap Data (GitHub-style)
    calendar_data = calculate_calendar_heatmap(completions, reviews)

    # 2. Performance by Topic
    topic_performance = calculate_topic_performance(completions, reviews)

    # 3. Review Success Rate
    review_analytics = calculate_review_analytics(reviews)

    # 4. Overall Statistics
    overall_stats = calculate_overall_stats(completions, reviews, calendar_data)

    # 5. Learning Trends
    learning_trends = calculate_learning_trends(completions)

    # 6. Timer-Based Performance Analytics
    timer_analytics = calculate_timer_analytics(completions)

    return {
        'calendar_data': calendar_data,
        'topic_performance': topic_performance,
        'review_analytics': review_analytics,
        'overall_stats': overall_stats,
        'learning_trends': learning_trends,
        'timer_analytics': timer_analytics
    }

def calculate_calendar_heatmap(completions, reviews):
    """Generate GitHub-style calendar heatmap data"""
    from datetime import datetime, timedelta
    import calendar

    # Get activity data for the last 365 days
    today = datetime.now().date()
    start_date = today - timedelta(days=364)  # 365 days including today

    activity_by_date = {}

    # Count completions per day
    for completion in completions:
        date = completion['date']
        if date not in activity_by_date:
            activity_by_date[date] = {'completions': 0, 'reviews': 0, 'total': 0}
        activity_by_date[date]['completions'] += 1
        activity_by_date[date]['total'] += 1

    # Count reviews per day
    for review in reviews:
        if review.get('completed_date'):
            date = review['completed_date']
            if date not in activity_by_date:
                activity_by_date[date] = {'completions': 0, 'reviews': 0, 'total': 0}
            activity_by_date[date]['reviews'] += 1
            activity_by_date[date]['total'] += 1

    # Generate calendar grid
    calendar_grid = []
    current_date = start_date

    while current_date <= today:
        date_str = current_date.strftime('%Y-%m-%d')
        activity = activity_by_date.get(date_str, {'completions': 0, 'reviews': 0, 'total': 0})

        calendar_grid.append({
            'date': date_str,
            'count': activity['total'],
            'completions': activity['completions'],
            'reviews': activity['reviews'],
            'weekday': current_date.weekday(),  # 0 = Monday
            'week': current_date.isocalendar()[1]
        })

        current_date += timedelta(days=1)

    return calendar_grid

def calculate_topic_performance(completions, reviews):
    """Calculate average performance by topic"""
    topic_ratings = {}

    # Collect ratings from completions
    for completion in completions:
        topic = completion['topic']
        track = completion['track']
        rating = completion.get('rating', 3)

        key = f"{track}: {topic}"
        if key not in topic_ratings:
            topic_ratings[key] = []
        topic_ratings[key].append(rating)

    # Collect ratings from reviews
    for review in reviews:
        if review.get('completed_date') and review.get('rating'):
            topic = review['topic']
            track = review['track']
            rating = review['rating']

            key = f"{track}: {topic}"
            if key not in topic_ratings:
                topic_ratings[key] = []
            topic_ratings[key].append(rating)

    # Calculate averages and sort by performance
    performance_data = []
    for topic, ratings in topic_ratings.items():
        avg_rating = sum(ratings) / len(ratings)
        performance_data.append({
            'topic': topic,
            'average_rating': round(avg_rating, 1),
            'total_attempts': len(ratings),
            'track': topic.split(':')[0]
        })

    # Sort by average rating (lowest first for identifying weak areas)
    performance_data.sort(key=lambda x: x['average_rating'])

    return performance_data

def calculate_review_analytics(reviews):
    """Calculate review success rates and patterns"""
    completed_reviews = [r for r in reviews if r.get('completed_date') and r.get('rating')]

    if not completed_reviews:
        return {
            'total_reviews': 0,
            'success_rate': 0,
            'by_interval': {},
            'rating_distribution': {}
        }

    # Success rate (rating >= 4 is considered successful recall)
    successful_reviews = [r for r in completed_reviews if r.get('rating', 0) >= 4]
    success_rate = len(successful_reviews) / len(completed_reviews) * 100

    # Success by review interval
    by_interval = {}
    for review in completed_reviews:
        interval = review.get('review_type', 'unknown')
        if interval not in by_interval:
            by_interval[interval] = {'total': 0, 'successful': 0}

        by_interval[interval]['total'] += 1
        if review.get('rating', 0) >= 4:
            by_interval[interval]['successful'] += 1

    # Calculate success rates by interval
    for interval in by_interval:
        total = by_interval[interval]['total']
        successful = by_interval[interval]['successful']
        by_interval[interval]['success_rate'] = (successful / total * 100) if total > 0 else 0

    # Rating distribution
    rating_distribution = {}
    for review in completed_reviews:
        rating = review.get('rating', 0)
        rating_distribution[rating] = rating_distribution.get(rating, 0) + 1

    return {
        'total_reviews': len(completed_reviews),
        'success_rate': round(success_rate, 1),
        'by_interval': by_interval,
        'rating_distribution': rating_distribution
    }

def calculate_overall_stats(completions, reviews, calendar_data):
    """Calculate overall learning statistics"""
    # Current streak
    streak = calculate_streak(completions)

    # Total activity days
    active_days = len([day for day in calendar_data if day['count'] > 0])

    # Average daily activity (activities per active day, not per calendar day)
    total_activities = sum(day['count'] for day in calendar_data)
    avg_daily_activity = total_activities / active_days if active_days > 0 else 0

    # Most productive day
    most_productive_day = max(calendar_data, key=lambda x: x['count']) if calendar_data else None

    # Track distribution
    track_counts = {}
    for completion in completions:
        track = completion['track'].title()
        track_counts[track] = track_counts.get(track, 0) + 1

    return {
        'current_streak': streak,
        'total_topics': len(completions),
        'total_reviews': len([r for r in reviews if r.get('completed_date')]),
        'active_days': active_days,
        'avg_daily_activity': round(avg_daily_activity, 1),
        'most_productive_day': most_productive_day,
        'track_distribution': track_counts
    }

def calculate_learning_trends(completions):
    """Calculate learning trends over time"""
    if not completions:
        return {'weekly_progress': [], 'monthly_progress': []}

    # Group by week
    weekly_counts = {}
    monthly_counts = {}

    for completion in completions:
        date = datetime.strptime(completion['date'], '%Y-%m-%d').date()

        # Weekly grouping
        week_key = f"{date.year}-W{date.isocalendar()[1]:02d}"
        weekly_counts[week_key] = weekly_counts.get(week_key, 0) + 1

        # Monthly grouping
        month_key = f"{date.year}-{date.month:02d}"
        monthly_counts[month_key] = monthly_counts.get(month_key, 0) + 1

    # Convert to sorted lists
    weekly_progress = [{'period': k, 'count': v} for k, v in sorted(weekly_counts.items())]
    monthly_progress = [{'period': k, 'count': v} for k, v in sorted(monthly_counts.items())]

    return {
        'weekly_progress': weekly_progress[-12:],  # Last 12 weeks
        'monthly_progress': monthly_progress[-6:]   # Last 6 months
    }

def calculate_timer_analytics(completions):
    """Calculate timer-based performance analytics"""
    timer_completions = [c for c in completions if c.get('completed_on_time') is not None]

    if not timer_completions:
        return {
            'on_time_rate': 0,
            'total_timed_sessions': 0,
            'on_time_count': 0,
            'over_time_count': 0,
            'by_track': {'coding': {'rate': 0, 'total': 0}, 'system_design': {'rate': 0, 'total': 0}},
            'recent_trend': []
        }

    # Overall statistics
    on_time_count = sum(1 for c in timer_completions if c['completed_on_time'] is True)
    over_time_count = sum(1 for c in timer_completions if c['completed_on_time'] is False)
    total_timed = len(timer_completions)
    on_time_rate = (on_time_count / total_timed * 100) if total_timed > 0 else 0

    # By track statistics
    track_stats = {'coding': {'rate': 0, 'total': 0}, 'system_design': {'rate': 0, 'total': 0}}
    for track in ['coding', 'system_design']:
        track_completions = [c for c in timer_completions if c['track'] == track]
        if track_completions:
            track_on_time = sum(1 for c in track_completions if c['completed_on_time'] is True)
            track_total = len(track_completions)
            track_stats[track] = {
                'rate': (track_on_time / track_total * 100) if track_total > 0 else 0,
                'total': track_total
            }

    # Recent trend (last 10 timed sessions)
    recent_sessions = sorted(timer_completions, key=lambda x: x['date'])[-10:]
    recent_trend = [
        {
            'date': session['date'],
            'on_time': session['completed_on_time'],
            'track': session['track'],
            'topic': session['topic']
        }
        for session in recent_sessions
    ]

    return {
        'on_time_rate': round(on_time_rate, 1),
        'total_timed_sessions': total_timed,
        'on_time_count': on_time_count,
        'over_time_count': over_time_count,
        'by_track': track_stats,
        'recent_trend': recent_trend
    }

@app.route('/practice')
def practice():
    """Practice mode page with random problems and mock interviews"""
    return render_template('practice.html', active_page='practice')

@app.route('/help')
def help_page():
    """Help and documentation page"""
    return render_template('help.html', active_page='help')

@app.route('/templates')
def templates_page():
    """Coding patterns and templates reference page"""
    return render_template('templates.html', active_page='templates')

@app.route('/system-design')
def system_design_page():
    """System design templates and concepts reference page"""
    return render_template('system-design.html', active_page='system-design')

@app.route('/api/random-problem', methods=['POST'])
def random_problem():
    """Get a random coding problem or system design topic based on filters"""
    data = request.get_json()
    track = data.get('track', 'coding')

    if track == 'coding':
        return get_random_coding_problem(data)
    elif track == 'system_design':
        return get_random_system_design(data)
    else:
        return jsonify({'error': 'Invalid track'}), 400

def get_random_coding_problem(filters):
    """Get a random coding problem with filters"""
    source = filters.get('source', 'curriculum')  # 'curriculum' or 'leetcode'

    if source == 'leetcode':
        return get_random_leetcode_problem(filters)
    else:
        return get_random_curriculum_problem(filters)

def get_random_curriculum_problem(filters):
    """Get a random coding problem from curriculum with filters"""
    difficulty = filters.get('difficulty', 'all')
    topic = filters.get('topic', 'all')

    # Load all coding curriculum
    curriculum = load_curriculum('coding')
    all_problems = []

    # Collect all problems from all days
    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            if 'problems' in day_info:
                for problem in day_info['problems']:
                    # Add topic info to problem
                    problem_with_topic = problem.copy()
                    problem_with_topic['topic_name'] = day_info['topic']
                    all_problems.append(problem_with_topic)

    # Filter by difficulty
    if difficulty != 'all':
        all_problems = [p for p in all_problems if p.get('difficulty', '').lower() == difficulty.lower()]

    # Filter by topic
    if topic != 'all':
        all_problems = [p for p in all_problems if topic.lower() in p.get('topic_name', '').lower()]

    if not all_problems:
        return jsonify({'error': 'No problems found matching criteria'}), 404

    # Select random problem
    selected_problem = random.choice(all_problems)

    # Find the day info that contains this problem
    selected_day = None
    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            if 'problems' in day_info:
                for problem in day_info['problems']:
                    if problem.get('number') == selected_problem.get('number'):
                        selected_day = day_info
                        break
                if selected_day:
                    break
        if selected_day:
            break

    return jsonify({
        'track': 'coding',
        'topic': selected_day['topic'] if selected_day else selected_problem['topic_name'],
        'activity': selected_day['activity'] if selected_day else 'Practice this problem',
        'detailed_content': selected_day.get('detailed_content', '') if selected_day else '',
        'problems': [selected_problem]
    })

def get_random_leetcode_problem(filters):
    """Get a random coding problem from LeetCode API with filters"""
    difficulty = filters.get('difficulty', 'all')
    topic = filters.get('topic', 'all')

    try:
        # Build LeetCode API query parameters
        params = {}

        # Map curriculum topic to LeetCode tags
        leetcode_tags = []
        if topic != 'all':
            leetcode_tags = TOPIC_TO_LEETCODE_TAGS.get(topic, [])
            if leetcode_tags:
                params['tags'] = '+'.join(leetcode_tags)

        # Map difficulty
        if difficulty != 'all':
            params['difficulty'] = difficulty.upper()

        # Set limit to get more options
        params['limit'] = 50

        # Make API request
        response = requests.get(f"{LEETCODE_API_BASE}/problems", params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        problems = data.get('problemsetQuestionList', [])

        if not problems:
            return jsonify({'error': 'No problems found matching criteria'}), 404

        # Filter out premium problems
        free_problems = [p for p in problems if not p.get('isPaidOnly', False)]

        if not free_problems:
            return jsonify({'error': 'No free problems found matching criteria'}), 404

        # Select random problem
        selected_problem = random.choice(free_problems)

        # Format response to match curriculum format
        formatted_problem = {
            'number': selected_problem.get('questionFrontendId', ''),
            'title': selected_problem.get('title', ''),
            'url': f"https://leetcode.com/problems/{selected_problem.get('titleSlug', '')}/",
            'difficulty': selected_problem.get('difficulty', '').title(),
            'description': f"Acceptance Rate: {selected_problem.get('acRate', 0):.1f}%",
            'topics': [tag.get('name', '') for tag in selected_problem.get('topicTags', [])],
            'source': 'leetcode'
        }

        # Get topic info from curriculum if available
        topic_name = topic if topic != 'all' else 'LeetCode Practice'
        topic_activity = f"Practice {topic_name} problems from LeetCode's extensive library"

        return jsonify({
            'track': 'coding',
            'topic': f"{topic_name} (LeetCode)",
            'activity': topic_activity,
            'detailed_content': f"This problem is from LeetCode's collection. Topics: {', '.join(formatted_problem['topics'])}",
            'problems': [formatted_problem],
            'source': 'leetcode',
            'total_available': len(free_problems)
        })

    except requests.RequestException as e:
        return jsonify({'error': f'Failed to fetch LeetCode problems: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Error processing LeetCode data: {str(e)}'}), 500

def get_random_system_design(filters):
    """Get a random system design topic with filters"""
    category = filters.get('category', 'all')

    # Load all system design curriculum
    curriculum = load_curriculum('system_design')
    all_topics = []

    # Collect all topics from all days
    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            topic_with_info = day_info.copy()
            all_topics.append(topic_with_info)

    # Filter by category (basic categorization based on topic content)
    if category != 'all':
        filtered_topics = []
        for topic in all_topics:
            topic_content = (topic.get('topic', '') + ' ' + topic.get('detailed_content', '')).lower()

            if category.lower() == 'fundamentals' and any(word in topic_content for word in ['scalability', 'availability', 'consistency', 'partition', 'trade-off']):
                filtered_topics.append(topic)
            elif category.lower() == 'databases' and any(word in topic_content for word in ['database', 'sql', 'nosql', 'redis', 'mongodb', 'postgres']):
                filtered_topics.append(topic)
            elif category.lower() == 'messaging' and any(word in topic_content for word in ['queue', 'messaging', 'kafka', 'rabbitmq', 'pub/sub']):
                filtered_topics.append(topic)
            elif category.lower() == 'caching' and any(word in topic_content for word in ['cache', 'caching', 'redis', 'memcached']):
                filtered_topics.append(topic)
            elif category.lower() == 'security' and any(word in topic_content for word in ['security', 'authentication', 'authorization', 'oauth']):
                filtered_topics.append(topic)
            elif category.lower() == 'monitoring' and any(word in topic_content for word in ['monitoring', 'logging', 'metrics', 'observability']):
                filtered_topics.append(topic)

        if filtered_topics:
            all_topics = filtered_topics

    if not all_topics:
        return jsonify({'error': 'No topics found matching criteria'}), 404

    # Select random topic
    selected_topic = random.choice(all_topics)

    return jsonify({
        'track': 'system_design',
        'topic': selected_topic['topic'],
        'activity': selected_topic['activity'],
        'detailed_content': selected_topic.get('detailed_content', ''),
        'resources': selected_topic.get('resources', []),
        'concepts': selected_topic.get('concepts', [])
    })

@app.route('/api/weakest-problem', methods=['POST'])
def weakest_problem():
    """Get a problem from the user's weakest topics based on ratings"""
    data = request.get_json()
    track = data.get('track', 'coding')

    # Load progress data to analyze ratings
    progress_data = load_json_data(PROGRESS_FILE)
    reviews_data = load_json_data(REVIEWS_FILE)

    # Collect all ratings for topics
    topic_ratings = {}

    # Analyze completion ratings
    for completion in progress_data.get('completions', []):
        if completion['track'] == track:
            topic = completion['topic']
            rating = completion.get('rating', 3)
            if topic not in topic_ratings:
                topic_ratings[topic] = []
            topic_ratings[topic].append(rating)

    # Analyze review ratings
    for review in reviews_data.get('scheduled_reviews', []):
        if review['track'] == track and review.get('completed_date') and review.get('rating'):
            topic = review['topic']
            rating = review['rating']
            if topic not in topic_ratings:
                topic_ratings[topic] = []
            topic_ratings[topic].append(rating)

    if not topic_ratings:
        return jsonify({'error': 'No completed topics found. Complete some topics first to identify weak areas!'}), 404

    # Calculate average ratings for each topic
    topic_averages = {}
    for topic, ratings in topic_ratings.items():
        topic_averages[topic] = sum(ratings) / len(ratings)

    # Find topics with lowest average ratings (≤ 2.5 = weak)
    weak_topics = [topic for topic, avg_rating in topic_averages.items() if avg_rating <= 2.5]

    if not weak_topics:
        # If no truly weak topics, get the bottom 3 topics
        sorted_topics = sorted(topic_averages.items(), key=lambda x: x[1])
        weak_topics = [topic for topic, rating in sorted_topics[:3]]

    if not weak_topics:
        return jsonify({'error': 'No topics found for practice'}), 404

    # Select a random weak topic
    selected_weak_topic = random.choice(weak_topics)
    avg_rating = topic_averages[selected_weak_topic]

    # Load curriculum and find the selected topic
    curriculum = load_curriculum(track)
    selected_day = None

    for week_name, days in curriculum['weeks'].items():
        for day_info in days:
            if day_info['topic'] == selected_weak_topic:
                selected_day = day_info
                break
        if selected_day:
            break

    if not selected_day:
        return jsonify({'error': f'Could not find curriculum data for topic: {selected_weak_topic}'}), 404

    # Format response based on track type
    if track == 'coding':
        return jsonify({
            'track': 'coding',
            'topic': f"{selected_day['topic']} (Avg Rating: {avg_rating:.1f}/5)",
            'activity': f"Focus practice - This is one of your weaker areas. {selected_day['activity']}",
            'detailed_content': selected_day.get('detailed_content', ''),
            'problems': selected_day.get('problems', [])
        })
    else:  # system_design
        return jsonify({
            'track': 'system_design',
            'topic': f"{selected_day['topic']} (Avg Rating: {avg_rating:.1f}/5)",
            'activity': f"Focus review - This topic needs reinforcement. {selected_day['activity']}",
            'detailed_content': selected_day.get('detailed_content', ''),
            'resources': selected_day.get('resources', []),
            'concepts': selected_day.get('concepts', [])
        })

@app.route('/api/curriculum/<track>/reset', methods=['POST'])
def reset_curriculum_to_default(track):
    """Reset curriculum to default values"""
    if track not in ['coding', 'system_design']:
        return jsonify({'error': 'Invalid track'}), 400

    try:
        import shutil
        import time

        # Define paths
        default_file = os.path.join(DATA_DIR, 'defaults', f'{track}_default.yaml')
        current_file = os.path.join(CURRICULUM_DIR, f'{track}.yaml')
        backup_file = f"{current_file}.backup_{int(time.time())}"

        # Check if default file exists
        if not os.path.exists(default_file):
            return jsonify({'error': 'Default curriculum file not found'}), 404

        # Create backup of current curriculum
        if os.path.exists(current_file):
            shutil.copy2(current_file, backup_file)

        # Restore from default
        shutil.copy2(default_file, current_file)

        return jsonify({
            'success': True,
            'message': f'{track.replace("_", " ").title()} curriculum reset to default successfully',
            'backup_created': backup_file
        })

    except Exception as e:
        return jsonify({'error': f'Failed to reset curriculum: {str(e)}'}), 500

# Timer API Endpoints
@app.route('/api/timer/state', methods=['GET'])
def get_timer_state():
    """Get current timer state"""
    try:
        timer_state = get_current_timer_state()
        return jsonify(timer_state)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/timer/start', methods=['POST'])
def start_timer():
    """Start a new timer session"""
    try:
        data = request.get_json()
        track = data.get('track')
        topic = data.get('topic')
        duration_minutes = data.get('duration', 25)  # Duration in minutes
        duration = duration_minutes * 60  # Convert to seconds

        # Stop any existing timer
        timer_state = load_timer_state()
        timer_state.update({
            'active': True,
            'paused': False,
            'start_time': datetime.now().isoformat(),
            'pause_time': None,
            'duration': duration,
            'remaining': duration,
            'track': track,
            'topic': topic,
            'completed': False,
            'total_pause_duration': 0
        })

        save_timer_state(timer_state)
        return jsonify({'success': True, 'timer_state': timer_state})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/timer/pause', methods=['POST'])
def pause_timer():
    """Pause the current timer"""
    try:
        timer_state = get_current_timer_state()

        if not timer_state['active']:
            return jsonify({'error': 'No active timer'}), 400

        if timer_state['paused']:
            return jsonify({'error': 'Timer already paused'}), 400

        timer_state['paused'] = True
        timer_state['pause_time'] = datetime.now().isoformat()

        save_timer_state(timer_state)
        return jsonify({'success': True, 'timer_state': timer_state})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/timer/resume', methods=['POST'])
def resume_timer():
    """Resume a paused timer"""
    try:
        timer_state = load_timer_state()

        if not timer_state['active'] or not timer_state['paused']:
            return jsonify({'error': 'No paused timer to resume'}), 400

        # Calculate how long we were paused and add to total
        if timer_state['pause_time']:
            pause_start = datetime.fromisoformat(timer_state['pause_time'])
            pause_duration = (datetime.now() - pause_start).total_seconds()

            # Add to cumulative pause duration
            if 'total_pause_duration' not in timer_state:
                timer_state['total_pause_duration'] = 0
            timer_state['total_pause_duration'] += pause_duration

        timer_state['paused'] = False
        timer_state['pause_time'] = None

        save_timer_state(timer_state)
        return jsonify({'success': True, 'timer_state': timer_state})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/timer/stop', methods=['POST'])
def stop_timer():
    """Stop the current timer"""
    try:
        timer_state = load_timer_state()

        if not timer_state['active']:
            return jsonify({'error': 'No active timer'}), 400

        timer_state.update({
            'active': False,
            'paused': False,
            'start_time': None,
            'pause_time': None,
            'duration': None,
            'remaining': None,
            'track': None,
            'topic': None,
            'completed': False
        })

        save_timer_state(timer_state)
        return jsonify({'success': True, 'timer_state': timer_state})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/advance-day', methods=['POST'])
def advance_day():
    """Advance to the next day for a specific track"""
    try:
        data = request.get_json()
        track = data.get('track')

        if not track or track not in ['coding', 'system_design']:
            return jsonify({'error': 'Valid track required (coding or system_design)'}), 400

        # Load current config
        config = load_config()

        # Get current day number before advancement
        current_day = get_day_number(track)

        # Check if we're already at day 28
        if current_day >= 28:
            return jsonify({'error': f'Already at final day (28) for {track}'}), 400

        # Increment acceleration days
        config['study_plan'][track]['acceleration_days'] = config['study_plan'][track].get('acceleration_days', 0) + 1

        # Save updated config
        save_json_data(CONFIG_FILE, config)

        # Get new day information
        new_day = get_day_number(track)
        new_topic = get_topic_for_day(track, new_day)

        # Calculate how many days ahead of schedule
        start_date = datetime.strptime(config['study_plan'][track]['start_date'], '%Y-%m-%d').date()
        natural_day = (datetime.now().date() - start_date).days + 1
        days_ahead = max(0, new_day - natural_day)

        return jsonify({
            'success': True,
            'track': track,
            'previous_day': current_day,
            'new_day': new_day,
            'new_topic': new_topic,
            'days_ahead': days_ahead,
            'message': f'Advanced to Day {new_day}: {new_topic["topic"] if new_topic else "Complete!"}'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get-advancement-info', methods=['GET'])
def get_advancement_info():
    """Get information about current day and advancement possibilities"""
    try:
        track = request.args.get('track')

        if not track or track not in ['coding', 'system_design']:
            return jsonify({'error': 'Valid track required'}), 400

        config = load_config()
        current_day = get_day_number(track)
        current_topic = get_topic_for_day(track, current_day)

        # Calculate next day info
        next_day = min(28, current_day + 1)
        next_topic = get_topic_for_day(track, next_day) if next_day <= 28 else None

        # Calculate days ahead of natural schedule
        start_date = datetime.strptime(config['study_plan'][track]['start_date'], '%Y-%m-%d').date()
        natural_day = (datetime.now().date() - start_date).days + 1
        days_ahead = max(0, current_day - natural_day)

        # Check if today's topic is completed
        today = datetime.now().date().strftime('%Y-%m-%d')
        progress_data = load_json_data(PROGRESS_FILE)
        topic_completed = False

        if current_topic:
            for completion in progress_data.get('completions', []):
                if (completion['date'] == today and
                    completion['track'] == track and
                    completion['topic'] == current_topic['topic']):
                    topic_completed = True
                    break

        return jsonify({
            'success': True,
            'track': track,
            'current_day': current_day,
            'current_topic': current_topic,
            'next_day': next_day,
            'next_topic': next_topic,
            'days_ahead': days_ahead,
            'topic_completed': topic_completed,
            'can_advance': topic_completed and next_day <= 28,
            'at_final_day': current_day >= 28
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5555)