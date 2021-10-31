from .animal import Animal


class Dog(Animal):
    def __init__(self, name: str = "Dog", init_parameters: dict = None):
        super().__init__(
            name=name,
            init_parameters=init_parameters,
            energy=100,
            energy_rate={
                "run": 10,
                "swim": 30
            }
        )
