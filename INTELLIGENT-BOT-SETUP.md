# 🤖 Intelligent Bot Setup Guide

## What's New?

You now have an **AI-powered bot** that understands natural language and creates professional Instagram posts through Slack conversations!

---

## 🧠 The "Big Brain" System

### What's Included:

1. **Knowledge Base** (`LEGACY_WINE_KNOWLEDGE_BASE.json`)
   - 50+ wine varieties
   - 40+ spirit brands
   - Seasonal content strategies
   - Hashtag library (100+ hashtags)
   - Content templates
   - Target audience data
   - Occasion-based messaging

2. **Intelligent Bot** (`intelligent-slack-bot.py`)
   - Natural language understanding
   - Context awareness (day, time, occasion)
   - Smart product detection
   - Auto image selection
   - Professional copy generation
   - Hashtag optimization

3. **Interactive Messaging**
   - Mention bot in Slack
   - Conversational interface
   - Threaded responses
   - Content suggestions

---

## 🚀 Quick Setup (3 Steps)

### Step 1: Install (If Not Done Already)
```bash
cd "/Users/justinetwaru/Desktop/claude code oct19"
./startup.sh
```

### Step 2: Start the Intelligent Bot
```bash
python3 intelligent-slack-bot.py
```

You'll see:
```
✅ Loaded knowledge base: LEGACY_WINE_KNOWLEDGE_BASE.json
🤖 Intelligent bot started!
📢 Listening for messages in channel C09M2PHPRJ6
💬 Mention me with requests like:
   - 'Create a post about bourbon for Sunday'
   - 'Make a wine post'
   - 'Suggest content ideas'
```

### Step 3: Message the Bot

Open Slack → #claude → Type:
```
@Legacy Wine MCP Bot create a wine post for Sunday
```

---

## 📚 What You Can Do Now

### Old Way (Manual):
```bash
# Had to manually create JSON files
./post-to-slack.sh slack-posts/sunday-wine.json
```

### New Way (Intelligent):
```
Just message the bot in Slack:
@Legacy Wine MCP Bot create a wine post for Sunday
```

**Bot automatically:**
- ✅ Understands you want a wine post
- ✅ Knows it's for Sunday
- ✅ Generates professional copy
- ✅ Selects perfect image
- ✅ Adds relevant hashtags
- ✅ Posts to Slack
- ✅ Ready for Instagram with ✅ reaction

---

## 🎯 How It Works

### 1. Natural Language Understanding

**You say:**
```
create a bourbon post
```

**Bot understands:**
- Action: CREATE
- Product: BOURBON
- Occasion: SUNDAY (detects current day)
- Tone: RELAXED (Sunday default)

### 2. Knowledge Base Lookup

