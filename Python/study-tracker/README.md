# 📚 Study Tracker

A local web application to track your coding interview and system design preparation using scientifically-optimized spaced repetition.

## ✨ Features

- **📅 Daily Dashboard** - See exactly what to learn and review each day
- **🧠 Spaced Repetition** - Automatic review scheduling (1, 3, 7, 14 days)
- **📊 Progress Tracking** - Visual history of completions and streaks
- **🔮 Preview Mode** - Plan upcoming days
- **📝 Notes & Ratings** - Track difficulty and insights
- **🎯 Dual Track** - Both coding algorithms and system design

## 🚀 Quick Start

```bash
# Clone or navigate to the study-tracker directory
cd study-tracker

# Setup (one time only)
make setup

# Run the application
make run

# Open http://localhost:5000 in your browser
```

## 📖 Available Commands

```bash
make help     # Show all available commands
make setup    # Create virtual environment and install dependencies
make run      # Start the study tracker
make dev      # Start with auto-reload for development
make test     # Run basic tests
make status   # Check project status
make clean    # Remove virtual environment
```

## 📁 Project Structure

```
study-tracker/
├── app.py                    # Main Flask application
├── Makefile                  # Automation commands
├── requirements.txt          # Python dependencies
├── data/
│   ├── curriculum/
│   │   ├── coding.yaml      # 28-day coding curriculum
│   │   └── system_design.yaml # 28-day system design curriculum
│   ├── progress.json        # Your completion history
│   └── reviews.json         # Scheduled reviews
└── templates/
    ├── dashboard.html       # Main daily view
    ├── history.html         # Progress history
    └── preview.html         # Upcoming schedule
```

## 🎯 How It Works

1. **Daily Learning**: Each day shows you new topics to learn
2. **Mark Complete**: Rate difficulty (1-5) and add notes
3. **Auto-Reviews**: System schedules reviews at optimal intervals
4. **Track Progress**: See streaks, completion rates, and history

## 🔧 Customization

**Edit Curriculum**: Modify `data/curriculum/*.yaml` files to:
- Add/remove topics
- Change time estimates
- Add more practice problems
- Adjust learning activities

**Change Review Intervals**: Edit `REVIEW_INTERVALS` in `app.py`

## 📊 Data Storage

- **Human-readable**: YAML curriculum files you can edit
- **Automatic tracking**: JSON files for progress and reviews
- **Local-only**: All data stays on your machine
- **Backup-friendly**: Simple file copying

## 🎓 Based on Science

This tool implements the spaced repetition schedule from the LaTeX study guides, optimized for maximum retention using cognitive science principles.

## ⚠️ Requirements

- Python 3.7+
- No external databases needed
- Runs entirely locally

## 🆘 Troubleshooting

```bash
# Check if everything is set up correctly
make status

# Reinstall dependencies
make clean && make setup

# Test basic functionality
make test
```

---

**Happy studying! 🎯 Master those algorithms and system designs!**