from animals import Cat, Tiger, Dog, Duck, Fish, FlyingFish, Animal


def do_actions(animal, name):
    a = animal(name)
    a.say()
    print(f"Start {a.name} Energy: {a.get_energy()}.")
    a.run()
    a.swim()
    a.fly()
    a.get_energy()
    print(f"Remaining {a.name} Energy: {a.get_energy()}.")


if __name__ == "__main__":
    # Cats
    do_actions(Cat, "Barsik")

    # Tigers
    do_actions(Tiger, "Alex")

    # Ducks
    do_actions(Duck, "Donald")

    # Dogs
    do_actions(Dog, "Bobik")

    # Simple Fish
    do_actions(Fish, "Nemo")

    # Flying Fish
    do_actions(FlyingFish, "Goldfish")

    # Animal
    do_actions(Animal, "Animal")
