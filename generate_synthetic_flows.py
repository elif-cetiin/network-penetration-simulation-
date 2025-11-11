#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/generate_synthetic_flows.py
Synthetic network flows generator for defensive analysis / lab use.
Author: Elif Cetin
"""

import csv
import random
from datetime import datetime, timedelta, timezone
import os

PORTS = [80, 443, 53, 22, 123, 8080]
PROTOCOLS = ["TCP", "UDP"]

SRC_POOL = [f"10.0.0.{i}" for i in range(2, 50)]
DST_POOL = [f"192.0.2.{i}" for i in range(1, 40)]

def generate_flows(minutes=60, out="safe_artifacts/synthetic_flows.csv"):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    now = datetime.now(timezone.utc)

    with open(out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "src_ip", "dst_ip", "dst_port", "protocol", "bytes", "label"])

        for m in range(minutes):
            for _ in range(random.randint(35, 45)):
                ts = now + timedelta(minutes=m, seconds=random.randint(0, 59))
                writer.writerow([
                    ts.isoformat(),
                    random.choice(SRC_POOL),
                    random.choice(DST_POOL),
                    random.choice(PORTS),
                    random.choice(PROTOCOLS),
                    random.randint(300, 1500),
                    "normal"
                ])

            if random.random() < 0.02:
                for _ in range(3):
                    ts = now + timedelta(minutes=m)
                    writer.writerow([
                        ts.isoformat(),
                        random.choice(SRC_POOL),
                        random.choice(DST_POOL),
                        random.choice([4444, 5555, 6666]),
                        "TCP",
                        random.randint(200_000, 900_000),
                        "anomaly"
                    ])

    print(f"✔ synthetic flows saved to: {out}")

if __name__ == "__main__":
    generate_flows()
