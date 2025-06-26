import os

# Funkcja sprawdza, czy dwa pliki mają taką samą zawartość.
def czy_ta_sama_zawartosc(plik1, plik2):
    rozmiar1 = os.path.getsize(plik1) # "mierzenie" rozmiaru pliku
    rozmiar2 = os.path.getsize(plik2)
    if rozmiar1 != rozmiar2:
        return False

    with open(plik1, 'r', encoding='utf-8') as file1, open(plik2, 'r', encoding='utf-8') as file2: # otwieranie plików jako file1 i file2
        linie1 = file1.readlines() # wczytywanie po linii
        linie2 = file2.readlines()

    if len(linie1) != len(linie2): # jeśli mają różną długość to są różne
        return False

    for l1, l2 in zip(linie1, linie2): # porównywanie linijek
        if l1 != l2:
            return False

    return True

# Funkcja buduje słownik, gdzie kluczem jest rozmiar pliku, a wartością lista plików o tym rozmiarze.
def budowa_slownika(katalog):
    slownik = {} # stworzenie słownika
    liczba_katalogow = 0
    liczba_plikow = 0

    for dirpath, _, filenames in os.walk(katalog): # przechodzenie przez katalog i podkatalogi
        liczba_katalogow += 1 # zwiększ licznik katalogów o 1 dla każdego przetwarzanego katalogu
        for filename in filenames:
            filepath = os.path.join(dirpath, filename) # uzyskanie pełnej ścieżki do pliku
            filesize = os.path.getsize(filepath) # uzyskanie rozmiaru pliku w bajtach
            if filesize in slownik: # sprawdzenie, czy rozmiar pliku jest już kluczem w słowniku
                slownik[filesize].append(filepath) # jeśli tak, dodaj ścieżkę pliku do listy
            else:
                slownik[filesize] = [filepath]  # jeśli nie, utwórz nowy wpis w słowniku z rozmiarem pliku jako kluczem i listą z jednym elementem (ścieżką pliku)
            liczba_plikow += 1 # zwiększ licznik plików o 1 dla każdego przetwarzanego pliku

    return slownik, liczba_katalogow, liczba_plikow


# Funkcja grupuje pliki o tej samej zawartości.
def grupuj_duplikaty(slownik):

    grupy = []
    for file_list in slownik.values(): # pętla po listach ścieżek plików w słowniku
        while file_list: # dopóki lista ścieżek plików nie jest pusta
            plik = file_list.pop(0) # usuń pierwszy element z listy i przypisz go do zmiennej 'plik'
            grupa = [plik]
            for inny_plik in file_list[:]:
                if czy_ta_sama_zawartosc(plik, inny_plik):
                    grupa.append(inny_plik)
                    file_list.remove(inny_plik)
            if len(grupa) > 1: # jeśli grupa zawiera duplikaty
                grupy.append(grupa)
    return grupy


def main():
    katalog = "katalog_testowy"
    print(f"Katalog bieżący: {os.getcwd()}") #wypisywanie na ekran
    print(f"Zaczynam analizę katalogu {katalog}")

    slownik, liczba_katalogow, liczba_plikow = budowa_slownika(katalog) # utworzenie słownika plików oraz zliczenie katalogów i plików
    grupy = grupuj_duplikaty(slownik) # grupy duplikatów plików na podstawie słownika

    print(f"Liczba przeanalizowanych katalogów: {liczba_katalogow}, liczba plików: {liczba_plikow}.")

    for grupa in grupy:
        rozmiar = os.path.getsize(grupa[0])
        print(f" rozm. pliku {rozmiar}, l. plików {len(grupa)}: {', '.join(grupa)},") # informacje o grupach duplikatów

    liczba_grup_duplikatow = len(grupy) # liczenie liczby grup duplikatów

    liczba_duplikatow = 0
    for grupa in grupy:
        for i in range(len(grupa)-1): # liczenie duplikatów
            liczba_duplikatow += 1

    calkowity_rozmiar = 0
    for grupa in grupy:
        for i in range(len(grupa) - 1):
            calkowity_rozmiar += os.path.getsize(grupa[i]) # liczenie całkowitego rozmiaru duplikatów

    print(f"Liczba grup duplikatów: {liczba_grup_duplikatow}, liczba duplikatów plików: {liczba_duplikatow} o łącznym rozmiarze {calkowity_rozmiar} bajtów.")


main()