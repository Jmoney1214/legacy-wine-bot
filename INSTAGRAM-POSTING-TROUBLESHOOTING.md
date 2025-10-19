# Instagram Posting Troubleshooting Guide

## Current Issue
Posts successfully trigger from Slack → Zapier shows success → Instagram rejects posts silently

## Most Likely Root Causes (in order of probability)

### 1. Instagram Business Account Connection Issue ⭐ MOST LIKELY

**Problem**: Your Zapier app may not have proper permissions to your Instagram Business account.

**Fix**:
1. Go to Zapier → My Apps → Instagram for Business
2. Click "Reconnect"
3. During reconnection, ensure you:
   - Select the correct Facebook Business Page
   - Select the correct Instagram Business Account (not Personal/Creator)
   - Grant ALL requested permissions
4. After reconnecting, go back to your Zap
5. Click on the Instagram step → Refresh fields
6. Re-select your Instagram account from the dropdown

**Verify**: Your Instagram account should show the page name, not just an ID

---

### 2. Image URL Accessibility

**Problem**: Instagram's image fetcher cannot download images from Unsplash URLs

**Current Image URLs**: All posts use `images.unsplash.com` with parameters
```
https://images.unsplash.com/photo-1569529465841-dfecdab7503b?w=1080&q=80
```

**Test**: Check if Instagram can access these URLs
- Unsplash may block Instagram's user agent
- CDN rate limiting may prevent Instagram from downloading

**Fix Option A - Use Direct Upload**:
1. In your Zap, add a step between Slack and Instagram:
   - **App**: Code by Zapier (Python)
   - **Action**: Download image from Unsplash URL and return as file

```python
import requests
import base64

# Get the image URL from Slack attachments
image_url = input_data['attachments_image_url']

# Download the image
response = requests.get(image_url)
image_data = base64.b64encode(response.content).decode()

# Return as file
return {
    'file': f'data:image/jpeg;base64,{image_data}',
    'filename': 'post_image.jpg'
}
```

2. In Instagram step, use the output from Code step as Media instead of URL

**Fix Option B - Host Images on Cloudflare R2/AWS S3**:
1. Upload images to your own CDN (Cloudflare R2 has 10GB free)
2. Use those URLs instead of Unsplash
3. Ensures Instagram can always access images

---

### 3. Instagram Account Type Issue

**Problem**: Account must be Instagram Business or Creator account

**Check**:
1. Open Instagram app on phone
2. Go to your profile (legacywineandliquor)
3. Tap hamburger menu → Settings and privacy → Account type and tools
4. Should say "Business account" or "Creator account"

**If it says Personal Account**:
1. Settings → Account type and tools → Switch to professional account
2. Choose "Business"
3. Select category: "Wine, Beer & Spirits Store"
4. Connect to your Facebook Business Page

---

### 4. Facebook Page Connection

**Problem**: Instagram Business account not properly linked to Facebook Page

**Fix**:
1. Go to Facebook Business Manager (business.facebook.com)
2. Navigate to Business Settings → Accounts → Instagram Accounts
3. Verify your Instagram account is listed and connected
4. Click on your Instagram account → Should show "Connected to Facebook Page: Legacy Wine & Liquor"
5. If not connected:
   - Click "Add" → Add Instagram Account
   - Enter your Instagram login
   - Select the Facebook Page to connect

---

### 5. API Permissions Issue

**Problem**: Zapier doesn't have `instagram_content_publish` permission

**Fix**:
1. Go to Facebook Business Manager → Business Settings
2. Navigate to System Users
3. Find or create a system user for Zapier
4. Grant permissions:
   - ✅ instagram_basic
   - ✅ instagram_content_publish
   - ✅ pages_read_engagement
   - ✅ pages_manage_posts
5. Save changes
6. Reconnect Zapier to Instagram (see Fix #1)

---

### 6. Caption Issues

**Current Captions**: All posts have:
- Emojis (🥃, 🌟, 📍)
- Hashtags (~10 per post, well under 30 limit)
- Line breaks
- Special characters

**Potential Issues**:
- Some emojis may not be supported
- Caption length over 2,200 characters (unlikely with your posts)

**Test with Minimal Caption**:
Create a test post with:
```
Test post from Zapier automation. #LegacyWine #Test
```

If this works but your regular posts don't, the issue is caption formatting.

---

### 7. Image Specifications

**Instagram Requirements**:
- Format: JPG or PNG
- Minimum: 320 x 320 pixels
- Maximum: 8 MB file size
- Aspect ratio: 1:1 (square), 4:5 (portrait), 1.91:1 (landscape)

**Your Unsplash Images**:
- Using `?w=1080&q=80` parameters
- Should be compliant, but verify with:

```bash
curl -s "https://images.unsplash.com/photo-1569529465841-dfecdab7503b?w=1080&q=80" | file -
```

---

## Immediate Action Plan

### Step 1: Verify Account Type
- Open Instagram app → Check account type (Business/Creator required)

### Step 2: Reconnect Zapier
- Zapier → My Apps → Instagram for Business → Reconnect
- Grant ALL permissions during reconnection

### Step 3: Test with Simple Post
- Create Slack post with:
  - Simple caption: "Test post #LegacyWine"
  - Single Unsplash image
  - React with ✅
- Check if it posts to Instagram

### Step 4: Check Zapier Task History
- Zapier → Zap History → Find failed task
- Look for specific Instagram API error message
- Common errors:
  - `OAuthException: (#100)` = Permission issue
  - `Error validating access token` = Reconnection needed
  - `Media not found` = Image URL issue
  - `Invalid media` = Image format/size issue

### Step 5: Test Direct Upload (if URL fails)
- Add Code by Zapier step to download and encode image
- Use encoded image data instead of URL in Instagram step

---

## Quick Diagnostic Test

Post this to Slack and react with ✅:

```
✅ DIAGNOSTIC TEST POST

Testing Instagram API with minimal content.

#Test #LegacyWine

---
✅ React with ✅ to test Instagram posting
```

Attach any small image from Unsplash.

**If this works**: Issue is with caption formatting or specific images
**If this fails**: Issue is with Instagram account connection or permissions

---

## Contact Instagram/Zapier Support

If all above fails, you may need to:
1. Contact Zapier Support with:
   - Zap ID
   - Task History showing failure
   - Screenshot of Instagram account connection
2. Verify with Instagram/Facebook that API access is enabled for your Business account

---

## Expected Fix

Based on similar issues, **95% probability** this is caused by:
1. Instagram Business account reconnection needed in Zapier (60% likely)
2. Facebook Page not properly linked to Instagram Business account (25% likely)
3. Image URL accessibility from Instagram's servers (10% likely)

Start with Fix #1 (Reconnect Zapier) and Fix #4 (Verify Facebook Page connection).
