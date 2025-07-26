#!/usr/bin/env bash

# smartfw - Simple CLI wrapper for firewall management (iptables-based)
# Supports: enable/disable firewall, add/remove IPs, show status

FW_CHAIN="SMARTFW"

function init_firewall() {
  sudo iptables -N $FW_CHAIN 2>/dev/null || true
  sudo iptables -C INPUT -j $FW_CHAIN 2>/dev/null || sudo iptables -I INPUT -j $FW_CHAIN
  echo "[smartfw] Initialized chain '$FW_CHAIN' and hooked into INPUT"
}

function enable_firewall() {
  init_firewall
  echo "[smartfw] Firewall enabled"
}

function disable_firewall() {
  sudo iptables -D INPUT -j $FW_CHAIN 2>/dev/null || true
  sudo iptables -F $FW_CHAIN
  sudo iptables -X $FW_CHAIN
  echo "[smartfw] Firewall disabled"
}

function block_ip() {
  local ip=$1
  if [ -z "$ip" ]; then
    echo "[smartfw] Usage: smartfw block <ip>"
    exit 1
  fi
  sudo iptables -A $FW_CHAIN -s $ip -j DROP
  echo "[smartfw] Blocked $ip"
}

function unblock_ip() {
  local ip=$1
  if [ -z "$ip" ]; then
    echo "[smartfw] Usage: smartfw unblock <ip>"
    exit 1
  fi
  sudo iptables -D $FW_CHAIN -s $ip -j DROP 2>/dev/null && echo "[smartfw] Unblocked $ip" || echo "[smartfw] IP not found"
}

function list_rules() {
  echo "[smartfw] Current rules in $FW_CHAIN:"
  sudo iptables -L $FW_CHAIN -n --line-numbers
}

function help() {
  echo "Usage: smartfw <command> [args]"
  echo "Commands:"
  echo "  enable            Initialize and enable firewall"
  echo "  disable           Flush and disable firewall"
  echo "  block <ip>        Block a specific IP address"
  echo "  unblock <ip>      Unblock a specific IP address"
  echo "  status            Show current rules"
  echo "  help              Show this message"
}

case "$1" in
enable)
  enable_firewall
  ;;
disable)
  disable_firewall
  ;;
block)
  block_ip "$2"
  ;;
unblock)
  unblock_ip "$2"
  ;;
status)
  list_rules
  ;;
help | *)
  help
  ;;
esac
