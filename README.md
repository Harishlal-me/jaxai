# 🎯 Jarvis Voice-Activated App Launcher

Launch any application on your computer using voice commands and clap patterns!

Say **"Jarvis"** + **Clap Pattern** = **App Launches Automatically** 🚀

## ✨ Features

- 🎤 **Voice Activation**: Say "Jarvis" to activate
- 👏 **Clap Detection**: Different clap patterns launch different apps
- 💻 **Cross-Platform**: Works on Windows, Linux, and macOS
- ⚙️ **Fully Customizable**: Easy configuration for any application
- 🎯 **No Internet Required**: All processing happens locally
- 🔊 **Audio Feedback**: Confirmation beeps when activated

## 🎮 Default Mappings

| Claps | Application |
|-------|-------------|
| 2     | VS Code     |
| 3     | Valorant    |
| 4     | Chrome      |
| 5     | Discord     |
| 6     | Spotify     |

## 📋 Requirements

- Python 3.7 or higher
- Microphone (built-in or external)
- Working audio input device

## 🚀 Installation

### Step 1: Install Python Dependencies

**Windows:**
```bash
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
pip3 install -r requirements.txt

# If you get audio errors, install portaudio first:
# Ubuntu/Debian:
sudo apt-get install portaudio19-dev python3-pyaudio

# macOS:
brew install portaudio
```

### Step 2: Grant Microphone Permissions

**Windows:**
- Settings → Privacy → Microphone
- Allow apps to access your microphone

**macOS:**
- System Preferences → Security & Privacy → Microphone
- Grant access to Terminal/Python

**Linux:**
- Usually no special permissions needed
- If issues, check PulseAudio/ALSA settings

## 🎯 Usage

### Quick Start

1. **Run the launcher:**
   ```bash
   python jarvis_launcher.py
   ```

2. **Say "Jarvis"** clearly into your microphone

3. **Wait for the confirmation beep** 🔔

4. **Clap the pattern** (e.g., 2 claps for VS Code)

5. **App launches!** ✅

### Example Commands

```
You: "Jarvis"
System: *BEEP* 🔔
You: *clap* *clap* 👏👏
System: 🚀 Launching VS Code...
```

```
You: "Jarvis"
System: *BEEP* 🔔
You: *clap* *clap* *clap* 👏👏👏
System: 🚀 Launching Valorant...
```

## ⚙️ Configuration

### Using the Config Editor

Run the configuration editor to customize your app mappings:

```bash
python config_editor.py
```

**Menu Options:**
1. **View current mappings** - See all configured apps
2. **Add new app** - Add a custom application
3. **Edit existing app** - Modify an existing mapping
4. **Remove app** - Delete a mapping
5. **Exit**

### Adding a Custom App

1. Run `python config_editor.py`
2. Select option `2` (Add new app)
3. Enter number of claps (1-10)
4. Enter app name
5. Enter launch commands for each OS

**Example: Adding Spotify**
```
Number of claps: 5
App name: Spotify

Windows command: spotify
Linux command: spotify
macOS command: open -a 'Spotify'
```

### Manual Configuration

Edit `app_config.json` directly:

```json
{
    "2": {
        "name": "VS Code",
        "windows": "code",
        "linux": "code",
        "darwin": "code"
    },
    "3": {
        "name": "Valorant",
        "windows": "C:\\Riot Games\\VALORANT\\live\\VALORANT.exe",
        "linux": "valorant",
        "darwin": "valorant"
    }
}
```

## 🎚️ Calibration

If claps aren't being detected properly, run the calibration tool:

```bash
python calibrate.py
```

**Calibration Options:**

1. **Test Microphone** - Check if your mic is working
2. **Monitor Audio Levels** - See real-time audio input
3. **Test Clap Detection** - Test the clap detection system
4. **Adjust Threshold** - Fine-tune sensitivity

**Tips for Better Detection:**
- Clap with hands 6-12 inches from microphone
- Use sharp, loud claps
- Wait 0.2 seconds between each clap
- Adjust threshold if too sensitive/insensitive

## 🔧 Troubleshooting

### "No module named 'speech_recognition'"
```bash
pip install SpeechRecognition
```

