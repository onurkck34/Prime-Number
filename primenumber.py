sayi = int(input("Enter a Number : "))
asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break
if asalMi:  
    print("PRIME")
else:
    print("NOT PRIME")
