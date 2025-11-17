# Network Penetration Simulation (Ethical Hacking Project)

This project documents ethical penetration testing activities executed in a controlled, isolated lab environment. Work was performed using Kali Linux (VM), Parrot OS, Wireshark, Nmap, and Python. The primary goals were to reproduce realistic attack patterns, capture and analyze network traffic, and produce synthetic flow data for defensive analysis and training.


---

# Project Scope

Actions performed in a virtual lab environment:

- Performed MAC flooding and ARP poisoning to observe switching and ARP table behavior.
- Simulated DoS-style traffic bursts to identify abnormal flow characteristics.
- Captured live packets with Wireshark and inspected protocol activity (TCP/UDP, ARP).
- Recorded findings and recommended mitigations for the observed vulnerabilities.

---

# Tools & Technologies

| Category               | Tools Used                          |
|------------------------|--------------------------------------|
| Penetration Testing    | Kali Linux, Parrot OS, Nmap, scripts |
| Traffic Capture/Analysis | Wireshark                           |
| Automation / Scripting | Python                                |
| Virtualization         | VirtualBox                            |
| Version Control        | Git & GitHub                          |

---

### Repository Structure

```text
/scripts                         → Python scripts used in the lab
│   └── generate_synthetic_flows.py
│   └── synthetic_flows.csv
/safe_artifacts                  → Generated artifacts (CSV, PCAP summaries)
requirements.txt                 → Python dependency list
ETHICS_AND_SAFE_USE.md           → Ethical usage and safety notice
README.md                        → Project overview

Author: Elif Cetin  
Lab environment: VirtualBox VMs (Kali Linux 2024.x), isolated VLAN, Sept 2025
