# 📝 PHASE 1: Notion API Integration

## Overview

Add Notion to manage your content calendar, track post performance, and organize product information.

---

## 🎯 What You'll Get

After this setup:
- ✅ Content calendar in Notion
- ✅ Bot reads upcoming posts from Notion
- ✅ Bot logs published posts to Notion
- ✅ Track engagement metrics
- ✅ Plan weekly/monthly content

---

## 🚀 Step-by-Step Setup

### Step 1: Create Notion Account (If Needed)

1. Go to https://www.notion.so
2. Sign up for free account (or log in)
3. Notion is free for personal use!

---

### Step 2: Get Your Notion API Key

1. **Go to Notion Integrations**
   - Visit: https://www.notion.so/my-integrations
   - Click "Create new integration"

2. **Configure Integration**
   ```
   Name: Legacy Wine Bot
   Associated workspace: [Your workspace]
   Type: Internal integration
   Capabilities:
     ✅ Read content
     ✅ Update content
     ✅ Insert content
   ```

3. **Copy Your API Key**
   - Click "Show" next to "Internal Integration Token"
   - Copy the token (starts with `secret_`)
   - Save it somewhere safe

   Example: `secret_abc123xyz789...`

---

### Step 3: Create Content Database in Notion

1. **Create New Page**
   - In Notion, click "+ New page"
   - Name it: "Legacy Wine Content Calendar"

2. **Create Database**
   - Type `/database` and select "Table - Inline"
   - Or click "Table" from toolbar

3. **Add These Columns**

   | Column Name | Type | Purpose |
   |-------------|------|---------|
   | **Post Title** | Title | Name of the post |
   | **Status** | Select | Draft, Scheduled, Published, Ideas |
   | **Product Category** | Select | Wine, Bourbon, Scotch, Spirits, Beer |
   | **Occasion** | Select | Sunday, Weekend, Brunch, Game Day |
   | **Scheduled Date** | Date | When to post |
   | **Published Date** | Date | When it was published |
   | **Instagram URL** | URL | Link to Instagram post |
   | **Performance** | Select | High, Medium, Low |
   | **Notes** | Text | Additional details |
   | **Image URL** | URL | Image used |
   | **Hashtags** | Text | Hashtags used |

4. **Add Status Options**
   - Click on "Status" column dropdown
   - Add options:
     - 💡 Ideas
     - ✏️ Draft
     - 📅 Scheduled
     - ✅ Published
     - 📊 Analyzed

5. **Add Product Category Options**
   - Click on "Product Category" dropdown
   - Add options:
     - 🍷 Wine - Red
     - 🍷 Wine - White
     - 🍷 Wine - Rosé
     - 🥂 Sparkling
     - 🥃 Bourbon
     - 🥃 Scotch
     - 🍹 Spirits
     - 🍺 Beer

6. **Add Occasion Options**
   - Click on "Occasion" dropdown
   - Add:
     - ☀️ Sunday
     - 🎉 Weekend
     - 🍳 Brunch
     - 🏈 Game Day
     - 💑 Date Night
     - 🎊 Celebration

---

### Step 4: Share Database with Integration

1. **Open your Content Calendar page in Notion**

2. **Click "..." (three dots) in top right**

3. **Select "Add connections"**

4. **Search for "Legacy Wine Bot"** (your integration name)

5. **Click to connect**

You should see: "Legacy Wine Bot can access this page"

---

### Step 5: Get Database ID

1. **Open your Content Calendar in Notion**

2. **Look at the URL in browser**
   ```
   https://www.notion.so/Your-Content-Calendar-abc123def456?v=...
   ```

3. **Copy the ID** (the part after the last `/` and before `?`)
   ```
   Example: abc123def456789...
   ```

---

### Step 6: Install Notion Python Package

```bash
cd "/Users/justinetwaru/Desktop/claude code oct19"
pip3 install notion-client
```

---

### Step 7: Add Notion Credentials to .env

```bash
# Open .env file
nano .env
```

Add these lines at the end:
```bash
# Notion Configuration
NOTION_API_KEY="secret_your_key_here"
NOTION_DATABASE_ID="your_database_id_here"
```

Save and exit (Ctrl+X, Y, Enter)

---

### Step 8: Test Notion Connection

Create test script:
```bash
cat > test-notion.py << 'EOF'
#!/usr/bin/env python3
import os
from pathlib import Path
from notion_client import Client

# Load .env
env_path = Path('.') / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value.strip('"').strip("'")

# Test connection
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

if not NOTION_API_KEY:
    print("❌ NOTION_API_KEY not found in .env")
    exit(1)

if not NOTION_DATABASE_ID:
    print("❌ NOTION_DATABASE_ID not found in .env")
    exit(1)

print("Testing Notion connection...")
notion = Client(auth=NOTION_API_KEY)

try:
    # Query database
    response = notion.databases.query(database_id=NOTION_DATABASE_ID)
    print("✅ Connected to Notion!")
    print(f"✅ Found {len(response['results'])} items in database")
    
    # Show database info
    db_info = notion.databases.retrieve(database_id=NOTION_DATABASE_ID)
    print(f"✅ Database: {db_info['title'][0]['plain_text']}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

print("\n🎉 Notion integration working!")
EOF

chmod +x test-notion.py
python3 test-notion.py
```

