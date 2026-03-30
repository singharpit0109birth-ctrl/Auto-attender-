Automated Voice Attendance System (AVAS)
A simple, lightweight Python project that uses Text-to-Speech (TTS) to automate the process of taking attendance. This was built as a BYOP (Build Your Own Project) with a focus on core logic and minimal dependencies.
 Project Description
This system replaces the manual reading of a name list. The program "speaks" each student's name out loud using your computer's voice engine. The user then simply types y or n to mark them present or absent. At the end of the session, it generates a clean, formatted report in the terminal.
Key Features:
 * Voice-Enabled: Uses the pyttsx3 library for offline text-to-speech.
 * Minimalist Design: No heavy databases or complex UI; runs entirely in the terminal.
 * Smart Input: Handles extra spaces or capital letters automatically.
 * Formatted Output: Displays a neat table of results once the roll call is finished.
 Getting Started
Prerequisites
You only need Python installed on your system. To enable the voice feature, install the following library:
pip install pyttsx3

How to Run
 * Clone this repository or download the .py file.
 * Open your terminal or command prompt.
 * Run the script:
   python attendance_system.py

 Built With
 * Python 3.x - The core programming language.
 * pyttsx3 - For converting text into spoken audio (offline).
 Project Structure
 * attendance_system.py: The main script containing the student list and logic.
 * README.md: Project documentation.
 Future Improvements
 * File Integration: Add the ability to read student names from a .csv or .txt file.
 * Data Logging: Save the final attendance report into a dated file (e.g., attendance_28_03_26.txt).
 * Voice Recognition: Implement a microphone listener so the user can say "Yes" or "No" instead of typing.
