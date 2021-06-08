import secrets
pw = ""
# Alle Variablen initialisieren!!!
gross = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klein = "abcdefghijklmnopqrstuvwxyz"
sonderzeichen = "!""#""$%&'()*+,-./:;<=>?@{|}~"
zahlen = "123456789"
# Den Nutzer die verschieden Funktionen zur verfügung stellen!
laenge = int(input("Willkommen im Passwortgenerator!"
                "\nBitte gebe die Passwortlänge ein!: "))
frage = input(
    "Möchtest du Großbuchstaben,Kleinbuchstaben,Zahlen und Sonderzeichen ,dann drücke die 1.,"
    "\nwenn du Kleinbuchstaben, Zahlen und Sonderzeichen willst, dann drücke die 2.,"
    "\nwenn du Zahlen und Sonderzeichen willst, dann drücke die 3.,"
    "\nwenn du nur Sonderzeichen willst, dann drücke die 4.,"
    "\nwenn du nur Großbuchstaben willst, dann drücke die 5.,"
    "\nwenn du nur Kleinbuchstaben willst, dann drücke die 6. ,"
    "\nwenn du nur Zahlen willst, dann drücke die 7. ,"
    "\nwenn du Sonderzeichen und Großbuchstaben willst, dann drücke die 8.!"
    "\nwenn du Sonderzeichen und Kleinbuchstaben willst, dann drücke die 9.!"
    "\nwenn du Sonderzeichen und Zahlen willst, dann drücke die 10.!"
    "\nwenn du nur Großbuchstaben und Kleinbuchstaben willst, dann drücke die 11.,"
    "\nwenn du nur Großbuchstaben und Zahlen willst, dann drücke die 12.,"
    "\nwenn du nur Kleinbuchstaben und Zahlen willst, dann drücke die 13. ,"
)
if frage == "1":
    for _ in range(laenge):
        pw = pw + secrets.choice(gross + klein + sonderzeichen + zahlen)
elif frage == "2":
    for _ in range(laenge):
        pw = pw + secrets.choice(klein + sonderzeichen + zahlen)
elif frage == "3":
    for _ in range(laenge):
        pw = pw + secrets.choice(sonderzeichen + zahlen)
elif frage == "4":
    for _ in range(laenge):
        pw = pw + secrets.choice(sonderzeichen)
elif frage == "5":
    for _ in range(laenge):
        pw = pw + secrets.choice(gross)
elif frage == "6":
    for _ in range(laenge):
        pw = pw + secrets.choice(klein)
elif frage == "7":
    for _ in range(laenge):
        pw = pw + secrets.choice(zahlen)
elif frage == "8":
    for _ in range(laenge):
        pw = pw + secrets.choice(gross + sonderzeichen)
elif frage == "9":
    for _ in range(laenge):
        pw = pw + secrets.choice(sonderzeichen + klein)
elif frage == "10":
    for _ in range(laenge):
        pw = pw + secrets.choice(zahlen + sonderzeichen)
elif frage == "11":
    for _ in range(laenge):
        pw = pw + secrets.choice(gross + klein)
elif frage == "12":
    for _ in range(laenge):
        pw = pw + secrets.choice(zahlen + gross)
elif frage == "13":
    for _ in range(laenge):
        pw = pw + secrets.choice(zahlen + klein)

print(pw)
