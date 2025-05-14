def greet_user(name):
    print(f"Salut, {name}!")
    print(f"Bun venit pe ramura feature-a și feature-b!")

def add_numbers(a, b):
    return a + b

def main():
    user_name = input("Introdu numele tău: ")
    greet_user(user_name)
    with open('output.txt', 'w') as f:
        f.write(f"Salut, {user_name}!\n")
    print("Mesajul a fost salvat în fișierul output.txt.")

if __name__ == "__main__":
    main()