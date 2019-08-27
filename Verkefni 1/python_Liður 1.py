#Liður 1
afangi = input("afgangi = ")
nafn = input("Nafn = ")

print ("Velkomin í áfangann " + afangi + " þetta verður skemmtileg önn hjá okkur " + nafn)

#Liður 2
print(" Skrifaðu tölu hærri en 100 ")
tala = int(input("tala = "))
if tala > 100:
    print(tala/5.5)
else:
    print("invalid number")

#Forritið biður notanda að slá inn tölu hærri en 100 og deilir síðan í hana með 5.5 og birtir svarið með 2 aukastöfum

#Liður 3
print( "Skrifaðu tvær heiltölur" )
tala1 = int(input( "tala1 = " ))
tala2 = int(input( "tala2 = " ))
print( tala1 * tala2 )
print( tala2 - tala1 )

#Forritið biður um tvær heiltölur, það á síðan að margfalda þessar tvær tölur saman og birta útkomuna á skjáinn.  
#Svo á forritið að draga fyrri töluna sem sleginn var inn frá þeirri seinni og skrifa þá útkomu á skjáinn. 

#liður 4
print( "hvað eru hliðarlengdirnar á kassanum" )
hlið1 = float(input("Hlið_L = "))
hlið2 = float(input("Hlið_B = "))
hlið3 = float(input("Hlið_H = "))
print( "svarið er " + str(hlið1 * hlið2 * hlið3))

#Forritið tekur inn 3 hliðarlengdir á kassa (heiltölur) og skilar rúmmáli kassans til notandans. Formúlan er: Rúmmál = hæð * lengd * breidd.