MIN_PAROV = 0
MAX_PAROV = 30

razlicnih_stumfov = 0  # a_t
najdenih_parov = 0     # b_t
likelihood = [1.0 for _ in range(MIN_PAROV, MAX_PAROV + 1)]

while True:
    try:
        print("\nTrenutno stanje:")
        # show normalized posterior under uniform prior
        Z = sum(likelihood)
        for k in range(razlicnih_stumfov, MAX_PAROV + 1):
            print(f"Parov: {k}, Posterior: {(likelihood[k]/Z if Z > 0 else 0):.12f}")

        a, b = razlicnih_stumfov, najdenih_parov
        t = a + b  # socks drawn so far
        user_input = input("Nov stumf? (1=new, 0=match) ").strip().lower()

        if user_input == "0":
            if b == a:
                print("Napaka! Ni mogoce tvoriti para brez unmatched nogavice.")
                break
            # update likelihood for each possible N
            for N in range(MAX_PAROV + 1):
                if N < a:  # infeasible: can't have seen more distinct pairs than exist
                    p = 0
                else:
                    remaining = 2*N - t
                    p = (a - b) / remaining if remaining > 0 else 0
                likelihood[N] *= p
            b += 1

        elif user_input == "1":
            for N in range(MAX_PAROV + 1):
                if N < a:
                    p = 0
                else:
                    remaining = 2*N - t
                    p = 2*(N - a) / remaining if remaining > 0 else 0
                likelihood[N] *= p
            a += 1

        else:
            print("Neveljavna izbira.")
            continue

        razlicnih_stumfov, najdenih_parov = a, b

    except KeyboardInterrupt:
        print("\nIzhod.")
        break
