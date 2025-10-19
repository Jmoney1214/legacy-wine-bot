# 🎯 MASTER GUIDE - ZAPIER MCP + INSTAGRAM OAUTH 2025

## ⚡ CRITICAL UPDATE: Instagram Changed Everything!

As of December 2024, Zapier's Instagram integration switched from the deprecated Basic Display API to the **Instagram for Business API with OAuth**. This means:

### What Changed:
- ❌ **OLD**: Manual Instagram Access Tokens (expired every 60 days)
- ✅ **NEW**: OAuth via Facebook (never expires, auto-refreshes)

### What This Means For You:
1. **NO MORE** hunting for Instagram tokens
2. **NO MORE** tokens expiring
3. **NO MORE** complex API setup
4. **JUST** click and connect via Facebook

---

## 📁 File Structure Explanation

### Core Automation Files:
- `claude-code-zap-v2.py` - **USE THIS!** Updated for OAuth
- `slack-social-zap-config-v2.json` - New config format
- `setup-oauth-v2.sh` - Quick setup script

### Old Files (Keep for Reference):
- `claude-code-zap-execution.py` - Old token-based version
- `slack-social-zap-config.json` - Old config with token fields

### Documentation:
- `QUICK_START_OAUTH.md` - Start here!- `INSTAGRAM_OAUTH_TROUBLESHOOTING.md` - Fix connection issues
- `ZAPIER_MCP_OAUTH_COMMANDS.md` - New command reference
- `TOKEN_SETUP_GUIDE.md` - Updated for OAuth

---

## 🚀 START HERE - 5 MINUTE SETUP

### 1️⃣ Get Slack Tokens (2 min)
```bash
# Still need these (Slack hasn't moved to OAuth in Zapier yet)
# Go to https://api.slack.com/apps
# Get: Bot Token (xoxb-...) and User Token (xoxp-...)
```

### 2️⃣ Connect Instagram via OAuth (2 min)
```bash
claude mcp zapier add_tools
```
Then:
1. Choose "Instagram for Business"
2. Click "Connect a new account"
3. Facebook window opens
4. Log in with your Facebook account
5. Select your Facebook Page
6. Grant permissions
7. Done!

### 3️⃣ Create .env File (30 sec)
```bash
cat > ~/Desktop/CLAUD\ RECON/.env << 'EOF'
SLACK_BOT_TOKEN="xoxb-YOUR-TOKEN"
SLACK_USER_TOKEN="xoxp-YOUR-TOKEN"SLACK_CHANNEL_ID="C-CHANNEL-ID"
SLACK_BOT_USER_ID="U-BOT-ID"
EOF
```

### 4️⃣ Run Automation (30 sec)
```bash
cd ~/Desktop/CLAUD\ RECON
python3 claude-code-zap-v2.py
```

---

## ⚠️ KNOWN ISSUE: Instagram Account Not Showing

This is a widespread issue (Dec 2024/Jan 2025). Here's the fix:

### Quick Fix:
1. Visit: https://www.facebook.com/settings?tab=business_tools
2. Find Zapier → Click "View and edit"
3. Enable: "Access profile and posts from Instagram account"
4. Go to Facebook Page settings → Linked Accounts
5. Disconnect and reconnect Instagram
6. Try Zapier connection again

### Alternative: Manual ID Method
```bash
# In Zapier MCP, when it asks for Instagram Account
# Instead of selecting from dropdown (if empty)
# Click "Enter custom value"
# Paste your Instagram Business Account ID (17841...)
```

---

## 📊 OAuth vs Token Comparison
| Feature | Old Token Method | New OAuth Method |
|---------|-----------------|------------------|
| Setup Time | 30-45 minutes | 5 minutes |
| Token Expiry | Every 60 days | Never (auto-refresh) |
| Manual Steps | 15+ steps | 3 steps |
| Facebook Dev Account | Required | Not needed |
| API Knowledge | Required | Not needed |
| Security | You manage tokens | Zapier manages |
| Error Rate | High | Low |

---

## 🧪 Test Commands

### Test Instagram Connection:
```bash
claude mcp zapier instagram_for_business_publish_photo_s '{
  "instructions": "Test only - do not post",
  "caption": "TEST",
  "media": "https://example.com/test.jpg"
}'
```

### Test Full Workflow:
```bash
# 1. Post test message in #claude as bot
# 2. React with ✅
# 3. Run: python3 claude-code-zap-v2.py
# 4. Check console for processing
```

---

## 📝 Message Format (Unchanged)
Legacy Wine MCP Bot posts in #claude:
```
Caption: 🍷 Sanford Bike Week is HERE! Stop by for our premium selection!
Image: https://images.unsplash.com/photo-1558981852-426c6c22a060
Publish: Now
#SanfordBikeWeek #LegacyWine #BikeWeek2025
```

---

## 🆘 Troubleshooting

### "No options available" error:
→ See INSTAGRAM_OAUTH_TROUBLESHOOTING.md

### Instagram not posting:
→ Ensure Business Account (not personal)
→ Facebook Page must be connected
→ You must be admin of both

### Slack not finding messages:
→ Bot must be in #claude channel
→ Check reactions:read permission

---

## 🎉 SUCCESS CHECKLIST

✅ Slack tokens in .env file
✅ Instagram connected via OAuth (no tokens!)
✅ Test commands working
✅ Message format understood
✅ Automation running

---

## 📞 Support

- Zapier OAuth issues: https://help.zapier.com
- Slack API: https://api.slack.com
- Instagram Business: https://business.instagram.com

---

Created: January 19, 2025
Updated for: Zapier Instagram for Business OAuth Integration
By: Legacy Wine Automation Team