class Programm1:
    def run(self):
        float_number = float(input("Gebe mir eine Kommazahl: "))
        integer = int(input("Gebe mir Eine Zahl: "))
        float_numberstring = str(float_number)
        integerstring = str(integer)
        print(f"Die Ganzzahl ist {integerstring} und die Kommazahl ist {float_numberstring}")

class Programm2:
    def run(self):
        zahl1 = input("Gebe mir die erste Zahl: ")
        zahl2 = input("Gebe mir die zweite Zahl: ")
        zahl1float = float(zahl1)
        zahl2float = float(zahl2)
        print(f"Die Summe der beiden Zahlen ist {zahl1float + zahl2float}")

class Programm3:
    def run(self):
        float_number = float(input("Gebe mir eine Kommazahl: "))
        float_number_int = int(float_number)
        print(f"Die Kommazahl ist {float_number}\n"
              f"Die umgewandelte Ganzzahl ist {float_number_int}")

class Programm4:
    def run(self):
        float_number = float(input("Gebe mir eine Kommazahl mit 4 Nachkommastellen: "))
        print(f"Die Zahl ohne die letzen 2 Nachkommastellen ist {round(float_number, 2)}")

def main():
    while True:
        print("Wähle ein Programm:")
        print("1. Programm 1")
        print("2. Programm 2")
        print("3. Programm 3")
        print("4. Programm 4")
        print("5. Beenden")

        choice = input("Deine Wahl: ")

        if choice == '1':
            programm = Programm1()
            programm.run()
        elif choice == '2':
            programm = Programm2()
            programm.run()
        elif choice == '3':
            programm = Programm3()
            programm.run()
        elif choice == '4':
            programm = Programm4()
            programm.run()
        elif choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte versuche es erneut.")

if __name__ == "__main__":
    main()