GuardianEye – Cybersecurity Multi-Feature Detection Prototype
GuardianEye is an all-in-one cybersecurity prototype that empowers users to proactively detect email phishing, suspicious URLs, and leaked media content. With a user-friendly Streamlit dashboard and robust Python backend, GuardianEye combines real-time content analysis with ethical, offline data handling for practical protection in 2025 and beyond.

Table of Contents
Features

Project Motivation

Tech Stack

Folder Structure

Setup & Installation

Usage

Screenshots

Customization

License

Features
Email Scanner: Analyzes pasted emails for phishing keywords, suspicious links, and spoofing patterns.

URL Analyzer: Detects dangerous URLs based on heuristics like punycode usage, IP domains, and suspicious patterns.

Media Leak Check: Flags uploaded images by comparing perceptual hashes against a known leak dataset.

Central Dashboard: Streamlit-powered UI lets you use all modules in one place, with real-time results and logs.

Offline & Ethical: All scanning is performed on your device, with no data sent to third parties.

(Planned) Logging and Analytics: Securely logs user inputs and scan metrics for analysis and improvement.

Project Motivation
With a growing rise in cyberattacks—ranging from phishing emails and malicious links to leaked media—GuardianEye was created for organizations and individuals who need a unified, practical, and modern security tool. Unlike many single-purpose or overly technical solutions, GuardianEye demonstrates an integrated defense workflow that’s accessible and effective.

Tech Stack
Frontend: Streamlit (Python)

Backend: Python (Modules: email, regex, urllib, imagehash, PIL)

Storage: Local JSON logs (for analytics)

Other: Modular Python codebase for easy expansion

Folder Structure
text
GuardianEye/
├── app.py
├── modules/
│   ├── email_scanner.py
│   ├── url_analyzer.py
│   ├── media_leak_check.py
│   └── logger.py
├── dataset/
│   └── known_leaks/
├── logs/
│   └── analytics.json
Setup & Installation
Clone the repository

bash
git clone https://github.com/yourname/GuardianEye.git
cd GuardianEye
Install dependencies

bash
pip install streamlit pillow imagehash
Run the dashboard

bash
streamlit run app.py
(Optional) Add known leaked images
Place images in dataset/known_leaks/ for media hash comparison.

Usage
Launch the dashboard using the setup instructions.

Use the Email Scanner tab to analyze emails for phishing.

Use the URL Analyzer to instantly check the safety of suspicious links.

Upload images in the Media Leak Check tab to search for duplicates/leaks.

All results display instantly in the dashboard and are also logged for later review.

s or visualizations.

Change dataset references to support larger or external leak databases.
