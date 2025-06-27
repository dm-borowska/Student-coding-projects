from turtle import *
import random

# mode("logo")  # ustawia tryb żółwia, że jest na środku ekranu, skierowany w górę
# reset()  # resetuje ustawienia systemu graficznego
# right(50)  # obraca się w prawo o x stopni
# left(5)  # obrót w lewo o x stopni
# width(1)  # ustawia grubość na x pikseli
# color("blue")  # ustawia kolor na x
# forward(150)  # idź na przód x pikseli
# done()  # jak narysuje to okienko graficzne ma nie znikać

WIDTH = 960
HEIGHT = 900
LEWY_DOLNY = (-WIDTH/2, -HEIGHT/2)
LICZBA_MUSZLI = 3
LICZBA_HOTELI = 2
LISTA_KOLOROW_MUSZLI = ["medium sea green", "orange", "orchid", "pink", "silver"]
LISTA_KOLOROW_HOTELU = ("blue", "brown", "green", "white")

def start():
    mode("logo")
    setup(width=WIDTH, height=HEIGHT)
    reset()
    speed(0)

def prostokat_wypelniony(x,y,kolor):
    color(kolor)
    fillcolor(kolor)
    begin_fill()
    for _ in range(2):
        forward(y)
        right(90)
        forward(x)
        right(90)
    end_fill()

def ocean():
    up()
    goto(LEWY_DOLNY)
    down()
    prostokat_wypelniony(WIDTH,4*HEIGHT/5, "sky blue")

def chmury():
    up()
    goto(LEWY_DOLNY)
    forward(4*HEIGHT/5)
    down()
    prostokat_wypelniony(WIDTH,HEIGHT/5, "grey")

def kapsula(szerokosc, wysokosc, liczba_okien, kolor):
    down()
    setheading(0) # zawsze żółw spojrzy do przodu
    polowa_wys = wysokosc /2
    szer_przez_l_okien = szerokosc/liczba_okien
    minimum = min(szer_przez_l_okien, wysokosc)
    promien = minimum/3
    setheading(90)
    fillcolor(kolor)
    for n in range(2):
        begin_fill()
        color(kolor)
        fd(szerokosc-(2*wysokosc/3))
        circle(wysokosc/3, 90, 1000)
        fd((wysokosc/3))
        circle(wysokosc/3, 90, 1000)
        end_fill()
    up()
    setheading(0)
    fd(polowa_wys)
    setheading(-90)
    fd(wysokosc/3)
    setheading(90)
    for x in range(liczba_okien):
        up()
        fd(szerokosc/(liczba_okien + 1))
        down()
        dot(promien, "cyan")
    up()
    fd(szerokosc / (liczba_okien + 1))
    # print("primien = ", promien)
    # print("liczba_okien= ", liczba_okien)
    # print("szer_przez_l_okien =", szer_przez_l_okien)
    # print("szerokosc = ", szerokosc)
    # print("wysokosc =", wysokosc)

def budowanie_pieter(szerokosc_kapsuly, wysokosc_kapsuly, parter, ile_pieter, liczba_okien):
    dlugosc_parteru = szerokosc_kapsuly * parter
    print(dlugosc_parteru)
    print(szerokosc_kapsuly)
    print(parter)
    up()
    setheading(270)
    fd(dlugosc_parteru)
    setheading(0)
    fd(wysokosc_kapsuly)
    setheading(90)
    polowa_szerokosci = szerokosc_kapsuly /2
    fd(polowa_szerokosci)
    szer_przez_l_okien = szerokosc_kapsuly / liczba_okien
    minimum = min(szer_przez_l_okien, wysokosc_kapsuly)
    promien = minimum/3
    setheading(-90)
    fd(promien)
    down()
    setheading(270)


