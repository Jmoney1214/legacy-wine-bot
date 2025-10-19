# 📝 UPDATED ZAPIER MCP COMMANDS - OAuth Version

## 🆕 Instagram OAuth Connection

### 1. Add Instagram for Business Integration
```bash
claude mcp zapier add_tools
# Select "Instagram for Business"
# Click "Connect a new account"
```

### 2. Test Instagram Connection
```bash
# This will show if Instagram is connected
claude mcp zapier instagram_for_business_publish_photo_s '{
  "instructions": "Test connection only",
  "caption": "TEST",
  "media": "https://example.com/test.jpg"
}'
```

## 📱 Instagram Publishing (No Token Needed!)

### Publish Single Photo
```bash
claude mcp zapier instagram_for_business_publish_photo_s '{
  "instructions": "Post to Instagram",
  "caption": "🍷 Sanford Bike Week is HERE! #LegacyWine #BikeWeek2025",
  "media": "https://images.unsplash.com/photo-1558981852-426c6c22a060",
  "instagramPageId": "AUTO"
}'
```

### Publish Carousel (Multiple Photos)```bash
claude mcp zapier instagram_for_business_publish_photo_s '{
  "instructions": "Post carousel to Instagram",
  "caption": "Check out our premium selection! 🍷",
  "media": ["https://url1.jpg", "https://url2.jpg", "https://url3.jpg"]
}'
```

### Publish Video
```bash
claude mcp zapier instagram_for_business_publish_video '{
  "instructions": "Post video to Instagram",
  "caption": "New arrivals at Legacy Wine! 🍾",
  "video": "https://example.com/video.mp4"
}'
```

## 🔧 Slack Commands (Same as Before)

### Find Messages with Reactions
```bash
claude mcp zapier slack_find_message '{
  "instructions": "Find messages from Legacy Wine MCP Bot with white_check_mark",
  "query": "from:Legacy Wine MCP Bot in:#claude has:white_check_mark",
  "sort_by": "timestamp"
}'
```

### Send Confirmation to Slack
```bash
claude mcp zapier slack_send_channel_message '{
  "instructions": "Send confirmation to #claude",