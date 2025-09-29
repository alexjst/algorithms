#!/usr/bin/env python3
"""
Legacy startup script for the Study Tracker

⚠️  RECOMMENDED: Use the Makefile instead!

Quick start:
    make setup
    make run

This script is kept for backward compatibility.
"""

import sys
import os

def main():
    print("⚠️  NOTICE: Please use the Makefile for better dependency management!")
    print()
    print("Recommended commands:")
    print("  make setup    # One-time setup with virtual environment")
    print("  make run      # Start the application")
    print("  make help     # See all commands")
    print()

    response = input("Continue with legacy startup? (y/N): ").lower()
    if response != 'y':
        print("👍 Good choice! Run 'make setup' then 'make run'")
        sys.exit(0)

    print("🚀 Starting Study Tracker (legacy mode)...")
    print("📚 Your personal spaced repetition learning companion")
    print()

    # Check if we're in virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  WARNING: Not running in virtual environment!")
        print("Consider using 'make setup' for better isolation.")
        print()

    # Check if requirements are installed
    try:
        import flask
        import yaml
        print("✅ Dependencies check passed")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: make setup")
        sys.exit(1)

    # Import and run the app
    try:
        from app import app
        print("🌐 Starting server at http://localhost:5555")
        print("📖 Open this URL in your browser to begin!")
        print()
        print("💡 Tips:")
        print("   - Bookmark the dashboard for daily use")
        print("   - Mark topics complete as you finish them")
        print("   - Check 'Preview' to plan upcoming days")
        print("   - Use 'History' to track your progress")
        print()
        print("⏹️  Press Ctrl+C to stop the server")
        print("-" * 50)

        app.run(debug=True, port=5555, host='127.0.0.1')

    except KeyboardInterrupt:
        print("\n👋 Study tracker stopped. Keep up the great work!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()