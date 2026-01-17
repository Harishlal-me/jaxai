#!/usr/bin/env python3
"""
Jarvis Launcher Demo & Test Script
Verify your installation and see examples
"""

import sys
import platform

def print_banner():
    """Print cool ASCII banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║        🎯  JARVIS APP LAUNCHER DEMO  🎯               ║
    ║                                                       ║
    ║     Voice-Activated Application Control System       ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)

def show_demo():
    """Show interactive demo"""
    print("\n" + "="*60)
    print("🎬 DEMO: How Jarvis Launcher Works")
    print("="*60 + "\n")
    
    print("Step-by-step walkthrough:\n")
    
    steps = [
        ("1️⃣", "START", "Run: python jarvis_launcher.py"),
        ("2️⃣", "SPEAK", "Say 'Jarvis' into your microphone"),
        ("3️⃣", "BEEP", "System plays confirmation beep 🔔"),
        ("4️⃣", "CLAP", "Clap 2 times 👏👏"),
        ("5️⃣", "LAUNCH", "VS Code opens automatically! 🚀"),
    ]
    
    for emoji, title, description in steps:
        print(f"{emoji}  {title:10} → {description}")
    
    print("\n" + "-"*60)
    print("\n💡 Example Interaction:\n")
    
    print("  User:   'Jarvis'")
    print("  System: *BEEP* 🔔")
    print("  User:   *clap* *clap* 👏👏")
    print("  System: 🚀 Launching VS Code...")
    print("  System: ✅ VS Code launched successfully!")
    
    print("\n" + "="*60 + "\n")

def show_commands():
    """Show all available commands"""
    print("\n" + "="*60)
    print("📋 AVAILABLE COMMANDS")
    print("="*60 + "\n")
    
    commands = [
        ("Jarvis + 👏👏", "VS Code", "Code editor"),
        ("Jarvis + 👏👏👏", "Valorant", "FPS game"),
        ("Jarvis + 👏👏👏👏", "Chrome", "Web browser"),
        ("Jarvis + 👏👏👏👏👏", "Discord", "Chat app"),
        ("Jarvis + 👏👏👏👏👏👏", "Spotify", "Music player"),
    ]
    
    print("┌─────────────────────┬──────────────┬────────────────┐")
    print("│ Voice Command       │ Launches     │ Description    │")
    print("├─────────────────────┼──────────────┼────────────────┤")
    
    for cmd, app, desc in commands:
        print(f"│ {cmd:19} │ {app:12} │ {desc:14} │")
    
    print("└─────────────────────┴──────────────┴────────────────┘")
    print("\n" + "="*60 + "\n")

def show_customization():
    """Show customization examples"""
    print("\n" + "="*60)
    print("⚙️  CUSTOMIZATION EXAMPLES")
    print("="*60 + "\n")
    
    print("Add your own apps easily!\n")
    
    examples = [
        ("Photoshop", "7", "For creative work"),
        ("Steam", "8", "For gaming"),
        ("Excel", "9", "For spreadsheets"),
        ("Notepad", "10", "For quick notes"),
    ]
    
    print("Example configurations:\n")
    
    for app, claps, purpose in examples:
        print(f"  {app}")
        print(f"    Claps: {claps}")
        print(f"    Purpose: {purpose}")
        print(f"    Command: python config_editor.py\n")
    
    print("="*60 + "\n")

def show_tips():
    """Show pro tips"""
    print("\n" + "="*60)
    print("💡 PRO TIPS")
    print("="*60 + "\n")
    
    tips = [
        ("🎤 Clear Speech", "Say 'Jarvis' clearly at normal volume"),
        ("👏 Sharp Claps", "Make distinct, loud claps"),
        ("⏱️  Timing", "Wait for beep before clapping"),
        ("🔇 Quiet Space", "Use in low-noise environment"),
        ("🎚️  Calibrate", "Run calibration for best results"),
        ("📍 Position", "Stay close to microphone"),
        ("🔁 Practice", "Gets better with use"),
    ]
    
    for title, tip in tips:
        print(f"  {title:20} → {tip}")
    
    print("\n" + "="*60 + "\n")

def check_system():
    """Check system compatibility"""
    print("\n" + "="*60)
    print("🖥️  SYSTEM CHECK")
    print("="*60 + "\n")
    
    # Python version
    py_version = sys.version.split()[0]
    print(f"Python Version: {py_version}")
    
    major, minor = sys.version_info[:2]
    if major >= 3 and minor >= 7:
        print("  ✅ Compatible")
    else:
        print("  ❌ Need Python 3.7+")
    
    # Operating System
    os_name = platform.system()
    print(f"\nOperating System: {os_name}")
    print(f"  ✅ Supported")
    
    # Check dependencies
    print("\nDependencies:")
    deps = [
        "speech_recognition",
        "sounddevice",
        "numpy",
        "pyaudio"
    ]
    
    for dep in deps:
        try:
            __import__(dep)
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} (Run: pip install {dep})")
    
    print("\n" + "="*60 + "\n")

def show_file_structure():
    """Show project structure"""
    print("\n" + "="*60)
    print("📁 PROJECT FILES")
    print("="*60 + "\n")
    
    files = [
        ("jarvis_launcher.py", "🚀 Main application - START HERE"),
        ("config_editor.py", "⚙️  Configure app mappings"),
        ("calibrate.py", "🎚️  Calibration tool"),
        ("setup_wizard.py", "📥 Installation helper"),
        ("requirements.txt", "📦 Dependencies list"),
        ("README.md", "📖 Full documentation"),
        ("QUICKSTART.md", "⚡ Quick start guide"),
        ("PROJECT_INFO.md", "ℹ️  Project information"),
    ]
    
    for filename, description in files:
        print(f"  {filename:25} → {description}")
    
    print("\n" + "="*60 + "\n")

def main_menu():
    """Main menu"""
    while True:
        print("\n" + "="*60)
        print("🎯 JARVIS LAUNCHER - DEMO MENU")
        print("="*60 + "\n")
        
        print("1. 🎬 See Demo Walkthrough")
        print("2. 📋 View Available Commands")
        print("3. ⚙️  See Customization Examples")
        print("4. 💡 Read Pro Tips")
        print("5. 🖥️  Check System Compatibility")
        print("6. 📁 View Project Files")
        print("7. 🚀 Quick Start Instructions")
        print("8. 🚪 Exit")
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == '1':
            show_demo()
        elif choice == '2':
            show_commands()
        elif choice == '3':
            show_customization()
        elif choice == '4':
            show_tips()
        elif choice == '5':
            check_system()
        elif choice == '6':
            show_file_structure()
        elif choice == '7':
            print("\n" + "="*60)
            print("🚀 QUICK START")
            print("="*60 + "\n")
            print("1. Install dependencies:")
            print("   pip install SpeechRecognition sounddevice numpy pyaudio\n")
            print("2. Run launcher:")
            print("   python jarvis_launcher.py\n")
            print("3. Say 'Jarvis' + clap pattern\n")
            print("="*60 + "\n")
        elif choice == '8':
            print("\n👋 Goodbye! Happy launching! 🚀\n")
            break
        else:
            print("\n❌ Invalid option")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print_banner()
    main_menu()
