#!/usr/bin/env bash

# --- CONFIG ---
VENV_DIR="$HOME/.smartfw-venv"
SMARTFW_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${VENV_DIR}/bin/python3"
PIP_BIN="${VENV_DIR}/bin/pip"

set -e

# --- INSTALL PYTHON VENV ---
echo "[smartfw] Creating virtual environment at $VENV_DIR..."
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# --- INSTALL PYTHON DEPENDENCIES ---
echo "[smartfw] Installing Python dependencies..."
$PIP_BIN install --upgrade pip
$PIP_BIN install -r "$SMARTFW_DIR/requirements.txt"

# --- LINK CLI ---
echo "[smartfw] Linking CLI tool to /usr/local/bin/smartfw..."
sudo ln -sf "$SMARTFW_DIR/cli/smartfw.sh" /usr/local/bin/smartfw
chmod +x "$SMARTFW_DIR/cli/smartfw.sh"

# --- INSTALL SYSTEMD SERVICE ---
echo "[smartfw] Installing systemd service..."
SERVICE_FILE="/etc/systemd/system/smartfw.service"
sudo tee "$SERVICE_FILE" >/dev/null <<EOF
[Unit]
Description=SmartFW - Intelligent Firewall
After=network.target

[Service]
ExecStart=${PYTHON_BIN} ${SMARTFW_DIR}/core/api/controller.py
WorkingDirectory=${SMARTFW_DIR}
Restart=always
User=$USER
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
EOF

# --- ENABLE AND START SERVICE ---
echo "[smartfw] Enabling and starting smartfw.service..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable smartfw.service
sudo systemctl restart smartfw.service

echo "[smartfw] ✅ SmartFW installed and running. Use 'smartfw status' to check rules."
