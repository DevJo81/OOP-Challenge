from pet import Pet

if __name__ == "__main__":
    my_pet = Pet("Luna")

    print (f"My pet's name is {my_pet.name}. Shes's a shih tzu🐾\n")

    print("Initial status:")
    print(my_pet.get_status())

    print(my_pet.eat() + "🥩")
    print(my_pet.sleep() + "⚡")
    print(my_pet.play() + " 😊")

    print("\nCurrent status:")
    print(my_pet.get_status())

    print("\n" + my_pet.train("speak") + "🐶")
    print(my_pet.train("roll over"))
    print(my_pet.show_tricks() + "✨")


