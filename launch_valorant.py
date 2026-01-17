#!/usr/bin/env python3
"""
Valorant Launcher - Python Version
Alternative to batch file for launching Valorant
"""

import subprocess
import os
import sys

def launch_valorant():
    """Launch Valorant using multiple methods"""
    
    # Common Valorant paths
    paths_to_try = [
        r"E:\VALORANT\Riot Games\VALORANT\live\VALORANT.exe",
        r"E:\VALORANT\Riot Games\Riot Client\RiotClientServices.exe",
        r"C:\Riot Games\VALORANT\live\VALORANT.exe",
        r"C:\Riot Games\Riot Client\RiotClientServices.exe",
        r"D:\Riot Games\VALORANT\live\VALORANT.exe",
        r"D:\Riot Games\Riot Client\RiotClientServices.exe",
    ]
    
    print("🎮 Launching Valorant...")
    
    # Try each path
    for path in paths_to_try:
        if os.path.exists(path):
            print(f"✅ Found: {path}")
            
            try:
                if "RiotClientServices" in path:
                    # Launch through Riot Client
                    subprocess.Popen([path, '--launch-product=valorant', '--launch-patchline=live'])
                else:
                    # Direct launch
                    subprocess.Popen(path)
                
                print("✅ Valorant launched successfully!")
                return True
                
            except Exception as e:
                print(f"❌ Failed to launch: {e}")
                continue
    
    # If we get here, nothing worked
    print("\n❌ Could not find Valorant!")
    print("\nPlease update the path in this script or use config_editor.py")
    print("Your Valorant might be in a different location.")
    return False

if __name__ == "__main__":
    launch_valorant()
