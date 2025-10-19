# 🚀 QUICK START GUIDE - ZAPIER MCP OAUTH VERSION

## What's New in 2025?
- ✅ **Instagram now uses OAuth** - No manual tokens!
- ✅ **Facebook login** handles everything
- ✅ **Automatic token management** by Zapier
- ⚠️ **Slack still needs tokens** (for now)

## 5-Minute Setup

### Step 1: Slack Tokens (2 minutes)
```bash
# Create .env file with Slack tokens only
cat > .env << 'EOF'
SLACK_BOT_TOKEN="xoxb-YOUR-TOKEN"
SLACK_USER_TOKEN="xoxp-YOUR-TOKEN"  
SLACK_CHANNEL_ID="C-CHANNEL-ID"
SLACK_BOT_USER_ID="U-BOT-ID"
EOF
```

### Step 2: Connect Instagram via OAuth (2 minutes)
```bash
# In Claude Code terminal
claude mcp zapier add_tools

# Then:
# 1. Choose "Instagram for Business"
# 2. Click "Connect a new account"
# 3. Facebook window opens
# 4. Log in with your Facebook
# 5. Select your Facebook Page
# 6. Grant permissions# 7. Done! No Instagram tokens needed!
```

### Step 3: Test Everything (1 minute)
```bash
# Test Instagram connection
claude mcp zapier instagram_for_business_publish_photo_s '{
  "instructions": "Test connection",
  "caption": "TEST",
  "media": "https://example.com/test.jpg"
}'

# Test Slack search
claude mcp zapier slack_find_message '{
  "instructions": "Find Legacy Wine MCP Bot messages",
  "query": "from:Legacy Wine MCP Bot"
}'
```

### Step 4: Run Automation
```bash
# Navigate to folder
cd ~/Desktop/CLAUD\ RECON

# Run updated automation
python3 claude-code-zap-v2.py

# Or use the OAuth setup script
./setup-oauth-v2.sh
```

## How The OAuth Flow Works

1. **You trigger**: React with ✅ on Slack message
2. **Automation detects**: Finds reaction via Slack API
3. **Parses content**: Extracts caption, image, hashtags4. **Posts via OAuth**: Zapier handles Instagram auth automatically
5. **No tokens expire**: OAuth refreshes automatically!

## Message Format (Same as Before)

Post this in #claude as Legacy Wine MCP Bot:
```
Caption: 🍷 Sanford Bike Week is HERE! Fuel your ride with our premium selection!
Image: https://images.unsplash.com/photo-1558981852-426c6c22a060
Publish: Now
#SanfordBikeWeek #LegacyWine #BikeWeek2025
```

## If Instagram Account Not Showing

This is a known issue (Dec 2024). Fix:

1. Go to: https://www.facebook.com/settings?tab=business_tools
2. Find Zapier → "View and edit"
3. Enable Instagram permissions
4. Disconnect/reconnect Instagram on Facebook Page
5. Reconnect in Zapier

Or use manual ID method (see INSTAGRAM_OAUTH_TROUBLESHOOTING.md)

## Benefits of OAuth vs Old Token Method

| Old Method (Tokens) | New Method (OAuth) |
|-------------------|-------------------|
| Manual token generation | Automatic via Facebook |
| Expires every 60 days | Auto-refreshes forever |
| Complex setup | Simple click & connect |
| Store sensitive tokens | Zapier handles security |

## Ready to Go! 🎉

Your automation is now using modern OAuth authentication.
No more expired tokens or manual refreshing!