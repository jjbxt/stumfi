MIN_PAROV = 0
MAX_PAROV = 30

razlicnih_stumfov = 0
najdenih_parov = 0
verjetnostna_porazdelitev = [1.0 for _ in range(MIN_PAROV, MAX_PAROV + 1)]

while True:
    try:
        print("\nTrenutno stanje:")
        for parov in range(razlicnih_stumfov, MAX_PAROV + 1):
            print(f"Parov: {parov}, Verjetnost: {verjetnostna_porazdelitev[parov]:.12f}")

        r, n = razlicnih_stumfov, najdenih_parov
        user_input = input("Nov stumf? ").strip().lower()

        match user_input:
            case "0":
                if najdenih_parov == razlicnih_stumfov:
                    print("Napaka! Ni mogoce tvoriti para, brez da bi najprej izvlekli stumf brez para. Prekinjam racunanje.")
                    break

                def prob(k: int, razlicnih_stumfov: int = r, najdenih_parov: int = n) -> float:
                    return (razlicnih_stumfov - najdenih_parov) / (2 * k - (razlicnih_stumfov + najdenih_parov))

                najdenih_parov += 1

            case "1":
                def prob(k: int, razlicnih_stumfov: int = r, najdenih_parov: int = n) -> float:
                    return 2 * (k - razlicnih_stumfov) / (2 * k - (razlicnih_stumfov + najdenih_parov))

                razlicnih_stumfov += 1

            case _:
                print("Neveljavna izbira. Poskusite znova.")
                continue

        for parov in range(razlicnih_stumfov, MAX_PAROV + 1):
            verjetnostna_porazdelitev[parov] *= prob(parov)

    except KeyboardInterrupt:
        print("\nProgram prekinjen. Izhod.")
        break
