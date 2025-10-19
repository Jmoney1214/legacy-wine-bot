# 📝 ZAPIER MCP COMMANDS FOR CLAUDE CODE

## Essential Commands for Legacy Wine Automation

### 1. Test Slack Connection
```bash
claude mcp zapier slack_find_user_by_name '{
  "full_name": "Legacy Wine MCP Bot",
  "instructions": "Find the Legacy Wine bot user"
}'
```

### 2. Get Channel Info
```bash
claude mcp zapier slack_get_conversation '{
  "channel": "claude",
  "instructions": "Get info about #claude channel"
}'
```

### 3. Find Messages with Reactions
```bash
claude mcp zapier slack_find_message '{
  "instructions": "Find messages from Legacy Wine MCP Bot in #claude with white_check_mark reactions",
  "query": "from:Legacy Wine MCP Bot in:#claude has:white_check_mark",
  "sort_by": "timestamp",
  "sort_dir": "desc"
}'
```

### 4. Get Message Reactions
```bash