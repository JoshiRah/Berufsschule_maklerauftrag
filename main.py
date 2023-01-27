'''
(c) Joshua Rahmlow - Rheinische Gesellschaft für Diakonie gGmbH 2023
Program: BS LS5.3 - Maklerauftrag
Author: Joshua Rahmlow
'''

## Static ##

user_error = 'Fehler bei Datenaufnahme\n'
liste_der_raumflaechen = []

## System ##

while True:
    try:
        val_rooms = int(input("Anzahl der Räume: ")) ## get the value of rooms in the flat ##
        break
    except:
        print(user_error)

for i in range(val_rooms):
    print("\nRaum Nr. ", i+1, ":")

    if input("\nIst der Raum rechteckig? (y/n) ") == "y": ## room rectengular? ##
        while True:
            try:
                lengh = float(input("Länge: "))
                break
            except:
                print(user_error)
        while True:
            try:
                width = float(input("Breite: "))
                break
            except:
                print(user_error)
        r = lengh * width
        liste_der_raumflaechen.append(r)

    else: ## if room is not rectengular ##
        liste_des_raumes = [] ## create a list to calculate the not rectengular room ##

        while True:
            try:
                log_rect = int(input("\nIn wie viele logische Rechtecke soll der Raum eingeteilt werden? ")) ##
                break
            except:
                print(user_error)

        for l in range(log_rect): ## calculate the log rectengulars ##
            print("\nBerechnung des ", l+1, ". logischen Rechtecks")
            while True:
                try:
                    len_log_rect = float(input("Länge: "))
                    break
                except:
                    print(user_error)
            while True:
                try:
                    witdh_log_rect = float(input("Breite: "))
                    break
                except:
                    print(user_error)

            r_log_rect = len_log_rect * witdh_log_rect ## calculate the area logic rectengular ##
            liste_des_raumes.append(r_log_rect) ## append the area of the logic rectengular to a list of this room ##

        liste_der_raumflaechen.append(sum(liste_des_raumes)) ## append the not-rectengular room to the flat ##

area = sum(liste_der_raumflaechen) ## sum all rooms in the list/flat ##

if val_rooms != 0:
    print("\n\nDie Wohnung ist ", area, "Quadratmeter groß.") ## print out the flats's area
else:
    print('\nDie Wohnung hat 0 Räume, somit keine Fläche.')