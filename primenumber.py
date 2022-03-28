sayi = int(input("Sayi Giriniz : "))
asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break
if asalMi:  #default ayari true oldugu icin == True yazmaya gerek yok 
    print("ASAL")
else:
    print("ASAL DEGIL")