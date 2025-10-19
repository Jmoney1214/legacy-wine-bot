# 🍷 Legacy Wine Slack-to-Social Automation V2.0

**UPDATED FOR 2025: Instagram now uses OAuth - No tokens needed!**

## 📋 What's New?

### Version 2.0 Changes (January 2025)
- ✅ **Instagram OAuth Integration** - Connect via Facebook, no manual tokens
- ✅ **Automatic token refresh** - Never expires
- ✅ **Simplified setup** - 5 minutes vs 30 minutes
- ✅ **Better reliability** - OAuth handles authentication
- ⚠️ **Slack tokens still required** (for now)

## 🚀 Quick Start

### Prerequisites
- Instagram Business Account (not personal)
- Facebook Page connected to Instagram
- Slack workspace with #claude channel
- Claude Code with Zapier MCP

### Setup (5 minutes)

1. **Get Slack Tokens** (see TOKEN_SETUP_GUIDE.md)
2. **Connect Instagram via OAuth:**
   ```bash
   claude mcp zapier add_tools
   # Choose Instagram for Business
   # Click Connect → Facebook OAuth
   ```
3. **Run automation:**
   ```bash
   python3 claude-code-zap-v2.py
   ```