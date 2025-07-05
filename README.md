# voice-based-email-system
This is a Python-based voice-enabled email system designed to help visually impaired users send and read emails using speech commands. It eliminates the need for manual typing or reading by integrating speech recognition, text-to-speech, and email automation.

#Project Title: Voice-Based Email System for Visually Impaired Users
#🧩 Key Features:
#🗣️ Voice Command Interface:
Uses speech recognition to interpret user commands like "send", "read", or "exit".

Communicates with the user using pyttsx3 (text-to-speech).

📤 Send Emails:
The system prompts the user to speak the email body.

Automatically sends the spoken content to a predefined recipient using SMTP with Gmail.

📥 Read Emails:
Connects to the Gmail inbox using IMAP (via easyimap).

Reads out the sender address, subject, and (optionally) email body for the most recent emails.

🔒 Secure Authentication:
Uses Gmail credentials and secure SMTP/IMAP connections (SMTP_SSL, imap.gmail.com).

⚙️ Technologies Used:
Functionality	Library
Speech-to-Text	speech_recognition
Text-to-Speech	pyttsx3
Email Reading	easyimap
Email Sending	smtplib
Voice Control	Python’s microphone, recognizer

🔍 How It Works:
System welcomes the user and waits for a voice command.

User says:

“send” → prompted to speak the email message, which is sent via Gmail.

“read” → reads the most recent emails (sender and subject).

“exit” → ends the session.

In case of unrecognized input, it notifies the user and repeats the prompt.

👁️ Target Audience:
Visually impaired individuals

People with accessibility needs

Users who prefer hands-free communication

🔐 Important Note:
Ensure you generate an App Password from Gmail for login, especially when 2FA is enabled. Never hardcode credentials in real deployments.