**Expected output:**
```
Testing Notion connection...
✅ Connected to Notion!
✅ Found 0 items in database
✅ Database: Legacy Wine Content Calendar
🎉 Notion integration working!
```

---

### Step 9: Add Sample Content Ideas to Notion

Manually add 5 ideas to your Notion database:

| Post Title | Status | Product Category | Occasion |
|-----------|--------|------------------|----------|
| Sunday Bourbon Special | 💡 Ideas | 🥃 Bourbon | ☀️ Sunday |
| Weekend Wine Selection | 💡 Ideas | 🍷 Wine - Red | 🎉 Weekend |
| Brunch Champagne | 💡 Ideas | 🥂 Sparkling | 🍳 Brunch |
| Game Day Beer | 💡 Ideas | 🍺 Beer | 🏈 Game Day |
| Scotch Collection | 💡 Ideas | 🥃 Scotch | ☀️ Sunday |

---

## 🤖 What the Bot Can Now Do

### Read Upcoming Posts from Notion

Bot can check: "What should I post today?"

```python
# Bot queries Notion for scheduled posts
scheduled_posts = notion.query_database(
    database_id=NOTION_DATABASE_ID,
    filter={
        "property": "Status",
        "select": {"equals": "📅 Scheduled"}
    }
)
```

### Log Published Posts to Notion

After posting, bot updates Notion:

```python
# Bot creates entry in Notion
notion.pages.create(
    parent={"database_id": NOTION_DATABASE_ID},
    properties={
        "Post Title": {"title": [{"text": {"content": "Sunday Wine Special"}}]},
        "Status": {"select": {"name": "✅ Published"}},
        "Published Date": {"date": {"start": "2025-10-19"}},
        "Product Category": {"select": {"name": "🍷 Wine - Red"}},
        "Performance": {"select": {"name": "High"}}
    }
)
```

### Get Content Ideas

Bot can read ideas from Notion:

```python
# Bot gets ideas with status "💡 Ideas"
ideas = notion.query_database(
    database_id=NOTION_DATABASE_ID,
    filter={
        "property": "Status",
        "select": {"equals": "💡 Ideas"}
    }
)
```

---

## 📊 Example Workflow

### Morning: Plan Your Posts

1. **Open Notion** → Content Calendar
2. **Add ideas** for the week
3. **Set status** to "📅 Scheduled"
4. **Set date** for each post

### During Day: Bot Checks Notion

```
Bot: "Checking Notion for scheduled posts..."
Bot: "Found: Sunday Wine Special scheduled for today"
Bot: "Creating post now..."
```

### After Posting: Bot Updates Notion

```
Bot: "Post published!"
Bot: "Updating Notion..."
Bot: "✅ Marked as Published in Notion"
```

---

## 🎯 Next Steps After Setup

Once Notion is working, you can:

1. **Plan weekly content** in Notion
2. **Bot reads from Notion** automatically
3. **Bot logs to Notion** after posting
4. **Track performance** in Notion
5. **Analyze what works** using Notion views

---

## ✅ Verification Checklist

Before moving to Phase 2, verify:

- [ ] Notion account created
- [ ] Integration created and API key obtained
- [ ] Content Calendar database created
- [ ] All columns added to database
- [ ] Database shared with integration
- [ ] Database ID copied
- [ ] Credentials added to .env
- [ ] notion-client installed (`pip3 install notion-client`)
- [ ] test-notion.py runs successfully
- [ ] Sample content added to database

---

## 🚨 Troubleshooting

### "Could not find database"

**Fix:**
1. Make sure you shared the database with your integration
2. Go to database → "..." → "Add connections" → Select your integration

### "Unauthorized"

**Fix:**
1. Check API key in .env is correct
2. Make sure it starts with `secret_`
3. No extra quotes or spaces

### "Invalid database_id"

**Fix:**
1. Database ID should be 32 characters (no dashes)
2. Copy from URL: `https://notion.so/xxxxx-THISISTHEID?v=yyy`
3. Use the part between the last `-` and `?`

---

## 📞 Need Help?

Run the test script:
```bash
python3 test-notion.py
```

If you see errors, check:
1. `.env` file has NOTION_API_KEY and NOTION_DATABASE_ID
2. Database is shared with integration
3. Database ID is correct (32 characters)

---

**Once this is working, we'll move to Phase 2: Deploy to Render! 🚀**

---

**Phase**: 1 of 3
**Status**: In Progress
**Next**: Phase 2 - Render Deployment
