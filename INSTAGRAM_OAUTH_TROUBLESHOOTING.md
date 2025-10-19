# 🔧 INSTAGRAM OAUTH TROUBLESHOOTING GUIDE

## Common Issues & Solutions (December 2024/January 2025)

### Issue 1: "No options available" / Instagram account not showing

**Solution:**
1. Go to Facebook Settings: https://www.facebook.com/settings?tab=business_tools
2. Find "Zapier" in the list
3. Click "View and edit"
4. Enable: "Access profile and posts from the Instagram account connected to your Page"
5. Save changes

Then:
1. Go to your Facebook Page settings
2. Click "Linked Accounts" → "Instagram"
3. Disconnect Instagram
4. Reconnect Instagram
5. Try connecting in Zapier again

### Issue 2: Manual Instagram Account ID Workaround

If account still not showing, use manual ID:

1. Get your Instagram Business Account ID:
```bash
# Go to Facebook Graph API Explorer
https://developers.facebook.com/tools/explorer/

# Run this query
GET /me/accounts?fields=instagram_business_account
```

2. In Zapier MCP, manually enter the ID: