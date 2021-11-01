"""
Tests for the basic class.
"""

import unittest
from animals import Animal


INIT_PARAMS = {
    "name": "Animal",
    "energy": 100,
    "energy_rate": {
        "fly": 5,
        "run": 10,
        "swim": 15
    }
}


class TestAnimal(unittest.TestCase):
    def setUp(self):
        """
        Method for initialization basic animals.
        """
        self.animal = Animal(
            name="Animal",
            energy_rate={
                "fly": 5,
                "run": 10,
                "swim": 15
            }
        )
        self.param_animal = Animal(init_parameters=INIT_PARAMS)

    def test_speak(self):
        """
        Method for testing animal speaking.
        """
        self.assertTrue(self.animal.say())
        self.assertEqual(self.animal.last_speech, "Hello, I'm an animal and my name is Animal.")

    def test_create(self):
        """
        Method for creating an object of the Animal class.
        """
        self.assertTrue(isinstance(self.animal, Animal))

    def test_animal_name(self):
        """
        Method for checking name of an animal.
        """
        self.assertEqual(self.animal.name, "Animal")

    def test_animal_energy(self):
        """
        Method for checking of an animal's energy.
        """
        self.assertEqual(self.animal.energy, 100)
        self.assertNotEqual(self.animal.energy, 101)
        self.assertNotEqual(self.animal.energy, 99)

    def test_unknown_action(self):
        """
        Method for checking of an unknown action.
        """
        self.assertFalse(self.animal.do_something(action="play"))
        self.assertFalse(self.animal.do_something(action="jump"))
        self.assertFalse(self.animal.do_something(action="think"))

    def test_init_params(self):
        """
        Method for checking of an initialization with init params.
        """
        self.assertEqual(self.param_animal.name, INIT_PARAMS.get("name", "Animal"))
        self.assertEqual(self.param_animal.energy, INIT_PARAMS.get("energy", 100))
        self.assertEqual(self.param_animal.energy_rate, INIT_PARAMS.get("energy_rate", {}))


if __name__ == "__main__":
    unittest.main()
