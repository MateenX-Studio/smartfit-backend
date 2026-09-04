# Import library to read the .env file
import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

# Get Supabase credentials
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Create the Supabase client (connection)
supabase = create_client(supabase_url, supabase_key)

print("Supabase connected successfully!")
print(f"Connected to: {supabase_url}")