from versenytavok import *

beolvas('bukkm2019.txt')

print(f'4. feladat: Versenytávot nem teljesítők: {celba_nem_erkezok_aranya()}%')
#print(f'4. feladat: Versenytávot nem teljesítők: {celba_nem_erkezok_aranya():.2f}%')

print(f'5. feladat: Női versenyzők száma a rövidtávú versenyen: {versenyzok_szama("Rövid","Nő")}fő')
# print(f'5. feladat: Férfi versenyzők száma a hosszú távú versenyen: {versenyzok_szama("Hosszú","Férfi")} fő')

if volt_tobb_mint(6*60*60): # 6 óránál volt-e több
    print('6. feladat: Volt ilyen versenyző')
else:
    print('6. feladat: Nem volt ilyen versenyző')

print('7. feladat: A felnőtt férfi (ff) kategória győztese rövid távon')
print(f'\tRajtszám: {gyoztes("Rövid","ff").rajtszam}')
print(f'\tNév: {gyoztes("Rövid","ff").nev}')
print(f'\tEgyesület: {gyoztes("Rövid","ff").egyesulet}')
print(f'\tIdő: {gyoztes("Rövid","ff").ido}')
