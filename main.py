import pyttsx3

# Initialize the speaker engine
engine = pyttsx3.init()

# List of 10 Indian names
names = ["Arjun", "Aditi", "Ishaan", "Sanya", "Vihaan", "Ananya", "Rohan", "Kavya", "Rahul", "Priya"]

attendance_log = {}

print("--- Automated Voice Attendance ---")

for name in names:
    # System speaks the name
    print(f"\nSystem: Is {name} present?")
    engine.say(f"Is {name} present?")
    engine.runAndWait()
    
    # User inputs response
    response = input("Response (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        attendance_log[name] = "Present"
    else:
        attendance_log[name] = "Absent"

# Final Summary
print("\n--- Attendance Report ---")
for person, status in attendance_log.items():
    print(f"{person:8}: {status}")

engine.say("Attendance marking complete.")
engine.runAndWait()