# 🚀 QUICK START GUIDE

## 📥 Installation (5 minutes)

### Step 1: Install Dependencies
```bash
pip install SpeechRecognition sounddevice numpy pyaudio
```

### Step 2: Run Setup Wizard (Optional)
```bash
python setup_wizard.py
```

### Step 3: Start Jarvis
```bash
python jarvis_launcher.py
```

## 🎯 How to Use

### Basic Usage:
1. **Say "Jarvis"** 🗣️
2. **Wait for beep** 🔔
3. **Clap pattern** 👏👏👏
4. **App launches!** 🚀

### Default Commands:

| Say "Jarvis" + | Launches |
|----------------|----------|
| 👏👏 (2 claps) | VS Code |
| 👏👏👏 (3 claps) | Valorant |
| 👏👏👏👏 (4 claps) | Chrome |
| 👏👏👏👏👏 (5 claps) | Discord |
| 👏👏👏👏👏👏 (6 claps) | Spotify |

## ⚙️ Customization

### Add Your Own Apps:
```bash
python config_editor.py
```

Then:
1. Choose option `2` (Add new app)
2. Enter number of claps
3. Enter app name
4. Enter launch command

### Example - Adding Notepad:
```
Number of claps: 7
App name: Notepad
Windows command: notepad
Linux command: gedit
macOS command: open -a TextEdit
```

## 🎚️ Troubleshooting

### Claps not detected?
```bash
python calibrate.py
```
- Choose option `3` (Test Clap Detection)
- Adjust threshold if needed

### Wake word not working?
- Check internet connection (needs Google API)
- Speak clearly: "JAR-VIS"
- Check microphone permissions

### App not launching?
Edit `app_config.json` with full app path:
```json
{
    "3": {
        "name": "Valorant",
        "windows": "C:\\Riot Games\\VALORANT\\live\\VALORANT.exe"
    }
}
```

## 💡 Tips

✅ **DO:**
- Speak clearly at normal volume
- Make sharp, loud claps
- Wait for beep before clapping
- Use in quiet environment

❌ **DON'T:**
- Whisper or shout
- Clap too quickly
- Clap during background noise
- Expect it to work offline (wake word needs internet)

## 🔧 Common Commands

| Action | Command |
|--------|---------|
| Start launcher | `python jarvis_launcher.py` |
| Edit apps | `python config_editor.py` |
| Calibrate | `python calibrate.py` |
| Run setup | `python setup_wizard.py` |

## 📁 Files Overview

```
jarvis-launcher/
├── jarvis_launcher.py    # 🚀 Main app (START HERE)
├── config_editor.py      # ⚙️ Edit app mappings
├── calibrate.py         # 🎚️ Adjust sensitivity
├── setup_wizard.py      # 📥 Installation helper
├── requirements.txt     # 📦 Dependencies
├── app_config.json      # ⚙️ Your app mappings
└── README.md           # 📖 Full documentation
```

## 🎮 Example Session

```
$ python jarvis_launcher.py

🎯 Jarvis App Launcher Initialized
💻 Detected OS: Windows

==================================================
🎤 JARVIS VOICE COMMANDS
==================================================

📢 Say: 'Jarvis' + [Clap Pattern]

   2 claps  → VS Code
   3 claps  → Valorant
   4 claps  → Chrome
   5 claps  → Discord
   6 claps  → Spotify

🚀 Jarvis Launcher is running!
💬 Say 'Jarvis' to activate

🎤 Listening for 'Jarvis'...
..........

✅ Wake word detected: 'jarvis'
🎧 Listening for claps...
🔔 *BEEP*

👏 Clap detection active...
👏 Clap 1 detected! (RMS: 0.456)
👏 Clap 2 detected! (RMS: 0.512)
👏 Clap 3 detected! (RMS: 0.489)

📊 Total claps detected: 3

🚀 Launching Valorant...
✅ Valorant launched successfully!

🎤 Ready for next command...
```

## 🆘 Need Help?

1. **Read full docs:** `README.md`
2. **Check troubleshooting:** Run calibration tool
3. **Test microphone:** `python calibrate.py` → Option 1
4. **View config:** `python config_editor.py` → Option 1

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Test with default apps
3. ✅ Add your own apps
4. ✅ Calibrate for best performance
5. ✅ Enjoy hands-free computing!

---

**Made with ❤️ for productivity enthusiasts**

*Questions? Check README.md for detailed information!*
