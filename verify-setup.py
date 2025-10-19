#!/usr/bin/env python3
"""
Setup Verification Script for Legacy Wine Automation
Checks all configurations and connections
"""

import json
import os
import sys
from pathlib import Path

class SetupVerifier:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.success = []
        
    def check_file_exists(self, filename):
        """Check if required file exists"""
        if Path(filename).exists():
            self.success.append(f"✅ Found: {filename}")
            return True
        else:
            self.errors.append(f"❌ Missing: {filename}")
            return False
    
    def check_env_file(self):
        """Check and validate .env file"""
        if not self.check_file_exists('.env'):
            self.warnings.append("⚠️  No .env file - copy .env.example and fill in tokens")
            return False        
        # Check for required environment variables
        required_vars = [
            'SLACK_BOT_TOKEN',
            'SLACK_USER_TOKEN',
            'SLACK_CHANNEL_ID',
            'INSTAGRAM_ACCESS_TOKEN',
            'ZAPIER_API_KEY'
        ]
        
        # Load .env file
        env_vars = {}
        with open('.env', 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value.strip('"')
        
        for var in required_vars:
            if var in env_vars:
                value = env_vars[var]
                if 'YOUR' in value or not value:
                    self.warnings.append(f"⚠️  {var} not configured")
                else:
                    self.success.append(f"✅ {var}: {value[:10]}...")
            else:
                self.errors.append(f"❌ Missing: {var}")
        
        return len(self.errors) == 0
        
    def check_config_file(self):
        """Check JSON configuration"""
        if not self.check_file_exists('slack-social-zap-config.json'):
            return False
            
        try:
            with open('slack-social-zap-config.json', 'r') as f:
                config = json.load(f)
                self.success.append("✅ Valid JSON configuration")
                return True
        except json.JSONDecodeError as e:
            self.errors.append(f"❌ Invalid JSON: {e}")
            return False
    
    def print_report(self):
        """Print verification report"""
        print("\n" + "="*60)
        print("🔍 LEGACY WINE AUTOMATION SETUP VERIFICATION")
        print("="*60)
        
        if self.success:
            print("\n✅ SUCCESS:")
            for msg in self.success:
                print(f"  {msg}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for msg in self.warnings:
                print(f"  {msg}")        
        if self.errors:
            print("\n❌ ERRORS:")
            for msg in self.errors:
                print(f"  {msg}")
        
        print("\n" + "="*60)
        
        if not self.errors:
            print("🎉 READY TO RUN! Execute: python3 claude-code-zap-execution.py")
        else:
            print("⚠️  Fix errors above before running automation")
        
        print("="*60 + "\n")
    
    def run(self):
        """Run all verification checks"""
        self.check_file_exists('slack-social-zap-config.json')
        self.check_file_exists('claude-code-zap-execution.py')
        self.check_file_exists('start-automation.sh')
        self.check_file_exists('TOKEN_SETUP_GUIDE.md')
        self.check_env_file()
        self.check_config_file()
        self.print_report()

if __name__ == "__main__":
    verifier = SetupVerifier()
    verifier.run()