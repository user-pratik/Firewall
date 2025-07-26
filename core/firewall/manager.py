import subprocess
from .chain_initializer import init_chain, flush_chain

CHAIN = "SMARTFW"

def block_ip(ip):
    init_chain()
    subprocess.run(["sudo", "iptables", "-A", CHAIN, "-s", ip, "-j", "DROP"])

def unblock_ip(ip):
    subprocess.run(["sudo", "iptables", "-D", CHAIN, "-s", ip, "-j", "DROP"], stderr=subprocess.DEVNULL)

def list_rules():
    subprocess.run(["sudo", "iptables", "-L", CHAIN, "-n", "--line-numbers"])

def disable_firewall():
    flush_chain()

