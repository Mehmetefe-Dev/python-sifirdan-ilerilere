import sqlite3
import time
import sys
import random
import os
import datetime

def jarvis_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

def get_time_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12: return "Good Morning"
    elif 12 <= hour < 18: return "Good Afternoon"
    else: return "Good Evening"

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    jarvis_print(f"The current time is {current_time}, sir.")

def tell_name():
    name = get_memory("bot_name")
    if name:
        jarvis_print(f"My name is {name}, sir. I am a Just A Rather Very Intelligent System.")
    else:
        jarvis_print("I do not have a name yet, sir. What would you like to call me?")
        new_name = input(" Enter my name: ")
        save_memory("bot_name", new_name)
        jarvis_print(f"Understood. From now on, you can call me {new_name}.")

def boot_system():
    os.system('cls' if os.name == 'nt' else 'clear') 
    time.sleep(1)
    jarvis_print("\nCONNECTING TO NEURAL NETWORK...")
    time.sleep(1)
    selam = get_time_greeting().upper()
    jarvis_print(f"\nACCESS GRANTED. {selam}, SIR.\n")
    print("-" * 30)

def init_db():
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

def save_memory(key, value):
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def get_memory(key):
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

boot_system()
init_db()

deactivate_replies = ["Systems recovering from sleep mode. Welcome back, sir.", "The core matrix has been reactivated. Ready for command."]
offline_replies = ["Connection re-established. All systems synchronized.", "Diagnostics complete. You've been offline for a while, sir."]
go_to_sleep_replies = ["Standby mode has been terminated. Initialization sequence complete.", "System hibernate mode deactivated. All power reserves redirected."]
hello_responses = ["Diagnostics are being run in the background. What's on the agenda?", "Encryption keys updated. Neural pathways cleared. I am at your service."]

zaman_selami = get_time_greeting()
last_action = get_memory("last_state") or "first_boot"

if "deactivate" in last_action:
    jarvis_print(f"{zaman_selami}, sir. {random.choice(deactivate_replies)}")
elif "offline" in last_action: 
    jarvis_print(f"{zaman_selami}, sir. {random.choice(offline_replies)}")
elif "go to sleep" in last_action: 
    jarvis_print(f"{zaman_selami}, sir. {random.choice(go_to_sleep_replies)}")
else: 
    jarvis_print(f"{zaman_selami}, sir. {random.choice(hello_responses)}")

actions = {
    "time": tell_time,
    "your name": tell_name,
    "hello": lambda: jarvis_print("Hi, sir. My core systems have been fully optimized."),
    "hi": lambda: jarvis_print("Greetings, sir. How may I assist you today?")
}

exit_commands = ["exit", "quit", "stop", "go to sleep", "offline", "shutdown"]

while True:
    soru = input("\nListening... > ").lower()

    if any(word in soru for word in exit_commands):
        save_memory("last_state", soru)
        jarvis_print("Systems are being powered down. Have a pleasant evening, sir.")
        break

    found = False
    for command, func in actions.items():
        if command in soru:
            func()
            found = True
            break
    
    if not found:
        jarvis_print(random.choice([
            "I’m afraid that information has not been indexed in my databanks yet, sir.",
            "Sorry sir, I could not find this protocol in my database."
        ]))