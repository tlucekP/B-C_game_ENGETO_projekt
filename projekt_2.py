"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Peter Tlučhoř
email: tluchor.peter@outlook.com

discord: Tlucek#0754
"""

import random # importuji modul pro generování náhodných proměnných
import time # importuji modul pro práci s časem (bude mi sloužit k počítání uběhnutého času hry v sekundách)


def generate_secret_number(): # Funkce pro vytvoření tajného čísla
    digits = list('123456789')  # První číslice nemůže být 0
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    remaining_digits = list('0123456789')
    secret_number = first_digit + ''.join(random.sample(remaining_digits, 3))
    return secret_number


def validate_guess(guess): # Funkce pro ověření vstupu uživatele
    if len(guess) != 4:
        return "Vstup musí být 4 číslice."
    if not guess.isdigit():
        return "Vstup musí obsahovat pouze číslice."
    if guess[0] == '0':
        return "Číslo nesmí začínat nulou."
    if len(set(guess)) != 4:
        return "Číslo musí mít unikátní číslice."
    return None

def evaluate_guess(secret, guess): # Funkce pro vyhodnocení bulls a cows
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def display_result(bulls, cows): # Funkce pro zobrazení výsledku s ohledem na jednotné a množné číslo
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"

def play_game(): # Funkce pro spuštění hry
    print("*" * 28)
    print("AHOJ! Pojď si zahrát hru Bulls & Cows!")
    print("*" * 28)
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Hádejte 4místné číslo: ")
        error = validate_guess(guess)
        
        if error:
            print(error)
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print(display_result(bulls, cows))

        if bulls == 4:
            elapsed_time = time.time() - start_time
            print(f"Gratulujeme! Uhádli jste číslo {secret_number} za {attempts} pokusů.")
            print(f"Čas: {elapsed_time:.2f} sekund")
            break

if __name__ == "__main__": # Spuštění hry
    play_game()
