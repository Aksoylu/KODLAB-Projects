## Ürünlere yorum yazan yapay zeka

Projelerle yapay zeka ve bilgisayarlı görü kitabının 6.bölümünün 3.projesi olarak geliştirilmiştir.

Proje İki ana bölümden oluşmaktadır :

1) Bir veri setinin tamamını analiz ederek yapay zekanın eğitilmesi ve model ağırlıklarının kaydedilmesini (eğitilmiş ağın kaydedilmesini) sağlayan program (Trainer)

- Bir LSTM yapay sinir ağı modeli oluşturulacaktır. 
- Oluşturulan model, eğitim parametreleri ve veri seti(ozitif veya negatif ürün yorumları) ile eğitilecektir. 
- Eğitim sonucu oluşan model ağırlıkları kayıt edilecektir.

2) Model ağırlıklarını belleğe yükleyerek istenen sayıda ve duyguda (pozitif veya negatif) yorum üreten program (Creator)

- Model ağırlıkları diskten okunarak çalışan model inşa edilecektir.
- Konsoldan aldığı komutlarla LSTM yapay sinir ağı yorumlar üretecektir. 

3) Arayüz ile etkileşim sağlayan program (Robot)

- Yapay zeka üreticisi tarafından üretilen yorum, bilgileri verilen bir web sitesine gönderilecektir.
- Telif hakkı ihlali olmaması açısı ile test amaçlı oluşturulmuş http://yz.aksoylu.space/test web sitesine gönderilecektir.
- Kodlar üzerinde değişiklik yapılarak sistemin e-pazar yeri sitelerine entegre olması sağlanılabilir.

