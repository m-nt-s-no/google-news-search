import newspaper
from newspaper.article import ArticleException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def fetch_with_selenium(url, wait_time = 5):
        """Fetch HTML using Selenium (for JS-rendered sites)"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.get(url)
            time.sleep(wait_time)  # Wait for JS to execute
            html = driver.page_source
            return html
        finally:
            driver.quit()

def fetch_article(url):
    """Fetch article with newspaper4k, using Selenium for JS-rendered content"""
    a = newspaper.Article(url)
    try:
        a.download()
        a.parse()
    except ArticleException:
        html = fetch_with_selenium(url)
        a = newspaper.Article(url, input_html=html)
        a.parse()
    return a # verify h/a/c/d completeness before returning article obj?

def get_content(results):
    for query in results:
        hits = results[query]
        if not hits:
            continue
        for hit in hits:
            url = hit['link']
            a = fetch_article(url)