# 🚀 Render Deployment Guide
## Deploy Legacy Wine Bot to Cloud (24/7 Operation)

---

## ✅ Prerequisites Completed
- ✅ Render account created
- ✅ GitHub repository: https://github.com/Jmoney1214/legacy-wine-bot
- ✅ Code pushed to GitHub

---

## 📋 Step-by-Step Deployment

### Step 1: Go to Render Dashboard
1. Open: https://dashboard.render.com
2. Log in with your account

### Step 2: Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**

### Step 3: Connect GitHub Repository
1. Click **"Connect GitHub"** (if not already connected)
2. Authorize Render to access your GitHub account
3. Find and select: **"legacy-wine-bot"**
4. Click **"Connect"**

### Step 4: Configure Web Service

**Basic Settings:**
- **Name**: `legacy-wine-bot` (or any name you prefer)
- **Region**: Oregon (US West) - *recommended for best performance*
- **Branch**: `main`
- **Root Directory**: *(leave blank)*
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python intelligent-slack-bot.py`

### Step 5: Add Environment Variables

Click **"Add Environment Variable"** and add each of these:

| Key | Value |
|-----|-------|
| `SLACK_BOT_TOKEN` | Your bot token (starts with `xoxb-`) |
| `SLACK_USER_TOKEN` | Your user token (starts with `xoxp-`) |
| `SLACK_CHANNEL_ID` | Your channel ID |
| `SLACK_BOT_USER_ID` | Your bot user ID |
| `ZAPIER_API_KEY` | Your Zapier API key |
| `NOTION_API_KEY` | Your Notion API key |

**To find your credentials:**
- Check your local `.env` file: `/Users/justinetwaru/Desktop/claude code oct19/.env`
- Or check the Postman environment file (local copy only)

### Step 6: Choose Plan

**Free Plan** (recommended to start):
- ✅ 750 hours/month (enough for 24/7 if only 1 service)
- ✅ Automatic deploys from GitHub
- ✅ Custom domain support
- ⚠️ Sleeps after 15 min of inactivity (wakes on first request)

**Starter Plan** ($7/month):
- ✅ Never sleeps (true 24/7)
- ✅ More compute resources
- ✅ Priority support

**Select:** Free (for testing) or Starter (for production)

### Step 7: Deploy
1. Click **"Create Web Service"**
2. Render will start building and deploying
3. Watch the deploy logs in real-time

---

## 🔍 Verify Deployment

### Check 1: Build Logs
You should see:
```
==> Installing dependencies
Successfully installed requests-2.31.0 python-dotenv-1.0.0 ...

==> Starting service
Bot is running! Listening for Slack events...
```

### Check 2: Service Status
- Status should show: **"Live"** (green)
- URL will be: `https://legacy-wine-bot.onrender.com` (or similar)

### Check 3: Test in Slack
1. Go to your Slack channel
2. Type: `@LegacyBot create a wine post for Sunday`
3. Bot should respond (even if you close your laptop!)

---

## 🎯 What Happens Next

### Automatic Deploys
- Every time you push to GitHub `main` branch
- Render automatically rebuilds and redeploys
- Zero downtime deployments

### 24/7 Operation
**Free Plan:**
- Bot sleeps after 15 min of no activity
- Wakes up on first Slack message (may take 30 seconds)
- Perfect for testing

**Starter Plan ($7/month):**
- Never sleeps
- Instant responses
- True 24/7 operation

---

## 🔧 Troubleshooting

### Error: "Build Failed"
**Check:**
- `requirements.txt` exists in repository
- All dependencies are spelled correctly
- Python version in `runtime.txt` is supported (3.11.6 is good)

**Fix:** Check build logs for specific error

### Error: "Application Failed to Start"
**Check:**
- Start command is: `python intelligent-slack-bot.py`
- File name is correct (case-sensitive)
- Environment variables are set

**Fix:** Check service logs for error messages

### Bot Not Responding in Slack
**Check:**
1. Service status is "Live" in Render dashboard
2. All environment variables are set correctly
3. Bot tokens haven't expired
4. Channel ID is correct

**Fix:** Check service logs for errors

---

## 📊 Monitor Your Bot

### View Logs
1. Go to Render dashboard
2. Click on your service: `legacy-wine-bot`
3. Click **"Logs"** tab
4. See real-time bot activity

### Example Log Output:
```
[2025-10-19 15:30:45] Bot started successfully
[2025-10-19 15:31:02] Message received from user U123456
[2025-10-19 15:31:02] Intent: create_post | Product: wine | Occasion: Sunday
[2025-10-19 15:31:03] Post generated and sent to Slack
```

---

## 🔄 Update Your Bot

### To deploy changes:
1. Edit code on your computer
2. Commit changes: `git add . && git commit -m "Update bot"`
3. Push to GitHub: `git push`
4. Render automatically detects and deploys

**No need to:**
- Manually restart anything
- Re-enter environment variables
- Reconfigure settings

---

## 💰 Cost Breakdown

### Free Plan
- **Cost**: $0/month
- **Limitations**: Sleeps after inactivity, 750 hours/month
- **Best for**: Testing, low-volume usage

### Starter Plan
- **Cost**: $7/month
- **Benefits**: Never sleeps, more resources, priority support
- **Best for**: Production, 24/7 instant responses

**Recommendation:** Start with Free, upgrade to Starter when you need instant responses.

---

## 🎉 Success Checklist

After deployment, verify:
- ✅ Render service shows "Live" status
- ✅ Build logs show successful installation
- ✅ Service logs show "Bot is running!"
- ✅ Bot responds to Slack messages
- ✅ Posts are generated correctly
- ✅ Knowledge base is being used

---

## 📞 Next Steps

**After Render deployment works:**
1. Test bot thoroughly in Slack
2. Try different commands:
   - "create a bourbon post"
   - "make a Sunday brunch wine post"
   - "post about whiskey for the weekend"
3. Check generated posts quality
4. Move to Phase 3: Add Claude API for even better AI content

---

## 🔗 Quick Links

- **Render Dashboard**: https://dashboard.render.com
- **GitHub Repository**: https://github.com/Jmoney1214/legacy-wine-bot
- **Documentation**: Check other `.md` files in project
- **Support**: Render has great docs at https://render.com/docs

---

**Created**: October 19, 2025
**Status**: Ready to Deploy
**Next Phase**: Claude API Integration (Phase 3)
