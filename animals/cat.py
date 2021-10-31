from .animal import Animal


class Cat(Animal):
    def __init__(self, name: str = "Cat", init_parameters: dict = None):
        super().__init__(
            name=name,
            init_parameters=init_parameters,
            energy=100,
            energy_rate={
                "run": 5
            }
        )
