#!/usr/bin/env python3
"""
Legacy Wine Slack-to-Social Automation for Claude Code - V2.0
Updated for Zapier Instagram for Business OAuth Integration (2025)
No manual Instagram tokens needed!
"""

import json
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import subprocess

class LegacyWineZapAutomation:
    """Main automation class using Zapier MCP with OAuth"""
    
    def __init__(self):
        self.config = self.load_config()
        self.processed_messages = set()
        self.instagram_connected = False
        
    def load_config(self) -> Dict:
        """Load configuration from JSON file"""
        config_file = 'slack-social-zap-config-v2.json'
        if not os.path.exists(config_file):
            config_file = 'slack-social-zap-config.json'
        
        with open(config_file, 'r') as f:
            return json.load(f)
    
    def run_zapier_mcp_command(self, command: str) -> str:        """Execute Zapier MCP command in Claude Code terminal"""
        full_command = f"claude mcp zapier {command}"
        print(f"🔧 Executing: {full_command}")
        
        try:
            result = subprocess.run(
                full_command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            print(f"❌ Error: {e}")
            return str(e)
    
    def connect_instagram(self):
        """Connect to Instagram using OAuth (no tokens needed!)"""
        print("\n📱 Connecting to Instagram for Business...")
        print("━" * 50)
        
        # Test Instagram connection
        test_command = 'instagram_for_business_publish_photo_s \'{"instructions": "Test connection", "caption": "TEST - DO NOT POST", "media": "https://example.com/test.jpg", "instagramPageId": "TEST"}\''
        
        result = self.run_zapier_mcp_command(test_command)
        
        if "No options available" in result or "not connected" in result.lower():            print("""
⚠️  Instagram not connected! Follow these steps:

1. Run: claude mcp zapier add_tools
2. Choose "Instagram for Business"
3. Click "Connect a new account"
4. Log in with Facebook (personal account that manages business)
5. Select your Facebook Page
6. Grant all permissions
7. Click "Done"

If account not showing:
- Go to https://www.facebook.com/settings?tab=business_tools
- Find Zapier → View and edit
- Enable Instagram permissions
- Reconnect in Zapier
            """)
            return False
        else:
            print("✅ Instagram for Business connected via OAuth!")
            self.instagram_connected = True
            return True
    
    def check_slack_reactions(self) -> List[Dict]:
        """Check for new white_check_mark reactions"""
        command = f'''slack_find_message '{{
            "instructions": "Find messages from Legacy Wine MCP Bot in #claude with white_check_mark reactions from last hour",
            "query": "from:Legacy Wine MCP Bot in:#claude has:white_check_mark",