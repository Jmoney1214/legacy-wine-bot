# 🤖 How to Use the Intelligent Slack Bot

## Overview

The intelligent bot can understand natural language and create professional Instagram posts through Slack conversations!

---

## 🚀 Quick Start

### 1. Start the Bot
```bash
cd "/Users/justinetwaru/Desktop/claude code oct19"
python3 intelligent-slack-bot.py
```

You'll see:
```
🤖 Intelligent bot started!
📢 Listening for messages in channel #claude
💬 Mention me with requests like:
   - 'Create a post about bourbon for Sunday'
   - 'Make a wine post'
   - 'Suggest content ideas'
```

### 2. Message the Bot in Slack

Open Slack → #claude channel → Mention the bot:

**Example:**
```
@Legacy Wine MCP Bot create a post about wine for Sunday
```

### 3. Bot Responds

The bot will:
1. ✅ Confirm it understood your request
2. 🎨 Generate a professional post with image
3. 📝 Post it to the channel
4. 📢 Tell you to react with ✅ to publish to Instagram

---

## 💬 What You Can Say to the Bot

### Creating Posts

```
@Legacy Wine MCP Bot create a post about bourbon

@Legacy Wine MCP Bot make a wine post for Sunday

@Legacy Wine MCP Bot post about scotch

@Legacy Wine MCP Bot create a weekend post about spirits

@Legacy Wine MCP Bot make a brunch post with champagne
```

### Getting Suggestions

```
@Legacy Wine MCP Bot suggest some content ideas

@Legacy Wine MCP Bot what should I post about?

@Legacy Wine MCP Bot help me with content
```

### General Help

```
@Legacy Wine MCP Bot help

@Legacy Wine MCP Bot what can you do?
```

---

## 🧠 What the Bot Understands

### Product Categories
- **Wine**: red wine, white wine, rosé, sparkling, champagne, prosecco
- **Spirits**: bourbon, scotch, whiskey, vodka, tequila, rum, gin
- **Beer**: craft beer, imports
- **General**: spirits, liquor, wine

### Occasions
- **Sunday**: Relaxed, brunch, unwinding
- **Weekend**: Parties, celebrations, game day
- **Weekday**: After work, date night
- **Special**: Holidays, celebrations, gifts

### Tone Detection
The bot automatically adjusts tone based on:
- Time of day (morning = brunch, evening = dinner)
- Day of week (Sunday = relaxed, Friday = party)
- Keywords (celebration = energetic, gift = thoughtful)

---

## 🎨 What the Bot Generates

Every post includes:

### 1. Title with Emojis
```
🍷 SUNDAY WINE SPECIAL 🍷
```

### 2. Engaging Body Copy
```
Unwind this Sunday with exceptional wines at exceptional prices!
```

### 3. Product List
```
✨ Premium Cabernet Sauvignon
✨ Elegant Pinot Noir
✨ Crisp Sauvignon Blanc
```

### 4. Call to Action
```
Visit Legacy Wine & Liquor in Downtown Sanford today!
📍 Open Sunday | Downtown Sanford, FL
```

### 5. Hashtags (8-12 relevant tags)
```
#Wine #SundayWine #WineLovers #LegacyWine #SanfordFL
```

### 6. Professional Image
- Automatically selects appropriate image from curated library
- High quality Unsplash photos
- Matches product category

---

## 📚 Knowledge Base

The bot has a "big brain" with knowledge about:

### Business Info
- Store name, location, hours
- Instagram handle and page ID
- Brand voice and tone

### Products
- **50+ wine varieties** (reds, whites, rosés, sparkling)
- **40+ spirits brands** (bourbon, scotch, vodka, tequila, etc)
- **Beer selection** (craft, import, domestic)

### Content Strategy
- Seasonal themes
- Occasion-based messaging
- Target audience preferences
- Best posting times

### Visual Library
- 10+ curated images for different products
- Professional, high-quality photos
- Consistent aesthetic

---

## 🎯 Example Conversations

### Example 1: Simple Request

**You:**
```
@Legacy Wine MCP Bot create a bourbon post
```

**Bot:**
```
✅ Got it! Creating a post about bourbon for sunday...

[Generates and posts:]
🥃 BOURBON LOVER'S SELECTION 🥃

Make your Sunday special with premium bourbon!

🌟 Buffalo Trace
🌟 Maker's Mark
🌟 Woodford Reserve
🌟 Four Roses

Visit Legacy Wine & Liquor in Downtown Sanford!
📍 Open Sunday | Downtown Sanford, FL

#Bourbon #Whiskey #LegacyWine #SanfordFL
[Image attached]

🎉 Post created! React with ✅ to publish to Instagram!
```

### Example 2: Specific Request

