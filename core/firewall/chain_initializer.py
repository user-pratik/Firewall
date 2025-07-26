import subprocess

CHAIN = "SMARTFW"

def init_chain():
    try:
        subprocess.run(["sudo", "iptables", "-N", CHAIN], stderr=subprocess.DEVNULL)
    except Exception:
        pass
    subprocess.run(["sudo", "iptables", "-C", "INPUT", "-j", CHAIN], stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "iptables", "-I", "INPUT", "-j", CHAIN])

def flush_chain():
    subprocess.run(["sudo", "iptables", "-F", CHAIN])
    subprocess.run(["sudo", "iptables", "-D", "INPUT", "-j", CHAIN], stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "iptables", "-X", CHAIN])

