#!/usr/bin/env python3
"""
Advanced Clap Detection Tester
Find the perfect threshold for your setup
"""

import sounddevice as sd
import numpy as np
import time
import json

def test_clap_levels():
    """Test and find optimal clap threshold"""
    print("\n" + "="*60)
    print("🎯 CLAP DETECTION CALIBRATION")
    print("="*60 + "\n")
    
    print("This will help you find the perfect clap detection threshold.\n")
    
    sample_rate = 44100
    clap_levels = []
    background_levels = []
    
    # Step 1: Measure background noise
    print("📊 Step 1: Measuring background noise...")
    print("   Stay quiet for 3 seconds...\n")
    
    def background_callback(indata, frames, time_info, status):
        rms = np.sqrt(np.mean(indata**2))
        background_levels.append(rms)
        bar = "█" * int(rms * 200)
        print(f"\rLevel: |{bar:<40}| {rms:.4f}", end="", flush=True)
    
    try:
        with sd.InputStream(callback=background_callback, channels=1, 
                           samplerate=sample_rate):
            time.sleep(3)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return
    
    avg_background = np.mean(background_levels)
    max_background = max(background_levels)
    
    print(f"\n\n✅ Background noise measured:")
    print(f"   Average: {avg_background:.4f}")
    print(f"   Maximum: {max_background:.4f}")
    
    # Step 2: Measure clap levels
    print("\n📊 Step 2: Measuring your claps...")
    print("   Clap 5 times (like you normally would)\n")
    print("   Starting in 3...")
    time.sleep(1)
    print("   2...")
    time.sleep(1)
    print("   1...")
    time.sleep(1)
    print("   GO! 👏\n")
    
    detected_peaks = []
    last_peak_time = 0
    
    def clap_callback(indata, frames, time_info, status):
        rms = np.sqrt(np.mean(indata**2))
        current_time = time.time()
        
        nonlocal last_peak_time
        
        # Show audio level
        bar = "█" * int(rms * 100)
        print(f"\rLevel: |{bar:<50}| {rms:.4f}", end="", flush=True)
        
        # Detect peaks (potential claps)
        if rms > max_background * 3:  # 3x background noise
            if current_time - last_peak_time > 0.2:  # Debounce
                detected_peaks.append(rms)
                last_peak_time = current_time
                print(f"\n👏 Peak {len(detected_peaks)}: {rms:.4f}")
    
    try:
        with sd.InputStream(callback=clap_callback, channels=1,
                           samplerate=sample_rate):
            time.sleep(8)  # Give time for 5 claps
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return
    
    if len(detected_peaks) == 0:
        print("\n\n⚠️  No claps detected!")
        print("   Try clapping louder or closer to the microphone.")
        return
    
    # Analysis
    print("\n\n" + "="*60)
    print("📊 ANALYSIS")
    print("="*60 + "\n")
    
    avg_clap = np.mean(detected_peaks)
    min_clap = min(detected_peaks)
    max_clap = max(detected_peaks)
    
    print(f"Detected {len(detected_peaks)} claps:")
    print(f"   Minimum clap level: {min_clap:.4f}")
    print(f"   Average clap level: {avg_clap:.4f}")
    print(f"   Maximum clap level: {max_clap:.4f}")
    print(f"\nBackground noise: {avg_background:.4f}")
    print(f"Clap/Background ratio: {avg_clap/avg_background:.1f}x\n")
    
    # Calculate recommended threshold
    # Set threshold between background and minimum clap
    recommended = (max_background * 2 + min_clap) / 3
    conservative = min_clap * 0.7  # 70% of minimum clap
    aggressive = min_clap * 0.5    # 50% of minimum clap
    
    print("="*60)
    print("🎯 RECOMMENDED THRESHOLDS")
    print("="*60 + "\n")
    
    print(f"Conservative (fewer false positives): {conservative:.3f}")
    print(f"Balanced (recommended):              {recommended:.3f}")
    print(f"Aggressive (detect softer claps):    {aggressive:.3f}")
    
    print("\n💡 Which to use?")
    print("   - Conservative: If you have background noise")
    print("   - Balanced: For most situations (RECOMMENDED)")
    print("   - Aggressive: If you want to clap softly")
    
    # Save recommendation
    save = input("\n💾 Save recommended threshold? (y/n): ").strip().lower()
    
    if save == 'y':
        choice = input("Which threshold? (c=conservative, b=balanced, a=aggressive): ").lower()
        
        if choice == 'c':
            threshold = conservative
        elif choice == 'a':
            threshold = aggressive
        else:
            threshold = recommended
        
        settings = {
            "clap_threshold": float(threshold),
            "background_noise": float(avg_background),
            "average_clap_level": float(avg_clap),
            "calibration_date": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open("clap_settings.json", 'w') as f:
            json.dump(settings, f, indent=4)
        
        print(f"\n✅ Saved threshold: {threshold:.3f}")
        print("   File: clap_settings.json")
        
        # Update jarvis_launcher.py
        print("\n📝 To use this threshold:")
        print(f"   1. Open jarvis_launcher.py")
        print(f"   2. Find: self.clap_threshold = 0.15")
        print(f"   3. Change to: self.clap_threshold = {threshold:.3f}")
        print("\n   OR run the auto-updater below!")
        
        auto_update = input("\n🔧 Auto-update jarvis_launcher.py? (y/n): ").strip().lower()
        
        if auto_update == 'y':
            try:
                with open("jarvis_launcher.py", 'r') as f:
                    content = f.read()
                
                # Find and replace threshold
                import re
                pattern = r'self\.clap_threshold = [0-9.]+(?:\s*#.*)?'
                replacement = f'self.clap_threshold = {threshold:.3f}  # Auto-calibrated'
                
                new_content = re.sub(pattern, replacement, content)
                
                with open("jarvis_launcher.py", 'w') as f:
                    f.write(new_content)
                
                print(f"✅ Updated jarvis_launcher.py with threshold: {threshold:.3f}")
                
            except Exception as e:
                print(f"❌ Could not auto-update: {e}")
                print("   Please update manually.")
    
    print("\n" + "="*60)
    print("✅ Calibration complete!")
    print("="*60 + "\n")

def quick_test():
    """Quick clap detection test"""
    print("\n" + "="*60)
    print("⚡ QUICK CLAP TEST")
    print("="*60 + "\n")
    
    # Try to load saved settings
    try:
        with open("clap_settings.json", 'r') as f:
            settings = json.load(f)
            threshold = settings["clap_threshold"]
            print(f"Using saved threshold: {threshold:.3f}\n")
    except:
        threshold = 0.15
        print(f"Using default threshold: {threshold:.3f}\n")
    
    print("Clap 3 times to test...")
    print("Starting in 3 seconds...\n")
    time.sleep(3)
    
    sample_rate = 44100
    claps = []
    last_clap = 0
    start_time = time.time()
    
    def test_callback(indata, frames, time_info, status):
        rms = np.sqrt(np.mean(indata**2))
        current_time = time.time()
        
        nonlocal last_clap
        
        # Visual feedback
        bar = "█" * int(rms * 100)
        print(f"\rLevel: |{bar:<50}| {rms:.4f}", end="", flush=True)
        
        if rms > threshold:
            if current_time - last_clap > 0.25:
                claps.append(current_time)
                last_clap = current_time
                print(f"\n👏 Clap {len(claps)} detected!")
    
    try:
        with sd.InputStream(callback=test_callback, channels=1,
                           samplerate=sample_rate):
            while time.time() - start_time < 5:
                time.sleep(0.1)
                if len(claps) >= 3 and time.time() - last_clap > 1.5:
                    break
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return
    
    print(f"\n\n✅ Detected {len(claps)} claps")
    
    if len(claps) == 3:
        print("🎉 Perfect! Detection is working well!")
    elif len(claps) < 3:
        print("⚠️  Detected fewer claps. Try:")
        print("   - Clapping louder")
        print("   - Lowering the threshold")
        print("   - Running full calibration")
    else:
        print("⚠️  Detected more claps (false positives). Try:")
        print("   - Raising the threshold")
        print("   - Reducing background noise")

def main():
    """Main menu"""
    while True:
        print("\n" + "="*60)
        print("🎚️  CLAP DETECTION CALIBRATOR")
        print("="*60 + "\n")
        
        print("1. 🎯 Full Calibration (Recommended)")
        print("2. ⚡ Quick Test")
        print("3. 📊 View Saved Settings")
        print("4. 🚪 Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            test_clap_levels()
        elif choice == '2':
            quick_test()
        elif choice == '3':
            try:
                with open("clap_settings.json", 'r') as f:
                    settings = json.load(f)
                print("\n📊 Saved Settings:")
                for key, value in settings.items():
                    print(f"   {key}: {value}")
            except:
                print("\n⚠️  No saved settings found.")
                print("   Run full calibration first!")
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()