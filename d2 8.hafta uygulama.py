def censor_words(text, banned_words):
    censored_text = text

    for word in banned_words:
        censored_text = censored_text.replace(word, "***")

    return censored_text


text = """İsrail hapishanelerindeki filistinlilerin yaşadığı sıkıntılara 
ve diğer hak ihlallerine dikkat çekmek amacıyla her yıl 17 nisan'da gerçekleştirilen
"Filistin Esirler Günü" dolayısıyla Batı Şeria'nın Ramallah kentinde gösteriler 
düzenlendi. İsrail güçleri guruplara gaz bombalarıyla müdahale etti.
İsrail Hava kuvvetleriyse Han Yunus kentinin doğusundaki Huzaa beldesine
hava saldırısı düzenledi.
30 Mart 2026 tarihinde, İsrail hapishanelerindeki Filistinli mahkumların yaşam haklarını
ihlal eden yasa,İsrail Meclisi'nde onaylandı.
"""

banned_words = ["İsrail"]

new_text = censor_words(text, banned_words)

print(new_text)




"""
ödev sorusu:
censor_words adında bir fonksiyon yazın. Fonksiyon iki parametre alacak: 
text (string) ve banned_words (yasaklı kelimeler listesi).

Fonksiyon, metin içindeki yasaklı kelimeleri bularak yerlerine *** koymalı ve
sansürlenmiş yeni bir metin döndürmelidir. (Orijinal girdiler değiştirilmemelidir).

"""
