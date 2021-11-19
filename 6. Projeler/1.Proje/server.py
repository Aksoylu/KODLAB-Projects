from flask import Flask, render_template, request
import ai.prediction as yapayZeka
import os
# başka bir URL den veri çekmek için gerekli kütüphaneler

# pip3 install 
# pip3 install 
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('root.html')

@app.route("/analiz", methods=['POST'])
def analizEt():
    if request.method == 'POST':
        tip = request.form.get('tip')
        veri = request.form.get('veri')
        if tip == "metin":
            tahminSonuc = yapayZeka.tahminEt(veri)
            if tahminSonuc == True:
                return "<font color='gren'>Bu haber yapay zeka tarafından <b>doğru</b> olarak tahmin edilmiştir. </font>"
            else:
                return "<font color='red'>Bu haber yapay zeka tarafından <b>sahte</b> olarak tahmin edilmiştir. </font>"
        
        if tip == "link":
            # linki çek
            headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
            r = requests.get(veri, headers=headersparam)
            soup = BeautifulSoup(r.content, "html", from_encoding='UTF-8')
            #span = soup.find_all("span")
            p = soup.find_all("p")

            metin = ""
            # Burada sayfadaki ilk 4 paragrafı alıyoruz. Bunu yapmamızdaki amaç özet veri üzerinde çalışmak.
            # Zira geliştirdiğimiz sinir ağı ve sayısal istatistik içeren haberlerin daha fazla doğruluk oranına sahip olduğuna
            # Kanaat verebilir. Bu bir yanılgı olacaktır. Bunu engellemek için bir özet çıkarıyoruz.
            index = 0
            for i in p:
                metin = metin + i.text
                index = index + 1
                if index >= 3:
                    break
            tahminSonuc = yapayZeka.tahminEt(metin)
            
            if tahminSonuc == True:
                return metin + "<br><font color='gren'>Bu haber yapay zeka tarafından <b>doğru</b> olarak tahmin edilmiştir. </font>"
            else:
                return metin +"<br><font color='red'>Bu haber yapay zeka tarafından <b>sahte</b> olarak tahmin edilmiştir. </font>"
            return metin

    else:
        return "Bir hata oluştu"


if __name__ == "__main__":
    app.run()
    