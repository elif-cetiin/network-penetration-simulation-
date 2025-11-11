#!/usr/bin/env python3
"""
generate_synthetic_flows.py
Creates a synthetic network flows CSV for defensive analysis and training.

Each row in the output CSV contains:
timestamp, src_ip, dst_ip, dst_port, protocol, bytes, label
"""

import csv
import random
from datetime import datetime, timedelta
import os

# Example ports & protocols observed in typical network traffic
PORTS = [80, 443, 53, 22, 123, 8080]
PROTOCOLS = ["TCP", "UDP"]

# IP address pools (private ranges and reserved test-range for dst)
SRC_POOL = [f"10.0.0.{i}" for i in range(2, 50)]
DST_POOL = [f"192.0.2.{i}" for i in range(1, 40)]  # RFC 5737 reserved documentation range


def generate_flows(minutes=60, out="safe_artifacts/synthetic_flows.csv"):
    """
    Generates synthetic network flow records and writes them to a CSV file.
    Normal traffic is generated every minute, with a small chance of anomaly spikes
    that simulate data exfiltration attempts.
    """
    dirpath = os.path.dirname(out)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    start_time = datetime.utcnow()

    with open(out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "src_ip", "dst_ip", "dst_port", "protocol", "bytes", "label"])

        for minute in range(minutes):
            # Normal flows (random volume per minute)
            for _ in range(random.randint(35, 45)):
                ts = start_time + timedelta(minutes=minute, seconds=random.randint(0, 59))
                writer.writerow([
                    ts.isoformat(),
                    random.choice(SRC_POOL),
                    random.choice(DST_POOL),
                    random.choice(PORTS),
                    random.choice(PROTOCOLS),
                    random.randint(300, 1500),
                    "normal"
                ])

            # Occasional anomaly spike (simulated exfiltration)
            if random.random() < 0.02:
                for _ in range(3):
                    ts = start_time + timedelta(minutes=minute)
                    writer.writerow([
                        ts.isoformat(),
                        random.choice(SRC_POOL),
                        random.choice(DST_POOL),
                        random.choice([4444, 5555, 6666]),
                        "TCP",
                        random.randint(200_000, 900_000),
                        "anomaly"
                    ])

    print(f"✔ Synthetic flows saved to: {out}")


if __name__ == "__main__":
    generate_flows()
