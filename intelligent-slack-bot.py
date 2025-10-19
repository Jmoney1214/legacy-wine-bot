#!/usr/bin/env python3
"""
Legacy Wine & Liquor - Intelligent Slack Bot
Interactive bot that creates and edits social media posts through Slack conversations
"""

import os
import json
import time
import requests
from datetime import datetime
from pathlib import Path

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

# Load knowledge base
KNOWLEDGE_BASE_FILE = 'LEGACY_WINE_KNOWLEDGE_BASE.json'
knowledge_base = {}

if os.path.exists(KNOWLEDGE_BASE_FILE):
    with open(KNOWLEDGE_BASE_FILE, 'r') as f:
        knowledge_base = json.load(f)
    print(f"✅ Loaded knowledge base: {KNOWLEDGE_BASE_FILE}")
else:
    print(f"⚠️  Knowledge base not found: {KNOWLEDGE_BASE_FILE}")

# Unsplash image library (curated for wine/spirits)
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
    "bar": "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=1080&q=80",
    "spirits": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=1080&q=80"
}

# Conversation state storage
conversation_states = {}
recent_posts = {}  # Store recent posts for editing


class IntelligentBot:
    """Intelligent bot that understands context and generates content"""
    
    def __init__(self):
        self.kb = knowledge_base
        
    def understand_intent(self, message_text):
        """Understand what the user wants to do"""
        text_lower = message_text.lower()
        
        # Detect intent
        if any(keyword in text_lower for keyword in ['create', 'make', 'post', 'write', 'send']):
            return 'create_post'
        elif any(keyword in text_lower for keyword in ['edit', 'change', 'update', 'fix', 'modify']):
            return 'edit_post'
        elif any(keyword in text_lower for keyword in ['suggest', 'ideas', 'help', 'what should']):
            return 'suggest_content'
        elif 'schedule' in text_lower or 'later' in text_lower:
            return 'schedule_post'
        else:
            return 'general_query'
    
    def extract_product_category(self, message_text):
        """Extract what product category user is asking about"""
        text_lower = message_text.lower()
        
        # Check for specific products
        if 'wine' in text_lower:
            if 'red' in text_lower:
                return 'red_wine'
            elif 'white' in text_lower:
                return 'white_wine'
            elif 'rosé' in text_lower or 'rose' in text_lower:
                return 'rose'
            elif 'sparkling' in text_lower or 'champagne' in text_lower or 'prosecco' in text_lower:
                return 'sparkling'
            else:
                return 'wine_general'
        
        elif any(keyword in text_lower for keyword in ['bourbon', 'whiskey', 'scotch', 'johnnie walker', 'maker']):
            if 'bourbon' in text_lower:
                return 'bourbon'
            elif 'scotch' in text_lower or 'johnnie' in text_lower:
                return 'scotch'
            else:
                return 'whiskey_general'
        
        elif any(keyword in text_lower for keyword in ['vodka', 'tequila', 'rum', 'gin', 'spirit']):
            return 'spirits_general'
        
        elif 'beer' in text_lower:
            return 'beer'
        
        return None
    
    def extract_occasion(self, message_text):
        """Extract the occasion or timing"""
        text_lower = message_text.lower()
        current_day = datetime.now().strftime('%A').lower()
        
        if 'sunday' in text_lower or (current_day == 'sunday' and 'today' in text_lower):
            return 'sunday'
        elif 'weekend' in text_lower or 'saturday' in text_lower or 'friday' in text_lower:
            return 'weekend'
        elif 'brunch' in text_lower:
            return 'brunch'
        elif 'game day' in text_lower or 'gameday' in text_lower:
            return 'game_day'
        elif 'celebration' in text_lower or 'party' in text_lower:
            return 'celebration'
        elif 'date night' in text_lower:
            return 'date_night'
        
        # Default to current day context
        if current_day in ['saturday', 'sunday']:
            return 'weekend'
        else:
            return 'weekday'
    
    def generate_post(self, product_category, occasion, custom_details=None):
        """Generate a complete post based on inputs"""
        
        # Get appropriate emoji
        emoji = "🍷"
        if product_category in ['bourbon', 'scotch', 'whiskey_general']:
            emoji = "🥃"
        elif product_category == 'beer':
            emoji = "🍺"
        elif product_category == 'sparkling':
            emoji = "🥂"
        
        # Generate title
        title = self._generate_title(product_category, occasion, emoji)
        
        # Generate body
        body = self._generate_body(product_category, occasion)
        
        # Generate product list
        products = self._generate_product_list(product_category)
        
        # Generate call to action
        cta = self._generate_cta(occasion)
        
        # Get hashtags
        hashtags = self._generate_hashtags(product_category, occasion)
        
        # Select image
        image_url = self._select_image(product_category)
        
        # Combine into final post
        caption_parts = [
            title,
            "",
            body,
            "",
            products,
            "",
            cta,
            "",
            "📍 Open Sunday | Downtown Sanford, FL",
            "",
            hashtags,
            "",
            image_url
        ]
        
        caption = "\n".join(caption_parts)
        
        return {
            "channel": SLACK_CHANNEL_ID,
            "text": caption,
            "attachments": [
                {
                    "fallback": title.replace(emoji, "").strip(),
                    "image_url": image_url
                }
            ],
            "unfurl_links": False,
            "unfurl_media": True
        }
    
    def _generate_title(self, product_category, occasion, emoji):
        """Generate attention-grabbing title"""
        titles = {
            'wine_general': f"{emoji} SUNDAY WINE SPECIAL {emoji}",
            'red_wine': f"{emoji} PREMIUM RED WINE SELECTION {emoji}",
            'white_wine': f"{emoji} CRISP WHITE WINE COLLECTION {emoji}",
            'rose': f"{emoji} ROSÉ ALL DAY {emoji}",
            'sparkling': f"{emoji} SPARKLING CELEBRATION {emoji}",
            'bourbon': f"🥃 BOURBON LOVER'S SELECTION 🥃",
            'scotch': f"🥃 PREMIUM SCOTCH COLLECTION 🥃",
            'whiskey_general': f"🥃 WHISKEY WEDNESDAY 🥃",
            'spirits_general': f"🥃 PREMIUM SPIRITS SHOWCASE 🥃",
            'beer': f"🍺 CRAFT BEER SELECTION 🍺"
        }
        
        # Add occasion context
        if occasion == 'sunday':
            return titles.get(product_category, f"{emoji} SUNDAY SPECIAL {emoji}")
        elif occasion == 'weekend':
            title = titles.get(product_category, f"{emoji} WEEKEND SPECIAL {emoji}")
            return title.replace("SELECTION", "WEEKEND").replace("SPECIAL", "WEEKEND")
        
        return titles.get(product_category, f"{emoji} SPECIAL SELECTION {emoji}")
    
    def _generate_body(self, product_category, occasion):
        """Generate engaging body copy"""
        bodies = {
            'sunday': [
                "Unwind this Sunday with exceptional selections at exceptional prices!",
                "Make your Sunday special with premium selections from Legacy Wine & Liquor!",
                "Perfect Sunday starts with the perfect bottle!"
            ],
            'weekend': [
                "Elevate your weekend celebration with our premium collection!",
                "Weekend plans? We've got you covered!",
                "Make this weekend unforgettable!"
            ],
            'celebration': [
                "Celebrate in style with our premium selection!",
                "Toast to the good times with exceptional quality!",
                "Make your celebration memorable!"
            ]
        }
        
        occasion_bodies = bodies.get(occasion, bodies['sunday'])
        return occasion_bodies[0]  # Can randomize later
    
    def _generate_product_list(self, product_category):
        """Generate bullet list of products"""
        if not self.kb:
            return "✨ Premium Selection Available"
        
        products = self.kb.get('product_categories', {})
        
        product_lists = {
            'wine_general': [
                "✨ Premium Red Wines",
                "✨ Crisp White Wines",
                "✨ Elegant Rosés",
                "✨ Sparkling Champagne & Prosecco"
            ],
            'red_wine': [
                "✨ Cabernet Sauvignon",
                "✨ Pinot Noir",
                "✨ Merlot",
                "✨ Malbec"
            ],
            'bourbon': [
                "🌟 Buffalo Trace",
                "🌟 Maker's Mark",
                "🌟 Woodford Reserve",
                "🌟 Four Roses",
                "🌟 Wild Turkey"
            ],
            'scotch': [
                "✨ Johnnie Walker Red Label",
                "✨ Johnnie Walker Black Label",
                "✨ Johnnie Walker Gold Reserve",
                "✨ Johnnie Walker Blue Label"
            ]
        }
        
        return "\n".join(product_lists.get(product_category, [
            "✨ Premium Selection",
            "✨ Expert Recommendations",
            "✨ Quality Guaranteed"
        ]))
    
    def _generate_cta(self, occasion):
        """Generate call to action"""
        ctas = [
            "Visit Legacy Wine & Liquor in Downtown Sanford today!",
            "Stop by and discover your new favorite!",
            "Our wine experts are here to help you find the perfect match!",
            "Come see us in Downtown Sanford!"
        ]
        return ctas[0]  # Can randomize
    
    def _generate_hashtags(self, product_category, occasion):
        """Generate relevant hashtags"""
        if not self.kb:
            return "#LegacyWine #SanfordFL #DowntownSanford"
        
        hashtags_lib = self.kb.get('hashtag_library', {})
        primary = hashtags_lib.get('primary', [])
        
        # Add category hashtags
        category_tags = []
        if 'wine' in product_category:
            category_tags = hashtags_lib.get('wine', [])[:4]
        elif product_category in ['bourbon', 'scotch', 'whiskey_general']:
            category_tags = hashtags_lib.get('spirits', [])[:4]
        
        # Add occasion hashtags
        occasion_tags = hashtags_lib.get('occasions', [])[:2]
        
        # Combine
        all_tags = primary + category_tags + occasion_tags
        return " ".join(all_tags[:12])  # Max 12 hashtags
    
    def _select_image(self, product_category):
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


