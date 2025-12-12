#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
SCRIPT: open_html.py
DESCRIPTION: Automatically finds and opens all HTML files (.html) in the 
             specified directory using the system's default web browser. 
             Opens each file in a new browser tab/window.
AUTHOR: Amir Ghavam / Gemini AI
VERSION: 1.1
USAGE: python3 open_html.py [optional_directory_path]
DEPENDENCIES: Standard Python libraries only (os, sys, webbrowser).
================================================================================
"""

import os        # For interacting with the operating system (paths, directories)
import sys       # For accessing command-line arguments (sys.argv)
import webbrowser # For opening files/URLs in the default web browser

def open_all_htmls(target_dir=None):
    """
    Scans a directory for HTML files and opens them in the default web browser.
    
    Args:
        target_dir (str, optional): The directory path to scan. If None, 
                                    the current working directory is used.
    """
    
    # 1. Determine the target directory.
    # Use the passed argument or default to the current working directory (cwd).
    if target_dir is None:
        cwd = os.getcwd()
    else:
        # Resolve the absolute path to handle relative paths passed as arguments
        cwd = os.path.abspath(target_dir)

    # 2. Validate the directory.
    if not os.path.isdir(cwd):
        print(f"Error: Directory '{cwd}' not found or is not a directory.")
        sys.exit(1)

    print(f"--- HTML File Opener ---")
    print(f"Searching for HTML files in: {cwd}")
    
    # 3. List all items (files/folders) in the target directory.
    try:
        files = os.listdir(cwd)
    except PermissionError:
        print(f"Error: Permission denied to access directory: {cwd}")
        sys.exit(1)

    # 4. Filter for files that end with '.html' (case-insensitive).
    # This list comprehension checks two things:
    # a) That the file name ends with '.html' (after converting to lowercase).
    # b) That the item is actually a file (not a subdirectory).
    html_files = [f for f in files 
                  if f.lower().endswith('.html') 
                  and os.path.isfile(os.path.join(cwd, f))]
    
    
    if not html_files:
        print("No HTML files found in the current directory.")
        return

    print(f"\nFound {len(html_files)} HTML file(s). Opening them now...")
    
    # 5. Iterate through the found HTML files and open them.
    for filename in html_files:
        # Construct the full, absolute file path for reliability.
        file_path = os.path.join(cwd, filename)
        
        # Construct the file URI. Using 'file://' with an absolute path 
        # is the standard and most reliable way for webbrowser.open functions.
        # Note: os.path.abspath ensures the path is fully resolved, improving cross-platform reliability.
        absolute_uri = 'file://' + os.path.abspath(file_path)
        
        print(f"  -> Opening: {filename}")
        
        # webbrowser.open_new_tab() attempts to open the URI in a new browser tab.
        # This is generally preferred over open() which might reuse an existing window.
        webbrowser.open_new_tab(absolute_uri)

    print("\n--- Finished ---")
    print(f"All {len(html_files)} files have been sent to the default browser.")


if __name__ == "__main__":
    
    # Check if a directory path was provided as a command-line argument.
    if len(sys.argv) > 1:
        # If an argument is provided, pass it to the function.
        target_directory = sys.argv[1]
    else:
        # Otherwise, the function will default to the current directory.
        target_directory = None
        
    # Execute the main function.
    open_all_htmls(target_directory)