def hotel(szerokosc_kapsuly, wysokosc_kapsuly, parter, ile_pieter, liczba_okien, kolor):
    szer_przez_l_okien = szerokosc_kapsuly/liczba_okien
    minimum = min(szer_przez_l_okien, wysokosc_kapsuly)
    promien = minimum/3
    for x in range(parter + 1):
        up()
        setheading(90)
        down()
        kapsula(szerokosc_kapsuly, wysokosc_kapsuly, liczba_okien, kolor)
        up()
        setheading(180)
        fd(wysokosc_kapsuly/2)
        setheading(90)
        fd(wysokosc_kapsuly/3)
        down()
    budowanie_pieter(szerokosc_kapsuly, wysokosc_kapsuly, parter, ile_pieter, liczba_okien)
    down()
    if ile_pieter == 1:
        return
    for y in range(parter):
        up()
        setheading(90)
        down()
        kapsula(szerokosc_kapsuly, wysokosc_kapsuly, liczba_okien, kolor)
        up()
        setheading(180)
        fd(wysokosc_kapsuly/2)
        setheading(90)
        fd(wysokosc_kapsuly/3)
        down()
    budowanie_pieter(szerokosc_kapsuly, wysokosc_kapsuly, parter, ile_pieter, liczba_okien)
    down()
    if ile_pieter == 2:
        return
    for z in range(parter - 1):
        up()
        setheading(90)
        down()
        kapsula(szerokosc_kapsuly, wysokosc_kapsuly, liczba_okien, kolor)
        up()
        setheading(180)
        fd(wysokosc_kapsuly/2)
        setheading(90)
        fd(wysokosc_kapsuly/3)
        down()
    budowanie_pieter(szerokosc_kapsuly, wysokosc_kapsuly, parter, ile_pieter, liczba_okien)
    down()

"""
Muszla z 4 obrotami po 5 segmentów każdy i początkową długością odcinka równą 100. 
Siatka złożona z kwadratów, kąt obrotu po każdym odcinku jest tak dobrany, 
by narysowanie wszystkich segmentów jednego obrotu wracało do początkowego kierunku żółwia. 
Przyrost długości boku wynosi czwartą część początkowej długości (czyli tu 25). Uwaga: 
wypełnianie kolejnych segmentów kolorem wymaga pamiętania położenia poprzednich odcinków (współrzędnych ich końców). 
Jaka struktura danych jest tu potrzebna? Przy pierwszym obrocie należy zakładać, 
że poprzedni (fikcyjny) obrót miał wszystkie końce odcinków w punkcie będącym środkiem muszli.  
Pisanie tej części programu należy zacząć od rysowania samego kształtu muszli. Wypełnianie kolorami należy zostawić na drugi etap.
"""
def muszla(dlugosc, segment, obrot, kolor):
    x = dlugosc
    setheading(0)
    color("black")
    czwarta_czesc = x/4
    alfa = 360/segment
    droga = []
    fillcolor(kolor)
    begin_fill()
    for k in range(obrot*segment):
        pozycja = pos()
        droga.append(pozycja)
        if (2 < len(droga) <= segment):
            color("orange")
            goto(droga[0])
            fillcolor(kolor)
            end_fill()
            begin_fill()
            goto(droga[-1])
            color("black")
        if(len(droga) > segment):
            color("orange")
            goto(droga[-segment - 1])
            fillcolor(kolor)
            end_fill()
            begin_fill()
            goto(droga[-1])
            color("black")
        color("black")
        fd(x)
        lt(alfa)
        x = x + czwarta_czesc
    punkt = droga[-segment]
    color(kolor)
    goto(punkt)
    fillcolor(kolor)
    end_fill()
    setheading(0)
    up()
    goto(droga[0])
    down()
    x = dlugosc
    for k in range(obrot * segment):
        color("black")
        fd(x)
        lt(alfa)
        x = x + czwarta_czesc

def main():
    start()
    speed(0)
    ocean()
    chmury()
    up()
    goto(0,0)
    down()
    for i in range(LICZBA_MUSZLI):
        x = random.randint(0, WIDTH)
        y = random.randint(0, int((4*HEIGHT)/5))
        up()
        goto(LEWY_DOLNY)
        setheading(0)
        fd(y)
        rt(90)
        fd(x)
        dlugosc = random.randint(4,7)
        segment = random.randint(5,9)
        obrot = random.randint(1, 4)
        kolor = random.choice(LISTA_KOLOROW_MUSZLI)
        down()
        muszla(dlugosc,segment, obrot, kolor)

    for z in range(LICZBA_HOTELI + 1):
        up()
        x = random.randint(-400, 400)
        y = random.randint(-480, -240)
        goto(x, y)
        szerokosc = random.randint(40, 90)
        polowa_szer = int(szerokosc / 2)
        wysokosc = random.randint(polowa_szer, szerokosc)
        parter = random.randint(1, 5)
        ile_pieter = random.randint(1, parter)
        liczba_okien = random.randint(1, 5)
        down()
        kolor_hotelu = random.choice(LISTA_KOLOROW_HOTELU)
        hotel(szerokosc, wysokosc, parter, ile_pieter, liczba_okien, kolor_hotelu)

    done()

main()

