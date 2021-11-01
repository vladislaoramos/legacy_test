"""
Tests for animal classes.
"""

import unittest
from animals import Cat, Dog, Duck, Tiger, Fish, FlyingFish


class WithNameTestCase(unittest.TestCase):
    """
    Test case for checking animals with name.
    """
    def setUp(self):
        """
        Method for creating test cases.
        (Animal with Name, Name)
        """
        self.with_name = [
            (Cat("Cat"), "Cat"), (Cat("Barsik"), "Barsik"),
            (Dog("Bobik"), "Bobik"), (Dog("Dog"), "Dog"),
            (Fish("Fish"), "Fish"), (Fish("Nemo"), "Nemo"),
            (Tiger("Tiger"), "Tiger"), (Tiger("Alex"), "Alex"),
            (FlyingFish("FlyingFish"), "FlyingFish"), (FlyingFish("Goldfish"), "Goldfish"),
            (Duck("Duck"), "Duck"), (Duck("Donald"), "Donald")
        ]

    def test_name(self):
        """
        Method for testing a correct creation of animals with name.
        """
        for animal, expected in self.with_name:
            self.assertEqual(animal.name, expected)


class WithoutNameTestCase(unittest.TestCase):
    """
    Test case for checking animals without name.
    """
    def setUp(self):
        """
        Method for creating test cases.
        (Animal, Standard Name for Animal)
        """
        self.without_name = [
            (Cat(), "Cat"), (Dog(), "Dog"),
            (Fish(), "Fish"), (Tiger(), "Tiger"),
            (FlyingFish(), "FlyingFish"), (Duck(), "Duck")
        ]

    def test_name(self):
        """
        Method for testing a correct creation of animals without name.
        """
        for animal, expected in self.without_name:
            self.assertEqual(animal.name, expected)


class EnergyTestCase(unittest.TestCase):
    """
    Test case for checking animal's energy.
    """
    def setUp(self):
        """
        Method for creating test cases.
        (Animal, Start Energy, Energy After Run-Swim-Fly)
        """
        self.energy_test = [
            (Cat(), 100, 95), (Dog(), 100, 60),
            (Fish(), 100, 95), (Tiger(), 100, 40),
            (FlyingFish(), 100, 75), (Duck(), 100, 60)
        ]

    def test_energy(self):
        """
        Method for testing a correct energy remainder.
        """
        for animal, start, remaining in self.energy_test:
            self.assertEqual(animal.energy, start)
            for action in "run", "swim", "fly":
                animal.do_something(action=action)
            self.assertEqual(animal.energy, remaining)


class SingleActionTestCase(unittest.TestCase):
    """
    Test case for checking animal's actions.
    """
    def test_ability(self):
        """
        Method for testing an animal's abilities.
        """
        self.assertTrue(Cat().run())

        self.assertTrue(Dog().run())
        self.assertTrue(Dog().swim())

        self.assertTrue(Fish().swim())

        self.assertTrue(FlyingFish().swim())
        self.assertTrue(FlyingFish().fly())

        self.assertTrue(Tiger().run())
        self.assertTrue(Tiger().swim())

        self.assertTrue(Duck().swim())
        self.assertTrue(Duck().fly())

    def test_inability(self):
        """
        Method for testing an animal's inabilities.
        """
        self.assertFalse(Cat().swim())
        self.assertFalse(Cat().fly())

        self.assertFalse(Dog().fly())

        self.assertFalse(Fish().run())
        self.assertFalse(Fish().fly())

        self.assertFalse(FlyingFish().run())

        self.assertFalse(Tiger().fly())

        self.assertFalse(Duck().run())


class SeveralActionTestCase(unittest.TestCase):
    """
    Test case for checking a series of an animal's actions.
    """
    def test_cat(self):
        """
        Method for testing a cat's actions.
        """
        cat = Cat()
        for _ in range(20):
            self.assertTrue(cat.run())
        self.assertFalse(cat.run())

    def test_dog(self):
        """
        Method for testing a dog's actions.
        """
        dog = Dog()
        self.assertTrue(dog.run())
        self.assertTrue(dog.swim())
        self.assertTrue(dog.swim())
        self.assertTrue(dog.swim())
        self.assertFalse(dog.run())

    def test_tiger(self):
        """
        Method for testing a tiger's actions.
        """
        tiger = Tiger()
        self.assertTrue(tiger.swim())
        self.assertTrue(tiger.swim())
        self.assertTrue(tiger.run())
        self.assertFalse(tiger.run())
        self.assertFalse(tiger.swim())

    def test_fish(self):
        """
        Method for testing a fish's actions.
        """
        fish = Fish()
        for _ in range(20):
            self.assertTrue(fish.swim())
        self.assertFalse(fish.swim())

    def test_flying_fish(self):
        """
        Method for testing a flying fish's actions.
        """
        fish = FlyingFish()
        for _ in range(4):
            self.assertTrue(fish.swim())
            self.assertTrue(fish.fly())
        self.assertFalse(fish.swim())
        self.assertFalse(fish.fly())

    def test_duck(self):
        """
        Method for testing a duck's actions.
        """
        duck = Duck()
        self.assertTrue(duck.fly())
        self.assertTrue(duck.fly())
        self.assertTrue(duck.fly())
        self.assertTrue(duck.swim())
        self.assertFalse(duck.swim())


class EnergyRateTestCase(unittest.TestCase):
    """
    Test case for checking animal's energy rate.
    """
    def setUp(self):
        """
        Method for creating test cases.
        (Animal, Energy Rate After Run-Swim-Fly)
        """
        self.rates = [
            (Cat(), 5),
            (Dog(), 40),
            (Tiger(), 60),
            (Fish(), 5),
            (FlyingFish(), 25),
            (Duck(), 40)
        ]

    def test_energy_rate(self):
        """
        Method for testing an animal's energy rate.
        (Animal, Energy Rate After Run-Swim-Fly)
        """
        for animal, expected in self.rates:
            start = animal.get_energy()
            for action in "run", "swim", "fly":
                animal.do_something(action=action)
            remaining = animal.get_energy()
            self.assertEqual(start - remaining, expected)


if __name__ == "__main__":
    unittest.main()
