import requests import re import time import sys import os import socket import json from urllib.parse import quote_plus

=== CONFIGURATION ===

ADMIN_NAME = "Lord Oblivion" ADMIN_PHONE = "+2348039420739" ADMIN_EMAIL = "anonymousoblivionj@gmail.com" VALID_KEYS = ["OBLIVION-2025-ACTIVE", "DARKMODE-KEY-999"]  # Add more valid keys here

=== ASCII BANNER ===

def show_banner(): os.system('clear' if os.name == 'posix' else 'cls') banner = ''' ╔════════════════════════════════════════════════════════╗ ║            O B L I V I O N   D A R K   T O O L         ║ ║                     [ G O D   M O D E ]                ║ ╚════════════════════════════════════════════════════════╝ ''' print(banner)

def locked_screen(): os.system('clear' if os.name == 'posix' else 'cls') print(""" ╔════════════════════════════════════════════════════════╗ ║        🔒 OBLIVION DARK TOOL - ACTIVATION REQUIRED 🔒     ║ ╠════════════════════════════════════════════════════════╣ ║   Contact Admin for Activation:                        ║ ║     👤 Name: {0: <44}║ ║     ☎ Phone: {1: <42}║ ║     📧 Email: {2: <42}║ ╚════════════════════════════════════════════════════════╝ """.format(ADMIN_NAME, ADMIN_PHONE, ADMIN_EMAIL))

key = input("\n🔑 Enter Activation Key: ").strip()
if key not in VALID_KEYS:
    print("\n❌ Invalid key. Exiting...")
    sys.exit()
print("\n✅ Activation successful! Launching Tool...\n")
time.sleep(2)

=== FUNCTIONS ===

def search_emails(domain): print("\n📧 Email Harvesting...") headers = {'User-Agent': 'Mozilla/5.0'} query = f"@{domain}" url = f"https://www.google.com/search?q={quote_plus(query)}" try: res = requests.get(url, headers=headers) found = set(re.findall(r'[\w.-]+@' + re.escape(domain), res.text)) for email in found: print("   -", email) except Exception as e: print("Error: ", e)

def search_subdomains(domain): print("\n🔍 Subdomain Enumeration...") try: url = f"https://crt.sh/?q=%25.{domain}&output=json" res = requests.get(url, timeout=10) if res.status_code == 200: data = res.json() subs = set(entry['name_value'] for entry in data) for sub in sorted(subs): print("   -", sub) except Exception as e: print("Error: ", e)

def whois_lookup(domain): print("\n🌐 WHOIS Lookup...") try: result = os.popen(f"whois {domain}").read() print(result) except Exception as e: print("Error: ", e)

def ip_geolocation(domain): print("\n📍 IP Geolocation...") try: ip = socket.gethostbyname(domain) print(f"IP: {ip}") res = requests.get(f"https://ipinfo.io/{ip}/json") data = res.json() for key, value in data.items(): print(f"{key.upper()}: {value}") except Exception as e: print("Error: ", e)

def dns_lookup(domain): print("\n📡 DNS Records...") try: result = os.popen(f"nslookup -type=any {domain}").read() print(result) except Exception as e: print("Error: ", e)

def phone_lookup(phone): print("\n📞 Phone Number Lookup...") try: res = requests.get(f"https://api.apilayer.com/number_verification/validate?number={phone}", headers={"apikey": "your_api_key"}) data = res.json() for k, v in data.items(): print(f"{k}: {v}") except Exception as e: print("Error: ", e)

def metadata_extraction(file_path): print("\n🧾 File Metadata Extraction...") try: from PyPDF2 import PdfReader reader = PdfReader(file_path) info = reader.metadata for k, v in info.items(): print(f"{k}: {v}") except Exception as e: print("Error: ", e)

def social_media_scrape(username): print("\n🔎 Social Media Enumeration...") platforms = { "Twitter": f"https://twitter.com/{username}", "Instagram": f"https://instagram.com/{username}", "Facebook": f"https://facebook.com/{username}", "LinkedIn": f"https://linkedin.com/in/{username}", "GitHub": f"https://github.com/{username}" } for name, url in platforms.items(): try: res = requests.get(url) if res.status_code == 200: print(f"✅ Found on {name}: {url}") else: print(f"❌ Not Found on {name}") except Exception: print(f"⚠️ Error checking {name}")

=== MAIN ===

def main(): locked_screen() show_banner()

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

if name == 'main': main()


