import os
from linkedin_api import Linkedin
from dotenv import load_dotenv

load_dotenv()

# LinkedIn credentials
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

api = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

def post_linkedin(text: str):
    """
    Posts a share on LinkedIn with the provided text.
    """
    response = api.post_share(comment=text)
    return response

if __name__ == "__main__":
    sample_text = "This is a sample LinkedIn post from the AI Social Media Agent."
    print(post_linkedin(sample_text))