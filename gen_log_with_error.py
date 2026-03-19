import random
import datetime
import os


def generate_error_log(filename="error_log.log", target_mb=2):
    target_bytes = target_mb * 1024 * 1024
    current_bytes = 0

    levels = ["INFO:", "DEBUG:", "WARNING:", "ERROR:", "ERROR:", "ERROR:"]  # Weighted toward ERROR
    errors = [
        "Database connection timeout",
        "NullPointerException in user_service.py",
        "Failed to write to /var/log/syslog",
        "Authentication failed for user 'admin'",
        "API Gateway returned 504 Gateway Timeout",
        "Disk quota exceeded",
        "Memory leak detected in worker thread 0x4f32"
    ]

    start_time = datetime.datetime.now() - datetime.timedelta(days=1)

    print(f"Generating {target_mb}MB log file...")

    with open(filename, "w", encoding='utf-8') as f:
        while current_bytes < target_bytes:
            # Increment time slightly for each log entry
            start_time += datetime.timedelta(seconds=random.randint(1, 10))
            timestamp = start_time.strftime("%Y-%m-%d %H:%M:%S")

            level = random.choice(levels)
            msg = random.choice(errors) if "ERROR" in level else "Normal operation heartbeat"

            line = f"[{timestamp}] {level} {msg}\n"
            f.write(line)
            current_bytes += len(line.encode('utf-8'))

    print(f"Success! '{filename}' is {os.path.getsize(filename) / (1024 * 1024):.2f} MB")


generate_error_log()