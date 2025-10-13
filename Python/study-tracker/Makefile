.PHONY: setup install run clean test help install-service uninstall-service service-status

# Variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Default target
help:
	@echo "📚 Study Tracker - Available Commands:"
	@echo ""
	@echo "  make setup            - Create virtual environment and install dependencies"
	@echo "  make run              - Start the study tracker application"
	@echo "  make install          - Install/update dependencies"
	@echo "  make clean            - Remove virtual environment"
	@echo "  make test             - Run basic tests"
	@echo "  make help             - Show this help message"
	@echo ""
	@echo "  make install-service  - Install as login item (auto-start on boot)"
	@echo "  make uninstall-service - Remove login item"
	@echo "  make service-status   - Check if service is running"
	@echo ""
	@echo "🚀 Quick start: make setup && make run"
	@echo "🚀 Auto-start: make setup && make install-service"

# Create virtual environment and install dependencies
setup: $(VENV_DIR)
	@echo "✅ Setup complete! Run 'make run' to start the application."

$(VENV_DIR):
	@echo "🔧 Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "📦 Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Virtual environment created and dependencies installed"

# Install/update dependencies
install: $(VENV_DIR)
	@echo "📦 Installing/updating dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the application
run: $(VENV_DIR)
	@echo "🚀 Starting Study Tracker..."
	@echo "📖 Open http://localhost:5555 in your browser"
	@echo "⏹️  Press Ctrl+C to stop"
	@echo ""
	$(PYTHON) app.py

# Run basic tests
test: $(VENV_DIR)
	@echo "🧪 Running basic tests..."
	$(PYTHON) -c "import yaml, json; print('✅ YAML and JSON modules work')"
	$(PYTHON) -c "import flask; print('✅ Flask module works')"
	$(PYTHON) -c "from app import app; print('✅ App imports successfully')"
	@echo "✅ All basic tests passed"

# Clean up virtual environment
clean:
	@echo "🧹 Cleaning up virtual environment..."
	rm -rf $(VENV_DIR)
	@echo "✅ Virtual environment removed"

# Development mode with auto-reload
dev: $(VENV_DIR)
	@echo "🔧 Starting in development mode..."
	@echo "📖 Open http://localhost:5555 in your browser"
	@echo "🔄 Auto-reload enabled"
	FLASK_ENV=development $(PYTHON) app.py

# Check if data files exist and create them if needed
init-data:
	@echo "📁 Checking data files..."
	@test -f data/progress.json || echo '{"completions": []}' > data/progress.json
	@test -f data/reviews.json || echo '{"scheduled_reviews": []}' > data/reviews.json
	@echo "✅ Data files ready"

# Show status of the project
status:
	@echo "📊 Study Tracker Status:"
	@echo ""
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "✅ Virtual environment: EXISTS"; \
	else \
		echo "❌ Virtual environment: MISSING (run 'make setup')"; \
	fi
	@if [ -f "data/progress.json" ]; then \
		echo "✅ Progress data: EXISTS"; \
	else \
		echo "⚠️  Progress data: MISSING"; \
	fi
	@if [ -f "data/reviews.json" ]; then \
		echo "✅ Reviews data: EXISTS"; \
	else \
		echo "⚠️  Reviews data: MISSING"; \
	fi

# Install as macOS login item (auto-start on boot)
install-service: $(VENV_DIR)
	@echo "🔧 Installing Study Tracker as login item..."
	@mkdir -p ~/Library/LaunchAgents
	@cat > ~/Library/LaunchAgents/com.studytracker.plist << 'PLISTEOF'\n\
<?xml version="1.0" encoding="UTF-8"?>\n\
<plist version="1.0">\n\
<dict>\n\
    <key>Label</key>\n\
    <string>com.studytracker</string>\n\
    <key>ProgramArguments</key>\n\
    <array>\n\
        <string>$(PWD)/$(VENV_DIR)/bin/python</string>\n\
        <string>$(PWD)/app.py</string>\n\
    </array>\n\
    <key>WorkingDirectory</key>\n\
    <string>$(PWD)</string>\n\
    <key>RunAtLoad</key>\n\
    <true/>\n\
    <key>KeepAlive</key>\n\
    <true/>\n\
    <key>StandardOutPath</key>\n\
    <string>$(PWD)/studytracker.log</string>\n\
    <key>StandardErrorPath</key>\n\
    <string>$(PWD)/studytracker.error.log</string>\n\
</dict>\n\
</plist>\n\
PLISTEOF
	@launchctl bootout gui/$$(id -u)/com.studytracker 2>/dev/null || true
	@launchctl bootstrap gui/$$(id -u) ~/Library/LaunchAgents/com.studytracker.plist
	@sleep 2
	@if curl -s -o /dev/null -w "%{http_code}" http://localhost:5555 2>/dev/null | grep -q 200; then \
		echo "✅ Service installed and running at http://localhost:5555"; \
		echo "📝 Logs: studytracker.log and studytracker.error.log"; \
	else \
		echo "⚠️  Service installed but may not be running. Check studytracker.error.log"; \
	fi

# Remove login item
uninstall-service:
	@echo "🗑️  Removing Study Tracker login item..."
	@launchctl bootout gui/$$(id -u)/com.studytracker 2>/dev/null || true
	@rm -f ~/Library/LaunchAgents/com.studytracker.plist
	@echo "✅ Service uninstalled"

# Check service status
service-status:
	@echo "📊 Study Tracker Service Status:"
	@echo ""
	@if [ -f ~/Library/LaunchAgents/com.studytracker.plist ]; then \
		echo "✅ Service installed"; \
		if launchctl print gui/$$(id -u)/com.studytracker >/dev/null 2>&1; then \
			echo "✅ Service loaded"; \
		else \
			echo "❌ Service NOT loaded"; \
		fi; \
		if curl -s -o /dev/null -w "%{http_code}" http://localhost:5555 2>/dev/null | grep -q 200; then \
			echo "✅ Service running at http://localhost:5555"; \
		else \
			echo "❌ Service NOT responding"; \
		fi; \
	else \
		echo "❌ Service not installed (run 'make install-service')"; \
	fi