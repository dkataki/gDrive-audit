📊 Google Drive File Audit - Internal Productivity App

This is a personal  internal-use productivity tool designed to help you stay informed about changes to key Google Drive files—such as Google Slides and Google Sheets—right from your desktop.

🧩 What It Does

Reads a list of Google Drive document URLs from a simple file-list.txt file
Fetches last modified time and last modified by metadata for each document
Displays the audit output directly in your terminal or saves it to a summary file
Can be triggered via a Mac desktop shortcut for quick, one-click access
🗂️ File Structure

.
├── audit_drive_files.py      # Main Python script
├── file-list.txt             # Your list of Google Slides/Sheets URLs
└── README.md                 # This documentation
✍️ How to Use

Add File URLs to file-list.txt
Each line should contain a valid Google Docs/Sheets/Slides URL:
https://docs.google.com/spreadsheets/d/1abc123XYZ...
https://docs.google.com/presentation/d/1def456LMN...
Run the Python Script
python3 audit_drive_files.py
View Output
You'll see who last modified each file and when.
Create Mac Shortcut (Optional)
Use macOS Shortcuts to run the script with a hotkey or from the menu bar.
🔒 Security Note

This app is designed for local use only and does not transmit or store your data externally. OAuth credentials are stored securely on your device via Google's authentication flow.
