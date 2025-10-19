# 🚀 Postman API Setup Guide
## Full API Control for Legacy Wine & Liquor

---

## 📦 What You Have

I've created 2 files for complete API control via Postman:

1. **`Legacy-Wine-API-Collection.postman_collection.json`** - All API endpoints
2. **`Legacy-Wine-API.postman_environment.json`** - All your credentials

---

## 🚀 Quick Setup (5 Steps)

### Step 1: Open Postman
- Download Postman: https://www.postman.com/downloads/
- Or use web version: https://web.postman.com

### Step 2: Import Collection
1. Click **"Import"** button (top left)
2. Drag and drop: `Legacy-Wine-API-Collection.postman_collection.json`
3. Click **"Import"**

### Step 3: Import Environment
1. Click **"Import"** button again
2. Drag and drop: `Legacy-Wine-API.postman_environment.json`
3. Click **"Import"**

### Step 4: Select Environment
1. In top right, click the dropdown (says "No Environment")
2. Select **"Legacy Wine API Environment"**

### Step 5: Test an API Call
1. In left sidebar, expand **"Legacy Wine & Liquor - Complete API Collection"**
2. Expand **"Slack API"**
3. Click **"Get Bot Info"**
4. Click **"Send"** button
5. Should see your bot info in response!

---

## 📚 API Collections Included

### 1. Slack API (4 endpoints)
- ✅ **Post Message to Channel** - Send messages/posts to #claude
- ✅ **Get Channel History** - Read recent messages
- ✅ **Add Reaction** - Add ✅ emoji to messages
- ✅ **Get Bot Info** - Test your bot token

### 2. Notion API (4 endpoints)
- ✅ **Create Database** - Create content calendar
- ✅ **Query Database** - Get scheduled posts
- ✅ **Create Page** - Add new post to calendar
- ✅ **Search Pages** - Find your pages/databases

### 3. Zapier API (2 endpoints)
- ✅ **List Zaps** - See all your Zaps
- ✅ **Get Zap History** - Check Zap execution history

### 4. Instagram Business API (2 endpoints)
- ✅ **Create Media Container** - Prepare Instagram post
- ✅ **Publish Media** - Publish to Instagram

---

## 🎯 Common Use Cases

### Use Case 1: Post to Slack via API

**Request**: Slack API → Post Message to Channel

**Body** (already configured):
```json
{
  "channel": "C09M2PHPRJ6",
  "text": "🍷 Test post from Postman API",
  "attachments": [
    {
      "fallback": "Test image",
      "image_url": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=1080&q=80"
    }
  ],
  "unfurl_links": false,
  "unfurl_media": true
}
```

**Click "Send"** → Post appears in #claude channel!

---

### Use Case 2: Create Notion Database

**Request**: Notion API → Create Database

**First, you need a parent page ID:**

1. Go to Notion
2. Create a blank page: "Legacy Wine Content Calendar"
3. Share it with your integration: "..." → "Add connections" → "Legacy Wine Bot"
4. Copy the page URL: `https://www.notion.so/Legacy-Wine-abc123def456?v=...`
5. Extract the ID (the part between last `/` and `?`): `abc123def456`

**Update the request body:**
- Replace `YOUR_PAGE_ID_HERE` with your page ID
- Click **"Send"**
- Database created!

---

### Use Case 3: Query Scheduled Posts

**Request**: Notion API → Query Database

**First, get your database ID:**
1. Open your database in Notion
2. Copy URL: `https://www.notion.so/abc123...?v=xyz`
3. The database ID is between `/` and `?`

**Update the URL:**
- Replace `YOUR_DATABASE_ID` with your ID
- Click **"Send"**
- See all scheduled posts!

---

### Use Case 4: Add Post to Notion

**Request**: Notion API → Create Page (Database Entry)

**Update the body:**
- Replace `YOUR_DATABASE_ID` with your database ID
- Modify the post details
- Click **"Send"**
- New post added to calendar!

---

## 🔑 Environment Variables

All credentials are stored in the environment file:

| Variable | Value | Used For |
|----------|-------|----------|
| `slack_bot_token` | xoxb-8592279508421... | Slack API auth |
| `slack_user_token` | xoxp-8592279508421... | Slack user operations |
| `slack_channel_id` | C09M2PHPRJ6 | #claude channel |
| `slack_bot_user_id` | U09LZ8FUHNH | Bot user ID |
| `notion_api_key` | ntn_672380142718... | Notion API auth |
| `zapier_api_key` | sk-ak-8jK4mzLC... | Zapier API auth |
| `instagram_page_id` | 17841463539272316 | Instagram Business ID |

