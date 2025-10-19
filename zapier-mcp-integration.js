#!/usr/bin/env node

/**
 * Legacy Wine Zapier MCP Integration
 * Runs in Claude Code to automate Slack to Instagram posting
 */

const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

// Configuration
const CONFIG = {
  slackChannel: 'claude',
  botName: 'Legacy Wine MCP Bot',
  triggerEmoji: 'white_check_mark',
  pollingInterval: 60000 // 60 seconds
};

class ZapierMCPAutomation {
  constructor() {
    this.processedMessages = new Set();
  }

  /**
   * Execute Zapier MCP command via Claude Code
   */
  async runZapierCommand(tool, params) {
    const command = `claude mcp zapier ${tool} '${JSON.stringify(params)}'`;
    console.log(`🔧 Running: ${tool}`);
    
    try {
      const { stdout, stderr } = await execPromise(command);