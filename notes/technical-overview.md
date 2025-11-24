---
slug: github-journal-note-technical-overview
id: github-journal-note-technical-overview
title: Journal Repository Overview
repo: justin-napolitano/journal
githubUrl: https://github.com/justin-napolitano/journal
generatedAt: '2025-11-24T18:39:51.792Z'
source: github-auto
summary: >-
  The **journal** repo is a static site generator and knowledge management tool
  built with Sphinx. It automates deployment and backups while storing articles
  and tutorials.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

The **journal** repo is a static site generator and knowledge management tool built with Sphinx. It automates deployment and backups while storing articles and tutorials. 

### Key Features
- Generates static HTML output with Sphinx
- Automated backup to Dropbox
- Built with Makefile and Python scripts

### Getting Started
1. **Clone the repo:**
   ```bash
   git clone https://github.com/justin-napolitano/journal.git
   cd journal
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Build the documentation:**
   ```bash
   make clean
   make html
   ```
4. **Deploy your site to GitHub Pages:**
   ```bash
   ./deploy.sh
   ```
5. **Backup your build:**
   ```bash
   python3 backup_html.py
   ```

### Gotchas
Ensure Python 3.5+ and the Dropbox SDK are installed. Double-check the `requirements.txt` for any dependencies that you might need.
