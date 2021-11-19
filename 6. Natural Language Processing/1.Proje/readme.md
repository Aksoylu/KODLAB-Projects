## Sahte ve gerçek haberleri ayırt eden yapay zeka

Projelerle yapay zeka ve bilgisayarlı görü kitabının 6.bölümünün 2.projesi olarak geliştirilmiştir.

Proje kapsamında yerel sunucuda (localhost) bir web sitesi çalışmaktadır.
Kullanıcılardan bu site üzerinden bir makale veya bir haber URL'i girmesi istenilir.

Girilen haber, yapay zeka tarafından analiz edilir. 

Analiz sonucu yine web site üzerinden kullanıcıya gösterilir.

Proje üç ana bölümden oluşmaktadır :

1) Web sunucusu : server.py

Kullanıcının arayüz olarak bir web sitesi ile sahte/doğru haberi ayırt etmesi amaçlanılmıştır. 
Bu nedenle Python'un web sunucu oluşturmaya olanak sağlayan "Flask" kütüphanesi tercih edilmiştir.



2) Eğitici : ai/trainer.py

Veri setini eğiterek yapay zeka modelinin diske kayıt edilmesini sağlayan programdır. Çalıştırıldığı andan itibaren eğitim işlemini başlatır ve çıktı olarak bir model dosyası üretir.

3) Sınıflandırıcı : ai/model.py

Model dosyasını kullanarak kendisine verilen inputu prediction işleminde kullanır (Doğru mu sahte haber mi analiz eder).
Sınıflandırıcı Flask'a gelen HTTP Request ile tetiklendiğinden analiz sonucu kullanıcıya web arayüzü üzerinden sunulur.