**You:**
```
@Legacy Wine MCP Bot make a weekend post about white wine for brunch
```

**Bot:**
```
✅ Got it! Creating a post about white_wine for brunch...

[Generates post with brunch-themed copy and white wine selection]
```

### Example 3: Getting Ideas

**You:**
```
@Legacy Wine MCP Bot suggest some content ideas
```

**Bot:**
```
💡 Content Ideas:
• Sunday Wine Special - showcase premium red & white wines
• Bourbon Collection - highlight top bourbons
• Weekend Party Essentials - spirits and mixers
• Date Night Wines - romantic selections
• Craft Beer Spotlight - local and imported

Which one would you like me to create?
```

**You:**
```
@Legacy Wine MCP Bot create the bourbon collection post
```

**Bot:**
```
✅ Got it! Creating a post about bourbon...
```

---

## 🔧 Advanced Features

### Context Awareness
The bot understands context:
- **Current day**: Knows if it's Sunday, weekend, or weekday
- **Time of day**: Adjusts messaging for morning/evening
- **Previous conversation**: Can reference earlier messages in thread

### Smart Image Selection
- Bourbon request → Bourbon glass image
- Wine request → Wine bottles/glasses
- Scotch request → Whisky tumbler
- Champagne → Sparkling wine flutes

### Hashtag Intelligence
- Combines primary store hashtags (#LegacyWine #SanfordFL)
- Adds product-specific hashtags (#Bourbon #Wine)
- Includes occasion hashtags (#SundayVibes #Weekend)
- Limits to 12 hashtags for optimal engagement

---

## 🛠️ Customization

### Edit the Knowledge Base

Want to add more products or change messaging?

```bash
nano LEGACY_WINE_KNOWLEDGE_BASE.json
```

You can edit:
- Product categories and brands
- Hashtag library
- Content templates
- Image URLs
- Business information

### Add More Images

Edit the `IMAGE_LIBRARY` in `intelligent-slack-bot.py`:

```python
IMAGE_LIBRARY = {
    "wine_red": "https://your-image-url.com/red-wine.jpg",
    "your_new_category": "https://your-image-url.com/new.jpg"
}
```

---

## 💡 Pro Tips

### 1. Be Specific
```
❌ "make a post"
✅ "create a bourbon post for Sunday"
```

### 2. Use Natural Language
```
✅ "post about white wine"
✅ "create a weekend scotch post"
✅ "make a brunch champagne post"
```

### 3. Request Suggestions First
If unsure what to post, ask:
```
@Legacy Wine MCP Bot suggest content ideas
```

### 4. Test Before Publishing
- Bot creates the post in Slack first
- Review before reacting with ✅
- If you don't like it, just ask for another!

### 5. Thread Conversations
Bot responds in threads to keep channel clean

---

## 🚨 Troubleshooting

### Bot Not Responding?

1. **Check bot is running:**
   ```bash
   # Should show "Intelligent bot started!"
   python3 intelligent-slack-bot.py
   ```

2. **Mention the bot correctly:**
   ```
   @Legacy Wine MCP Bot [your request]
   ```

3. **Check .env file:**
   ```bash
   cat .env | grep SLACK_BOT_TOKEN
   ```

### Bot Generates Wrong Content?

1. **Be more specific:**
   ```
   Instead of: "make a post"
   Try: "create a red wine post for Sunday dinner"
   ```

2. **Check knowledge base:**
   ```bash
   cat LEGACY_WINE_KNOWLEDGE_BASE.json
   ```

### Post Not Appearing on Instagram?

1. Bot only creates post in Slack
2. You must react with ✅ to trigger Zapier
3. Zapier publishes to Instagram
4. Check zapier.com/app/history for errors

---

## 📊 Bot Capabilities Summary

| Feature | Status |
|---------|--------|
| Natural language understanding | ✅ |
| Product category detection | ✅ |
| Occasion detection | ✅ |
| Smart image selection | ✅ |
| Hashtag generation | ✅ |
| Context awareness | ✅ |
| Knowledge base integration | ✅ |
| Threaded conversations | ✅ |
| Content suggestions | ✅ |
| Post editing | 🚧 Coming soon |
| Scheduling | 🚧 Coming soon |

---

## 🎉 You're Ready!

### Start using now:

1. **Start the bot:**
   ```bash
   python3 intelligent-slack-bot.py
   ```

2. **Open Slack** → #claude channel

3. **Message the bot:**
   ```
   @Legacy Wine MCP Bot create a wine post for Sunday
   ```

4. **Wait for bot to generate post**

5. **React with ✅** to publish to Instagram!

---

**Created**: October 19, 2025
**Bot Version**: 1.0
**Status**: ✅ Ready to Use
