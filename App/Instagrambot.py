import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import random
from instabot import Bot

# Load the CSV file
file_path = 'Examplar Prospects List.csv'
df = pd.read_csv(file_path)

# Assuming the website links are in column 'F'
websites = df.iloc[:, 5]  # Adjust the column index as necessary

# Instagram bot setup
bot = Bot()
bot.login(username="pixelevate_solutions", password="businessmodel1@rao")

def extract_instagram_username(instagram_url):
    # This function assumes that the Instagram URL is in the form of https://www.instagram.com/username/
    # It extracts 'username' from the URL
    match = re.search(r"instagram.com/([^/?#&]+)", instagram_url)
    if match:
        return match.group(1)
    else:
        return None

# List to hold all extracted Instagram usernames
all_usernames = []

for url in websites:
    print(f"Checking {url}...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if "instagram.com" in href:
                    username = extract_instagram_username(href)
                    if username and username not in all_usernames:
                        all_usernames.append(username)
        else:
            print(f"Could not retrieve {url}")
    except requests.RequestException as e:
        print(f"Error: {e}")

# Selecting one random username from the list
if all_usernames:
    selected_username = random.choice(all_usernames)

    # Sending a message to the selected username
    bot.send_message("Hi, How are you", [selected_username])
    print(f"Message sent to {selected_username}")
else:
    print("No Instagram usernames found to message.")
