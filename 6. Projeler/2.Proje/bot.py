#pip3 install selenium
#pip3 install webdriver-manager


import io
import ai.prediction as yapayzeka
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


url = "http://aksoylu.space/kodlab/yorumolusturucu/"

browser.get(url)

yorumKutusu = browser.find_element_by_id("input_text")
yorumButton = browser.find_element_by_link_text("Yorum Gönder")


tip = input("Nasıl yorum istiyorsunuz (p/n)")
if tip == 'p':
    tip = 1
else:
    tip = 0

sayi = int(input("Yorum sayısı girin :"))
anahtarKelime = input("Anahtar kelime:")


for i in range(sayi):
    uretilenYorum = yapayzeka.yorum_uret(tip,anahtarKelime)
    yorumKutusu.send_keys(uretilenYorum)
    time.sleep(1)
    yorumButton.click()
    time.sleep(1)
    yorumKutusu.clear()
   
