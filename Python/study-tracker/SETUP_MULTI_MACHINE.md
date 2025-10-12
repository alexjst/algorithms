# Multi-Machine Setup Guide

This guide explains how to set up the Study Tracker on multiple computers with automatic data sync via GitHub.

## How It Works

The application automatically syncs your progress data across machines:
- **On Startup**: Pulls latest changes from GitHub
- **Before Every Push**: Pulls remote changes to detect conflicts
- **Smart Conflict Resolution**: Automatically merges conflicting changes
  - **progress.json**: Combines completions from both machines
  - **reviews.json**: Merges reviews, prefers completed ones
  - **timer_state.json**: Keeps most recently updated timer
  - **config.json**: Prefers local settings
- **After Every Update**: Commits and pushes changes to GitHub
- Data files stay in sync even when using multiple machines simultaneously

## Setup on Second Machine

### 1. Clone the Repository
```bash
git clone https://github.com/alexjst/algorithms.git
cd algorithms/Python/study-tracker
```

### 2. Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Git (if needed)
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 4. Start the Application
```bash
python app.py
```

The app will automatically pull the latest data on startup!

## Using Multiple Machines

### Best Practices
1. ~~**Always restart the app** when switching machines~~ **Not needed!** Changes are pulled automatically before push
2. **Complete your work** before closing - changes are pushed automatically
3. **Check the console** for sync status messages
4. **Simultaneous use is now safe** - conflicts are auto-merged

### What Gets Synced
✅ Progress completions and ratings
✅ Review schedules and completions
✅ Timer state
✅ Configuration (start dates, acceleration)

### What Doesn't Get Synced
❌ Curriculum content (in git but rarely changes)
❌ Local environment settings (port, LaunchAgent config)

## Troubleshooting

### "Uncommitted changes detected, skipping pull"
**Cause**: You have local changes that haven't been committed
**Fix**: Check `git status` and either commit or discard changes

### "Git pull failed" or "Git push failed"
**Cause**: Network issues or authentication problems
**Fix**:
1. Check internet connection
2. Verify GitHub credentials: `git push origin master` (manually test)
3. Check git remote: `git remote -v`

### Merge Conflicts
**Now handled automatically!** The app uses smart merge logic:
- **progress.json**: Combines all completions from both machines (no data loss)
- **reviews.json**: Merges reviews intelligently (prefers completed reviews)
- **timer_state.json**: Uses the most recently updated timer state
- **config.json**: Keeps your local configuration

If automatic merge fails, fallback uses local version. Check console logs for details.

### Disable Auto-Sync (Emergency)
If sync is causing issues, temporarily disable it:

In `app.py`, change:
```python
GIT_SYNC_ENABLED = False  # Was: True
```

Then restart the app. Remember to manually sync with `git pull/push`.

## Optional: Auto-Startup on Second Machine

### macOS
Follow the same LaunchAgent setup as the first machine (see CLAUDE.md).

### Linux (systemd)
Create `/etc/systemd/system/study-tracker.service`:
```ini
[Unit]
Description=Study Tracker
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/path/to/study-tracker
ExecStart=/path/to/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable: `sudo systemctl enable study-tracker && sudo systemctl start study-tracker`

### Windows (Task Scheduler)
1. Open Task Scheduler
2. Create Basic Task → "Study Tracker"
3. Trigger: "When I log on"
4. Action: Start a program → `C:\Python\python.exe`
5. Arguments: `C:\path\to\study-tracker\app.py`

## Monitoring Sync Status

Watch the console output when the app starts and when you make changes:

```
INFO:__main__:Starting application...
INFO:__main__:Pulling latest changes from git...
INFO:__main__:Git pull successful
...
INFO:__main__:Git push successful: Auto-sync: 2025-10-12 15:30:45
```

## Security Note

The app pushes data to a **public GitHub repository**. If you want to keep your progress private:

1. Make the repository private on GitHub (Settings → Change visibility)
2. Or fork to a private repo and update the remote: `git remote set-url origin https://github.com/YOUR_USERNAME/your-private-repo.git`
