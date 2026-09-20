# PySec Automator

PySec Automator is a Python cybersecurity project I built to practice network scanning, log analysis, and basic security automation.

The idea behind the project was to combine a few common security tasks into one simple command-line tool instead of keeping them as separate Python scripts.

## Features

The program currently has four main functions:

- Scan common TCP ports on a target IP address
- Analyze SSH authentication logs
- Detect repeated failed login attempts
- Assign basic LOW, MEDIUM, and HIGH risk levels
- Generate a security report automatically
- Run the scanner, log analyzer, and report generator together using the Full Security Analysis option

## Project Structure

```text
PySec-Automator/
│
├── logs/
│   └── sample_auth.log
│
├── reports/
│   └── security_report.txt
│
├── log_analyzer.py
├── main.py
├── reporter.py
├── scanner.py
└── README.md
```

## How to Run

Make sure Python is installed on your system.

Open a terminal inside the project folder and run:

```bash
python main.py
```

The program will display the following menu:

```text
==================================================
              PYSEC AUTOMATOR
==================================================

1. Network Port Scanner
2. Security Log Analyzer
3. Generate Security Report
4. Run Full Security Analysis
5. Exit
```

For local testing, I used:

```text
127.0.0.1
```

This is the localhost address, which points back to your own computer.

## Network Port Scanner

The scanner uses Python sockets to test a small set of common TCP ports.

The current ports include:

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

The scanner reports whether each tested port is open or closed.

## Log Analyzer

The log analyzer reads authentication events from:

```text
logs/sample_auth.log
```

It looks for events such as:

- Successful logins
- Failed password attempts
- Invalid users
- Repeated failed logins from the same IP address

It then counts the failed attempts associated with each IP address.

## Basic Risk Detection

I added simple detection logic to classify repeated failed login attempts.

The current thresholds are:

```text
1-2 failed attempts  -> LOW
3-5 failed attempts  -> MEDIUM
6+ failed attempts   -> HIGH
```

These thresholds were created for this project and are not intended to represent a real production security standard.

## Security Report

PySec Automator can automatically create a report at:

```text
reports/security_report.txt
```

The report contains:

- Target IP address
- Network scan results
- Authentication event statistics
- Failed login analysis
- Suspicious IP addresses
- Most suspicious IP
- Overall risk level

## What I Learned

Building this project helped me practice:

- Python fundamentals
- Functions and modules
- Python sockets
- TCP ports and network services
- Reading and parsing log files
- Regular expressions
- Dictionaries and loops
- Basic security detection logic
- Error handling
- Automating security reports
- Organizing a Python project into multiple files

It also helped me understand how small Python scripts can be combined to automate repetitive cybersecurity tasks.

## Limitations

This is a learning project and is not intended to replace tools such as Nmap or a production SIEM.

The network scanner currently checks only a small set of TCP ports and uses basic socket connections.

The risk detection system also uses simple thresholds rather than advanced detection or behavioral analysis.

The authentication logs included in this repository are synthetic sample logs created for testing the log analyzer.

## Future Improvements

Some features I would like to add in the future:

- Custom port ranges
- Better detection of filtered or unreachable ports
- More detailed service information
- More log detection rules
- JSON or CSV report output
- Threat intelligence integration
- Improved command-line interface

## Disclaimer

This project was created for learning and defensive security practice.

The network scanning functionality should only be used on systems that you own or have explicit permission to test.git add 