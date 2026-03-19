import random
import os


def generate_2mb_log(filename="test_log.log"):
    # Typical log components
    ips = [f"192.168.1.{i}" for i in range(1, 100)]
    methods = ["GET", "POST", "PUT", "DELETE"]
    endpoints = ["/home", "/login", "/api/v1/data", "/img/logo.png", "/cart/add"]
    codes = ["200", "404", "500", "302"]

    target_size = 2 * 1024 * 1024  # 2MB in bytes
    current_size = 0

    print(f"Generating {filename}...")

    with open(filename, "w") as f:
        while current_size < target_size:
            # Create a fake Apache-style log line
            line = f'{random.choice(ips)} - - [20/May/2024:10:00:01 +0000] ' \
                   f'"{random.choice(methods)} {random.choice(endpoints)} HTTP/1.1" ' \
                   f'{random.choice(codes)} {random.randint(100, 5000)}\n'
            f.write(line)
            current_size += len(line)

    print(f"Done! Created {filename} ({os.path.getsize(filename) / (1024 * 1024):.2f} MB)")


generate_2mb_log()