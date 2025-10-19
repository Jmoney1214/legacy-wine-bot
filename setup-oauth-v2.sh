#!/bin/bash

# Legacy Wine Automation Setup V2 - OAuth Edition
# No Instagram tokens needed!

echo "🍷 LEGACY WINE AUTOMATION V2.0 - OAUTH SETUP"
echo "============================================="
echo "Instagram now uses OAuth - NO TOKENS NEEDED!"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "📋 SETUP CHECKLIST:"
echo ""

echo "1️⃣  SLACK SETUP (Tokens still needed)"
echo "   ✓ Create Slack App at https://api.slack.com/apps"
echo "   ✓ Get Bot Token (xoxb-...)"
echo "   ✓ Get User Token (xoxp-...)"
echo "   ✓ Get Channel ID for #claude"
echo ""

echo "2️⃣  INSTAGRAM SETUP (OAuth - No tokens!)"
echo "   ✓ Instagram Business Account (not personal)"
echo "   ✓ Facebook Page connected to Instagram"
echo "   ✓ Admin access to both"
echo ""

echo "3️⃣  ZAPIER MCP SETUP"echo "   Run these commands in Claude Code:"
echo ""
echo -e "${GREEN}# Add Instagram for Business integration${NC}"
echo "claude mcp zapier add_tools"
echo ""
echo -e "${GREEN}# Connect Instagram (OAuth flow)${NC}"
echo "1. Choose 'Instagram for Business'"
echo "2. Click 'Connect a new account'"
echo "3. Facebook OAuth window opens"
echo "4. Log in with your Facebook"
echo "5. Select your Facebook Page"
echo "6. Grant permissions"
echo "7. Done - No tokens needed!"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 CREATE .env FILE (Slack tokens only):"
echo ""

cat > .env.slack << 'EOF'
# Slack Tokens (still required)
SLACK_BOT_TOKEN="xoxb-YOUR-TOKEN"
SLACK_USER_TOKEN="xoxp-YOUR-TOKEN"
SLACK_CHANNEL_ID="C-YOUR-CHANNEL-ID"
SLACK_BOT_USER_ID="U-YOUR-BOT-ID"

# Instagram uses OAuth now - no tokens needed!
INSTAGRAM_CONNECTION="Connected via OAuth"
EOF