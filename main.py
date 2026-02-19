from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
import undetected_chromedriver as uc # Yeni kütüphanemiz eklendi
from seleniumbase import Driver
from seleniumbase import SB

class emlak:
    def __init__(self, row):
        elemanlar = row.find_elements(By.TAG_NAME , "td")
        self.ilan = elemanlar[1].text
        self.m2 = elemanlar[2].text
        self.oda = elemanlar[3].text
        self.fiyat = elemanlar[4].text
        self.ilan_tarihi = elemanlar[5].text
        self.semt = elemanlar[6].text

print("Hosgeldiniz, tarayıcı başlatılıyor (Bot koruması atlatılıyor)...")

driver = Driver(uc=True)
wait = WebDriverWait(driver, 30)

url = "https://www.sahibinden.com/"
driver.get(url)

# ... sb.open("https://www.sahibinden.com/") satırından hemen sonra:

print("Site kontrol ediliyor...")
try:
            # Sitede arama kutusunu 4 saniye boyunca bulmaya çalış
            SB.wait_for_element_visible('//*[@id="searchText"]', timeout=4)
            print("✅ Profil tanındı! Güvenlik doğrulaması çıkmadı, otomatik devam ediliyor...")
            
except Exception:
            # 4 saniye içinde arama kutusu çıkmadıysa, demek ki Cloudflare ekranındayız
            print("\n" + "="*55)
            print("⚠️ DİKKAT: Güvenlik doğrulaması (Cloudflare) tespit edildi!")
            print("Lütfen farenizle kutucuğu manuel olarak işaretleyin.")
            input("Site SİZİN ONAYINIZLA yüklendikten sonra ENTER'a basın: ")
            print("="*55 + "\n")

        # --- Buradan sonra normal arama sorma kısmına geçer ---

try:
    arama_kutusu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchText"]')))
    arama = input("İstediğiniz aramayı yapınız (Örn: Kadıköy Satılık): ")
    arama_kutusu.send_keys(arama + Keys.ENTER)
except Exception as e:
    print(f"Arama kutusu bulunamadı veya hata oluştu: {e}")

# Sayfanın ve sonuçların yüklenmesi için bekleme
time.sleep(5)

# --- Excel Kayıt Kısmı ---
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "İlanlar"
ws.append(["İlan", "M2", "Oda", "Fiyat", "Tarih", "Semt"])

try:
    # Arama sonuçları listesinin gelmesini bekle
    ilan_ozellikleri = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    print(f"Toplam {len(ilan_ozellikleri)} satır bulundu. Veriler çekiliyor...")
    
    for row in ilan_ozellikleri:
        try:
            veri = emlak(row)
            ws.append([veri.ilan, veri.m2, veri.oda, veri.fiyat, veri.ilan_tarihi, veri.semt])
        except Exception:
            # Sitedeki reklam veya boş satırları atlamak için
            pass

    wb.save("İlanlar.xlsx")
    print("İşlem tamamlandı, veriler excele kaydedildi.")

except Exception as e:
    print(f"Veri çekilirken hata oluştu: {e}")

finally:
    # İşlem bitince tarayıcıyı kapatmak isterseniz bu satırı açın
    # driver.quit()
    pass