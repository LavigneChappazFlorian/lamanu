#exo1
#code = "Iholflwdwlrq#yrxv#dyh}#uhxvvl#d#ghfu|swhu#fh#phvvdjh#$#Pdlqwhqdqw#yrxv#srxyh}#sdvvhu#d#o*h{huflfh#vxlydqw1"
#resultat = ""
#for element in code : 
    #nb = ord(element)
    #nb = nb - 3
    #nb = chr(nb)
    #resultat = resultat + nb
#print(resultat)

#exo2 
msg = input(str("Ecris ton message ici : "))
caractere_non_ascii = []
for i in msg :
   if not (ord(i) <= 127) :
      caractere_non_ascii.append(hex(ord(i)))

print(caractere_non_ascii)