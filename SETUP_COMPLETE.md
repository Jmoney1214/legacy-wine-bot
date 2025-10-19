# ✅ LEGACY WINE AUTOMATION - COMPLETE SETUP

## 📂 Your CLAUD RECON folder now contains:

### Core Files:
- `slack-social-zap-config.json` - Main configuration
- `claude-code-zap-execution.py` - Python automation script
- `zapier-mcp-integration.js` - Node.js alternative
- `start-automation.sh` - Quick start script
- `verify-setup.py` - Setup verification tool

### Documentation:
- `README.md` - Overview and quick start
- `TOKEN_SETUP_GUIDE.md` - Complete token setup instructions
- `ZAPIER_MCP_COMMANDS.md` - Zapier MCP command reference
- `CLAUDE_CODE_COMMANDS.txt` - Copy-paste commands for Claude Code

### Configuration:
- `.env.example` - Environment template (copy to .env)

## 🎯 NEXT STEPS:

### 1. Get Your Tokens
Open `TOKEN_SETUP_GUIDE.md` for detailed instructions on getting:
- Slack Bot Token (xoxb-...)
- Slack User Token (xoxp-...)
- Instagram Access Token
- Zapier API Key
### 2. Create Your .env File
```bash
cd ~/Desktop/CLAUD\ RECON
cp .env.example .env
nano .env  # Add your actual tokens
```

### 3. Run in Claude Code Terminal
```bash
# Navigate to folder
cd ~/Desktop/CLAUD\ RECON

# Verify setup
python3 verify-setup.py

# Start automation
python3 claude-code-zap-execution.py
```

## 📱 HOW IT WORKS:

1. **Legacy Wine MCP Bot** posts in #claude:
   ```
   Caption: 🍷 Your message here
   Image: https://your-image-url.jpg
   Publish: Now
   ```

2. **You react** with ✅ (white_check_mark)

3. **Automation triggers** and posts to Instagram

4. **Confirmation** sent back to #claude
## ⚡ QUICK TEST:

### Test Slack Connection:
```bash
claude mcp zapier slack_find_user_by_name '{"full_name": "Legacy Wine MCP Bot", "instructions": "Find bot"}'
```

### Test Instagram (dry run):
```bash
claude mcp zapier instagram_for_business_publish_photo_s '{"instructions": "Test", "caption": "TEST", "media": "https://example.com/test.jpg", "instagramPageId": "YOUR_PAGE"}'
```

## 🔒 SECURITY REMINDERS:

1. **NEVER** commit .env to Git
2. Add to .gitignore: `.env`
3. Rotate tokens regularly
4. Use read-only permissions where possible

## 💡 TROUBLESHOOTING:

- **"Channel not found"** → Use Channel ID (starts with C), not name
- **"Invalid token"** → Regenerate in Slack API dashboard
- **"Instagram failed"** → Ensure Business Account + Facebook Page connected
- **"No reactions found"** → Check bot has reactions:read permission

## 🎉 READY TO AUTOMATE!

Your Legacy Wine Slack-to-Instagram automation is fully configured.
Just add your tokens to .env and run: `python3 claude-code-zap-execution.py`

Questions? Check the documentation files or run `python3 verify-setup.py`