#!/usr/bin/python3
"""
A function that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Fetches and prints the titles of the top ten hot posts from a subreddit.
    If the subreddit is invalid or has no posts, prints None.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0 (by /u/yourusername)"}
    response = requests.get(url, headers=headers, allow_redirects=False, params={"limit": 10})
    
    if response.status_code != 200:
        print("None")
        return
    
    try:
        jsonData = response.json()
        posts = jsonData.get("data", {}).get("children", [])
        
        if not posts:
            print("None")
            return
        
        for post in posts:
            print(post.get("data", {}).get("title", "None"))
    except (ValueError, KeyError):
        print("None")


# Example Usage
# top_ten("programming")  # Should print top 10 post titles or None
