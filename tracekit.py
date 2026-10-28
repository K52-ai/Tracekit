#!/usr/bin/env python3
import subprocess
import json
import sys
import os
import hashlib
import re

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def get_hashes(filepath):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha256.hexdigest()

def get_magic_bytes(filepath):
    with open(filepath, "rb") as f:
        return f.read(8).hex().upper()

def extract_strings(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    strings = re.findall(rb'[ -~]{6,}', data)
    return [s.decode('utf-8') for s in strings[:15]]

def analyze_file(filepath):
    if not os.path.exists(filepath):
        print(f"{Colors.RED}[-] Error: File not found!{Colors.ENDC}")
        return

    print(f"\n{Colors.CYAN}=== TraceKit v2.0 | by K52-ai ==={Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Target: {Colors.BOLD}{filepath}{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Extracting forensic data...{Colors.ENDC}\n")

    try:
        result = subprocess.run(['exiftool', '-j', filepath], capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)[0]

        md5_hash, sha256_hash = get_hashes(filepath)
        magic = get_magic_bytes(filepath)
        
        create_date = data.get('CreateDate') or data.get('DateTimeOriginal') or data.get('FileModifyDate') or "Unknown"
        software = data.get('Software') or data.get('Creator') or data.get('Producer') or "Unknown"
        device_make = data.get('Make', '')
        device_model = data.get('Model', '')
        device = f"{device_make} {device_model}".strip() if (device_make or device_model) else "Unknown"
        
        gps_lat = data.get('GPSLatitude')
        gps_lon = data.get('GPSLongitude')
        gps = f"{gps_lat}, {gps_lon}" if (gps_lat and gps_lon) else "No GPS Data"

        print(f"{Colors.CYAN}--------------------------------------------------{Colors.ENDC}")
        print(f"{Colors.BOLD} File Name    :{Colors.ENDC} {os.path.basename(filepath)}")
        print(f"{Colors.BOLD} File Size    :{Colors.ENDC} {data.get('FileSize', 'Unknown')}")
        print(f"{Colors.BOLD} File Type    :{Colors.ENDC} {data.get('FileType', 'Unknown')}")
        print(f"{Colors.BOLD} Magic Bytes  :{Colors.ENDC} {magic}")
        print(f"{Colors.CYAN}--------------------------------------------------{Colors.ENDC}")
        print(f"{Colors.BOLD} Creation Date:{Colors.ENDC} {Colors.GREEN}{create_date}{Colors.ENDC}")
        print(f"{Colors.BOLD} Software Used:{Colors.ENDC} {Colors.YELLOW}{software}{Colors.ENDC}")
        print(f"{Colors.BOLD} Device       :{Colors.ENDC} {Colors.YELLOW}{device}{Colors.ENDC}")
        print(f"{Colors.BOLD} GPS Location :{Colors.ENDC} {Colors.YELLOW}{gps}{Colors.ENDC}")
        print(f"{Colors.CYAN}--------------------------------------------------{Colors.ENDC}")
        print(f"{Colors.BOLD} MD5 Hash     :{Colors.ENDC} {md5_hash}")
        print(f"{Colors.BOLD} SHA256 Hash  :{Colors.ENDC} {sha256_hash}")
        print(f"{Colors.CYAN}--------------------------------------------------{Colors.ENDC}")
        
        print(f"{Colors.BOLD} Hidden Strings (First 15):{Colors.ENDC}")
        strings = extract_strings(filepath)
        for s in strings:
            print(f"  {Colors.CYAN}->{Colors.ENDC} {s[:80]}")
        
        print(f"{Colors.CYAN}--------------------------------------------------{Colors.ENDC}\n")

    except subprocess.CalledProcessError:
        print(f"{Colors.RED}[-] Error: ExifTool failed to process the file.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.RED}[-] Error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        try:
            path = input(f"{Colors.YELLOW}Enter file path: {Colors.ENDC}").strip()
            if path:
                path = path.strip("'\"")
                analyze_file(path)
        except KeyboardInterrupt:
            print("\nExiting...")
