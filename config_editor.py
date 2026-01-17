#!/usr/bin/env python3
"""
Jarvis App Configuration Editor
Easily add/edit/remove app mappings
"""

import json
import os
import platform

def load_config():
    """Load existing configuration"""
    if os.path.exists("app_config.json"):
        with open("app_config.json", 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    """Save configuration to file"""
    with open("app_config.json", 'w') as f:
        json.dump(config, f, indent=4)
    print("✅ Configuration saved!")

def display_config(config):
    """Display current configuration"""
    print("\n" + "="*60)
    print("📋 CURRENT APP MAPPINGS")
    print("="*60)
    
    if not config:
        print("No mappings configured yet!")
        return
    
    for claps, app_info in sorted(config.items(), key=lambda x: int(x[0])):
        print(f"\n{claps} Claps → {app_info['name']}")
        print(f"  Windows: {app_info.get('windows', 'Not configured')}")
        print(f"  Linux:   {app_info.get('linux', 'Not configured')}")
        print(f"  macOS:   {app_info.get('darwin', 'Not configured')}")
    
    print("\n" + "="*60 + "\n")

def add_app(config):
    """Add a new app mapping"""
    print("\n➕ ADD NEW APP MAPPING")
    print("-" * 40)
    
    # Get number of claps
    while True:
        try:
            claps = input("Number of claps (1-10): ").strip()
            if 1 <= int(claps) <= 10:
                break
            print("❌ Please enter a number between 1 and 10")
        except ValueError:
            print("❌ Please enter a valid number")
    
    if claps in config:
        overwrite = input(f"⚠️  {claps} claps already mapped to '{config[claps]['name']}'. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("❌ Cancelled")
            return
    
    # Get app name
    app_name = input("App name (e.g., 'VS Code', 'Valorant'): ").strip()
    
    # Get commands for each OS
    print("\n🖥️  Enter launch commands for each OS:")
    print("    (Press Enter to skip an OS)\n")
    
    windows_cmd = input("  Windows command: ").strip()
    linux_cmd = input("  Linux command: ").strip()
    macos_cmd = input("  macOS command: ").strip()
    
    # Create mapping
    config[claps] = {
        "name": app_name,
        "windows": windows_cmd,
        "linux": linux_cmd,
        "darwin": macos_cmd
    }
    
    save_config(config)
    print(f"\n✅ Added mapping: {claps} claps → {app_name}")

def remove_app(config):
    """Remove an app mapping"""
    print("\n➖ REMOVE APP MAPPING")
    print("-" * 40)
    
    display_config(config)
    
    claps = input("Enter number of claps to remove (or 'cancel'): ").strip()
    
    if claps.lower() == 'cancel':
        print("❌ Cancelled")
        return
    
    if claps in config:
        app_name = config[claps]['name']
        confirm = input(f"Remove '{app_name}' ({claps} claps)? (y/n): ")
        if confirm.lower() == 'y':
            del config[claps]
            save_config(config)
            print(f"✅ Removed {app_name}")
    else:
        print(f"❌ No mapping found for {claps} claps")

def edit_app(config):
    """Edit an existing app mapping"""
    print("\n✏️  EDIT APP MAPPING")
    print("-" * 40)
    
    display_config(config)
    
    claps = input("Enter number of claps to edit (or 'cancel'): ").strip()
    
    if claps.lower() == 'cancel':
        print("❌ Cancelled")
        return
    
    if claps not in config:
        print(f"❌ No mapping found for {claps} claps")
        return
    
    app_info = config[claps]
    print(f"\n📝 Editing: {app_info['name']}")
    print("    (Press Enter to keep current value)\n")
    
    # Edit app name
    new_name = input(f"  App name [{app_info['name']}]: ").strip()
    if new_name:
        app_info['name'] = new_name
    
    # Edit commands
    print(f"\n  Current Windows command: {app_info.get('windows', 'Not set')}")
    new_win = input("  New Windows command: ").strip()
    if new_win:
        app_info['windows'] = new_win
    
    print(f"\n  Current Linux command: {app_info.get('linux', 'Not set')}")
    new_linux = input("  New Linux command: ").strip()
    if new_linux:
        app_info['linux'] = new_linux
    
    print(f"\n  Current macOS command: {app_info.get('darwin', 'Not set')}")
    new_macos = input("  New macOS command: ").strip()
    if new_macos:
        app_info['darwin'] = new_macos
    
    save_config(config)
    print(f"\n✅ Updated mapping for {claps} claps")

def main():
    """Main menu"""
    config = load_config()
    
    while True:
        print("\n" + "="*60)
        print("🎯 JARVIS APP CONFIGURATION EDITOR")
        print("="*60)
        print("\n1. 👀 View current mappings")
        print("2. ➕ Add new app")
        print("3. ✏️  Edit existing app")
        print("4. ➖ Remove app")
        print("5. 🚪 Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            display_config(config)
        elif choice == '2':
            add_app(config)
        elif choice == '3':
            edit_app(config)
        elif choice == '4':
            remove_app(config)
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
