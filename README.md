# 🎤 NOVA - Voice-Activated Desktop Assistant

**Nova** is an intelligent voice-activated app launcher with voice responses.

Say **"Hey Nova"** → She responds → Clap pattern → App launches!

---

## 🌟 Features

✅ **Voice Activation** - Say "Hey Nova" to activate  
✅ **Voice Responses** - Nova talks back to you  
✅ **Clap Patterns** - Different claps launch different apps  
✅ **Auto-Exit** - Closes after launching an app  
✅ **Fully Customizable** - Add any app you want  
✅ **Cross-Platform** - Windows, Linux, macOS  

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install SpeechRecognition sounddevice numpy pyttsx3
```

### 2. Run Nova
```bash
python nova_launcher.py
```

### 3. Use It!
**You:** "Hey Nova"  
**Nova:** "You called me. Now talk."  
**You:** 👏👏👏  
**Nova:** "Launching Valorant!"  

---

## 🗣️ Voice Commands

```
"Hey Nova" + 👏           = WhatsApp
"Hey Nova" + 👏👏         = VS Code
"Hey Nova" + 👏👏👏       = Valorant
"Hey Nova" + 👏👏👏👏     = Chrome
"Hey Nova" + 👏👏👏👏👏   = Brave
```

---

## 💬 Nova's Voice Responses

| Action | Nova Says |
|--------|-----------|
| Wake word detected | "You called me. Now talk." |
| 1 clap (WhatsApp) | "Opening WhatsApp." |
| 2 claps (VS Code) | "Launching VS Code. Happy coding!" |
| 3 claps (Valorant) | "Launching Valorant. Enjoy your game!" |
| 4 claps (Chrome) | "Opening Chrome for you." |
| 5 claps (Brave) | "Launching Brave Browser." |
| No claps | "I didn't hear any claps. Try again." |
| Unknown pattern | "I don't know that command." |

---

## ⚙️ Configuration

Edit `app_config.json` to customize:

```json
{
    "1": {
        "name": "WhatsApp",
        "windows": "start whatsapp:"
    }
}
```

Add your own apps using `config_editor.py`

---

## 🎚️ Adjust Sensitivity

### Voice Detection (if "Hey Nova" is hard to trigger)
Edit `nova_launcher.py`:
```python
self.recognizer.energy_threshold = 300  # Lower = more sensitive
```

### Clap Detection (if claps aren't detected)
```python
self.clap_threshold = 0.08  # Lower = more sensitive
```

Or run: `python test_clap_values.py`

---

## 🐛 Troubleshooting

**"Hey Nova" not detected:**
- Lower `energy_threshold` to 200
- Speak at normal volume
- Check microphone permissions

**Claps not detected:**
- Run `test_clap_values.py`
- Clap louder
- Adjust `clap_threshold`

**App won't launch:**
- Test command manually
- Check path in `app_config.json`
- Run as Administrator

---

## 📁 Files

```
├── nova_launcher.py          # Main application
├── app_config.json          # App mappings
├── config_editor.py         # Add/edit apps
├── test_clap_values.py      # Calibration
├── requirements.txt         # Dependencies
└── README.md               # This file
```

---

## 🎯 Usage Example

```bash
$ python nova_launcher.py

🎤 Listening for 'Hey Nova'...
```

**You:** "Hey Nova"

```
✅ Wake word detected!
🔊 Nova: "You called me. Now talk."
🔔 *BEEP*

👏 Clap detection active...
```

**You:** 👏👏👏

```
👏 CLAP 1 DETECTED!
👏 CLAP 2 DETECTED!
👏 CLAP 3 DETECTED!

📊 Total claps: 3
🚀 Launching Valorant...
🔊 Nova: "Launching Valorant. Enjoy your game!"
✅ Done! Exiting...
```

---

## 🔮 Future Features (Roadmap)

- [ ] Background mode (system tray)
- [ ] Works from any app/screen
- [ ] Overlay interface
- [ ] More voice responses
- [ ] Offline wake word
- [ ] Custom wake words
- [ ] Gesture recognition

---

## 💡 Tips

✅ Speak clearly at normal volume  
✅ Wait for Nova's response before clapping  
✅ Make sharp, loud claps  
✅ Stay near microphone (1-2 feet)  
✅ Use in quiet environment  

---

## 🙏 Credits

Built with Python, SpeechRecognition, pyttsx3, sounddevice

---

**Say "Hey Nova" and start voice controlling your computer!** 🎤✨

```bash
python nova_launcher.py
```
