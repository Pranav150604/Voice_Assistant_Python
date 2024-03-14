# Voice Assistant - Nⱥno多oτ<br>
# Overview
This is a Python-based Voice Assistant program capable of performing various tasks such as wishing the user according to the time of the day, opening web browsers, searching Wikipedia, playing songs on Spotify, sending emails, and more. The assistant interacts with the user through voice commands and responses.

## Features
Voice Recognition: Utilizes the speech_recognition library to recognize spoken commands.<br>
Text-to-Speech: Implements the pyttsx3 library for text-to-speech conversion, allowing the assistant to respond audibly.<br>
Time-based Greetings: Greets the user according to the current time of the day.<br>
Web Browsing: Can open websites such as YouTube, Google, Stack Overflow, etc., using the webbrowser module.<br>
Wikipedia Search: Provides summaries of Wikipedia articles based on user queries.<br>
Music Playback: Can play songs on Spotify.<br>
Email Sending: Capable of sending emails using SMTP.<br>
Visual Studio Code Integration: Opens Visual Studio Code for coding tasks.<br>
## Installation
Clone the repository or download the source code.<br>
Ensure you have Python installed on your system.<br>
Install the required Python libraries using pip:
pip install pyttsx3 speech_recognition wikipedia<br>
Make sure to have a compatible version of Visual Studio Code installed if intending to use that feature.
## Usage
Run the voice_assistant.py script.
The assistant will greet you based on the time of day.
Speak commands such as:
"Open YouTube"
"What is the time?"
"Play songs"
"Send email"
"Quit"
## Configuration
Ensure that your system has a working microphone for voice input.
For sending emails, update the sendEmail() function with your email credentials and allow access to less secure apps in your Gmail settings.
## Notes
This program may require adjustments or additional configurations depending on your system environment.
Issues may arise with voice recognition and text-to-speech functionality on certain platforms, particularly when running on Google Colab due to driver issues.
Feel free to customize and extend the functionality of the assistant according to your requirements.
