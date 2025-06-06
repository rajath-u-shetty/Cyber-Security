# ﻿🔍 Basic Port Scanner
A lightweight Python-based TCP port scanner designed for educational purposes. This tool demonstrates fundamental concepts in socket programming and network scanning.

# 📌 Overview
This script scans a target IP address or domain for open TCP ports within a specified range (default: 1–1024). It uses Python’s socket module to attempt connections and reports open ports.

# ✅ For educational use only
⚠️ Do not scan unauthorized targets

# 🚀 Features
Scans TCP ports in the range 1–1024

Detects open ports on the target host
Implements socket timeout handling
(Planned) Threading support for faster scanning

# 🛠️ Tech Stack
Language: Python 3.x
Modules:
socket (core functionality)
time (optional, for measuring scan duration)
threading (optional, for future concurrency)

# 📦 Usage
Clone the repository or copy the script.
Run the script:
bash
Copy
Edit
python port_scanner.py
Input a domain or IP when prompted (e.g., scanme.nmap.org).

View the list of open ports in the console.
🧪 Sample Output
text
Copy
Edit
Enter IP address or domain to scan: scanme.nmap.org
Scanning target: scanme.nmap.org
Port 22 is OPEN
Port 80 is OPEN
...

# 🧠 Learning Outcomes
TCP/IP fundamentals and port behavior
Python socket programming essentials
Handling network timeouts and exceptions
Responsible and ethical scanning practices

# ✅ Conclusion
This project provides a hands-on introduction to network communication and cybersecurity fundamentals. You'll learn how TCP port scanning works at a low level and gain experience in writing efficient, ethical, and educational network tools.

It also serves as a foundation for more advanced projects like:
Multi-threaded scanners
Banner grabbers
Custom vulnerability scanners
Ideal for learners interested in ethical hacking, penetration testing, or network administration.
