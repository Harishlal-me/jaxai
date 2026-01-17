#!/usr/bin/env python3
"""
Jarvis Voice-Activated App Launcher
Say "Jarvis" + Clap Pattern to launch apps
- 2 claps = VS Code
- 3 claps = Valorant
- 4 claps = Chrome
etc.
"""

import speech_recognition as sr
import sounddevice as sd
import numpy as np
import subprocess
import platform
import time
import threading
from collections import deque
from datetime import datetime
import json
import os

class JarvisLauncher:
    def __init__(self, config_file="app_config.json"):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Wake word settings
        self.wake_word = "jarvis"
        self.is_listening_for_claps = False
        self.activation_timeout = 5  # seconds to wait for claps after wake word
        
        # Clap detection settings
        self.sample_rate = 44100
        self.clap_threshold = 0.09  # Amplitude threshold for clap detection (VERY SENSITIVE)
        self.clap_window = 0.1  # Time window in seconds
        self.max_wait_time = 5  # Max seconds to wait for claps (INCREASED)
        self.min_clap_interval = 0.20  # Minimum time between claps (seconds) (INCREASED for clearer detection)
        
        # Audio buffer for clap detection
        self.audio_buffer = deque(maxlen=int(self.sample_rate * 0.5))
        self.detected_claps = []
        
        # Config file for app mappings
        self.config_file = config_file
        self.app_mappings = self.load_config()
        
        # System detection
        self.system = platform.system()
        
        print("🎯 Jarvis App Launcher Initialized")
        print(f"💻 Detected OS: {self.system}")
        self.print_commands()
    
    def load_config(self):
        """Load or create app configuration"""
        default_config = {
            "2": {
                "name": "VS Code",
                "windows": "code",
                "linux": "code",
                "darwin": "code"
            },
            "3": {
                "name": "Valorant",
                "windows": "launch_valorant.bat",
                "linux": "valorant",  # Via Wine/Proton
                "darwin": "valorant"
            },
            "4": {
                "name": "Chrome",
                "windows": "chrome",
                "linux": "google-chrome",
                "darwin": "open -a 'Google Chrome'"
            },
            "5": {
                "name": "Discord",
                "windows": "discord",
                "linux": "discord",
                "darwin": "open -a 'Discord'"
            },
            "6": {
                "name": "Spotify",
                "windows": "spotify",
                "linux": "spotify",
                "darwin": "open -a 'Spotify'"
            }
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                print("⚠️  Error loading config, using defaults")
                return default_config
        else:
            # Save default config
            with open(self.config_file, 'w') as f:
                json.dump(default_config, f, indent=4)
            print(f"✅ Created default config: {self.config_file}")
            return default_config
    
    def print_commands(self):
        """Print available commands"""
        print("\n" + "="*50)
        print("🎤 JARVIS VOICE COMMANDS")
        print("="*50)
        print("\n📢 Say: 'Jarvis' + [Clap Pattern]\n")
        
        for claps, app_info in sorted(self.app_mappings.items()):
            print(f"   {claps} claps  → {app_info['name']}")
        
        print("\n" + "="*50)
        print("🎯 How to use:")
        print("   1. Say 'Jarvis' clearly")
        print("   2. Wait for confirmation beep")
        print("   3. Clap the pattern (2-6 claps)")
        print("   4. App launches automatically!")
        print("="*50 + "\n")
    
    def listen_for_wake_word(self):
        """Listen continuously for the wake word 'Jarvis'"""
        print("🎤 Listening for 'Jarvis'...")
        
        with self.microphone as source:
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            while True:
                try:
                    print(".", end="", flush=True)
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=3)
                    
                    try:
                        # Recognize speech
                        text = self.recognizer.recognize_google(audio).lower()
                        
                        if self.wake_word in text:
                            print(f"\n\n✅ Wake word detected: '{text}'")
                            print("🎧 Listening for claps...")
                            self.play_confirmation_beep()
                            return True
                            
                    except sr.UnknownValueError:
                        pass
                    except sr.RequestError as e:
                        print(f"\n⚠️  Speech recognition error: {e}")
                        time.sleep(1)
                        
                except sr.WaitTimeoutError:
                    pass
                except KeyboardInterrupt:
                    print("\n\n👋 Shutting down...")
                    return False
    
    def play_confirmation_beep(self):
        """Play a confirmation sound"""
        try:
            duration = 0.1
            freq = 800
            t = np.linspace(0, duration, int(self.sample_rate * duration))
            beep = np.sin(2 * np.pi * freq * t) * 0.3
            sd.play(beep, self.sample_rate)
            sd.wait()
        except:
            print("🔔 *BEEP*")
    
    def detect_claps(self):
        """Detect clap patterns using real-time audio analysis"""
        print("👏 Clap detection active for 5 seconds...")
        print(f"💡 Threshold set to: {self.clap_threshold:.3f}")
        print("💡 TIP: Clap loudly and clearly")
        print("💡 You have 2.5 SECONDS after each clap to do the next one")
        print("💡 Watch the countdown timer! ⏱️\n")
        
        claps = []
        last_clap_time = 0
        start_time = time.time()
        check_count = 0
        
        def audio_callback(indata, frames, time_info, status):
            """Process audio in real-time"""
            nonlocal check_count, last_clap_time
            check_count += 1
            
            if status:
                print(f"Status: {status}")
            
            # Calculate RMS (Root Mean Square) for volume detection
            rms = np.sqrt(np.mean(indata**2))
            
            current_time = time.time()
            
            # Show audio level bar every 5 checks for better visibility
            if check_count % 5 == 0:
                bar_length = int(rms * 200)  # Scale up for visibility
                bar = "█" * min(bar_length, 40)
                
                # Show threshold marker
                threshold_pos = int(self.clap_threshold * 200)
                threshold_marker = " " * min(threshold_pos, 40) + "***"
                
                # Color indicator
                if rms > self.clap_threshold:
                    status_icon = "🟢 CLAP!"
                else:
                    status_icon = "⚪"
                
                # Show countdown if we have claps
                countdown_text = ""
                if len(claps) > 0:
                    time_since_last = current_time - last_clap_time
                    time_remaining = 2.5 - time_since_last
                    if time_remaining > 0:
                        countdown_text = f" | ⏱️  {time_remaining:.1f}s to clap again"
                
                print(f"\r{status_icon} |{bar:<40}| {rms:.3f}{countdown_text}  ", end="", flush=True)
            
            # Detect clap (loud sudden sound)
            if rms > self.clap_threshold:
                # Avoid duplicate detections (debounce)
                if current_time - last_clap_time > self.min_clap_interval:
                    claps.append(current_time)
                    last_clap_time = current_time
                    print(f"\n\n👏 CLAP {len(claps)} DETECTED! (Level: {rms:.3f})")
                    print(f"   ⏱️  You have 2.5 seconds to clap again (if you want more claps)\n")
        
        # Start audio stream
        try:
            with sd.InputStream(callback=audio_callback, channels=1, 
                               samplerate=self.sample_rate):
                # Wait for claps
                while time.time() - start_time < self.max_wait_time:
                    time.sleep(0.1)
                    
                    # If we got claps and no new clap for 2.5 seconds, finish
                    # INCREASED from 1.5 to 2.5 to give more time for additional claps
                    if len(claps) > 0 and time.time() - last_clap_time > 2.5:
                        print("\n⏱️  No more claps detected, processing...")
                        break
        
        except Exception as e:
            print(f"\n❌ Audio error: {e}")
            return 0
        
        num_claps = len(claps)
        print(f"\n📊 Total claps detected: {num_claps}")
        return num_claps
    
    def launch_app(self, num_claps):
        """Launch application based on clap count"""
        clap_str = str(num_claps)
        
        if clap_str not in self.app_mappings:
            print(f"❌ No app mapped to {num_claps} claps")
            print("💡 Available mappings:")
            for claps, app in self.app_mappings.items():
                print(f"   {claps} claps → {app['name']}")
            return False
        
        app_info = self.app_mappings[clap_str]
        app_name = app_info['name']
        
        # Get command based on OS
        if self.system == "Windows":
            command = app_info.get("windows", "")
        elif self.system == "Linux":
            command = app_info.get("linux", "")
        elif self.system == "Darwin":  # macOS
            command = app_info.get("darwin", "")
        else:
            print(f"❌ Unsupported OS: {self.system}")
            return False
        
        if not command:
            print(f"❌ No command configured for {app_name} on {self.system}")
            return False
        
        print(f"\n🚀 Launching {app_name}...")
        
        try:
            if self.system == "Windows":
                # Windows command - use different methods based on file type
                if command.endswith('.bat'):
                    # Batch file - check if relative path, make absolute
                    if not os.path.isabs(command):
                        command = os.path.abspath(command)
                    print(f"   Running batch file: {command}")
                    if os.path.exists(command):
                        subprocess.Popen(command, shell=True)
                    else:
                        print(f"   ⚠️  Batch file not found: {command}")
                        print(f"   💡 Make sure launch_valorant.bat is in the same folder as jarvis_launcher.py")
                        return False
                elif command.endswith('.exe') and os.path.exists(command):
                    # Direct .exe file - use start command to avoid permission issues
                    subprocess.Popen(['cmd', '/c', 'start', '', command], 
                                   shell=False,
                                   creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.DETACHED_PROCESS)
                elif os.path.exists(command):
                    # File exists - try to run directly
                    subprocess.Popen(command, shell=True)
                else:
                    # Command name only - use shell
                    subprocess.Popen(command, shell=True)
            elif self.system == "Darwin":  # macOS
                subprocess.Popen(command, shell=True)
            else:  # Linux
                subprocess.Popen(command, shell=True)
            
            print(f"✅ {app_name} launched successfully!")
            print(f"💡 Check your taskbar if {app_name} doesn't appear immediately")
            return True
            
        except PermissionError as e:
            print(f"❌ Permission denied to launch {app_name}")
            print(f"\n💡 SOLUTION - Run as Administrator:")
            print(f"   1. Right-click Command Prompt")
            print(f"   2. Select 'Run as Administrator'")
            print(f"   3. Navigate to this folder")
            print(f"   4. Run: python jarvis_launcher.py")
            return False
        except Exception as e:
            print(f"❌ Failed to launch {app_name}: {e}")
            print(f"\n💡 SOLUTIONS:")
            print(f"   1. Try running as Administrator (see above)")
            print(f"   2. Verify the file path exists:")
            print(f"      {command}")
            print(f"   3. Try launching manually to test the path")
            return False
    
    def run(self):
        """Main loop - exits after successful launch"""
        print("\n🚀 Jarvis Launcher is running!")
        print("💬 Say 'Jarvis' to activate")
        print("💡 Will auto-close after launching app\n")
        
        try:
            # Listen for wake word (only once)
            if self.listen_for_wake_word():
                # Detect claps
                num_claps = self.detect_claps()
                
                if num_claps > 0:
                    # Launch corresponding app
                    success = self.launch_app(num_claps)
                    
                    if success:
                        print("\n✅ App launched successfully!")
                        print("👋 Jarvis is shutting down...")
                        time.sleep(1)
                        print("✅ Done! Exiting...\n")
                        import sys
                        sys.exit(0)  # Force exit
                    else:
                        print("\n❌ Failed to launch app.")
                        print("💡 Run: python jarvis_launcher.py to try again\n")
                        import sys
                        sys.exit(1)
                else:
                    print("⚠️  No claps detected.")
                    print("💡 Run: python jarvis_launcher.py to try again\n")
                    import sys
                    sys.exit(1)
                    
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            import sys
            sys.exit(0)


if __name__ == "__main__":
    launcher = JarvisLauncher()
    launcher.run()