**Using variables in requests:**
Use {{variable_name}} syntax, e.g.: `{{slack_bot_token}}`

---

## 🧪 Testing Each API

### Test 1: Slack API
```
Request: Slack API → Get Bot Info
Click: Send
Expected: Your bot info (user_id, team_id, etc.)
```

### Test 2: Notion API  
```
Request: Notion API → Search Pages
Click: Send
Expected: List of your Notion pages
```

### Test 3: Zapier API
```
Request: Zapier API → List Zaps
Click: Send
Expected: All your Zaps
```

---

## 🎨 Creating Your Notion Database via API

**Step-by-step:**

1. **Create parent page in Notion**:
   - Notion → "+ New page" → Name it "Content Calendar"
   - Share with integration: "..." → "Add connections" → "Legacy Wine Bot"

2. **Get page ID from URL**:
   - URL: `https://www.notion.so/Content-Calendar-abc123def456?v=...`
   - ID: `abc123def456`

3. **Use Postman**:
   - Open: Notion API → Create Database
   - Replace `YOUR_PAGE_ID_HERE` with `abc123def456`
   - Click **"Send"**

4. **Database created!**
   - Refresh Notion
   - See database with all columns

5. **Save database ID**:
   - Open database in Notion
   - Copy URL: `https://www.notion.so/xyz789...?v=...`
   - Database ID: `xyz789...`
   - Save this for future API calls!

---

## 📊 Response Examples

### Successful Slack Post:
```json
{
  "ok": true,
  "channel": "C09M2PHPRJ6",
  "ts": "1760881632.946109",
  "message": {
    "text": "🍷 Test post from Postman API",
    ...
  }
}
```

### Successful Notion Database Creation:
```json
{
  "object": "database",
  "id": "abc-123-def-456",
  "created_time": "2025-10-19T...",
  "title": [
    {
      "text": {
        "content": "Content Calendar"
      }
    }
  ],
  ...
}
```

---

## 🚨 Troubleshooting

### Error: "Unauthorized" (Slack)
**Fix**: Check your `slack_bot_token` in environment

### Error: "Unauthorized" (Notion)
**Fix**: 
1. Check `notion_api_key` is correct
2. Make sure you shared the page with your integration

### Error: "Invalid page_id" (Notion)
**Fix**: Double-check the page ID from the URL

### Error: "Could not find database"
**Fix**: Make sure the database is shared with your integration

---

## 🎯 Next Steps

### Now that you have Postman set up:

1. **Test all APIs** - Run each request once
2. **Create Notion database** - Use "Create Database" request
3. **Add sample data** - Use "Create Page" request
4. **Query your data** - Use "Query Database" request
5. **Automate workflows** - Use Postman Collections Runner

---

## 💡 Pro Tips

### 1. Save Responses
After getting database ID or page ID, save it in environment variables:
- Gear icon → Edit environment → Add new variable

### 2. Use Variables Everywhere
Replace hard-coded values with `{{variable_name}}`

### 3. Chain Requests
Use Postman Tests tab to extract values from responses and set them as variables

### 4. Create Tests
Add assertions to verify responses:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### 5. Export for Backup
File → Export → Save collection and environment

---

## 📞 Quick Reference

### File Locations:
```
/Users/justinetwaru/Desktop/claude code oct19/
├── Legacy-Wine-API-Collection.postman_collection.json
├── Legacy-Wine-API.postman_environment.json
└── POSTMAN-API-GUIDE.md (this file)
```

### Import to Postman:
1. Postman → Import
2. Drag both JSON files
3. Select environment in top-right dropdown

### Test Connection:
- Slack: "Get Bot Info" endpoint
- Notion: "Search Pages" endpoint  
- Zapier: "List Zaps" endpoint

---

## 🎉 You're Ready!

You now have **complete API control** via Postman for:
- ✅ Slack (posting, reading, reactions)
- ✅ Notion (databases, pages, queries)
- ✅ Zapier (Zaps, history)
- ✅ Instagram (media creation, publishing)

**Start testing!** Open Postman and try the "Get Bot Info" request.

---

**Created**: October 19, 2025
**Status**: Ready to Use
**Support**: Check response examples and troubleshooting sections above