### "Could not find PyAudio"

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip3 install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip3 install pyaudio
```

### Wake Word Not Detected

1. **Check internet connection** (Google Speech Recognition needs internet)
2. **Speak clearly** and at normal volume
3. **Say "Jarvis"** by itself (don't combine with other words)
4. **Check microphone permissions**

### Claps Not Detected

1. **Run calibration tool**: `python calibrate.py`
2. **Monitor audio levels** to see if claps register
3. **Adjust threshold** - lower for more sensitivity
4. **Try louder claps** or move closer to microphone
5. **Check for background noise** interference

### App Won't Launch

1. **Check app path** in `app_config.json`
2. **Verify app is installed** on your system
3. **Try full path** instead of command name
4. **Check OS-specific command** is correct

**Windows Example:**
```json
"windows": "C:\\Program Files\\Application\\app.exe"
```

**Linux Example:**
```json
"linux": "/usr/bin/application"
```

**macOS Example:**
```json
"darwin": "open -a 'Application Name'"
```

## 🎨 Customization

### Change Wake Word Sensitivity

Edit `jarvis_launcher.py`:
```python
self.recognizer.energy_threshold = 4000  # Lower = more sensitive
self.recognizer.dynamic_energy_threshold = True
```

### Adjust Clap Timing

Edit `jarvis_launcher.py`:
```python
self.min_clap_interval = 0.15  # Seconds between claps
self.max_wait_time = 3  # Max wait time for claps
self.clap_threshold = 0.3  # Detection sensitivity
```

### Change Confirmation Sound

Edit the `play_confirmation_beep()` function:
```python
freq = 800  # Frequency in Hz
duration = 0.1  # Duration in seconds
```

## 📁 Project Structure

```
jarvis-launcher/
├── jarvis_launcher.py      # Main application
├── config_editor.py        # Configuration tool
├── calibrate.py           # Calibration tool
├── requirements.txt       # Python dependencies
├── app_config.json        # App mappings (auto-generated)
├── calibration_settings.json  # Calibration data
└── README.md             # This file
```

## 🤖 How It Works

1. **Wake Word Detection**
   - Continuously listens to microphone
   - Uses Google Speech Recognition
   - Detects "Jarvis" in speech

2. **Clap Detection**
   - Monitors audio amplitude (RMS)
   - Detects sudden loud sounds
   - Counts claps with debouncing

3. **App Launching**
   - Maps clap count to application
   - Executes OS-specific command
   - Launches app in background

## 🎯 Advanced Usage

### Run on Startup (Windows)

1. Create a batch file `start_jarvis.bat`:
```batch
@echo off
cd C:\path\to\jarvis-launcher
python jarvis_launcher.py
```

2. Press `Win+R`, type `shell:startup`
3. Copy the batch file there

### Run on Startup (Linux)

Add to `~/.bashrc` or create a systemd service:
```bash
# In ~/.bashrc
python3 /path/to/jarvis_launcher.py &
```

### Run on Startup (macOS)

Create a Launch Agent or add to Login Items:
```bash
# Add to Login Items in System Preferences
```

## 🔐 Privacy

- ✅ All audio processing happens locally
- ✅ Speech recognition uses Google's API (requires internet)
- ✅ No audio is stored or recorded
- ✅ No personal data collected
- ✅ Open source - inspect the code yourself!

## 💡 Tips & Tricks

1. **Clear Speech**: Say "Jarvis" clearly and at normal speaking volume
2. **Sharp Claps**: Make sharp, distinct claps for best detection
3. **Timing**: Wait for the beep before clapping
4. **Environment**: Use in quiet environment for best results
5. **Microphone**: Closer to mic = better detection

## 🐛 Known Issues

- Requires internet for speech recognition (Google API)
- May have false positives with loud background noise
- Some antivirus software may flag app launching
- Performance varies with microphone quality

## 🚀 Future Enhancements

- [ ] Offline wake word detection
- [ ] More complex voice commands
- [ ] GUI interface
- [ ] Custom wake words
- [ ] Gesture recognition
- [ ] Hotkey fallback
- [ ] Cloud sync for settings
- [ ] Mobile app integration

## 📝 License

This project is open source and available for personal use.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 🙏 Credits

Inspired by the wake-up project and Iron Man's JARVIS assistant.

## 📞 Support

If you encounter issues:
1. Run the calibration tool
2. Check troubleshooting section
3. Verify microphone permissions
4. Test with simple apps first (like Notepad)

## ⚡ Quick Reference

| Command | Action |
|---------|--------|
| `python jarvis_launcher.py` | Start the launcher |
| `python config_editor.py` | Edit app mappings |
| `python calibrate.py` | Calibrate clap detection |
| Say "Jarvis" | Activate listening |
| Clap N times | Launch app mapped to N |

---

**Made with ❤️ for hands-free computing**

🎯 Happy launching! 🚀
