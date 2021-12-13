# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

szam = int(input('Kérlek adj meg egy számot: '))
szam1 = int(input('Kérlek adj meg még egy számot: '))
szam2 = int(input('Kérlek adj meg még egy utolsó számot: '))


if szam < szam1 < szam2 :
  print('Első szám a legkisebb')

elif szam1 > szam > szam2 :
  print('Harmadik szám a legkisebb')

else:
  print('második szám a legkisebb')

