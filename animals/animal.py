"""
A module with the base class.
"""


class Animal:
    """
    Base class for creating an animal.
    """

    KIND_STR = {
        "Cat": "a cat",
        "Dog": "a dog",
        "Tiger": "a tiger",
        "Animal": "an animal",
        "FlyingFish": "a flying fish",
        "Fish": "a fish",
        "Duck": "a duck"
    }

    def __init__(self,
                 name: str = "Animal",
                 energy: int = 100,
                 init_parameters: dict = None,
                 energy_rate: dict = None):
        """
        Animal initial.
        :param name: Animal name.
        :param energy: Animal energy level.
        :param init_parameters: Initial parameters.
        :param energy_rate: Possible actions and energy rate for them.
        """

        self.last_speech = None
        if init_parameters is None:
            init_parameters = {}
        self.name = init_parameters.get("name", name)
        self.energy = init_parameters.get("energy", energy)

        if energy_rate is None:
            energy_rate = {}
        self.energy_rate = init_parameters.get("energy_rate", energy_rate)

    def say(self) -> bool:
        """
        Method for making the animal speak.
        """
        cls_name = self.__class__.__name__
        kind = self.__class__.KIND_STR[cls_name]
        self.last_speech = f"Hello, I'm {kind} and my name is {str(self.name)}."
        print(self.last_speech)
        return True

    def run(self) -> bool:
        """
        Method for making the animal run.
        """
        return self.do_something(action="run")

    def swim(self) -> bool:
        """
        Method for making the animal swim.
        """
        return self.do_something(action="swim")

    def fly(self) -> bool:
        """
        Method for making the animal fly.
        """
        return self.do_something(action="fly")

    def get_energy(self) -> int:
        """
        Method for getting the energy level of an animal.
        """
        return self.energy

    def do_something(self, action: str) -> bool:
        """
        Method for making the animal action with checking.
        :param action: Action text key.
        :return: True if the action was, otherwise False.
        """
        if action not in ("run", "fly", "swim"):
            print(f"My name is {self.name} and I don't know what is it.")
            return False

        if action in self.energy_rate.keys():
            if self.energy - self.energy_rate[action] >= 0:
                self.energy -= self.energy_rate[action]
                print(f"My name is {self.name} and I can {action}.")
                return True
            else:
                print(f"My name is {self.name} and I have no energy to {action}.")
        else:
            print(f"My name is {self.name} and I can't {action}.")

        return False
