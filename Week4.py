print("Checking login attempts...")

login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]

failed_counts = {}

for attempt in login_attempts:
    username = attempt[0]
    status = attempt[1]

    if status == "failed":
        if username not in failed_counts:
            failed_counts[username] = 1
        else:
            failed_counts[username] += 1

        if failed_counts[username] == 3:
            print(f"ALERT: User '{username}' has 3 failed login attempts")

print("Security check complete")


#  ---------Exercise 2
print("Scanning network devices...")

devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]

total_risks = 0

for device in devices:
    ip = device[0]
    open_ports = device[1]

    for port in open_ports:
        if port in risky_ports:
            print(f"WARNING: {ip} has risky port {port} open")
            total_risks += 1

print(f"Scan complete: {total_risks} security risks found")



# ----- Exercise 3
print("Validating passwords...")

passwords = [
    "Pass123",
    "SecurePassword1",
    "weak",
    "MyP@ssw0rd",
    "NOLOWER123"
]

compliant = 0
non_compliant = 0

for password in passwords:
    length_ok = len(password) >= 8
    uppercase_ok = False
    lowercase_ok = False
    digit_ok = False

    # Check each character
    for char in password:
        if char >= "A" and char <= "Z":
            uppercase_ok = True
        if char >= "a" and char <= "z":
            lowercase_ok = True
        if char >= "0" and char <= "9":
            digit_ok = True

    # Build failure reason
    reason = ""

    if not length_ok:
        reason += "Too short"

    if not uppercase_ok:
        if reason != "":
            reason += ", "
        reason += "No uppercase"

    if not lowercase_ok:
        if reason != "":
            reason += ", "
        reason += "No lowercase letters"

    if not digit_ok:
        if reason != "":
            reason += ", "
        reason += "No digits"

    # Print result
    if length_ok and uppercase_ok and lowercase_ok and digit_ok:
        print(f"PASS: '{password}' - Meets all requirements")
        compliant += 1
    else:
        print(f"FAIL: '{password}' - {reason}")
        non_compliant += 1

print(f"Summary: {compliant} compliant, {non_compliant} non-compliant")
