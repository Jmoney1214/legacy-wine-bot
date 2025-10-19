#!/bin/bash

# Legacy Wine Slack-to-Social Quick Start for Claude Code
# Run this in Claude Code terminal

echo "🍷 LEGACY WINE SOCIAL AUTOMATION QUICKSTART"
echo "==========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Check for required files
echo "📁 Checking required files..."
if [ -f "slack-social-zap-config.json" ]; then
    echo -e "${GREEN}✓${NC} Config file found"
else
    echo -e "${RED}✗${NC} Config file missing"
    exit 1
fi

# Step 2: Load environment variables
if [ -f ".env" ]; then
    echo -e "${GREEN}✓${NC} Loading environment variables"
    source .env
else    echo -e "${YELLOW}⚠${NC} No .env file found. Creating template..."
    
    cat > .env << 'EOF'
# Slack Configuration
SLACK_BOT_TOKEN="xoxb-YOUR-TOKEN"
SLACK_USER_TOKEN="xoxp-YOUR-TOKEN"
SLACK_CHANNEL_ID="C-YOUR-CHANNEL-ID"
SLACK_BOT_USER_ID="U-YOUR-BOT-ID"

# Instagram Configuration
INSTAGRAM_ACCOUNT_ID="YOUR-ACCOUNT-ID"
INSTAGRAM_ACCESS_TOKEN="YOUR-ACCESS-TOKEN"
FACEBOOK_PAGE_ID="YOUR-PAGE-ID"

# Zapier Configuration
ZAPIER_API_KEY="YOUR-API-KEY"
EOF

    echo -e "${YELLOW}⚠${NC} Please edit .env file with your tokens"
    exit 1
fi

echo ""
echo "🔐 Injecting tokens into configuration..."

# Use Python to update the JSON config
python3 << 'PYTHON_SCRIPT'
import json
import os