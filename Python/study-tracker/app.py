from flask import Flask, render_template, request, redirect, url_for, jsonify
import yaml
import json
from datetime import datetime, timedelta
import os
import random

app = Flask(__name__)

# Add JSON filter for templates
def tojsonfilter(value):
    return json.dumps(value)

app.jinja_env.filters['tojsonfilter'] = tojsonfilter

# Configuration
DATA_DIR = "data"
CURRICULUM_DIR = f"{DATA_DIR}/curriculum"
PROGRESS_FILE = f"{DATA_DIR}/progress.json"
REVIEWS_FILE = f"{DATA_DIR}/reviews.json"
CONFIG_FILE = f"{DATA_DIR}/config.json"

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
    """Calculate current day number (1-28) based on configured start date for track"""
    config = load_config()
    start_date_str = config['study_plan'][track]['start_date']
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()

    today = datetime.now().date()
    days_elapsed = (today - start_date).days + 1
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

    # Get due reviews
    due_reviews = get_due_reviews(today)

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
        # Mark review as complete
        reviews_data = load_json_data(REVIEWS_FILE)
        for review in reviews_data.get('scheduled_reviews', []):
            if (review['topic'] == topic and
                review['track'] == track and
                review['due_date'] == today and
                not review.get('completed_date')):
                review['completed_date'] = today
                review['rating'] = rating
                review['notes'] = notes
                break
        save_json_data(REVIEWS_FILE, reviews_data)

    return jsonify({'status': 'success'})

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
    dates = {}
    for completion in completions:
        date = completion['date']
        if date not in dates:
            dates[date] = 0
        dates[date] += 1

    # Count consecutive days
    today = datetime.now().date()
    streak = 0
    current_date = today

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

    # Average daily activity
    total_activities = sum(day['count'] for day in calendar_data)
    avg_daily_activity = total_activities / len(calendar_data) if calendar_data else 0

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)