# Google News Search Automation

This script runs scheduled Google News searches using the Google Custom Search API, filters results to news sources, and can email the top results.

## Features
- Automated Google News searches based on a schedule (ex. hourly, daily)
- Filters to reputable news sources via Custom Search Engine
- (strech goal) Stores past results in SQLite to avoid duplicates
- (stretch goal) Sends results via email

## Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/google-news-search.git
    cd google-news-search
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create .env file based on .env.example:
    ```bash
    cp .env.example .env
    ```
4. Run the script:
    ```bash
    python news_search.py
    ```