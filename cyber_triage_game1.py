import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, speed=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def intro():
    clear_screen()
    print_slow("====================================================", 0.005)
    print_slow("       🤖 CYBER TRIAGE: RUNTIME DEFENDER 🤖         ", 0.01)
    print_slow("====================================================", 0.005)
    print_slow("\nSYSTEM ALERT: Suspicious outbound spikes detected.", 0.02)
    print_slow("Your mission: Deploy a 6-hour triage cycle agent to capture the breach", 0.02)
    print_slow("before critical infrastructure data is exfiltrated.\n", 0.02)
    input("Press ENTER to boot up the defensive terminal...")

def play_game():
    intro()
    score = 0
    cycle = 1
    compromised = False
    storage_capacity = 100 # MB Max for triage logs
    storage_used = 0

    while cycle <= 4 and not compromised:
        clear_screen()
        print(f"--- HOUR: {(cycle-1)*6}:00 | CYCLE: {cycle}/4 | STORAGE LOAD: {storage_used}/{storage_capacity} MB ---\n")
        
        # Scenario Generation
        events = [
            {"desc": "An unknown process is trying to edit system binaries.", "type": "file", "threat": "High"},
            {"desc": "A dynamic IP address is establishing a socket on Port 4444.", "type": "network", "threat": "Critical"},
            {"desc": "Routine cloud cron-jobs are updating log rotations.", "type": "noise", "threat": "None"}
        ]
        current_event = random.choice(events)
        
        print_slow(f"🚨 ALERT TRIGGERED: {current_event['desc']}")
        print(f"Threat Classification: {current_event['threat']}\n")
        
        print("Choose your Forensic Triage action:")
        print("1. [Full Disk Capture] Copy raw binaries & memory (High Storage, Max Evidence)")
        print("2. [Delta Triage] Log text-based SHA-256 hashes only (Low Storage, Fast)")
        print("3. [Ignore] Treat as legitimate system background noise")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == "1":
            storage_used += 40
            print_slow("\n[+] Full capture successful. Highly detailed artifacts stored.")
            if current_event['type'] != 'noise':
                score += 50
                print_slow("-> Threat intercepted successfully!")
            else:
                score -= 10
                print_slow("-> Penalty: Wasted storage array assets on false alarms.")
                
        elif choice == "2":
            storage_used += 2
            print_slow("\n[+] Delta evaluation complete. 120-byte text string appended to log.")
            if current_event['type'] != 'noise':
                score += 100
                print_slow("-> Threat caught instantly via file path analysis!")
            else:
                print_slow("-> Heartbeat written. Zero storage bloat.")
                
        elif choice == "3":
            if current_event['type'] != 'noise':
                compromised = True
                print_slow("\n❌ CRITICAL CRASH: The payload executed. System compromised.", 0.05)
            else:
                score += 20
                print_slow("\n[+] Correct decision. Kept runtime pipeline clear.")

        if storage_used > storage_capacity:
            print_slow("\n⚠️ STORAGE EXPLOSION: Local logs overwhelmed production disk allocation!", 0.05)
            compromised = True

        cycle += 1
        input("\nPress ENTER to step forward 6 hours to the next cycle...")

    clear_screen()
    print("====================================================")
    if compromised:
        print(f"💀 GAME OVER. The attacker outsmarted your triage baseline. Final Score: {score}")
    else:
        print(f"🎉 SUCCESS! You defended the enterprise network for 24 hours! Final Score: {score}")
    print("====================================================")

if __name__ == "__main__":
    play_game()
