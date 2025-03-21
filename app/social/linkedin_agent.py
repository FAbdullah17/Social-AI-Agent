import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
LINKEDIN_URN_ID = os.getenv("LINKEDIN_URN_ID")

def post_linkedin_update(post_content):
    """
    Posts a status update to LinkedIn using the official UGC Posts API.
    
    Args:
        post_content (str): The text content of the post.
    
    Returns:
        None; prints the result.
    """
    api_url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    payload = {
        "author": f"urn:li:person:{LINKEDIN_URN_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": post_content},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 201:
        print("Post successful!")
    else:
        print(f"Failed to post: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    sample_text = "🚀 Automating LinkedIn posts using Python and the official LinkedIn API! #AI #Automation"
    post_linkedin_update(sample_text)
