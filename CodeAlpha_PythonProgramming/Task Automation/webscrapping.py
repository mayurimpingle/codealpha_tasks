import requests
from bs4 import BeautifulSoup

# Step 1: Fetch webpage
url = "https://www.python.org"   # Authentic, official Python website
response = requests.get(url)

if response.status_code == 200:
    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip()

    # Step 3: Save to file
    with open("title.txt", "w", encoding="utf-8") as f:
        f.write(title)

    print("Webpage title saved to title.txt")
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)