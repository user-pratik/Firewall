# 🔥 SmartFW: Smart Firewall for Linux Servers

**SmartFW** is an intelligent firewall system for Ubuntu/Linux servers that combines deterministic `iptables` rules with machine learning to block suspicious IPs and anomalous traffic patterns in real time.

It is lightweight, modular, and easy to deploy.

## ✨ Features

- ✅ CLI Control — Easily enable/disable, block/unblock IPs, and view status  
- ✅ Rule-Based Protection — Uses `iptables` for deterministic filtering  
- ✅ Packet Sniffer — Captures live traffic via Scapy  
- ✅ ML-Based Anomaly Detection — Uses models like Isolation Forest  
- ✅ Online Learning Support — Model updates itself live  
- ✅ Systemd Integration — Persistent background daemon  

## 🏗️ Architecture

```
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
| (iptables)    | <--------------  |     (Scapy sniffer)      |
+---------------+     alerts       +--------------------------+
                                                |
                                     +----------v-----------+
                                     |  Feature Extractor    |
                                     +----------+-----------+
                                                |
                                     +----------v-----------+
                                     | ML Anomaly Detector   |
                                     +----------+-----------+
                                                |
                                     +----------v-----------+
                                     | Real-time Action Hook |
                                     +-----------------------+
```

## ⚙️ Installation

### 🧰 Prerequisites

- Python 3.8+
- `iptables` (pre-installed on most Linux distros)
- Python packages: `scapy`, `sklearn`, `joblib`, `river` (optional for online learning)

### 📦 Install

```bash
cd smartfw  
bash scripts/install.sh  
```

Start the service:

```bash
sudo systemctl start smartfw  
```

To auto-start on boot:

```bash
sudo systemctl enable smartfw  
```

## 🛡️ CLI Usage

```bash
smartfw enable           # Enable the firewall  
smartfw disable          # Disable and flush rules  
smartfw block <ip>       # Block a specific IP  
smartfw unblock <ip>     # Unblock an IP  
smartfw status           # List current firewall rules  
smartfw help             # Show help  
```

## 📁 Logs

- `logs/traffic.log` — All intercepted traffic (features only)  
- `logs/alerts.log` — Anomalies and blocked actions  

## 🤖 ML Training and Online Learning

### Offline Training (Initial)

```bash
python3 core/ml_agent/train.py  
```

### Online Learning Loop (Example)

```python
# Example inside train.py  
def update_model_with_new_log():  
    new_data = load_recent_logs("logs/traffic.log")  
    model.partial_fit(new_data)  # Use online-capable model
```

💡 For live model updates, use libraries like `river` or `SGDClassifier` from `sklearn.linear_model`.

## 🔧 Systemd Integration

```bash
sudo systemctl enable smartfw     # Auto-start on boot  
sudo systemctl start smartfw      # Start the daemon  
sudo systemctl stop smartfw       # Stop the daemon  
```

## 🧪 Testing

```bash
cd test/unit_tests  
python3 -m unittest discover  
```

## 🤝 Contributing

Pull requests and issues are welcome!

Ideas to contribute:
- Enhance detection logic
- Add more ML models or hybrid detectors
- Integrate with monitoring dashboards
- Add alert hooks (email, webhook, etc.)

## 👤 Author

**Pratik Anand**  
📧 Email: pratik.csdev@gmail.com  
🌐 GitHub: [user-pratik](https://github.com/user-pratik)

## 📜 License

MIT License — see `LICENSE` file for full terms.
