# 🤖 PHASE 3: Claude API Integration (Advanced AI)

## Overview

Add Anthropic's Claude API to generate more creative, varied, and intelligent post copy.

---

## 🎯 What You'll Get

After this setup:
- ✅ More creative and varied post copy
- ✅ Better natural language understanding
- ✅ Personalized responses
- ✅ Context-aware generation
- ✅ Ability to refine and edit posts conversationally

**Cost**: ~$5-10/month for typical usage (250-500 posts)

---

## 🚀 Step-by-Step Setup

### Step 1: Create Anthropic Account

1. **Go to Anthropic Console**
   - Visit: https://console.anthropic.com

2. **Sign up**
   - Use email or Google account
   - Verify email

3. **Complete onboarding**

---

### Step 2: Get API Key

1. **Go to API Keys page**
   - https://console.anthropic.com/settings/keys

2. **Click "Create Key"**

3. **Name your key**
   ```
   Name: Legacy Wine Bot
   ```

4. **Copy the API key**
   - Starts with `sk-ant-api03-...`
   - **Save it immediately** (you can't see it again!)

   Example: `sk-ant-api03-abc123xyz789...`

5. **Add credits** (if needed)
   - Go to: https://console.anthropic.com/settings/billing
   - Add $20-50 to start
   - Claude API charges per request (~$0.01-0.05 per post)

---

### Step 3: Install Claude Python SDK

```bash
cd "/Users/justinetwaru/Desktop/claude code oct19"
pip3 install anthropic
```

---

### Step 4: Add Claude API Key to .env

```bash
# Open .env file
nano .env
```

Add this line at the end:
```bash
# Claude/Anthropic API
ANTHROPIC_API_KEY="sk-ant-api03-your_key_here"
```

Save and exit (Ctrl+X, Y, Enter)

---

### Step 5: Test Claude API Connection

Create test script:
```bash
cat > test-claude.py << 'EOF'
#!/usr/bin/env python3
import os
from pathlib import Path
from anthropic import Anthropic

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
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

if not ANTHROPIC_API_KEY:
    print("❌ ANTHROPIC_API_KEY not found in .env")
    exit(1)

print("Testing Claude API connection...")
client = Anthropic(api_key=ANTHROPIC_API_KEY)

try:
    # Test with simple message
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=100,
        messages=[{
            "role": "user",
            "content": "Say 'API connection successful!' if you can read this."
        }]
    )
    
    response = message.content[0].text
    print(f"✅ Claude Response: {response}")
    print("✅ Claude API connection successful!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

print("\n🎉 Claude API integration working!")
EOF

chmod +x test-claude.py
python3 test-claude.py
```

**Expected output:**
```
Testing Claude API connection...
✅ Claude Response: API connection successful!
✅ Claude API connection successful!
🎉 Claude API integration working!
```

---

### Step 6: Update Intelligent Bot to Use Claude API

Now we'll enhance your bot to use Claude for more creative generation.

Create enhanced bot version:
```bash
cat > intelligent-slack-bot-enhanced.py << 'EOFENHANCED'
#!/usr/bin/env python3
"""
Legacy Wine & Liquor - Enhanced Intelligent Slack Bot with Claude API
Now with advanced AI generation capabilities
"""

import os
import json
import time
import requests
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic

# Load environment variables
env_path = Path('.') / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value.strip('"').strip("'")

# Configuration
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_CHANNEL_ID = os.getenv('SLACK_CHANNEL_ID')
SLACK_BOT_USER_ID = os.getenv('SLACK_BOT_USER_ID')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Initialize Claude client
claude_client = None
if ANTHROPIC_API_KEY:
    claude_client = Anthropic(api_key=ANTHROPIC_API_KEY)
    print("✅ Claude API enabled")
else:
    print("⚠️  Claude API not configured (will use template-based generation)")

# Load knowledge base
KNOWLEDGE_BASE_FILE = 'LEGACY_WINE_KNOWLEDGE_BASE.json'
knowledge_base = {}

if os.path.exists(KNOWLEDGE_BASE_FILE):
    with open(KNOWLEDGE_BASE_FILE, 'r') as f:
        knowledge_base = json.load(f)
    print(f"✅ Loaded knowledge base: {KNOWLEDGE_BASE_FILE}")

# Image library
IMAGE_LIBRARY = {
    "wine_red": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=1080&q=80",
    "wine_white": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=1080&q=80",
    "wine_bottles": "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1080&q=80",
    "wine_glasses": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=1080&q=80",
    "bourbon": "https://images.unsplash.com/photo-1569529465841-dfecdab7503b?w=1080&q=80",
    "whiskey": "https://images.unsplash.com/photo-1527281400683-1aae777175f8?w=1080&q=80",
    "cocktails": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1080&q=80",
    "champagne": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=1080&q=80",
    "beer": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=1080&q=80",
    "spirits": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=1080&q=80"
}


def generate_post_with_claude(product_category, occasion, user_request=""):
    """Use Claude API to generate creative, personalized post"""
    
    if not claude_client:
        return None
    
    # Build context from knowledge base
    products = knowledge_base.get('product_categories', {})
    hashtags = knowledge_base.get('hashtag_library', {})
    
    # Create prompt for Claude
    prompt = f"""You are a social media expert for Legacy Wine & Liquor, a premium wine and spirits store in Downtown Sanford, Florida.

Create an engaging Instagram post for the following:
- Product Category: {product_category}
- Occasion: {occasion}
- User Request: {user_request if user_request else 'Create an engaging post'}

Available products:
{json.dumps(products, indent=2)}

Brand Voice: Friendly, knowledgeable, premium without being pretentious, local and community-focused

Post Requirements:
1. Start with an emoji-filled title (e.g., 🍷 SUNDAY WINE SPECIAL 🍷)
2. Write 2-3 engaging sentences about the products/occasion
3. Include a bulleted list of 4-5 specific products with emojis
4. Add a call-to-action about visiting the store
5. Include location: "📍 Open Sunday | Downtown Sanford, FL"
6. Add 8-12 relevant hashtags from: {hashtags}
7. Keep it under 2000 characters
8. Make it feel authentic and local

Format the post as plain text, ready to post."""

    try:
        message = claude_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        generated_text = message.content[0].text
        return generated_text
        
    except Exception as e:
        print(f"⚠️  Claude API error: {e}")
        return None


def send_slack_message(text, thread_ts=None):
    """Send a message to Slack"""
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "channel": SLACK_CHANNEL_ID,
        "text": text
    }
    
    if thread_ts:
        payload["thread_ts"] = thread_ts
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def select_image(product_category):
    """Select appropriate image"""
    image_map = {
        'wine_general': 'wine_bottles',
        'red_wine': 'wine_red',
        'white_wine': 'wine_white',
        'rose': 'wine_white',
        'sparkling': 'champagne',
        'bourbon': 'bourbon',
        'scotch': 'whiskey',
        'whiskey_general': 'whiskey',
        'spirits_general': 'spirits',
        'beer': 'beer'
    }
    
    image_key = image_map.get(product_category, 'wine_bottles')
    return IMAGE_LIBRARY.get(image_key, IMAGE_LIBRARY['wine_bottles'])


def post_to_slack(text, image_url, thread_ts=None):
    """Post formatted content with image to Slack"""
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Append image URL to text
    full_text = f"{text}\n\n{image_url}"
    
    payload = {
        "channel": SLACK_CHANNEL_ID,
        "text": full_text,
        "attachments": [{
            "fallback": "Post image",
            "image_url": image_url
        }],
        "unfurl_links": False,
        "unfurl_media": True
    }
    
    if thread_ts:
        payload["thread_ts"] = thread_ts
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def listen_for_messages():
    """Listen for messages mentioning the bot"""
    print("🤖 Enhanced Intelligent bot started!")
    print(f"📢 Listening for messages in channel {SLACK_CHANNEL_ID}")
    print("💬 Now with Claude AI for creative generation!")
    print("\nPress Ctrl+C to stop\n")
    
    last_check = time.time()
    
    while True:
        try:
            # Get recent messages
            url = "https://slack.com/api/conversations.history"
            headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
            params = {
                "channel": SLACK_CHANNEL_ID,
                "limit": 10,
                "oldest": last_check
            }
            
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            
            if data.get('ok') and data.get('messages'):
                messages = data['messages']
                
                for message in reversed(messages):
                    text = message.get('text', '')
                    user = message.get('user')
                    ts = message.get('ts')
                    
                    # Skip bot's own messages
                    if user == SLACK_BOT_USER_ID:
                        continue
                    
                    # Check if bot is mentioned
                    if f'<@{SLACK_BOT_USER_ID}>' in text:
                        print(f"\n📨 Received message: {text[:100]}...")
                        
                        # Remove bot mention
                        clean_text = text.replace(f'<@{SLACK_BOT_USER_ID}>', '').strip()
                        
                        # Extract product and occasion (simple detection)
                        product = 'wine_general'
                        if 'bourbon' in clean_text.lower():
                            product = 'bourbon'
                        elif 'scotch' in clean_text.lower():
                            product = 'scotch'
                        elif 'beer' in clean_text.lower():
                            product = 'beer'
                        
                        occasion = 'sunday'
                        if 'weekend' in clean_text.lower():
                            occasion = 'weekend'
                        elif 'brunch' in clean_text.lower():
                            occasion = 'brunch'
                        
                        # Confirm understanding
                        send_slack_message(
                            f"✅ Got it! Using Claude AI to create a creative post about {product} for {occasion}...",
                            thread_ts=ts
                        )
                        
                        # Generate with Claude
                        post_text = generate_post_with_claude(product, occasion, clean_text)
                        
                        if post_text:
                            # Select image
                            image_url = select_image(product)
                            
                            # Post to Slack
                            result = post_to_slack(post_text, image_url, thread_ts=ts)
                            
                            if result.get('ok'):
                                send_slack_message(
                                    "🎉 Post created with Claude AI! React with ✅ to publish to Instagram!",
                                    thread_ts=ts
                                )
                            else:
                                send_slack_message(
                                    f"❌ Error creating post: {result.get('error')}",
                                    thread_ts=ts
                                )
                        else:
                            send_slack_message(
                                "⚠️  Claude API not available, would you like me to use template-based generation instead?",
                                thread_ts=ts
                            )
            
            last_check = time.time()
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\n\n👋 Bot stopped by user")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(10)


if __name__ == "__main__":
    if not SLACK_BOT_TOKEN:
        print("❌ Error: SLACK_BOT_TOKEN not found in environment")
        exit(1)
    
    listen_for_messages()
EOFENHANCED

chmod +x intelligent-slack-bot-enhanced.py
```

---

### Step 7: Test Enhanced Bot Locally

```bash
python3 intelligent-slack-bot-enhanced.py
```

**You should see:**
```
✅ Claude API enabled
✅ Loaded knowledge base: LEGACY_WINE_KNOWLEDGE_BASE.json
🤖 Enhanced Intelligent bot started!
📢 Listening for messages in channel C09M2PHPRJ6
💬 Now with Claude AI for creative generation!
```

---

### Step 8: Test in Slack

Open Slack → #claude:
```
@Legacy Wine MCP Bot create a creative bourbon post for Sunday
```

**Bot will:**
1. Acknowledge: "✅ Using Claude AI to create a creative post..."
2. Call Claude API to generate creative copy
3. Post the AI-generated content with image
4. Say: "🎉 Post created with Claude AI! React with ✅"

---

### Step 9: Compare Generation Quality

#### Template-Based (Old):
```
🥃 SUNDAY BOURBON SELECTION 🥃

Unwind this Sunday with premium bourbon!

🌟 Buffalo Trace
🌟 Maker's Mark
🌟 Woodford Reserve

Visit Legacy Wine & Liquor!
```

#### Claude AI-Generated (New):
```
🥃 SUNDAY BOURBON TREASURES 🥃

Discover the art of fine bourbon this Sunday! From the smooth caramel notes of Buffalo Trace to the wheated warmth of Maker's Mark, our expertly curated collection offers something for every palate. Whether you're a bourbon enthusiast or just beginning your journey, our knowledgeable staff is here to guide you to your perfect bottle.

✨ Buffalo Trace - Kentucky's finest, rich vanilla & toffee notes
✨ Maker's Mark - Smooth wheated bourbon, cherry & oak
✨ Woodford Reserve - Complex & balanced, perfect neat or cocktails
✨ Four Roses Single Barrel - Floral spice, bourbon perfection
✨ Wild Turkey 101 - Bold & robust, legendary character

Stop by Legacy Wine & Liquor in Downtown Sanford today! Our bourbon collection is waiting to elevate your Sunday evening.

📍 Open Sunday | Downtown Sanford, FL
🥃 Expert recommendations available

#Bourbon #Whiskey #LegacyWine #SanfordFL #BourbonLover #WhiskeyWednesday #DowntownSanford #FloridaLiving #PremiumSpirits #SundayVibes #CraftSpirits #LocalBusiness
```

**Notice the difference:**
- More creative and engaging
- Descriptive product details
- Better flow and storytelling
- Personalized to request
- More natural and authentic

---

### Step 10: Update Render Deployment (Optional)

If you deployed to Render in Phase 2:

```bash
# Rename enhanced version to main
mv intelligent-slack-bot-enhanced.py intelligent-slack-bot.py

# Commit and push
git add .
git commit -m "Add Claude API integration"
git push
```

**Add ANTHROPIC_API_KEY to Render:**
1. Render Dashboard → Your Service
2. Environment → Add Environment Variable
3. Key: `ANTHROPIC_API_KEY`
4. Value: `sk-ant-api03-...`
5. Save

Render will auto-redeploy with Claude API!

---

## 💰 Claude API Pricing

### How It Works
- Charged per token (words processed)
- Input tokens: $3 per 1M tokens
- Output tokens: $15 per 1M tokens

### Real Usage Examples

**1 Social Media Post:**
- Input: ~500 tokens (your prompt + context)
- Output: ~300 tokens (generated post)
- Cost: ~$0.01 per post

**250 Posts/Month:**
- Cost: ~$2.50/month

**500 Posts/Month:**
- Cost: ~$5/month

**1000 Posts/Month:**
- Cost: ~$10/month

**Typical usage for Legacy Wine: $5-10/month**

---

## 🎨 Advanced Features with Claude

### 1. Conversational Editing
```
You: Create a bourbon post
Bot: [Creates post]
You: Make it more energetic
Bot: [Regenerates with energetic tone]
You: Add more product details
Bot: [Adds detailed descriptions]
```

### 2. Seasonal Adaptation
```
You: Create a summer wine post
Claude: [Focuses on rosé, light wines, pool parties]

You: Create a winter wine post  
Claude: [Focuses on reds, cozy evenings, holidays]
```

### 3. Brand Voice Consistency
Claude learns your brand voice from knowledge base and maintains it across all posts.

### 4. Creative Variations
Ask Claude to create multiple versions:
```
You: Give me 3 different bourbon post ideas
Claude: [Generates 3 unique approaches]
```

---

## ✅ Verification Checklist

Before considering Phase 3 complete:

- [ ] Anthropic account created
- [ ] API key obtained
- [ ] Credits added to account
- [ ] anthropic package installed
- [ ] ANTHROPIC_API_KEY added to .env
- [ ] test-claude.py runs successfully
- [ ] Enhanced bot script created
- [ ] Bot responds with Claude-generated content
- [ ] Quality of posts improved
- [ ] (Optional) Deployed to Render with API key

---

## 🚨 Troubleshooting

### "API key not valid"

**Fix:**
1. Check key in .env starts with `sk-ant-api03-`
2. No extra quotes or spaces
3. Key copied correctly from Anthropic console

### "Insufficient credits"

**Fix:**
1. Go to https://console.anthropic.com/settings/billing
2. Add credits ($20-50 recommended)
3. Credit card required

### "Rate limit exceeded"

**Fix:**
1. You're making too many requests too quickly
2. Add delay between requests: `time.sleep(2)`
3. Upgrade to higher tier if needed

### "Model not found"

**Fix:**
Use correct model name:
```python
model="claude-3-5-sonnet-20241022"  # Latest Claude 3.5 Sonnet
```

---

## 📊 Monitoring Usage

### Check Usage in Anthropic Console

1. Go to: https://console.anthropic.com/settings/usage
2. See:
   - Requests made
   - Tokens used
   - Cost breakdown
   - Daily/monthly usage

### Set Budget Alerts

1. Settings → Billing → Budget Alerts
2. Set alert at $5, $10, $20
3. Get email when approaching limit

---

## 🎯 Best Practices

### 1. Use Claude for Creative Tasks
- Post generation
- Variations and rewrites
- Personalized responses

### 2. Use Templates for Simple Posts
- Quick, standard posts
- Saves API costs
- Faster generation

### 3. Cache Knowledge Base
- Provide knowledge base context efficiently
- Reduce token usage

### 4. Monitor Costs
- Check usage weekly
- Set budget alerts
- Optimize prompts

---

## 🎉 Congratulations!

You've completed all 3 phases!

### Your System Now Has:
1. ✅ **Notion API** - Content planning and tracking
2. ✅ **Render Deployment** - 24/7 cloud operation
3. ✅ **Claude API** - Advanced AI generation

### What You Can Do:
- ✅ Plan content in Notion
- ✅ Message bot from anywhere (24/7)
- ✅ Generate creative, varied posts with AI
- ✅ Track performance in Notion
- ✅ Scale to unlimited posts

### Your Complete Stack:
```
Notion (Content Planning)
    ↓
Intelligent Bot (Render - 24/7)
    ↓
Claude API (AI Generation)
    ↓
Slack (Review & Approve)
    ↓
Zapier (Automation)
    ↓
Instagram (Publishing)
```

---

**Phase**: 3 of 3
**Status**: Complete ✅
**Your system is now FULLY ENHANCED! 🚀**
