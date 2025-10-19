# 🔐 UPDATED TOKEN SETUP GUIDE - 2025 VERSION
## Legacy Wine Slack-to-Social Automation

### ⚡ MAJOR UPDATE: Instagram Now Uses OAuth!
No more manual Instagram Access Tokens! Zapier now handles Instagram authentication automatically through OAuth.

---

## 1. SLACK TOKENS (Still Required)

### A. Slack Bot Token (xoxb-)
1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. Name it: "Legacy Wine Social Poster"
4. Select your workspace
5. Go to "OAuth & Permissions" in sidebar
6. Add these Bot Token Scopes:
   - `channels:read`
   - `channels:history`
   - `reactions:read`
   - `chat:write`
   - `users:read`
7. Click "Install to Workspace"
8. Copy the "Bot User OAuth Token" (starts with xoxb-)

```bash
SLACK_BOT_TOKEN="xoxb-YOUR-TOKEN-HERE"
```

### B. Slack User Token (xoxp-)
1. In the same app, go to "OAuth & Permissions"
2. Add these User Token Scopes:
   - `reactions:read`   - `channels:read`
   - `channels:history`
3. Reinstall the app
4. Copy the "User OAuth Token" (starts with xoxp-)

```bash
SLACK_USER_TOKEN="xoxp-YOUR-TOKEN-HERE"
```

### C. Get Channel ID
1. Open Slack in browser
2. Go to #claude channel
3. Click channel name → "About" → scroll down
4. Copy Channel ID (starts with C)

```bash
SLACK_CHANNEL_ID="C1234567890"
```

### D. Get Bot User ID
1. In Slack, click on Legacy Wine MCP Bot profile
2. Click "View full profile"
3. Click "More" → "Copy member ID"

```bash
SLACK_BOT_USER_ID="U1234567890"
```

---

## 2. INSTAGRAM FOR BUSINESS (OAuth - NO TOKEN NEEDED!)

### A. Prerequisites
1. **Instagram Business Account** (not personal)
2. **Facebook Page** connected to your Instagram3. **Admin access** to both Facebook Page and Instagram

### B. Connect Instagram to Zapier (OAuth Flow)
1. In Zapier MCP or Zapier.com
2. Choose "Instagram for Business" integration
3. Click "Connect a new account"
4. **Facebook OAuth window opens**
5. Log in with your Facebook account (personal account that manages the business)
6. Select the Facebook Page connected to your Instagram
7. Grant these permissions:
   - Access profile and posts from Instagram account
   - Manage your Pages
   - Show list of Pages you manage
8. Click "Done" or "Continue"
9. Zapier automatically handles tokens!

### C. If Instagram Account Not Showing
Common issue as of Dec 2024. Fix:
1. Go to https://www.facebook.com/settings?tab=business_tools
2. Find Zapier in the list
3. Click "View and edit"
4. Enable: "Access profile and posts from the Instagram account connected to your Page"
5. Go to your Facebook Page settings
6. Click "Linked Accounts" → Instagram
7. Disconnect and reconnect Instagram
8. Reconnect in Zapier

### D. Manual Instagram Account ID (Backup Method)