#!/usr/bin/env python3
"""
Book Recommender System - Easy Setup Script
Automatically installs dependencies and runs the application.
"""

import subprocess
import sys
import os

def check_setup():
    """Quick setup check"""
    required_files = ['app.py', 'books.pkl', 'popular.pkl', 'pt.pkl', 'similarity_scores.pkl']
    missing = [f for f in required_files if not os.path.exists(f)]
    
    if missing:
        print("Missing required files:")
        for file in missing:
            print(f"   - {file}")
        print("\nRun 'python test_setup.py' for detailed diagnostics")
        return False
    return True

def main():
    print("Book Recommender System")
    print("=" * 40)
    
    # Quick setup check
    print("Checking setup...")
    if not check_setup():
        return
    
    print("Setup looks good!")
    print("\nStarting Flask application...")
    
    # Import and run the Flask app
    try:
        from app import app
        
        print("\n" + "=" * 40)
        print("APPLICATION READY!")
        print("=" * 40)
        print("Local URL: http://localhost:5000")
        print("Network URL: http://127.0.0.1:5000")
        print("\nTips:")
        print("   • Try popular books like '1984' or 'Harry Potter'")
        print("   • Use exact book titles for recommendations")
        print("   • Press Ctrl+C to stop the server")
        print("=" * 40)
        
        # Optional: Auto-open browser after a delay
        def open_browser():
            import time
            import webbrowser
            time.sleep(1.5)
            webbrowser.open('http://localhost:5000')
        
        import threading
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Run the Flask app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except ImportError as e:
        print(f"Error importing app: {e}")
        print("Run 'pip install -r requirements.txt' to install dependencies")
    except KeyboardInterrupt:
        print("\n\nApplication stopped by user")
    except Exception as e:
        print(f"Error starting application: {e}")
        print("Check your setup with 'python test_setup.py'")

if __name__ == "__main__":
    main()