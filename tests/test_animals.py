import unittest
from animals import Cat, Dog, Duck, Tiger, Fish, FlyingFish


test_cat = Cat()
test_dog = Dog()
test_fish = Fish()
test_flying_fish = FlyingFish()
test_tiger = Tiger()
test_duck = Duck()

name_test = [
    (test_cat, "Cat"), (test_dog, "Dog"),
    (test_fish, "Fish"), (test_tiger, "Tiger"),
    (test_flying_fish, "FlyingFish"), (test_duck, "Duck")
]

energy_test = [
    (Cat(), 100), (Dog(), 100),
    (Fish(), 100), (Tiger(), 100),
    (FlyingFish(), 100), (Duck(), 100)
]

actions_single_test = [
    (test_cat, "run", True), (test_cat, "swim", False), (test_cat, "fly", False),

    (test_dog, "run", True), (test_dog, "swim", True), (test_dog, "fly", False),

    (test_fish, "run", False), (test_fish, "swim", True), (test_fish, "fly", False),

    (test_flying_fish, "run", False), (test_flying_fish, "fly", True), (test_flying_fish, "swim", True),

    (test_tiger, "run", True), (test_tiger, "swim", True), (test_tiger, "fly", False),

    (test_duck, "run", False), (test_duck, "swim", True), (test_duck, "fly", True)
]

actions_energy_test = [
    (test_cat, "run", 5), (test_dog, "run", 10),
    (test_fish, "run", 0), (test_flying_fish, "run", 0),
    (test_tiger, "run", 20), (test_duck, "run", 0),
    (test_cat, "swim", 0), (test_dog, "swim", 30),
    (test_fish, "swim", 5), (test_flying_fish, "swim", 5),
    (test_tiger, "swim", 40), (test_duck, "swim", 10),
    (test_cat, "fly", 0), (test_dog, "fly", 0),
    (test_fish, "fly", 0), (test_flying_fish, "fly", 20),
    (test_tiger, "fly", 0), (test_duck, "fly", 30),
]

new_tiger = Tiger()
new_dog = Dog()
new_duck = Duck()

several_actions_test = [
    (new_tiger, "run", True),
    (new_tiger, "run", True),
    (new_tiger, "run", True),
    (new_tiger, "run", True),
    (new_tiger, "run", True),
    (new_tiger, "run", False),

    (new_dog, "swim", True),
    (new_dog, "swim", True),
    (new_dog, "swim", True),
    (new_dog, "swim", False),

    (new_duck, "fly", True),
    (new_duck, "fly", True),
    (new_duck, "fly", True),
    (new_duck, "fly", False),
]


class TestAnimals(unittest.TestCase):
    def test_name(self):
        for test, expected in name_test:
            self.assertEqual(test.name, expected)

    def test_energy(self):
        for test, expected in energy_test:
            self.assertEqual(test.energy, expected)

    def test_single_actions(self):
        for animal, action, expected in actions_single_test:
            self.assertEqual(animal.do_something(action=action), expected)

    def test_action_rate(self):
        for animal, action, expected_rate in actions_energy_test:
            self.assertEqual(animal.energy_rate.get(action, 0), expected_rate)

    def test_several_actions(self):
        for animal, action, expected_ans in several_actions_test:
            self.assertEqual(animal.do_something(action=action), expected_ans)


if __name__ == "__main__":
    unittest.main()
