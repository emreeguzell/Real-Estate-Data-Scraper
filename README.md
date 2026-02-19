This project is a high-performance web scraping tool designed to extract real estate listings from Sahibinden.com and export them directly into a structured Excel file. It is built using Python, SeleniumBase, and Openpyxl.

🇹🇷 Türkçe Proje Özeti
Bu araç, Sahibinden.com üzerindeki emlak ilanlarını otomatik olarak çekmek ve bir Excel dosyasına kaydetmek için geliştirilmiştir. SeleniumBase'in gelişmiş "undetected" modunu kullanarak bot korumalarını aşar ve verileri düzenli bir tablo haline getirir.

✨ Key Features (Özellikler)

Anti-Bot Bypass: Uses SeleniumBase with undetected-mode to navigate through Cloudflare and other bot-detection systems.

Session Persistence: Supports user_data_dir to save browser cookies and sessions, minimizing the need for repetitive manual verification.

Smart Waiting: Implements advanced wait conditions to ensure elements are loaded before interaction.

OOP Design: Utilizes a clean Emlak class structure to handle and organize listing data efficiently.

Excel Integration: Automatically generates an .xlsx file with detailed headers (Listing Title, m², Room Count, Price, Date, and Location).

🛠️ Requirements (Gereksinimler)

Python 3.x

SeleniumBase

Openpyxl

🚀 Installation & Usage (Kurulum ve Kullanım)

Clone the repository:

Bash
git clone https://github.com/yourusername/sahibindenscraping.git
cd sahibindenscraping
Install dependencies:

Bash
pip install seleniumbase openpyxl
Run the script:

Bash
python main.py
How it works:

The browser will launch and navigate to the site.

If a Cloudflare verification screen appears, solve it manually and press ENTER in the terminal.

Enter your search query (e.g., "Kadıköy Satılık Daire") when prompted.

The results will be gathered and saved to İlanlar.xlsx in the project folder.

📂 Project Structure (Proje Yapısı)
main.py: The core automation logic and data extraction.

⚠️ Disclaimer (Yasal Uyarı)
This project is intended for educational and personal use only. Scraping websites may violate their Terms of Service. The developer is not responsible for any misuse of this tool or potential legal consequences. Always respect the site's robots.txt and legal policies.
