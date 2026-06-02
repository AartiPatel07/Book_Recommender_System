#!/usr/bin/env python3
"""
Book Recommender System - Setup Test Script
This script helps verify that your setup is working correctly.
"""

import sys
import os
from pathlib import Path

def print_status(message, status):
    """Print status messages"""
    if status:
        print(f"[PASS] {message}")
    else:
        print(f"[FAIL] {message}")
    return status

def test_python_version():
    """Test if Python version is compatible"""
    version = sys.version_info
    required = (3, 7)
    is_compatible = version >= required
    print_status(f"Python {version.major}.{version.minor}.{version.micro} (required: 3.7+)", is_compatible)
    return is_compatible

def test_required_packages():
    """Test if all required packages are installed"""
    required_packages = ['flask', 'numpy', 'pandas', 'sklearn']
    all_installed = True
    
    for package in required_packages:
        try:
            __import__(package)
            print_status(f"{package} package installed", True)
        except ImportError:
            print_status(f"{package} package installed", False)
            all_installed = False
    
    return all_installed

def test_required_files():
    """Test if all required files exist"""
    required_files = [
        'app.py',
        'books.pkl',
        'popular.pkl', 
        'pt.pkl',
        'similarity_scores.pkl',
        'templates/index.html',
        'templates/recommend.html'
    ]
    
    all_present = True
    for file_path in required_files:
        exists = Path(file_path).exists()
        print_status(f"{file_path} exists", exists)
        if not exists:
            all_present = False
    
    return all_present

def test_pickle_files():
    """Test if pickle files can be loaded"""
    import pickle
    
    pickle_files = ['books.pkl', 'popular.pkl', 'pt.pkl', 'similarity_scores.pkl']
    all_loadable = True
    
    for pkl_file in pickle_files:
        try:
            with open(pkl_file, 'rb') as f:
                data = pickle.load(f)
            print_status(f"{pkl_file} loads successfully", True)
        except Exception as e:
            print_status(f"{pkl_file} loads successfully", False)
            print(f"   Error: {e}")
            all_loadable = False
    
    return all_loadable

def test_app_imports():
    """Test if the main app can be imported"""
    try:
        import app
        print_status("app.py imports successfully", True)
        return True
    except Exception as e:
        print_status("app.py imports successfully", False)
        print(f"   Error: {e}")
        return False

def main():
    """Run all tests"""
    print("Book Recommender System - Setup Verification")
    print("=" * 50)
    
    tests = [
        ("Python Version", test_python_version),
        ("Required Packages", test_required_packages), 
        ("Required Files", test_required_files),
        ("Pickle Files", test_pickle_files),
        ("App Import", test_app_imports)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\nTesting: {test_name}")
        print("-" * 30)
        result = test_func()
        results.append(result)
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    if all(results):
        print("SUCCESS! Your setup is ready to run!")
        print("\nNext steps:")
        print("1. Run: python app.py")
        print("2. Open: http://localhost:5000")
        print("3. Test the application!")
    else:
        print("ISSUES DETECTED! Please fix the failed tests above.")
        print("\nCommon solutions:")
        print("1. Install packages: pip install -r requirements.txt")
        print("2. Check file locations and permissions")
        print("3. Verify Python version (3.7+ required)")
    
    print("\nFor detailed help, see: SETUP_GUIDE.md")

if __name__ == "__main__":
    main()