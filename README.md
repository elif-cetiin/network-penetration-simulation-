# Network Penetration Simulation (Ethical Hacking Project)

This project documents ethical penetration testing activities executed in a controlled, isolated lab environment. Work was performed using Kali Linux (VM), Parrot OS, Wireshark, Nmap, and Python. The primary goals were to reproduce realistic attack patterns, capture and analyze network traffic, and produce synthetic flow data for defensive analysis and training.

Author: Elif Cetin  
Lab environment: VirtualBox VMs (Kali Linux 2024.x), isolated VLAN, Sept 2025

---

# Project Scope

Actions performed in a virtual lab environment:

- Performed MAC flooding and ARP poisoning to observe switching/ARP table behavior.
- Simulated DoS-style traffic bursts to identify abnormal flow characteristics.
- Captured live packets with Wireshark and inspected protocol activity (TCP/UDP, ARP).
- Recorded findings and recommended mitigations for the observed vulnerabilities.

---

# Tools & Technologies

| Category               | Tools Used                                             |
|------------------------|--------------------------------------------------------|
| Penetration Testing    | Kali Linux, Parrot OS, Nmap, small MAC-flood scripts   |
| Traffic Capture/Analysis| Wireshark                                              |
| Automation / Scripting | Python (data generator + small parsers)                |
| Virtualization         | VirtualBox                                             |
| Version Control        | Git & GitHub                                           |

---

### Repository Structure

```text
/scripts                         → Custom Python scripts used in the lab
│   └── generate_synthetic_flows.py   (creates synthetic CSV traffic data)
│   └── synthetic_flows_sample.csv    (small example output)
/safe_artifacts                  → Generated artifacts (CSV, PCAP summaries)
requirements.txt                 → Python dependency list (pandas, matplotlib)
ETHICS_AND_SAFE_USE.md           → Ethical usage and safety notice
README.md                        → This project overview
```

