SmartFW: Smart Firewall for Linux Servers

SmartFW is an intelligent firewall system for Ubuntu/Linux servers that combines deterministic iptables rules with machine learning to block suspicious IPs and anomalous traffic patterns in real time.

It is built to be lightweight, modular, and easy to deploy.

Features

✅ CLI control for enabling/disabling, blocking IPs, viewing status

✅ Deterministic rule-based blocking using iptables

✅ Packet sniffer for logging raw traffic

✅ ML-based anomaly detection using Isolation Forest

✅ Online learning support

✅ Systemd integration for persistent background service

Architecture

                +------------------------+
                |      CLI Interface     |
                +-----------+------------+
                            |
                            v
                +-----------+------------+
                |      Core Controller   | <--- future HTTP or socket API
                +-----------+------------+
                            |
        +-------------------+--------------------+
        |                                        |
        v                                        v
+---------------+                  +--------------------------+
| Rule Enforcer |                  |   Packet Interceptor     |
| (iptables)    | <--------------  | (scapy sniffer)          |
+---------------+     alerts       +--------------------------+
                                                |
                                     +----------v-----------+
                                     |  Feature Extractor    |
                                     +----------+-----------+
                                                |
                                     +----------v-----------+
                                     |   ML Anomaly Detector |
                                     +----------+-----------+
                                                |
                                     +----------v-----------+
                                     | Real-time Action Hook |
                                     +-----------------------+

Installation

Prerequisites

Python 3.8+

iptables (already present on most Linux systems)

scapy, sklearn, joblib (install via pip)

Install Script

cd smartfw
bash scripts/install.sh

Then start the service:

sudo systemctl start smartfw

CLI Usage

smartfw enable             # Enable the firewall
smartfw disable            # Disable and flush rules
smartfw block <ip>         # Block a specific IP
smartfw unblock <ip>       # Unblock an IP
smartfw status             # List current firewall rules
smartfw help               # Show help

Logs

logs/traffic.log - All intercepted traffic (features only)

logs/alerts.log - Anomalies and blocked actions

ML Training and Online Learning

Initial training (offline):

python3 core/ml_agent/train.py

Online learning (continuous updates):

# core/ml_agent/train.py (example addition)
def update_model_with_new_log():
    ... # Load new logs since last training
    model.partial_fit(new_data)  # Assumes online-capable model (e.g. SGDClassifier)

For full online learning support, replace IsolationForest with an incremental learner like River, SGDClassifier, etc.

Systemd Management

sudo systemctl enable smartfw
sudo systemctl start smartfw
sudo systemctl stop smartfw

Testing

To run unit tests:

cd test/unit_tests
python3 -m unittest discover

Contributing

PRs, issues, and discussions are welcome. If you have ideas for improving detection, model tuning, or integration with other tools, feel free to contribute!

License

MIT License. See LICENSE file for details.


