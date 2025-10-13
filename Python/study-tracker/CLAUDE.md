# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development
```bash
make setup              # Create venv and install dependencies (one-time)
make run                # Start app on http://localhost:5555
make dev                # Start with auto-reload and FLASK_ENV=development
make test               # Run basic import tests
make status             # Check setup status
make clean              # Remove venv

# Auto-start service (macOS)
make install-service    # Install as login item (auto-start on boot)
make uninstall-service  # Remove login item
make service-status     # Check if service is running
```

### Testing Changes
After making changes to `app.py` or templates, simply refresh the browser. For development with auto-reload, use `make dev`.

No separate linting or type checking commands are configured. The `make test` command only validates basic imports.

## Architecture

### Application Type
Flask web application with Jinja2 templates. Single-file architecture in `app.py` (2,233 lines). Runs locally on port 5555.

### Core Concept: Spaced Repetition Study Tracker
Implements spaced repetition for coding interview prep across two tracks:
1. **Coding Track**: LeetCode-style algorithm problems
2. **System Design Track**: Conceptual questions and scenarios

Each completed topic automatically schedules reviews at intervals: 1, 3, 7, 14 days (configurable in `data/config.json`).

### Data Flow

**Learning Flow**:
1. User opens dashboard → `get_topic_for_day(track, day)` loads today's topic from YAML curriculum
2. User completes topic → `/complete` endpoint saves to `progress.json` and calls `schedule_reviews()` 
3. `schedule_reviews()` creates 4 review entries in `reviews.json` (one per interval)

**Review Flow**:
1. Dashboard loads → `get_due_reviews(today)` finds reviews where `due_date == today`
2. For coding: `get_topic_problems()` fetches LeetCode problems from curriculum
3. For system design: `select_review_questions()` randomly samples questions based on review type
4. User completes review → `/complete` endpoint marks review as completed and updates intervals

### Key Data Structures

**Curriculum** (`data/curriculum/{coding,system_design}.yaml`):
- 28-day structured curriculum with topics, problems, and practice questions
- Coding: Each day has LeetCode problems with difficulty, tags, and URLs
- System Design: Each day has practice questions categorized by type (estimation, concepts, tradeoffs, scenarios)

**Progress** (`data/progress.json`):
```json
{
  "completions": [
    {
      "date": "2025-10-12",
      "topic": "Arrays & Hashing",
      "track": "coding",
      "rating": 4,
      "notes": "...",
      "problems": [...],
      "time_taken": 45
    }
  ]
}
```

**Reviews** (`data/reviews.json`):
```json
{
  "scheduled_reviews": [
    {
      "topic": "Arrays & Hashing",
      "track": "coding",
      "scheduled_date": "2025-10-12",
      "due_date": "2025-10-13",
      "review_type": "1-day",
      "completed_date": null
    }
  ]
}
```

### Critical Functions in app.py

**Data Loading** (lines 424-442):
- `load_curriculum(track)`: Loads YAML curriculum files
- `load_json_data(filename)`: Reads JSON with file locking
- `save_json_data(filename, data, sync=True)`: Writes JSON and triggers git sync if enabled

**Day Calculation** (lines 450-472):
- `get_day_number(track)`: Calculates current day number based on start_date in config
- `get_topic_for_day(track, day)`: Returns topic dict from curriculum for given day
- `get_due_reviews(date_str)`: Returns all reviews due on a specific date (with deduplication logic to show only the most urgent review per topic)

**Question Selection** (lines 509-572):
- `get_system_design_practice_questions(topic, track)`: Extracts all practice questions for a topic from curriculum
- `select_review_questions(topic, track, review_type)`: Randomly samples questions based on review type (1-day: 3 questions, 3-day: 5 questions, etc.)
- **Format**: Returns list of dicts with keys: `type`, `question`, `answer`, `id`

**Review Scheduling** (lines 688-720):
- `schedule_reviews(topic, track, completed_date)`: Creates 4 review entries (1, 3, 7, 14 days) in reviews.json
- Checks for existing reviews and adjusts intervals if needed
- Each review has a unique `review_type` (e.g., "1-day", "3-day")

**Git Sync** (lines 103-398):
- `GIT_SYNC_ENABLED = True` (line 65) controls auto-sync
- `git_pull()`: Pulls changes before data operations
- `git_push(message)`: Commits and pushes after data changes
- `smart_merge_json()`: Three-way merge for concurrent changes
- Uses `FileLock` class to prevent concurrent access

### Templates Structure

**dashboard.html** (26k tokens):
- Main view showing today's topics and due reviews
- Contains embedded JavaScript for timer functionality and practice sessions
- Practice questions displayed inline with toggle answers for new learning
- Review questions shown with interactive answer input, hint button, and time tracking

**Key Template Variables**:
- `coding_topic` / `system_design_topic`: Today's topics from curriculum
- `due_reviews`: List of reviews due today (coding or system_design)
- `review.problems`: List of LeetCode problems for coding reviews
- `review.practice_questions`: List of question dicts for system design reviews (must have `.type`, `.question`, `.answer`)

**Answer/Hint Toggle** (dashboard.html:2100-2109):
- JavaScript function `toggleAnswer(button)` toggles visibility of answer/hint
- Used in both "New Learning" section (shows answer) and "Due Reviews" section (shows hint)
- Button text changes between "Show Answer/Hint" and "Hide Answer"

### Common Issues

**Practice Questions Display Bug** (fixed in app.py:556-570):
- `select_review_questions()` must extract `question` and `answer` from dicts loaded from YAML
- Template expects questions as list of dicts with keys: `type`, `question`, `answer`, `id`
- Bug was: assigned full dict to `'question'` field instead of extracting `question_dict['question']`

**File Locking**:
- All JSON reads/writes use `FileLock` to prevent corruption during git sync
- Lock files: `DATA_LOCK_FILE`, `GIT_LOCK_FILE`
- Timeout: 30 seconds

**Day Number Calculation**:
- Each track (coding, system_design) has independent `start_date` in config
- Days can be "accelerated" via `acceleration_days` setting
- Formula: `days_since_start + 1 + acceleration_days`

### Configuration

**data/config.json**:
- `study_plan.{coding,system_design}.start_date`: Controls which day is "Day 1"
- `study_plan.{coding,system_design}.acceleration_days`: Skip ahead N days
- `settings.review_intervals`: Array of days for review scheduling (default: [1, 3, 7, 14])

### Curriculum Editing

Both YAML files follow same structure:
```yaml
weeks:
  week_1:
    - day: 1
      topic: "Topic Name"
      problems:  # coding only
        - title: "Problem Name"
          difficulty: "Medium"
          url: "https://..."
      practice_questions:  # system_design only
        estimation:
          - question: "..."
            answer: "..."
        concepts: [...]
        tradeoffs: [...]
        scenarios: ["..."]  # Can be strings without answers
```

When modifying curriculum:
- Maintain consistent structure for both tracks
- System design questions can be dicts (with answers) or strings (scenarios without answers)
- Template handles both formats via `{% if item is mapping %}`
