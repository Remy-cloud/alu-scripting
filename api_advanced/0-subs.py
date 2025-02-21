#!/usr/bin/python3
"""
Module that interacts with the Reddit API to retrieve the number of subscribers 
for a given subreddit. Returns 0 if the subreddit is invalid or does not exist.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit using the Reddit API.
    Returns 0 if the subreddit is invalid.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: Number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0

# Example Outputs
# print(number_of_subscribers("python"))  # Existing subreddit
# print(number_of_subscribers("nonexistentsubreddit1234"))  # Non-existing subreddit
