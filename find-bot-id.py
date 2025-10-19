#!/usr/bin/env python3
"""
Find your Slack Bot User ID
Run this after adding your bot token to .env
"""

import os
import requests
from pathlib import Path

def load_env():
    """Load environment variables from .env file"""
    env_file = Path('.env')
    if not env_file.exists():
        print("❌ No .env file found!")
        print("Create one with: SLACK_BOT_TOKEN='xoxb-YOUR-TOKEN'")
        return None
    
    env_vars = {}
    with open(env_file, 'r') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                env_vars[key] = value.strip('"\'')
    
    return env_vars

def find_bot_user_id():
    """Find the bot user ID using auth.test"""
    env = load_env()
    if not env:
        return
    
    token = env.get('SLACK_BOT_TOKEN')
    if not token or 'YOUR' in token:        print("❌ Bot token not configured in .env")
        print("Add: SLACK_BOT_TOKEN='xoxb-YOUR-ACTUAL-TOKEN'")
        return
    
    print("🔍 Finding Bot User ID...")
    print("=" * 50)
    
    # Method 1: auth.test
    response = requests.get(
        "https://slack.com/api/auth.test",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    if response.status_code == 200:
        data = response.json()
        if data.get("ok"):
            print("✅ Found Bot Information:")
            print(f"   Bot User ID: {data.get('user_id')}")
            print(f"   Bot Username: {data.get('user')}")
            print(f"   Team: {data.get('team')}")
            print(f"   Team ID: {data.get('team_id')}")
            
            # Save to file
            with open('BOT_USER_ID.txt', 'w') as f:
                f.write(f"BOT_USER_ID={data.get('user_id')}\n")
                f.write(f"BOT_USERNAME={data.get('user')}\n")
            
            print("\n📝 Saved to BOT_USER_ID.txt")
            print("\n🎯 Add this to your .env file:")
            print(f"   SLACK_BOT_USER_ID=\"{data.get('user_id')}\"")
            
            return data.get('user_id')        else:
            print(f"❌ Error: {data.get('error')}")
            if data.get('error') == 'invalid_auth':
                print("   Token is invalid. Check your bot token.")
            elif data.get('error') == 'not_authed':
                print("   Token is missing or malformed.")
    else:
        print(f"❌ HTTP Error: {response.status_code}")

def find_bot_in_users_list():
    """Alternative: Search for bot in users list"""
    env = load_env()
    if not env:
        return
    
    token = env.get('SLACK_BOT_TOKEN')
    if not token or 'YOUR' in token:
        return
    
    print("\n🔍 Searching users list for 'Legacy Wine'...")
    
    response = requests.get(
        "https://slack.com/api/users.list",
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": 200}
    )
    
    if response.status_code == 200:
        data = response.json()
        if data.get("ok"):
            for user in data.get("members", []):
                name = user.get("real_name", "").lower()
                profile_name = user.get("profile", {}).get("real_name", "").lower()                if "legacy" in name or "wine" in name or "legacy" in profile_name or "wine" in profile_name:
                    print(f"\n📌 Found potential match:")
                    print(f"   Name: {user.get('real_name')}")
                    print(f"   ID: {user.get('id')}")
                    print(f"   Is Bot: {user.get('is_bot')}")
                    if user.get('is_bot'):
                        print(f"   ✅ This is likely your bot!")

if __name__ == "__main__":
    print("🤖 SLACK BOT USER ID FINDER")
    print("=" * 50)
    
    # Try auth.test first
    bot_id = find_bot_user_id()
    
    # If not found, try users list
    if not bot_id:
        find_bot_in_users_list()
    
    print("\n" + "=" * 50)
    print("✨ Done!")