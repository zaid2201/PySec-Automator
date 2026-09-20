from scanner import scan_ports
from log_analyzer import analyze_logs
from reporter import generate_report


def main():

    print("\n" + "=" * 50)
    print("              PYSEC AUTOMATOR")
    print("=" * 50)

    print("\n1. Network Port Scanner")
    print("2. Security Log Analyzer")
    print("3. Generate Security Report")
    print("4. Run Full Security Analysis")
    print("5. Exit")

    choice = input("\nSelect an option (1-5): ").strip()


    # ==========================================
    # OPTION 1 - NETWORK PORT SCANNER
    # ==========================================

    if choice == "1":

        print("\n--- NETWORK PORT SCANNER ---")

        target = input(
            "Enter target IP address: "
        ).strip()

        scan_ports(target)


    # ==========================================
    # OPTION 2 - SECURITY LOG ANALYZER
    # ==========================================

    elif choice == "2":

        print("\n--- SECURITY LOG ANALYZER ---")

        results = analyze_logs()

        # Stop if log file could not be analyzed
        if results is None:
            print("Log analysis could not be completed.")
            return

        print("\nSECURITY SUMMARY")
        print("-" * 40)

        print(
            f"Total Events:        "
            f"{results['total_events']}"
        )

        print(
            f"Successful Logins:   "
            f"{results['successful_logins']}"
        )

        print(
            f"Failed Logins:       "
            f"{results['failed_logins']}"
        )

        print(
            f"Invalid Users:       "
            f"{results['invalid_users']}"
        )

        print(
            f"Suspicious IPs:      "
            f"{len(results['failed_attempts'])}"
        )


        print("\nFAILED LOGIN ANALYSIS")
        print("-" * 40)

        for ip, attempts in sorted(
            results["failed_attempts"].items(),
            key=lambda item: item[1],
            reverse=True
        ):

            if attempts >= 6:
                level = "HIGH"

            elif attempts >= 3:
                level = "MEDIUM"

            else:
                level = "LOW"

            print(
                f"[{level:<6}] "
                f"{ip:<18} "
                f"{attempts} failed attempts"
            )


        print("\nTHREAT SUMMARY")
        print("-" * 40)

        print(
            f"Most Suspicious IP: "
            f"{results['most_suspicious_ip']}"
        )

        print(
            f"Overall Risk Level: "
            f"{results['overall_risk']}"
        )


    # ==========================================
    # OPTION 3 - GENERATE REPORT
    # ==========================================

    elif choice == "3":

        print("\n--- GENERATE SECURITY REPORT ---")

        generate_report()


    # ==========================================
    # OPTION 4 - FULL SECURITY ANALYSIS
    # ==========================================

    elif choice == "4":

        print("\n" + "=" * 50)
        print("       PYSEC FULL SECURITY ANALYSIS")
        print("=" * 50)

        target = input(
            "\nEnter target IP address: "
        ).strip()


        # STEP 1 - PORT SCAN

        print(
            "\n[1/3] Running Network Port Scan..."
        )

        scan_results = scan_ports(target)

        # Stop if IP address was invalid
        if scan_results is None:
            print(
                "Full security analysis stopped."
            )
            return


        # STEP 2 - LOG ANALYSIS

        print(
            "\n[2/3] Running Security Log Analysis..."
        )

        log_results = analyze_logs()

        # Stop if log file could not be analyzed
        if log_results is None:
            print(
                "Full security analysis stopped."
            )
            return


        print("\nLog Analysis Summary:")

        print(
            f"Total Events:       "
            f"{log_results['total_events']}"
        )

        print(
            f"Failed Logins:      "
            f"{log_results['failed_logins']}"
        )

        print(
            f"Suspicious IPs:     "
            f"{len(log_results['failed_attempts'])}"
        )

        print(
            f"Overall Risk:       "
            f"{log_results['overall_risk']}"
        )


        # STEP 3 - GENERATE REPORT

        print(
            "\n[3/3] Generating Security Report..."
        )

        generate_report(
            target,
            scan_results
        )


        print("\n" + "=" * 50)
        print(
            "       FULL SECURITY ANALYSIS COMPLETE"
        )
        print("=" * 50)

        print(f"\nTarget: {target}")

        print(
            f"Risk Level: "
            f"{log_results['overall_risk']}"
        )

        print(
            "Report: reports/security_report.txt"
        )


    # ==========================================
    # OPTION 5 - EXIT
    # ==========================================

    elif choice == "5":

        print("\nExiting PySec Automator.")


    # ==========================================
    # INVALID MENU OPTION
    # ==========================================

    else:

        print(
            "\n[ERROR] Invalid option."
        )

        print(
            "Please select a number from 1 to 5."
        )


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()