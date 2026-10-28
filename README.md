🚀 TRACEKIT v2.0

⚡ Advanced Digital Forensics & Metadata Extractor

TraceKit is a powerful forensic analysis tool written in Python. It is designed to extract hidden metadata, cryptographic hashes, magic bytes, and hidden strings from any file type (Images, PDFs, Videos, Documents). It acts as a digital x-ray for files, perfect for OSINT investigations, malware analysis, and digital forensics.

✨ Features

🛡️ **Deep Metadata Extraction:** Retrieves the true creation date, time, software used, and device information using `ExifTool`.
🧬 **Cryptographic Hashes:** Calculates MD5 and SHA256 hashes to verify file integrity and check for known malware.
🔍 **Hidden Strings Extraction:** Scans the binary code of the file to uncover hidden emails, passwords, URLs, and internal paths.
🔢 **Magic Bytes Identification:** Detects the true file type regardless of the file extension (e.g., identifying a hidden `.exe` renamed to `.jpg`).
📍 **GPS Coordinates:** Extracts geographical coordinates from images if they exist in the metadata.
🎨 **Clean & Colorful UI:** Outputs a professional, easy-to-read forensic report directly to the terminal.

📋 Requirements

🐧 Linux, macOS, or Windows
🐍 Python 3.8 or later
📦 ExifTool (Required for metadata extraction)

🛠️ Installation

Step 1 — Install system dependencies (ExifTool)
For Arch Linux:
    sudo pacman -S perl-image-exiftool

For Ubuntu/Debian:
    sudo apt install libimage-exiftool-perl

Step 2 — Clone the repository
    git clone https://github.com/K52-ai/TraceKit.git
    cd TraceKit

Step 3 — Make the script executable (optional)
    chmod +x tracekit.py

▶️ Usage

Step 1 — Run the tool without arguments (Interactive prompt)
    python3 tracekit.py

Step 2 — Enter the file path when prompted
    Enter file path: /path/to/your/file.pdf

Step 3 — Run the tool directly with a file path
    python3 tracekit.py /path/to/your/file.jpg

📝 How It Works

Step 1 — The tool calculates the MD5 and SHA256 hashes of the file to verify its integrity.
Step 2 — It reads the first 8 bytes to identify the "Magic Bytes" (the true file signature).
Step 3 — It runs `ExifTool` in the background to extract deep metadata (Creation Date, Software, Device, GPS).
Step 4 — It scans the raw binary data using regular expressions to extract human-readable strings (Emails, URLs, text).
Step 5 — It prints a formatted, colored report to the terminal.

📊 Results Output

The tool outputs a report divided into three sections:
1. **Basic Info:** File Name, Size, Type, Magic Bytes.
2. **Metadata:** Creation Date, Software Used, Device, GPS Location.
3. **Hashes & Strings:** MD5, SHA256, and the first 15 hidden strings found in the file.

🖼️ Screenshots

Add your actual screenshots to the assets/ folder, then reference them:

    ![TraceKit Output](assets/output.png)

⚠️ Important Notes

🛡️ Some software (like Telegram or WhatsApp) automatically strips metadata before saving files. In such cases, the tool will correctly report "Unknown".
🔍 Extracting strings from highly compressed or encrypted files may yield unreadable binary data.
⚡ The tool reads the entire file into memory for hashing. Not recommended for extremely large files (e.g., >2GB) on low-RAM systems.

⚖️ Responsible Use

Use TraceKit only on files you own or have explicit permission to analyze. Respect privacy and applicable laws.

📜 License

MIT License. See LICENSE for details.

👨‍💻 Author

K52-ai
🔗 GitHub Repository: https://github.com/K52-ai/TraceKit
