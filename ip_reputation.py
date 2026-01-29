import requests
import sys

def banner():
    print("""
====================================
   IP REPUTATION CHECKER (EDU)
   Author : Shibnath Hansda
   Purpose: Educational Only
====================================
""")

def check_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        print("\n[+] IP Information")
        print("--------------------")
        print(f"IP        : {data.get('ip', 'N/A')}")
        print(f"City      : {data.get('city', 'N/A')}")
        print(f"Region    : {data.get('region', 'N/A')}")
        print(f"Country   : {data.get('country', 'N/A')}")
        print(f"Org       : {data.get('org', 'N/A')}")
        print(f"Location  : {data.get('loc', 'N/A')}")
        print(f"Timezone  : {data.get('timezone', 'N/A')}")

        # Simple reputation logic
        org = data.get("org", "").lower()
        if "vpn" in org or "hosting" in org or "cloud" in org:
            print("\n⚠️  Warning: This IP may belong to VPN / Hosting / Proxy")
        else:
            print("\n✅ This IP looks like a normal ISP address")

    except Exception as e:
        print("[-] Error fetching IP info:", e)

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 2:
        print("Usage: python ip_reputation.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    check_ip(ip_address)
  
