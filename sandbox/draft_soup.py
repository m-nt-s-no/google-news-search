from bs4 import BeautifulSoup
import requests
import re

url = "https://techcrunch.com/author/ronjourn/page/83/?__hstc=259903189.2f3f33a24b44870ec4a577029c49e44b.1726185600094.1726185600095.1726185600096.1&__hssc=259903189.1.1726185600097&__hsfp=451136374"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags_with_specific_text = soup.find_all(string="Adobe")
print(f"Found {len(tags_with_specific_text)} tags with the specific text.")
print(tags_with_specific_text)
