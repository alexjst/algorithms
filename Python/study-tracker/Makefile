.PHONY: setup install run clean test help

# Variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Default target
help:
	@echo "📚 Study Tracker - Available Commands:"
	@echo ""
	@echo "  make setup    - Create virtual environment and install dependencies"
	@echo "  make run      - Start the study tracker application"
	@echo "  make install  - Install/update dependencies"
	@echo "  make clean    - Remove virtual environment"
	@echo "  make test     - Run basic tests"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "🚀 Quick start: make setup && make run"

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
	@echo "📖 Open http://localhost:5000 in your browser"
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
	@echo "📖 Open http://localhost:5000 in your browser"
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