#Liður 1
loop = True
while loop:
    val = int(input("veldu tölu = "))
    if val % 5 == 0:
        print("talan er í 5* töflunni")
    else:
        print("talan er ekki í 5* töflunni")
    reset = input("viltu keyra forritið aftur? [Y/N] "). upper()
    if reset == "Y":
        continue
    else:
        loop = False
    
    