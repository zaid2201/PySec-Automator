import re


def analyze_logs():

    failed_attempts = {}

    total_events = 0
    successful_logins = 0
    failed_logins = 0
    invalid_users = 0

    # ==========================================
    # OPEN LOG FILE
    # ==========================================

    try:
        log_file = open(
            "logs/sample_auth.log",
            "r"
        )

    except FileNotFoundError:

        print("\n[ERROR] Authentication log file not found.")
        print("Expected file: logs/sample_auth.log\n")

        return None


    # ==========================================
    # ANALYZE LOGS
    # ==========================================

    with log_file:

        for line in log_file:

            if not line.strip():
                continue

            total_events += 1

            if (
                "Accepted password" in line
                or "Accepted publickey" in line
            ):
                successful_logins += 1

            if "Invalid user" in line:
                invalid_users += 1

            if "Failed password" in line:

                failed_logins += 1

                ip_match = re.search(
                    r"from (\d+\.\d+\.\d+\.\d+)",
                    line
                )

                if ip_match:

                    ip = ip_match.group(1)

                    if ip in failed_attempts:
                        failed_attempts[ip] += 1

                    else:
                        failed_attempts[ip] = 1


    # ==========================================
    # THREAT ANALYSIS
    # ==========================================

    if failed_attempts:

        most_suspicious_ip = max(
            failed_attempts,
            key=failed_attempts.get
        )

        highest_attempts = (
            failed_attempts[most_suspicious_ip]
        )

        if highest_attempts >= 6:
            overall_risk = "HIGH"

        elif highest_attempts >= 3:
            overall_risk = "MEDIUM"

        else:
            overall_risk = "LOW"

    else:

        most_suspicious_ip = "None"
        overall_risk = "LOW"


    return {
        "total_events": total_events,
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "invalid_users": invalid_users,
        "failed_attempts": failed_attempts,
        "most_suspicious_ip": most_suspicious_ip,
        "overall_risk": overall_risk
    }