Bot checks knowledge base for:
- Bourbon brands (Buffalo Trace, Maker's Mark, etc.)
- Appropriate hashtags (#Bourbon #Whiskey)
- Best image (bourbon glass photo)
- Sunday messaging (relaxed, unwinding theme)

### 3. Smart Generation

Bot creates:
```
🥃 SUNDAY BOURBON SELECTION 🥃

Unwind this Sunday with premium bourbon!

🌟 Buffalo Trace
🌟 Maker's Mark
🌟 Woodford Reserve

Visit Legacy Wine & Liquor in Downtown Sanford!
📍 Open Sunday | Downtown Sanford, FL

#Bourbon #SundayVibes #LegacyWine #SanfordFL
[image_url]
```

### 4. Posts to Slack

Bot posts formatted content with image ready for Instagram!

---

## 💡 Example Conversations

### Example 1: Wine Request
```
You: @Legacy Wine MCP Bot make a red wine post

Bot: ✅ Got it! Creating a post about red_wine for sunday...
     [Posts professional red wine content]
     🎉 Post created! React with ✅ to publish to Instagram!
```

### Example 2: Weekend Bourbon
```
You: @Legacy Wine MCP Bot create a weekend bourbon post

Bot: ✅ Got it! Creating a post about bourbon for weekend...
     [Posts energetic weekend-themed bourbon content]
```

### Example 3: Need Ideas
```
You: @Legacy Wine MCP Bot suggest content

Bot: 💡 Content Ideas:
     • Sunday Wine Special
     • Bourbon Collection
     • Weekend Party Essentials
     • Date Night Wines
     • Craft Beer Spotlight
     
     Which one would you like me to create?

You: @Legacy Wine MCP Bot create the bourbon collection

Bot: ✅ Got it! Creating a post about bourbon...
```

---

## 🧠 The Bot's Intelligence

### Product Detection
Understands mentions of:
- Wine (red, white, rosé, sparkling, champagne)
- Bourbon (Buffalo Trace, Maker's Mark, etc.)
- Scotch (Johnnie Walker, Glenlivet, etc.)
- Spirits (vodka, tequila, rum, gin)
- Beer (craft, import)

### Occasion Detection
Recognizes:
- **Sunday** → Relaxed, brunch, unwinding
- **Weekend** → Parties, celebrations, fun
- **Brunch** → Mimosas, champagne, light wines
- **Game Day** → Beer, spirits, entertaining
- **Date Night** → Wine, romantic selections

### Context Awareness
- Knows current day and time
- Adjusts tone (morning = energetic, evening = relaxed)
- Seasonal awareness (summer = rosé, winter = red wine)
- Event detection (holidays, celebrations)

### Smart Defaults
If you just say "create a post":
- Uses current day (Sunday = wine special)
- Selects appropriate products
- Generates relevant copy
- Adds timely hashtags

---

## 📊 Knowledge Base Contents

### Business Information
- Store name, location, hours
- Instagram handle and page ID
- Brand voice and personality
- Target audience demographics

### Product Library
```json
Wine: 50+ varieties
  - Red: Cabernet, Pinot Noir, Merlot, Malbec, etc.
  - White: Chardonnay, Sauvignon Blanc, etc.
  - Rosé: Provence, Spanish, California
  - Sparkling: Champagne, Prosecco, Cava

Spirits: 40+ brands
  - Bourbon: Buffalo Trace, Maker's Mark, etc.
  - Scotch: Johnnie Walker (all labels)
  - Vodka, Tequila, Rum, Gin

Beer: Craft, Import, Domestic
```

### Content Strategy
- Seasonal themes (Spring, Summer, Fall, Winter)
- Occasion templates (Sunday, Weekend, Celebration)
- Tone guidelines (Friendly, Premium, Local)
- Post structures (Title, Body, Products, CTA)

### Visual Library
- 10+ curated Unsplash images
- Product-specific photos
- High quality, professional
- Consistent aesthetic

### Hashtag Library
```
Primary: #LegacyWine #SanfordFL #DowntownSanford
Wine: #Wine #WineLovers #RedWine #WhiteWine
Spirits: #Bourbon #Whiskey #Scotch #PremiumSpirits
Occasions: #SundayVibes #Weekend #Brunch #GameDay
Location: #Florida #CentralFlorida #SupportLocal
```

---

## 🔧 Customization

### Add New Products

Edit `LEGACY_WINE_KNOWLEDGE_BASE.json`:
```json
{
  "product_categories": {
    "wine": {
      "red_wines": [
        "Cabernet Sauvignon",
        "YOUR NEW WINE HERE"
      ]
    }
  }
}
```

### Add New Hashtags
```json
{
  "hashtag_library": {
    "wine": [
      "#Wine",
      "#YourNewHashtag"
    ]
  }
}
```

### Add New Images
Edit `intelligent-slack-bot.py`:
```python
IMAGE_LIBRARY = {
    "wine_red": "https://your-image-url.com",
    "your_category": "https://another-image.com"
}
```

### Customize Messaging
Edit templates in knowledge base:
```json
{
  "content_guidelines": {
    "tone": "YOUR CUSTOM TONE",
    "call_to_action": [
      "Your custom CTA"
    ]
  }
}
```

---

## 🎯 Advanced Features

### 1. Multi-Turn Conversations
```
You: @Bot suggest ideas
Bot: [Shows 5 ideas]
You: @Bot create #2
Bot: [Creates bourbon post]
```

### 2. Context Memory
Bot remembers conversation context within threads

### 3. Smart Image Matching
- Bourbon request → Bourbon glass image
- Wine request → Wine bottles/glasses
- Scotch → Whisky tumbler

### 4. Hashtag Optimization
- Combines primary store tags
- Adds product-specific tags
- Includes occasion tags
- Limits to 12 for best engagement

### 5. Time-Aware Posting
- Sunday morning → Brunch theme
- Sunday evening → Dinner/relaxation
- Friday → Weekend party prep
- Weekday → After-work treats

---

## 🚀 Running the Bot

### Start the Bot
```bash
python3 intelligent-slack-bot.py
```

### Keep It Running (Background)
```bash
# Run in background
nohup python3 intelligent-slack-bot.py > bot.log 2>&1 &

# Check if running
ps aux | grep intelligent-slack-bot

# Stop background bot
pkill -f intelligent-slack-bot.py
```

### Auto-Start on Boot (Optional)
Create launch agent:
```bash
# See full instructions in startup.sh
```

---

## ✅ Testing the System

### Test 1: Simple Request
```
@Legacy Wine MCP Bot create a wine post
```
**Expected**: Bot creates wine post with image and hashtags

### Test 2: Specific Request
```
@Legacy Wine MCP Bot make a bourbon post for Sunday
```
**Expected**: Sunday-themed bourbon content

### Test 3: Content Suggestions
```
@Legacy Wine MCP Bot suggest some ideas
```
**Expected**: List of 5 content ideas

### Test 4: Help Request
```
@Legacy Wine MCP Bot help
```
**Expected**: Usage instructions

---

## 📈 Comparison: Old vs New

### Old Manual System
```
1. Create JSON file manually
2. Add caption, image URL, hashtags
3. Run: ./post-to-slack.sh file.json
4. React with ✅
```

### New Intelligent System
```
1. Message bot: "create a wine post"
2. React with ✅
```

**Time saved**: 5 minutes → 10 seconds!

---

## 🎉 You're All Set!

### Quick Start Commands

```bash
# Start the intelligent bot
python3 intelligent-slack-bot.py

# In another terminal, if you want old method too
./post-to-slack.sh slack-posts/sunday-wine.json
```

### In Slack

```
@Legacy Wine MCP Bot create a wine post for Sunday
@Legacy Wine MCP Bot suggest content ideas
@Legacy Wine MCP Bot make a bourbon post
```

---

## 📞 Troubleshooting

### Bot not responding?
1. Check bot is running: `ps aux | grep intelligent`
2. Check .env file has BOT_USER_ID
3. Make sure you're mentioning the bot: `@Legacy Wine MCP Bot`

### Wrong content generated?
1. Be more specific: "create a RED wine post for SUNDAY dinner"
2. Check knowledge base: `cat LEGACY_WINE_KNOWLEDGE_BASE.json`

### Want to customize?
1. Edit knowledge base for content changes
2. Edit bot script for behavior changes
3. Restart bot after changes

---

**Created**: October 19, 2025
**System Version**: 2.0 (Intelligent)
**Status**: ✅ Ready to Use!
