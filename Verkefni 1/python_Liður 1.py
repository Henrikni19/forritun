#Liður 1
afangi = input("Í hvaða áfanga ert þú í = ")
nafn = input("Hvað er nafnið þitt = ")

print ("Velkomin í áfangann " + afangi + " þetta verður skemmtileg önn hjá okkur " + nafn)

#Liður 2
print(" Skrifaðu tölu hærri en 100 sem verður deilt í 5.5 ")
tala = int(input("tala = ") or 100)

if tala > 100:
    print (round(tala/5.5,2))
else:
    print("invalid number")

#Liður 3
print( "Skrifaðu tvær heiltölur sem munu margfaldast og tekið tölu1 frá tölu2" )
tala1 = int(input( "tala1 = " ) or 1)
tala2 = int(input( "tala2 = " ) or 1)
print( tala1 * tala2 )
print( tala2 - tala1 )

#liður 4
print( "Hvað eru hliðarlengdirnar á kassanum" )
hlið1 = float(input("Hlið_L = ") or 1)
hlið2 = float(input("Hlið_B = ") or 1)
hlið3 = float(input("Hlið_H = ") or 1)
print( "svarið er " + str(hlið1 * hlið2 * hlið3))

#Liður 5
print("Hér finnum við út hvað faðir þinn var gamall þegar þú fæddist, skrifaðu aldurinn þinn og faðir þíns")
kid = int(input("Aldurinn þinn = "))
dad = int(input("Aldur faðirins = "))
print("Faðir þinn var " + str(dad - kid) + " ára þegar þú fæddist")

#Liður 6
print("Hér ætlum við að finna út meðaltal á 3 einstaklingum")
person1 = int(input("Einstaklingur_1 = "))
person2 = int(input("Einstaklingur_2 = "))
person3 = int(input("Einstaklingur_3 = "))
print ("Meðaltal aldurs þeirra er " + str((person1 + person2 + person3) / 3))

print("Gaman að geta aðstoðað þig við þessa útreikninga " + nafn)