import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(height=300,width=1000,bg='white') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

zoznam=[] #vytvorím si zoznam

subor=open('zastavba_na_ulici.txt','r') #otvorim si daný súbor a môžem s neho čítať 

for riadok in subor: #for cyklus, ktorým si prechádzam riadky v danom súbore
    zoznam.append(riadok.strip()) #ukladám si každý riadok súboru do zoznamu
 
x=10 #nastavím si premennú x na 10
y=200 #nastavím si premennú y na 200
for j in zoznam: #for cyklus, ktorým si prechádzam čísla v zozname 
    pom = j.split() #čísla zo zoznamu si ukladám do pomocnej premennej pom
    sirka = str(pom[0]) #do premennej sirka si ukladám šírku budovy
    vyska = str(pom[1]) #do premennej vyska si ukladám výšku budovy
    if int(vyska)==0: #podmienka, ktorou kontrolujem či mám voľný pozemok alebo tam má byť budova
        canvas.create_rectangle(x,y,x+int(sirka),y-int(vyska),outline='green',width=2) #vykreslujem miesto voľného pozemku
        x=x+int(sirka) #premennú x si zväčšujem o šírku budovy, aby som mohol vykresliť ďalšiu budovu alebo voľný pozemok
    else: #ak nie je splnená podmienka
        canvas.create_rectangle(x,y,x+int(sirka),y-int(vyska),fill='grey') #vykreslujem si budovy
        x=x+int(sirka) #premennú x si zväčšujem o šírku budovy, aby som mohol vykresliť ďalšiu budovu alebo voľný pozemok

x1=10 #nastavím si premennú x1 na 10
y1=200 #nastavím si premennú y1 na 200
def vykresli(): #funkcia, ktorá vykresluje budovy s čiarami v rozdiele výšky
    global x1,y1 #premenné x1,y1 si nastavím na globálne
    rozdiel=entry1.get() #do premennej rozdiel uložím číslo rozdielu vo výške medzi budovami
    for j in zoznam: #for cyklus, ktorým si prechádzam čísla v zozname 
        pom = j.split() #čísla zo zoznamu si ukladám do pomocnej premennej pom
        sirka = str(pom[0]) #do premennej sirka si ukladám šírku budovy
        vyska = str(pom[1]) #do premennej vyska si ukladám výšku budovy
        if int(vyska)==0: #podmienka, ktorou kontrolujem či mám voľný pozemok alebo tam má byť budova
            canvas.create_rectangle(x1,y1,x1+int(sirka),y1-int(vyska),outline='green',width=2) #vykreslujem miesto voľného pozemku
            x1=x1+int(sirka) #premennú x si zväčšujem o šírku budovy, aby som mohol vykresliť ďalšiu budovu alebo voľný pozemok
        else:
            canvas.create_rectangle(x1,y1,x1+int(sirka),y1-int(vyska),fill='grey') #vykreslujem si budovy
            x1=x1+int(sirka) #premennú x si zväčšujem o šírku budovy, aby som mohol vykresliť ďalšiu budovu alebo voľný pozemok
            canvas.create_line(210,190,210,170-int(rozdiel),fill='red',width=2) #
            canvas.create_line(380,160,380,130-int(rozdiel),fill='red',width=2)  # dočasné riešenie vykreslenia čiar ešte treba dokončiť a prerobiť
            canvas.create_line(420,170,420,130-int(rozdiel),fill='red',width=2) #

subor.close() #zavriem súbor
 
entry1 = tkinter.Entry() # pripravím si vstup
entry1.pack()            # vytvorím si vstup

button1 = tkinter.Button(text='vykresli',command=vykresli) #pripravím si tlačítko, ktoré bude označené daným textom a keď ho stlačím zavolám danú funkciu
button1.pack() #vytvorím si tlačítko