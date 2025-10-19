#!/bin/bash

###############################################################################
# Legacy Wine & Liquor - Slack to Instagram Automation
# Complete Setup and Startup Script
# Created: October 19, 2025
###############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

###############################################################################
# Helper Functions
###############################################################################

print_header() {
    echo ""
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}============================================${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

###############################################################################
# Check System Requirements
###############################################################################

check_system_requirements() {
    print_header "Checking System Requirements"
    
    # Check for macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        print_success "Running on macOS"
    else
        print_warning "This script is optimized for macOS"
    fi
    
    # Check for Homebrew
    if command -v brew &> /dev/null; then
        print_success "Homebrew is installed"
    else
        print_error "Homebrew not found"
        echo "Install Homebrew first: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
}

###############################################################################
# Install Python and Dependencies
###############################################################################

install_python() {
    print_header "Setting Up Python Environment"
    
    # Check Python 3
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python 3 is installed: $PYTHON_VERSION"
    else
        print_info "Installing Python 3..."
        brew install python3
        print_success "Python 3 installed"
    fi
    
    # Check pip3
    if command -v pip3 &> /dev/null; then
        print_success "pip3 is installed"
    else
        print_info "Installing pip3..."
        python3 -m ensurepip --upgrade
        print_success "pip3 installed"
    fi
    
    # Install Python packages
    print_info "Installing Python packages..."
    
    # Required packages
    PYTHON_PACKAGES=(
        "requests"
        "python-dotenv"
    )
    
    for package in "${PYTHON_PACKAGES[@]}"; do
        if pip3 show "$package" &> /dev/null; then
            print_success "$package already installed"
        else
            print_info "Installing $package..."
            pip3 install "$package" --quiet
            print_success "$package installed"
        fi
    done
}

###############################################################################
# Install Node.js and npm
###############################################################################

install_nodejs() {
    print_header "Setting Up Node.js Environment"
    
    # Check Node.js
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node --version)
        print_success "Node.js is installed: $NODE_VERSION"
    else
        print_info "Installing Node.js..."
        brew install node
        print_success "Node.js installed"
    fi
    
    # Check npm
    if command -v npm &> /dev/null; then
        NPM_VERSION=$(npm --version)
        print_success "npm is installed: $NPM_VERSION"
    else
        print_error "npm not found (should come with Node.js)"
        exit 1
    fi
}

###############################################################################
# Install/Configure MCP (Model Context Protocol)
###############################################################################

install_mcp() {
    print_header "Setting Up MCP (Model Context Protocol)"
    
    # Check if Claude Desktop is installed
    CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
    
    if [ -d "$CLAUDE_CONFIG_DIR" ]; then
        print_success "Claude Desktop configuration directory found"
    else
        print_warning "Claude Desktop config directory not found"
        print_info "Creating directory: $CLAUDE_CONFIG_DIR"
        mkdir -p "$CLAUDE_CONFIG_DIR"
    fi
    
    # Check for MCP server configuration
    MCP_CONFIG_FILE="$CLAUDE_CONFIG_DIR/claude_desktop_config.json"
    
    if [ -f "$MCP_CONFIG_FILE" ]; then
        print_success "MCP configuration file exists"
        
        # Check if Zapier MCP is configured
        if grep -q "zapier" "$MCP_CONFIG_FILE"; then
            print_success "Zapier MCP server is configured"
        else
            print_warning "Zapier MCP not found in configuration"
            print_info "You may need to add Zapier MCP manually"
        fi
    else
        print_warning "MCP configuration file not found"
        print_info "Will create a basic configuration"
        
        # Create basic MCP config
        cat > "$MCP_CONFIG_FILE" << 'EOFMCP'
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-zapier"],
      "env": {
        "ZAPIER_API_KEY": ""
      }
    }
  }
}
EOFMCP
        print_success "Basic MCP configuration created"
        print_warning "You need to add your ZAPIER_API_KEY to: $MCP_CONFIG_FILE"
    fi
}

###############################################################################
# Install npm Packages (if needed)
###############################################################################

install_npm_packages() {
    print_header "Setting Up npm Packages"
    
    # Check if package.json exists
    if [ -f "package.json" ]; then
        print_info "Found package.json, installing dependencies..."
        npm install
        print_success "npm packages installed"
    else
        print_info "No package.json found, checking global packages..."
        
        # Install MCP server for Zapier globally (optional)
        if npm list -g @modelcontextprotocol/server-zapier &> /dev/null; then
            print_success "Zapier MCP server already installed globally"
        else
            print_info "Installing Zapier MCP server globally..."
            npm install -g @modelcontextprotocol/server-zapier
            print_success "Zapier MCP server installed"
        fi
    fi
}

###############################################################################
# Check and Configure Environment Variables
###############################################################################

