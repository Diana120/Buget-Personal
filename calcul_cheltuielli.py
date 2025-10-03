import csv
import pandas as pd



buget_alocat = float(input("Buget Initial= "))
siguranta_procent=float(buget_alocat*0.2)
investitii_procent=float(buget_alocat*0.2)
necesar_procent=float(buget_alocat*0.4)
distractii_procent=float(buget_alocat*0.1)
invatare_procent=float(buget_alocat*0.1)


with open('buget.csv', 'w', newline='') as buget_initial:
    b=csv.writer(buget_initial)
    b.writerow(['Buget initial =', buget_alocat, 'lei'])
    b.writerow(['Categorie repartizare buget', 'Procent din buget initial'])
    b.writerow(['Buget investitii', '20%'])
    b.writerow(['Buget siguranta', '20%'])
    b.writerow(['Buget mancare si utilitati', '40%'])
    b.writerow(['Buget distractii', '10%'])
    b.writerow(['Buget invatare', '10%'])

with open('buget_investitii.csv', 'w', newline='') as investitii:
    i=csv.writer(investitii)
    i.writerow(['Categorie', 'Total buget aloca'])
    i.writerow(['Buget investitii', investitii_procent ])

with open ('buget_siguranta.csv', 'w', newline='') as siguranta:
    s=csv.writer(siguranta)
    s.writerow(['Categorie', 'Total buget alocat'])
    s.writerow(['Buget siguranta', siguranta_procent])

with open('buget_mancare_utilitati.csv', 'w', newline='') as necesar:
    n=csv.writer(necesar)
    n.writerow(['Buget Categorie', 'Total buget alocat'])
    n.writerow(['Buget mancare-utilitati', necesar_procent])
    n.writerow([])
    n.writerow(['Categorie produs', 'Pret (lei)'])
   
with open('buget_mancare_utilitati.csv', 'a', newline='') as necesar:
    p=csv.writer(necesar)
    p.writerow(['Banane', 7])
    p.writerow(['Apa', 12])
    p.writerow(['Paine', 7])
    p.writerow(['plata lumna', 200])
    p.writerow(['plata apa', 200])

buget_citire=pd.read_csv('buget_mancare_utilitati.csv', skiprows=3)
print(buget_citire)

total=buget_citire['Pret (lei)'].sum() #Totalul sumei chletuite
print(total)

limita=float(necesar_procent*0.9) # daca s-a cheltuit mai mult de 90% mesaj de atentionare
if total>=limita:
    print('Esti la limita')

with open('buget_mancare_utilitati.csv', 'a', newline='') as necesar:
    add=csv.writer(necesar)
    add.writerow([])
    add.writerow(['Total Cheltuieli', total])

# Buget distractii
limita_distractii= float(distractii_procent*0.9)
with open('buget_distractii.csv', 'w', newline='') as enjoy:
    joy=csv.writer(enjoy)
    joy.writerow(['Buget Categorie', 'Total buget alocat'])
    joy.writerow(['Buget mancare-utilitati', distractii_procent])
    joy.writerow(['Cheltuieli', 'Pret (lei)'])
with open('buget_distractii.csv', 'a', newline='') as enjoy:
    j=csv.writer(enjoy)
    j.writerow(['Vacanta', 5000])
    j.writerow(['Petrecere', 600])
    j.writerow(['Inghetata', 10])  

joy_citire=pd.read_csv('buget_distractii.csv', skiprows=2) 
print(joy_citire)

total_distractii=float(joy_citire['Pret (lei)'].sum())
print(total_distractii)

if total_distractii>limita_distractii:
    print('Hei! Ia-o mai usor.')

with open('buget_distractii.csv', 'a', newline='') as enjoy:
    joy=csv.writer(enjoy)
    joy.writerow([])
    joy.writerow(['Total cheltuieli', total_distractii])

# Buget invatare
limita_invatare=float(invatare_procent*0.9)
with open('buget_invatare.csv', 'w', newline='') as growth:
    g=csv.writer(growth)
    g.writerow(['Buget Categorie', 'Total buget alocat'])
    g.writerow(['Buget mancare-utilitati', invatare_procent])
    g.writerow(['Cheltuieli', 'Pret (lei)'])
with open('buget_invatare.csv', 'a', newline='') as growth:
    g=csv.writer(growth)
    g.writerow(['Carte', 40])
    g.writerow(['Carte', 30])
    g.writerow(['Curs', 300])

growth_citire=pd.read_csv('buget_invatare.csv', skiprows=2)
print(growth_citire)

total_growth=float(growth_citire['Pret (lei)'].sum())
print(total_growth)

if total_growth > limita_invatare:
    print('Hei! Asteapta pana mai adaugi niste bani. <3')

with open('buget_invatare.csv', 'a', newline='') as growth:
    g=csv.writer(growth)
    g.writerow([])
    g.writerow(['Total cheltuieli: ', total_growth ])






    
    





