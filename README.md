# 🔥 SmartFW: Smart Firewall for Linux Servers

**SmartFW** is an intelligent firewall system for Ubuntu/Linux servers that combines **deterministic iptables rules** with **machine learning** to block suspicious IPs and anomalous traffic patterns in real time.

It is lightweight, modular, and easy to deploy.

---

## ✨ Features

- ✅ **CLI Control** — Easily enable/disable, block/unblock IPs, and view status.
- ✅ **Rule-Based Protection** — Uses `iptables` for deterministic filtering.
- ✅ **Packet Sniffer** — Captures live traffic via `scapy`.
- ✅ **ML-Based Anomaly Detection** — Built-in support for models like Isolation Forest.
- ✅ **Online Learning Support** — Updates the model live as traffic is logged.
- ✅ **Systemd Integration** — Runs as a background Linux service.

---

## 🏗️ Architecture

lua
Copy
Edit
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
+---------------+ +--------------------------+
| Rule Enforcer | | Packet Interceptor |
| (iptables) | <-------------- | (scapy sniffer) |
+---------------+ alerts +--------------------------+
|
+----------v-----------+
| Feature Extractor |
+----------+-----------+
|
+----------v-----------+
| ML Anomaly Detector |
+----------+-----------+
|
+----------v-----------+
| Real-time Action Hook |
+-----------------------+

yaml
Copy
Edit

---

## ⚙️ Installation

### 🧰 Prerequisites

- Python 3.8+
- `iptables` (usually pre-installed on Linux)
- Python packages: `scapy`, `sklearn`, `joblib`

### 📦 Install Script

```bash
cd smartfw
bash scripts/install.sh
Start the service:

bash
Copy
Edit
sudo systemctl start smartfw
🛡️ CLI Usage
bash
Copy
Edit
smartfw enable           # Enable the firewall
smartfw disable          # Disable and flush rules
smartfw block <ip>       # Block a specific IP
smartfw unblock <ip>     # Unblock an IP
smartfw status           # List current firewall rules
smartfw help             # Show help
📁 Logs
logs/traffic.log — All intercepted traffic (features only)

logs/alerts.log — Anomalies and blocked actions

🤖 ML Training and Online Learning
Initial Offline Training
bash
Copy
Edit
python3 core/ml_agent/train.py
Online Learning Loop (Example)
python
Copy
Edit
# Example snippet inside train.py
def update_model_with_new_log():
    ...
    model.partial_fit(new_data)  # Use an online-capable model
💡 For full online learning, consider using libraries like river or models like SGDClassifier.

🔧 Systemd Management
bash
Copy
Edit
sudo systemctl enable smartfw     # Auto-start on boot
sudo systemctl start smartfw      # Start service
sudo systemctl stop smartfw       # Stop service
🧪 Testing
Run all unit tests:

bash
Copy
Edit
cd test/unit_tests
python3 -m unittest discover
🤝 Contributing
Pull requests, bug reports, and feature suggestions are welcome!

Improve detection logic

Add new models or update training loop

Integrate with external monitoring systems

Author - Pratik Anand
Contact @ pratik.csdev@gmail.com

📜 License
MIT License — see LICENSE for full terms.
