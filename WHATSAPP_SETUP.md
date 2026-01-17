# 📱 WHATSAPP SETUP

## ✅ WhatsApp Added!

**1 clap** now opens WhatsApp! 👏

---

## 🎯 Your Complete Commands

```
👏                 = WhatsApp 📱
👏👏               = VS Code 💻
👏👏👏             = Valorant 🎮
👏👏👏👏           = Chrome (harishlalme9a@gmail.com) 🌐
👏👏👏👏👏         = Brave Browser 🦁
```

---

## 🧪 Test WhatsApp First

**Method 1: Protocol Handler (Already configured)**
```cmd
start whatsapp:
```
✅ Opens WhatsApp Desktop app (if installed)

**Method 2: Direct Path**
If that doesn't work, WhatsApp is usually here:
```
C:\Users\HARISHLAL'S PC\AppData\Local\WhatsApp\WhatsApp.exe
```

**Test it:**
```cmd
"C:\Users\HARISHLAL'S PC\AppData\Local\WhatsApp\WhatsApp.exe"
```

**Method 3: Web WhatsApp**
If you use WhatsApp Web instead:
```cmd
start chrome --app=https://web.whatsapp.com
```

---

## ⚙️ Update Config (If Needed)

**If `start whatsapp:` doesn't work:**

### For WhatsApp Desktop App:
```json
"1": {
    "name": "WhatsApp",
    "windows": "\"C:\\Users\\HARISHLAL'S PC\\AppData\\Local\\WhatsApp\\WhatsApp.exe\""
}
```

### For WhatsApp Web:
```json
"1": {
    "name": "WhatsApp",
    "windows": "start chrome --app=https://web.whatsapp.com"
}
```

---

## 🚀 Quick Test

```powershell
python jarvis_launcher.py
```

Say "Jarvis" → 👏 (one clap) → WhatsApp opens! 📱

---

## 💡 Tips

**Single Clap Tip:**
- Make it a clean, loud clap 👏
- Wait for the detection message
- System will wait 2.5 seconds for more claps
- If no more claps → launches WhatsApp!

**Example:**
```
You: "Jarvis"
🔔 *BEEP*
You: 👏 (wait 2.5 seconds)
📊 Total claps detected: 1
🚀 Launching WhatsApp...
✅ WhatsApp launched successfully!
👋 Jarvis is shutting down...
```

---

## 📂 Finding WhatsApp Location

**If you need to find where WhatsApp is installed:**

```cmd
where WhatsApp
```

Or check these common locations:
- `C:\Users\HARISHLAL'S PC\AppData\Local\WhatsApp\WhatsApp.exe`
- `C:\Program Files\WhatsApp\WhatsApp.exe`
- `C:\Program Files (x86)\WhatsApp\WhatsApp.exe`

---

## ✅ Complete Updated Config

```json
{
    "1": {
        "name": "WhatsApp",
        "windows": "start whatsapp:"
    },
    "2": {
        "name": "VS Code",
        "windows": "code"
    },
    "3": {
        "name": "Valorant",
        "windows": "\"E:\\VALO\\Riot Games\\Riot Client\\RiotClientServices.exe\" --launch-product=valorant --launch-patchline=live"
    },
    "4": {
        "name": "Chrome (harishlalme9a@gmail.com)",
        "windows": "start chrome --profile-directory=\"Default\""
    },
    "5": {
        "name": "Brave Browser",
        "windows": "start brave"
    }
}
```

---

## 🎯 All Your Commands

| Claps | App | Command |
|-------|-----|---------|
| 👏 | WhatsApp | Say "Jarvis" + 1 clap |
| 👏👏 | VS Code | Say "Jarvis" + 2 claps |
| 👏👏👏 | Valorant | Say "Jarvis" + 3 claps |
| 👏👏👏👏 | Chrome (Profile) | Say "Jarvis" + 4 claps |
| 👏👏👏👏👏 | Brave | Say "Jarvis" + 5 claps |

---

**You're all set!** 🎉

Just test: `start whatsapp:` in cmd

If that works, you're good to go! If not, update the path in `app_config.json` 📱
