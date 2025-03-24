import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LinkedIn API credentials from .env file
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
MEMBER_ID = os.getenv("LINKEDIN_MEMBER_ID")

# Validate credentials
if not ACCESS_TOKEN or not MEMBER_ID:
    raise ValueError("Missing LinkedIn API credentials. Check your .env file.")

# LinkedIn API URL
LINKEDIN_API_URL = "https://api.linkedin.com/v2/ugcPosts"

# Correctly formatted author field
AUTHOR_URN = f"urn:li:person:{MEMBER_ID}"

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

# Payload for posting content
payload = {
    "author": AUTHOR_URN,  # Correct format
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "This is a test post from my LinkedIn API integration!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

# Send the request
response = requests.post(LINKEDIN_API_URL, headers=HEADERS, json=payload)

# Handle the response
if response.status_code == 201:
    print("✅ Successfully posted to LinkedIn!")
else:
    print(f"❌ Failed to post: {response.status_code} - {response.text}")
