# Algandmed
kasutaja_limiiit = 20
kasutatud_tunnid = 0
paevade_arv = 0

rakendused = {}

# Administraatori parool
admin_parool = "admin123"


# Administraatori funktsioon
def administraator():

    global kasutaja_limiiit

    parool = input("Sisesta administraatori parool: ")

    if parool == admin_parool:

        print("\nAdministraatori menüü")
        print("1. Muuda kasutuslimiiti")
        print("2. Vaata statistikat")

        valik = input("Vali tegevus: ")

        if valik == "1":
            uus_limiiit = float(input("Sisesta uus nädalane limiit: "))
            kasutaja_limiiit = uus_limiiit
            print("Kasutuslimiit on muudetud!")

        elif valik == "2":
            print("Nädalane limiit:", kasutaja_limiiit, "tundi")
            print("Kasutatud:", kasutatud_tunnid, "tundi")

    else:
        print("Vale parool!")


# Tavakasutaja funktsioon
def kasutaja():

    global kasutatud_tunnid
    global paevade_arv

    print("\nKasutaja menüü")
    print("1. Lisa kasutusaeg")
    print("2. Vaata statistikat")

    valik = input("Vali tegevus: ")

    if valik == "1":

        paevade_arv += 1

        arvuti_aeg = float(input("Mitu tundi kasutasid arvutit täna? "))
        kasutatud_tunnid += arvuti_aeg

        print("Sisestatud kasutusaeg!")

        while True:

            app = input("Millist rakendust kasutasid? (Lõpetamiseks kirjuta 'ei'): ")

            if app == "ei":
                break

            aeg = float(input("Mitu tundi kasutasid seda rakendust? "))

            if app in rakendused:
                rakendused[app] += aeg
            else:
                rakendused[app] = aeg

    elif valik == "2":

        print("\n--- KASUTUSSTATISTIKA ---")

        print("Kasutatud aega:", kasutatud_tunnid, "tundi")
        print("Allesjäänud aega:",
              kasutaja_limiiit - kasutatud_tunnid, "tundi")

        if paevade_arv > 0:
            keskmine = kasutatud_tunnid / paevade_arv
            print("Päevade keskmine kasutusaeg:", keskmine, "tundi")

        print("\nRakenduste kasutusaeg:")

        for app in rakendused:
            print(app, "-", rakendused[app], "tundi")

        if kasutatud_tunnid >= kasutaja_limiiit:
            print("HOIATUS! Kasutuslimiit on täis!")

        else:
            print("Kasutuslimiit ei ole veel täis.")


# Programmi põhiosa
while True:

    print("\n=== ARVUTIKASUTUSE JÄLGIJA ===")
    print("1. Administraator")
    print("2. Tavakasutaja")
    print("3. Välju")

    valik = input("Vali kasutajatüüp: ")

    if valik == "1":
        administraator()

    elif valik == "2":
        kasutaja()

    elif valik == "3":
        print("Programm lõpetati.")
        break

    else:
        print("Vale valik!")
