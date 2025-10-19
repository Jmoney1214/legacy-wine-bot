# 🤖 HOW TO FIND YOUR BOT USER ID

## Method 1: Slack App/Browser (Easiest)

1. **Open Slack** (web or desktop app)
2. **Find your bot** (Legacy Wine MCP Bot) in the workspace
3. **Click on the bot's name** to open its profile
4. **Click the three dots** (More actions) 
5. **Select "View full profile"**
6. **Click the three dots again** in the profile modal
7. **Select "Copy member ID"**

The ID will look like: `U1234567890` (starts with U)

## Method 2: Using Slack API Test

Run this command with your bot token:

```bash
curl -X GET https://slack.com/api/auth.test \
  -H "Authorization: Bearer xoxb-YOUR-BOT-TOKEN"
```

Response will include:
```json
{
  "ok": true,
  "url": "https://yourworkspace.slack.com/",
  "team": "Your Workspace",
  "user": "legacy_wine_mcp_bot",
  "user_id": "U1234567890",  <-- THIS IS YOUR BOT USER ID
  "team_id": "T1234567890"}
```

## Method 3: Slack Web Inspector

1. Open Slack in your web browser
2. Right-click on your bot (Legacy Wine MCP Bot)
3. Select "Inspect Element"
4. Look for `data-user-id="U..."` in the HTML
5. That's your bot user ID

## Method 4: Using Python

```python
import requests

BOT_TOKEN = "xoxb-YOUR-BOT-TOKEN"

# Get bot user info
response = requests.get(
    "https://slack.com/api/auth.test",
    headers={"Authorization": f"Bearer {BOT_TOKEN}"}
)

data = response.json()
if data["ok"]:
    print(f"Bot User ID: {data['user_id']}")
    print(f"Bot Username: {data['user']}")
else:
    print(f"Error: {data['error']}")
```

## Method 5: In Slack App Settings

1. Go to https://api.slack.com/apps
2. Select your app (Legacy Wine Social Poster)3. Go to "OAuth & Permissions"
4. Look under "Bot User OAuth Token"
5. The bot user ID is often shown there

## Method 6: Using Users.list API

```bash
# List all users and search for your bot
curl -X GET "https://slack.com/api/users.list" \
  -H "Authorization: Bearer xoxb-YOUR-BOT-TOKEN" \
  | grep -B 5 -A 5 "Legacy Wine MCP Bot"
```

## Method 7: Zapier MCP Command

In Claude Code, run:

```bash
claude mcp zapier slack_find_user_by_name '{
  "full_name": "Legacy Wine MCP Bot",
  "instructions": "Find the Legacy Wine bot user and return the user ID"
}'
```

## What the Bot User ID Looks Like

- Format: `U1234567890` or `U12AB34CD56`
- Always starts with `U`
- 11-12 characters long
- Alphanumeric (letters and numbers)

## Example Response from auth.test:

```json
{
  "ok": true,
  "url": "https://legacywine.slack.com/",