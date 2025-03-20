import os
from dotenv import load_dotenv
from linkedin_api import Linkedin

load_dotenv()

LI_AT_COOKIE = os.getenv("LI_AT_COOKIE")
JSESSIONID = os.getenv("JSESSIONID")

api = Linkedin("", "", cookies={"li_at": LI_AT_COOKIE, "JSESSIONID": JSESSIONID})

def post_linkedin_update(text):
    """Posts a status update to LinkedIn."""
    try:
        response = api.submit_share(text=text)
        print("Post successful:", response)
    except Exception as e:
        print("Failed to post:", e)

if __name__ == "__main__":
    sample_text = "🚀 Automating LinkedIn posts using Python! #AI #Automation"
    post_linkedin_update(sample_text)