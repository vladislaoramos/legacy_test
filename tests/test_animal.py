import unittest
from animals import Animal


class TestAnimal(unittest.TestCase):
    @staticmethod
    def init_animal():
        return Animal("Animal", energy_rate={"fly": 5, "run": 10, "swim": 15})

    def test_speak(self):
        animal = TestAnimal.init_animal()
        self.assertTrue(animal.say())
        self.assertEqual(animal.last_speech, "Hello, I'm an animal and my name is Animal.")

    def test_create(self):
        animal = TestAnimal.init_animal()
        self.assertTrue(isinstance(animal, Animal))

    def test_animal_name(self):
        animal = TestAnimal.init_animal()
        self.assertEqual(animal.name, "Animal")

    def test_animal_energy(self):
        animal = TestAnimal.init_animal()
        self.assertEqual(animal.energy, 100)
        self.assertNotEqual(animal.energy, 101)
        self.assertNotEqual(animal.energy, 99)

    def test_unknown_action(self):
        animal = TestAnimal.init_animal()
        self.assertFalse(animal.do_something(action="play"))
        self.assertFalse(animal.do_something(action="jump"))
        self.assertFalse(animal.do_something(action="think"))

    def test_init_params(self):
        pass


if __name__ == "__main__":
    unittest.main()