md = {
    "Aura":"saygınlık seviyesi",
    "instalock":"oyuna girdiğin anda başkalarının isteğine bakmazsızın karakter seçmek",
    "JK":"sadece saka demek"
    }
kelime=input("kelimeniz?")
if kelime in md.keys():
    print(md[kelime])
else:
    print("elimizde yok")
