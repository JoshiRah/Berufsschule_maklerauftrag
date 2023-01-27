'''
(c) Joshua Rahmlow - Rheinische Gesellschaft für Diakonie gGmbH 2023
Program: BS LS5.3 - Maklerauftrag
Author: Joshua Rahmlow
'''

## Static ##

user_error = 'Fehler bei Datenaufnahme\n'
list_of_roomspace = []

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
        list_of_roomspace.append(r)

    else: ## if room is not rectengular ##
        list_of_room = [] ## create a list to calculate the not rectengular room ##

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
            list_of_room.append(r_log_rect) ## append the area of the logic rectengular to a list of this room ##

        list_of_roomspace.append(sum(list_of_room)) ## append the not-rectengular room to the flat ##

area = sum(list_of_roomspace) ## sum all rooms in the list/flat ##

if val_rooms != 0 and val_rooms >= 0:
    print("\n\nDie Wohnung ist ", area, "Quadratmeter groß.") ## print out the flats's area

elif val_rooms != 0 and val_rooms <= 0:
    print("\n\nEine negative Raumanzahl funktioniert nicht") ## print out the flats's area

else:
    print('\nDie Wohnung hat 0 Räume, somit keine Fläche.')