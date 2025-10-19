# ⚡ Deploy to Render NOW - Quick Checklist

## 🎯 You're Ready to Deploy!

Everything is set up. Follow these steps exactly:

---

## Step 1: Go to Render
**Open:** https://dashboard.render.com

---

## Step 2: Create New Web Service
1. Click **"New +"** (top right)
2. Select **"Web Service"**
3. Click **"Connect GitHub"** (if needed)
4. Find and select: **legacy-wine-bot**
5. Click **"Connect"**

---

## Step 3: Configure Service

**Fill in these fields:**

| Field | Value |
|-------|-------|
| Name | `legacy-wine-bot` |
| Region | `Oregon (US West)` |
| Branch | `main` |
| Root Directory | *(leave blank)* |
| Runtime | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python intelligent-slack-bot.py` |

---

## Step 4: Add Environment Variables

Click **"Add Environment Variable"** button

**Then add these 6 variables:**

Open the file: `RENDER-ENV-VARIABLES.md` (in this folder)

Copy each Key and Value from that file into Render.

**Quick checklist:**
- [ ] SLACK_BOT_TOKEN
- [ ] SLACK_USER_TOKEN
- [ ] SLACK_CHANNEL_ID
- [ ] SLACK_BOT_USER_ID
- [ ] ZAPIER_API_KEY
- [ ] NOTION_API_KEY

---

## Step 5: Choose Plan

**Free Plan** (recommended to start):
- Free for 750 hours/month
- Sleeps after 15 min of inactivity
- Wakes on first message (30 sec delay)

**Or Starter Plan** ($7/month):
- Never sleeps
- Instant responses 24/7

**Select your plan** and click **"Create Web Service"**

---

## Step 6: Wait for Deployment

You'll see:
```
==> Cloning repository...
==> Installing dependencies...
==> Starting service...
```

**Wait for:** Status shows **"Live"** (green)

Should take 2-3 minutes.

---

## Step 7: Test It!

1. Go to Slack: #claude channel
2. Type: `@LegacyBot create a wine post for Sunday`
3. Bot should respond!

**If it works:**
- ✅ Bot is now running 24/7 in the cloud
- ✅ You can close your laptop and bot still works
- ✅ Every GitHub push auto-deploys updates

---

## 🚨 If Something Goes Wrong

### Build Failed
- Check Render logs for error messages
- Verify `requirements.txt` exists in GitHub
- Verify Python version is 3.11.6

### Bot Not Responding
- Check Render service status is "Live"
- Check environment variables are all set
- Check Render logs for errors

---

## 📊 Monitor Your Bot

**View logs:**
1. Render dashboard → your service
2. Click **"Logs"** tab
3. See real-time activity

**Expected log output:**
```
Bot is running! Listening for Slack events...
Message received from user U123456
Intent: create_post | Product: wine
Post generated and sent!
```

---

## 🎉 After Successful Deployment

**Next steps:**
1. Test different bot commands in Slack
2. Verify knowledge base is working
3. Check post quality and formatting
4. Move to **Phase 3: Claude API** for even better AI content

---

## 📁 Files You Need

**In this folder:**
- ✅ `RENDER-DEPLOYMENT-GUIDE.md` - Full detailed guide
- ✅ `RENDER-ENV-VARIABLES.md` - Your credentials to copy
- ✅ `DEPLOY-NOW.md` - This quick checklist

**On GitHub:**
- ✅ All code is already pushed
- ✅ Repository: https://github.com/Jmoney1214/legacy-wine-bot

---

## ⏱️ Time Estimate

- **Setup in Render:** 5-10 minutes
- **Deployment wait:** 2-3 minutes
- **Testing:** 2 minutes
- **Total:** ~15 minutes

---

**Ready? Go to:** https://dashboard.render.com

**Start with:** New + → Web Service → Connect GitHub → legacy-wine-bot

---

**Status:** ✅ Code is ready | ✅ GitHub is ready | ⏳ Deploy to Render NOW!
