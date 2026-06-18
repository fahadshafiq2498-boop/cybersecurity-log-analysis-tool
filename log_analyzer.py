# Simple cybersecurity log analysis tool



failed_login_count = 0

with open("sample_auth.log", "r") as log_file:
    for line in log_file:
        if "Failed password" in line:
            failed_login_count += 1
            print("Suspicious login attempt found:", line.strip())

print("\nTotal failed login attempts:", failed_login_count)

