# Google News Search Automation

This script runs scheduled Google searches using the Google Custom Search API, filtered to news sources.

## Features
- Automated Google searches based on a schedule (ex. hourly, daily)
- Filters to reputable news sources via Custom Search Engine
- (strech goal) Stores past results in SQLite to avoid duplicates
- (stretch goal) Sends results via email

## Requirements
1. You will need to set up a Programmable Search Engine with Google, and set which sites to search on there.
2. You will need a Google Custom Search API key.

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
