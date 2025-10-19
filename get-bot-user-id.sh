#!/bin/bash
# Get Bot User ID using Slack API

# Replace with your actual bot token
BOT_TOKEN="xoxb-YOUR-BOT-TOKEN"

# Method 1: Get bot info directly
echo "Method 1: Using bots.info (if you have the bot ID already)"
curl -X POST https://slack.com/api/bots.info \
  -H "Authorization: Bearer $BOT_TOKEN" \
  -H "Content-Type: application/json"

echo ""
echo "Method 2: Get authenticated bot user info"
curl -X GET https://slack.com/api/auth.test \
  -H "Authorization: Bearer $BOT_TOKEN"

echo ""
echo "Method 3: List all users and find your bot"
curl -X GET "https://slack.com/api/users.list?limit=200" \
  -H "Authorization: Bearer $BOT_TOKEN" | grep -A 5 -B 5 "Legacy Wine"