def post_to_slack(post_data, thread_ts=None):
    """Post formatted content to Slack"""
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = post_data.copy()
    if thread_ts:
        payload["thread_ts"] = thread_ts
    
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    if result.get('ok'):
        # Store the post for potential editing
        post_ts = result.get('message', {}).get('ts')
        if post_ts:
            recent_posts[post_ts] = post_data
    
    return result


def listen_for_messages():
    """Listen for messages mentioning the bot"""
    print("🤖 Intelligent bot started!")
    print(f"📢 Listening for messages in channel {SLACK_CHANNEL_ID}")
    print("💬 Mention me with requests like:")
    print("   - 'Create a post about bourbon for Sunday'")
    print("   - 'Make a wine post'")
    print("   - 'Suggest content ideas'")
    print("\nPress Ctrl+C to stop\n")
    
    bot = IntelligentBot()
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
                
                for message in reversed(messages):  # Process oldest first
                    # Check if bot is mentioned or message is a DM
                    text = message.get('text', '')
                    user = message.get('user')
                    ts = message.get('ts')
                    
                    # Skip bot's own messages
                    if user == SLACK_BOT_USER_ID:
                        continue
                    
                    # Check if bot is mentioned
                    if f'<@{SLACK_BOT_USER_ID}>' in text or message.get('channel_type') == 'im':
                        print(f"\n📨 Received message: {text[:100]}...")
                        
                        # Remove bot mention
                        clean_text = text.replace(f'<@{SLACK_BOT_USER_ID}>', '').strip()
                        
                        # Understand intent
                        intent = bot.understand_intent(clean_text)
                        
                        if intent == 'create_post':
                            # Extract details
                            product = bot.extract_product_category(clean_text)
                            occasion = bot.extract_occasion(clean_text)
                            
                            # Confirm understanding
                            send_slack_message(
                                f"✅ Got it! Creating a post about {product or 'our products'} for {occasion}...",
                                thread_ts=ts
                            )
                            
                            # Generate and post
                            post_data = bot.generate_post(product or 'wine_general', occasion)
                            result = post_to_slack(post_data, thread_ts=ts)
                            
                            if result.get('ok'):
                                send_slack_message(
                                    "🎉 Post created! React with ✅ to publish to Instagram!",
                                    thread_ts=ts
                                )
                            else:
                                send_slack_message(
                                    f"❌ Error creating post: {result.get('error')}",
                                    thread_ts=ts
                                )
                        
                        elif intent == 'suggest_content':
                            suggestions = [
                                "💡 Content Ideas:",
                                "• Sunday Wine Special - showcase premium red & white wines",
                                "• Bourbon Collection - highlight top bourbons like Buffalo Trace, Maker's Mark",
                                "• Weekend Party Essentials - spirits and mixers for entertaining",
                                "• Date Night Wines - romantic wine selections",
                                "• Craft Beer Spotlight - local and imported craft beers",
                                "\nWhich one would you like me to create?"
                            ]
                            send_slack_message("\n".join(suggestions), thread_ts=ts)
                        
                        else:
                            # General help response
                            help_text = [
                                "👋 Hi! I can help you create Instagram posts!",
                                "",
                                "Try saying:",
                                "• 'Create a post about bourbon'",
                                "• 'Make a Sunday wine post'",
                                "• 'Suggest content ideas'",
                                "• 'Post about scotch for the weekend'",
                                "",
                                "I'll generate a professional post with images, hashtags, and captions!"
                            ]
                            send_slack_message("\n".join(help_text), thread_ts=ts)
            
            last_check = time.time()
            time.sleep(5)  # Check every 5 seconds
            
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
