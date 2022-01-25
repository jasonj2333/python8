wyraz = input()
if wyraz.lower() == wyraz.lower()[::-1]:
    print('tak')
else:
   print(wyraz, wyraz.upper()[::-1], sep='')