configure_environment() {
    print_header "Configuring Environment Variables"
    
    if [ -f ".env" ]; then
        print_success ".env file found"
        
        # Check if all required variables are present
        REQUIRED_VARS=(
            "SLACK_BOT_TOKEN"
            "SLACK_USER_TOKEN"
            "SLACK_CHANNEL_ID"
            "SLACK_BOT_USER_ID"
            "ZAPIER_API_KEY"
        )
        
        MISSING_VARS=()
        
        for var in "${REQUIRED_VARS[@]}"; do
            if grep -q "^$var=" .env; then
                # Check if variable has a value
                VALUE=$(grep "^$var=" .env | cut -d'=' -f2 | tr -d '"' | tr -d "'")
                if [ -n "$VALUE" ]; then
                    print_success "$var is set"
                else
                    print_warning "$var is present but empty"
                    MISSING_VARS+=("$var")
                fi
            else
                print_error "$var is missing"
                MISSING_VARS+=("$var")
            fi
        done
        
        if [ ${#MISSING_VARS[@]} -eq 0 ]; then
            print_success "All environment variables are configured"
        else
            print_warning "Some environment variables need configuration:"
            for var in "${MISSING_VARS[@]}"; do
                echo "  - $var"
            done
            print_info "Please edit the .env file and add the missing values"
        fi
    else
        print_error ".env file not found"
        print_info "Creating template .env file..."
        
        cat > .env << 'EOFENV'
# Slack Configuration
SLACK_BOT_TOKEN="xoxb-your-bot-token-here"
SLACK_USER_TOKEN="xoxp-your-user-token-here"
SLACK_CHANNEL_ID="C09M2PHPRJ6"
SLACK_BOT_USER_ID="U09LZ8FUHNH"

# Zapier Configuration
ZAPIER_API_KEY="sk-ak-your-zapier-api-key-here"
EOFENV
        
        print_success "Template .env file created"
        print_warning "Please edit .env and add your API credentials"
        exit 1
    fi
}

###############################################################################
# Verify Setup
###############################################################################

verify_setup() {
    print_header "Verifying Setup"
    
    if [ -f "verify-setup.py" ]; then
        print_info "Running verification script..."
        python3 verify-setup.py
    else
        print_warning "verify-setup.py not found, skipping verification"
    fi
}

###############################################################################
# Create Additional Helper Scripts
###############################################################################

create_helper_scripts() {
    print_header "Creating Helper Scripts"
    
    # Create quick post script
    cat > post-to-slack.sh << 'EOFPOST'
#!/bin/bash
# Quick script to post to Slack

if [ $# -eq 0 ]; then
    echo "Usage: ./post-to-slack.sh <post-file.json>"
    echo "Example: ./post-to-slack.sh slack-posts/sunday-wine.json"
    exit 1
fi

POST_FILE="$1"

if [ ! -f "$POST_FILE" ]; then
    echo "Error: File not found: $POST_FILE"
    exit 1
fi

# Load bot token from .env
SLACK_BOT_TOKEN=$(grep SLACK_BOT_TOKEN .env | cut -d'=' -f2 | tr -d '"' | tr -d "'")

if [ -z "$SLACK_BOT_TOKEN" ]; then
    echo "Error: SLACK_BOT_TOKEN not found in .env"
    exit 1
fi

echo "Posting to Slack..."
curl -X POST https://slack.com/api/chat.postMessage \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d @"$POST_FILE"

echo ""
echo "✅ Post sent! Check Slack and react with ✅ to publish to Instagram"
EOFPOST
    
    chmod +x post-to-slack.sh
    print_success "Created post-to-slack.sh"
    
    # Create run automation script
    cat > run-automation.sh << 'EOFRUN'
#!/bin/bash
# Run the automation script

if [ ! -f "claude-code-zap-execution.py" ]; then
    echo "Error: claude-code-zap-execution.py not found"
    exit 1
fi

echo "Starting Legacy Wine & Liquor automation..."
python3 claude-code-zap-execution.py
EOFRUN
    
    chmod +x run-automation.sh
    print_success "Created run-automation.sh"
}

###############################################################################
# Display Usage Instructions
###############################################################################

display_usage() {
    print_header "Setup Complete! 🎉"
    
    echo ""
    echo -e "${GREEN}All dependencies installed and configured!${NC}"
    echo ""
    echo -e "${BLUE}📝 Quick Start Guide:${NC}"
    echo ""
    echo "1. Verify everything is working:"
    echo "   ${YELLOW}python3 verify-setup.py${NC}"
    echo ""
    echo "2. Post to Slack manually:"
    echo "   ${YELLOW}./post-to-slack.sh slack-posts/sunday-wine.json${NC}"
    echo ""
    echo "3. Run automation (monitors Slack reactions):"
    echo "   ${YELLOW}./run-automation.sh${NC}"
    echo ""
    echo "4. View documentation:"
    echo "   ${YELLOW}cat README.md${NC}"
    echo "   ${YELLOW}cat REACTION-TO-INSTAGRAM-ZAP.md${NC}"
    echo ""
    echo -e "${BLUE}📂 Important Files:${NC}"
    echo "   .env - Your API credentials"
    echo "   slack-posts/ - Sample posts ready to use"
    echo "   README.md - Complete documentation"
    echo "   INVENTORY.md - What's included in this folder"
    echo ""
    echo -e "${BLUE}🔗 Workflow:${NC}"
    echo "   1. Run post-to-slack.sh with a post file"
    echo "   2. Check #claude channel in Slack"
    echo "   3. React with ✅ to publish to Instagram"
    echo "   4. Check Instagram to verify post appeared"
    echo ""
    echo -e "${GREEN}Ready to go! 🚀${NC}"
    echo ""
}

###############################################################################
# Main Execution
###############################################################################

main() {
    clear
    
    echo ""
    echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                                                        ║${NC}"
    echo -e "${BLUE}║   Legacy Wine & Liquor - Automation Setup Script      ║${NC}"
    echo -e "${BLUE}║   Slack to Instagram Publishing System                ║${NC}"
    echo -e "${BLUE}║                                                        ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    # Run all setup steps
    check_system_requirements
    install_python
    install_nodejs
    install_mcp
    install_npm_packages
    configure_environment
    create_helper_scripts
    verify_setup
    display_usage
}

# Run main function
main
