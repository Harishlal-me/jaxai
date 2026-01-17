#!/usr/bin/env python3
"""
Jarvis Launcher Setup Script
Automated installation and configuration
"""

import subprocess
import sys
import platform
import os

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_python_version():
    """Check if Python version is compatible"""
    print_header("🐍 Checking Python Version")
    
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required!")
        print("Please upgrade Python: https://www.python.org/downloads/")
        return False
    
    print("✅ Python version is compatible!")
    return True

def install_dependencies():
    """Install required Python packages"""
    print_header("📦 Installing Dependencies")
    
    packages = [
        "SpeechRecognition",
        "sounddevice",
        "numpy",
    ]
    
    # Check if PyAudio is available
    try:
        import pyaudio
        print("✅ PyAudio already installed")
    except ImportError:
        print("⚠️  PyAudio not found. Attempting to install...")
        packages.append("pyaudio")
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            
            if package == "pyaudio":
                print("\n⚠️  PyAudio installation failed!")
                print("Please install manually:")
                
                system = platform.system()
                if system == "Windows":
                    print("  pip install pipwin")
                    print("  pipwin install pyaudio")
                elif system == "Linux":
                    print("  sudo apt-get install portaudio19-dev python3-pyaudio")
                    print("  pip3 install pyaudio")
                elif system == "Darwin":
                    print("  brew install portaudio")
                    print("  pip3 install pyaudio")
    
    print("\n✅ Dependency installation complete!")

def check_microphone():
    """Check if microphone is available"""
    print_header("🎤 Checking Microphone")
    
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        
        # List available microphones
        print("Available microphones:")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"  [{index}] {name}")
        
        # Test default microphone
        with sr.Microphone() as source:
            print("\n✅ Default microphone detected!")
            print("Testing microphone... (speak now)")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            
        return True
        
    except Exception as e:
        print(f"❌ Microphone error: {e}")
        print("\nPlease check:")
        print("  - Microphone is connected")
        print("  - Microphone permissions are granted")
        print("  - No other app is using the microphone")
        return False

def create_desktop_shortcut():
    """Create desktop shortcut (optional)"""
    print_header("🖥️  Desktop Shortcut")
    
    create = input("Create desktop shortcut? (y/n): ").strip().lower()
    
    if create != 'y':
        print("Skipped.")
        return
    
    system = platform.system()
    current_dir = os.getcwd()
    
    if system == "Windows":
        # Windows shortcut
        shortcut_path = os.path.join(os.path.expanduser("~"), "Desktop", "Jarvis Launcher.bat")
        with open(shortcut_path, 'w') as f:
            f.write(f"@echo off\n")
            f.write(f"cd {current_dir}\n")
            f.write(f"python jarvis_launcher.py\n")
            f.write(f"pause\n")
        print(f"✅ Shortcut created: {shortcut_path}")
        
    elif system == "Darwin":
        # macOS shortcut
        print("On macOS, add to Login Items manually:")
        print(f"  System Preferences → Users & Groups → Login Items")
        print(f"  Add: {os.path.join(current_dir, 'jarvis_launcher.py')}")
        
    elif system == "Linux":
        # Linux .desktop file
        desktop_path = os.path.join(os.path.expanduser("~"), ".local", "share", "applications", "jarvis-launcher.desktop")
        os.makedirs(os.path.dirname(desktop_path), exist_ok=True)
        
        with open(desktop_path, 'w') as f:
            f.write("[Desktop Entry]\n")
            f.write("Type=Application\n")
            f.write("Name=Jarvis Launcher\n")
            f.write("Comment=Voice-activated app launcher\n")
            f.write(f"Exec=python3 {os.path.join(current_dir, 'jarvis_launcher.py')}\n")
            f.write(f"Path={current_dir}\n")
            f.write("Terminal=true\n")
            f.write("Categories=Utility;\n")
        
        os.chmod(desktop_path, 0o755)
        print(f"✅ Desktop entry created: {desktop_path}")

def setup_config():
    """Initial configuration"""
    print_header("⚙️  Configuration")
    
    print("Default app mappings:")
    print("  2 claps → VS Code")
    print("  3 claps → Valorant")
    print("  4 claps → Chrome")
    print("  5 claps → Discord")
    print("  6 claps → Spotify")
    
    customize = input("\nCustomize app mappings now? (y/n): ").strip().lower()
    
    if customize == 'y':
        print("\n💡 Run 'python config_editor.py' to customize")
        subprocess.call([sys.executable, "config_editor.py"])
    else:
        print("You can customize later with: python config_editor.py")

def run_calibration():
    """Run calibration tool"""
    print_header("🎚️  Calibration")
    
    calibrate = input("Run calibration tool now? (recommended) (y/n): ").strip().lower()
    
    if calibrate == 'y':
        subprocess.call([sys.executable, "calibrate.py"])
    else:
        print("You can calibrate later with: python calibrate.py")

def main():
    """Main setup process"""
    print("\n" + "="*60)
    print("🎯 JARVIS VOICE-ACTIVATED APP LAUNCHER")
    print("    Setup Wizard")
    print("="*60)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    install_dependencies()
    
    # Check microphone
    check_microphone()
    
    # Setup configuration
    setup_config()
    
    # Run calibration
    run_calibration()
    
    # Create shortcut
    create_desktop_shortcut()
    
    # Final message
    print_header("✅ Setup Complete!")
    print("To start Jarvis Launcher:")
    print("  python jarvis_launcher.py")
    print("\nOther commands:")
    print("  python config_editor.py  - Edit app mappings")
    print("  python calibrate.py      - Calibrate clap detection")
    print("\n🎯 Say 'Jarvis' + clap pattern to launch apps!")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled.")
    except Exception as e:
        print(f"\n❌ Setup error: {e}")
        print("Please check the README.md for manual installation steps.")
