#!/bin/bash
echo "[*] Uninstalling smartfw..."
sudo systemctl stop smartfw
sudo systemctl disable smartfw
sudo rm -f /usr/local/bin/smartfw
sudo rm -f /etc/systemd/system/smartfw.service
echo "[✓] Uninstalled smartfw"
