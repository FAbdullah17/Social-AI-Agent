import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

print("Client ID:", os.getenv("LINKEDIN_CLIENT_ID"))
print("Client Secret:", os.getenv("LINKEDIN_CLIENT_SECRET"))
print("Redirect URI:", os.getenv("LINKEDIN_REDIRECT_URI"))
print("Access Token:", os.getenv("LINKEDIN_ACCESS_TOKEN"))
print("Member ID:", os.getenv("LINKEDIN_MEMBER_ID"))