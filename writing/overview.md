---
slug: github-journal-writing-overview
id: github-journal-writing-overview
title: 'My Journal: A Static Site and Knowledge Management System'
repo: justin-napolitano/journal
githubUrl: https://github.com/justin-napolitano/journal
generatedAt: '2025-11-24T17:36:03.242Z'
source: github-auto
summary: >-
  I built this project called "journal" because I wanted a streamlined way to
  manage my notes, articles, and tutorials. It’s a static site generator using
  Sphinx that’s capable of doing much more than just displaying content. Here’s
  a rundown of what it is, why it exists, the tech behind it, and my plans for
  the future.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I built this project called "journal" because I wanted a streamlined way to manage my notes, articles, and tutorials. It’s a static site generator using Sphinx that’s capable of doing much more than just displaying content. Here’s a rundown of what it is, why it exists, the tech behind it, and my plans for the future.

## What is Journal?

At its core, journal is a combination of a static site and a knowledge management system. It’s designed to help me organize and share a considerable collection of articles and tutorials. The aim was to create something that doesn’t just work, but also emphasizes simplicity in both use and deployment. 

### Why It Exists

I needed a way to not only write but archive and retrieve information efficiently. A jumbled mess of markdown files in my local directory just wouldn’t cut it anymore. I wanted a central hub where I could maintain a growing library of information without frills. Plus, I enjoy the control that a self-hosted system provides.

## Key Features

- **Static Site Generation with Sphinx**: Easy to convert my markdown files into a well-structured HTML format.
- **Automated Deployment and Backup**: I've integrated scripts that handle deployment to GitHub Pages and backup to Dropbox, keeping my data safe.
- **Extensive Content Collection**: This isn’t just a diary; it’s filled with articles, tutorials, and references all in one place.
- **Bibliography Management**: Citation support helps me manage references seamlessly.
- **Integration with Dropbox**: Automated backups ensure my content is never lost.
- **Build Automation**: Using Makefile and Python scripts keeps the process efficient.

## Tech Stack

Here’s a quick look at the tech I used in this project:

- **Primary Language**: HTML, generated via Sphinx.
- **Scripting**: Bash and Python (version 3.5+).
- **Documentation Formats**: reStructuredText, Markdown, and MyST.
- **Build Tools**: Make and Python subprocess.
- **Deployment**: Using `ghp-import` to manage GitHub Pages.
- **Backup**: Dropbox API integration for file storage.

## Getting Started

If you’re interested in trying out journal, here’s how to get it up and running:

### Prerequisites

- Python 3.5 or higher
- Dropbox SDK for Python (`pip install dropbox`)
- Make
- Bash shell

### Installation

Clone the repo and install dependencies quickly:

```bash
git clone https://github.com/justin-napolitano/journal.git
cd journal
pip install -r requirements.txt
```

### Build the Documentation

Building the documentation is as simple as running:

```bash
make clean
make html
```

### Deployment

A quick call to a script does all the work:

```bash
./deploy.sh
```

For backup, run:

```bash
python3 backup_html.py
```

## Project Structure

Here’s a brief overview of my project structure. It may look like a lot at first, but everything has its place:

```
journal/
├── acp.sh                  
├── backup_html.py          
├── deploy.sh               
├── Makefile                
├── requirements.txt        
├── source/                 
│   ├── _toc.yml            
│   ├── conf.py             
│   ├── index.md            
│   └── parts/              
└── todo/                   
```

Each script and folder plays a specific role in keeping things organized and functional.

## Key Design Decisions

I made several design decisions that shaped the final product. One of the main ones was the use of Sphinx. It’s powerful for documentation, and I wanted the best for my content. Also, the choice to implement backup and deployment scripts was crucial. There’s peace of mind knowing that my content is both live and safely stored in the cloud.

## Trade-offs

No project comes without its trade-offs. I opted for a simpler Sphinx setup over pursuing a full-fledged CMS. This means that while it’s lightweight, it may not have all the features a heavy-duty solution offers. But for my needs, this simplicity has been a blessing, streamlining my focus back to content rather than overly complex configurations.

## Future Work / Roadmap

Looking ahead, I see several areas for improvement:

- **Automation Scripts**: I want to enhance error handling and logging in my current scripts. It’s crucial for ensuring reliability.
- **Expand Documentation**: Additional tutorials would be great; the more guidance, the better.
- **CI/CD Integration**: Automating deployment through CI/CD would save me time and reduce headaches.
- **Support for PDF Output**: Adding support for generating PDF files via LaTeX could broaden accessibility.
- **Script Refactoring**: I plan to clear up the code for better readability and maintainability.

## Keep in Touch

I've put a ton of work into this project, and I’m excited to keep the updates coming. If you want to follow along, I share updates on Mastodon, Bluesky, and Twitter/X. 

In the meantime, head over to the [repo](https://github.com/justin-napolitano/journal) if you want to dive into the code or have a look at the [documentation](https://docs.jnapolitano.io). I’d love to hear your thoughts or see how you’re using it!
