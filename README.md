🎤 Nova Desktop Assistant
Always-on voice assistant for Windows - Launch your favorite apps with just your voice!

🌟 Features

✅ Always Running - Starts automatically with Windows
✅ System Tray Integration - Runs quietly in the background
✅ Voice Activated - Say "Hey Nova" anytime
✅ Fast App Launching - Open apps instantly with voice commands
✅ Customizable - Add your own apps and commands
✅ Low Resource Usage - Minimal CPU and memory footprint


📋 Prerequisites

Windows 10/11
Python 3.9 or higher
Microphone
Internet connection (for voice recognition)


🚀 Installation
Step 1: Install Dependencies
bash# Navigate to the Nova folder
cd D:\jarvis

# Create virtual environment (if not exists)
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install required packages
pip install SpeechRecognition pyaudio pystray pillow
Step 2: Configure Your Apps
Edit app_config.json to add your applications:
json{
  "1": {
    "name": "WhatsApp",
    "windows": "start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
  },
  "2": {
    "name": "VS Code",
    "windows": "code"
  }
}
Step 3: Install to Windows Startup

Right-click install_nova.bat
Select "Run as Administrator"
Wait for "INSTALLATION COMPLETE!"
Restart your computer


🎯 Usage
Starting Nova
Option 1: Automatic (Recommended)

Nova starts automatically when Windows boots up
Look for the purple "N" icon in your system tray

Option 2: Manual

Double-click start_nova.bat
Nova will start in the background

Using Voice Commands

Say "Hey Nova" to activate
Wait for Nova's response: "Nova here. You called me. Now talk."
Say your command, for example:

"Open WhatsApp"
"Launch VS Code"
"Open Chrome"
"Start Valorant"



Available Commands
Say ThisOpens This"WhatsApp"WhatsApp Desktop"VS Code" / "Code"Visual Studio Code"Chrome" / "Google"Google Chrome"Brave"Brave Browser"Valorant"Valorant Game
System Tray Options
Right-click the Nova icon in the system tray:

Toggle Listening - Pause/resume voice detection
Quit Nova - Stop the assistant


📁 File Structure
D:\jarvis\
├── nova_desktop_assistant.py    # Main Python script
├── app_config.json              # App configuration
├── install_nova.bat             # Startup installer
├── start_nova.bat               # Manual launcher
├── start_nova_silent.vbs        # Silent startup script
├── README.md                    # This file
└── .venv\                       # Virtual environment

⚙️ Configuration
Adding New Apps

Open app_config.json
Add a new entry with a unique ID:

json{
  "6": {
    "name": "Spotify",
    "windows": "start spotify:"
  }
}

Open nova_desktop_assistant.py
Add voice command mapping (around line 24):

pythonself.voice_commands = {
    # ... existing commands ...
    "spotify": "6",
    "music": "6"
}

Add voice response (around line 33):

pythonself.voice_responses = {
    # ... existing responses ...
    "6": "Opening Spotify. Enjoy your music!"
}
Adjusting Voice Sensitivity
Edit nova_desktop_assistant.py (around line 121):
pythonself.recognizer.energy_threshold = 2500  # Lower = more sensitive

🔧 Troubleshooting
Nova doesn't start automatically

Check if shortcut exists:

Press Win + R, type shell:startup, press Enter
Look for "Nova Assistant.lnk"


If missing, run install_nova.bat as Administrator again

"Hey Nova" not detected

Check your microphone is working
Try speaking louder or closer to the mic
Adjust energy_threshold in the code (see Configuration)

Commands not recognized

Speak clearly and wait for Nova's prompt
Check internet connection (Google Speech API requires it)
Verify command is in voice_commands dictionary

Microphone error on startup
bashpip install pyaudio
If that fails, download the wheel file for your Python version from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
App doesn't launch

Verify the command in app_config.json works manually
Test in Command Prompt first
Check for typos in app paths


🛑 Uninstalling
Remove from Startup

Press Win + R
Type: shell:startup
Delete "Nova Assistant.lnk"

Complete Removal

Remove from startup (above)
Delete the entire D:\jarvis\ folder


🔒 Privacy & Security

Voice data: Sent to Google Speech Recognition API for processing
No data stored: Nova doesn't save your voice recordings
Local execution: All app launching happens on your computer
No telemetry: Nova doesn't send usage data anywhere


📝 System Requirements

OS: Windows 10/11
Python: 3.9+
RAM: 100-200 MB
Disk: ~50 MB
Internet: Required for voice recognition


🤝 Support
If you encounter issues:

Check the Troubleshooting section above
Verify all dependencies are installed
Run Nova manually with python nova_desktop_assistant.py to see error messages
Check that your microphone has proper permissions in Windows Settings


📜 Version History
v1.0 (Current)

Initial release
Wake word detection
System tray integration
Auto-startup support
Voice command app launching


🎓 Tips & Best Practices

Clear speech: Speak clearly and at normal pace
Wait for prompt: Always wait for "Now talk" before giving commands
Quiet environment: Works best with minimal background noise
Good microphone: Use a quality microphone for better recognition
One command at a time: Give one command, wait for completion


📞 Quick Reference
Starting Nova
bash# Manual start
start_nova.bat

# Or from Python
python nova_desktop_assistant.py
Installing to Startup
bash# Run as Administrator
install_nova.bat
Voice Flow

"Hey Nova" → Wake word activation
Wait for response → "Nova here. You called me. Now talk."
"Open WhatsApp" → Command execution
Wait for "Work done, sir" → Ready for next "Hey Nova"


Made with ❤️ for hands-free productivity
Nova - Your always-on voice assistant
