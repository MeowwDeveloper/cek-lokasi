import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
from bs4 import BeautifulSoup

def get_precise_location(lokasi):
    search_url = f"https://www.google.com/search?q={lokasi}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        if result:
            return result.text
        else:
            return "Lokasi detail tidak ditemukan"
    else:
        return "Gagal mengambil lokasi dari pencarian Google"

# input nomor telepon
nomor_hp = input("Masukkan nomor telepon (kode negara +62): ")
print("Melacak nomor...")

# parsing nomor telepon
nomor_parsed = phonenumbers.parse(nomor_hp, "ID")
zona_waktu = timezone.time_zones_for_number(nomor_parsed)
operator = carrier.name_for_number(nomor_parsed, "id")
lokasi_negara = geocoder.description_for_number(nomor_parsed, "id")

# mendapatkan lokasi lebih akurat
lokasi_lebih_akurat = get_precise_location(lokasi_negara)

# validasi nomor telepon
valid_nomor = phonenumbers.is_valid_number(nomor_parsed)
possible_nomor = phonenumbers.is_possible_number(nomor_parsed)

# menampilkan hasil
print(f"Zona Waktu: {', '.join(zona_waktu)}")
print(f"Operator: {operator}")
print(f"Lokasi (berdasarkan kode negara): {lokasi_negara}")
print(f"Lokasi lebih akurat: {lokasi_lebih_akurat}")
print(f"Valid Mobile Number: {valid_nomor}")
print(f"Checking Possibility of Number: {possible_nomor}")
