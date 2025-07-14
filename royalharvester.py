 import os
import sys
import time
import socket
import json
import requests
import re
from urllib.parse import quote_plus

ADMIN_NAME = "Lord Oblivion"
ADMIN_PHONE = "+2348039420739"
ADMIN_EMAIL = "anonymousoblivionj@gmail.com"

VALID_KEYS = [
    "OBLIVION-2025-ACTIVE",
    "DARKMODE-KEY-999"
]
def locked_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('''
╔════════════════════════════════════════════════════════╗
║          🔒 OBLIVION DARK TOOL - ACTIVATION 🔒         ║
╠════════════════════════════════════════════════════════╣
║  This tool is locked. Please enter your activation key ║
╚════════════════════════════════════════════════════════╝
''')
    key = input("\n🔑 Enter Activation Key: ").strip()
    if key not in VALID_KEYS:
        print("\n❌ Invalid key. Exiting...")
        sys.exit()
    print("\n✅ Activation successful! Launching Tool...\n")
    time.sleep(2)
    def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = '''
╔════════════════════════════════════════════════════════╗
║            O B L I V I O N   D A R K   T O O L         ║
║                   [ G O D   M O D E ]                  ║
╚════════════════════════════════════════════════════════╝
'''
    print(banner)

def search_emails(domain):
    print("\n📧 Email Harvesting...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    query = f"@{domain}"
    url = f"https://www.google.com/search?q={quote_plus(query)}"
    try:
        res = requests.get(url, headers=headers)
        found = set(re.findall(r'[\w\.-]+@' + re.escape(domain), res.text))
        for email in found:
            print("   -", email)
    except Exception as e:
        print("Error:", e)

def search_subdomains(domain):
    print("\n🔍 Subdomain Enumeration...")
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        res = requests.get(url)
        if res.status_code == 200:
            entries = res.json()
            subs = sorted(set(entry['name_value'] for entry in entries))
            for sub in subs:
                print("   -", sub)
        else:
            print("Error fetching data.")
    except Exception as e:
        print("Error:", e)

def whois_lookup(domain):
    print("\n🌐 WHOIS Lookup...")
    try:
        result = os.popen(f"whois {domain}").read()
        print(result)
    except Exception as e:
        print("Error:", e)

def ip_geolocation(domain):
    print("\n📍 IP Geolocation...")
    try:
        ip = socket.gethostbyname(domain)
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()
        for key in ['query', 'country', 'regionName', 'city', 'isp']:
            print(f"   {key.title()}: {data.get(key, 'N/A')}")
    except Exception as e:
        print("Error:", e)

def dns_lookup(domain):
    print("\n📡 DNS Records...")
    try:
        result = os.popen(f"nslookup -type=any {domain}").read()
        print(result)
    except Exception as e:
        print("Error:", e)

def phone_lookup(phone):
    print("\n📞 Phone Number Lookup...")
    try:
        res = requests.get(f"https://api.apilayer.com/number_verification/validate?number={phone}",
                           headers={"apikey": "YOUR_API_KEY"})
        data = res.json()
        for key in ['number', 'valid', 'country_name', 'location', 'carrier', 'line_type']:
            print(f"   {key.title()}: {data.get(key, 'N/A')}")
    except Exception as e:
        print("Error:", e)

def metadata_extraction(file_path):
    print("\n🧾 File Metadata Extraction...")
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        meta = reader.metadata
        if meta:
            for key, val in meta.items():
                print(f"   {key}: {val}")
        else:
            print("   No metadata found.")
    except Exception as e:
        print("Error:", e)

def social_media_scrape(username):
    print("\n🔎 Social Media Enumeration...")
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://facebook.com/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "GitHub": f"https://github.com/{username}"
    }
    for platform, url in platforms.items():
        try:
            res = requests.get(url)
            if res.status_code == 200:
                print(f"   ✅ {platform}: {url}")
            else:
                print(f"   ❌ {platform}: Not Found")
        except Exception as e:
            print(f"   ❌ {platform}: Error")
def main():
    locked_screen()
    show_banner()

    if len(sys.argv) < 2:
        print("Usage: python royalharvester.py target.com [--phone=NUMBER] [--file=PDF_PATH] [--user=USERNAME]")
        return

    target = sys.argv[1]
    phone = None
    file = None
    username = None

    for arg in sys.argv[2:]:
        if arg.startswith("--phone="):
            phone = arg.split("=", 1)[1]
        elif arg.startswith("--file="):
            file = arg.split("=", 1)[1]
        elif arg.startswith("--user="):
            username = arg.split("=", 1)[1]

    search_emails(target)
    search_subdomains(target)
    whois_lookup(target)
    ip_geolocation(target)
    dns_lookup(target)

    if phone:
        phone_lookup(phone)
    if file:
        metadata_extraction(file)
    if username:
        social_media_scrape(username)

if __name__ == "__main__":
    main()


