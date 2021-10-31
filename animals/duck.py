from .animal import Animal


class Duck(Animal):
    def __init__(self, name: str = "Duck", init_parameters: dict = None):
        super().__init__(
            name=name,
            init_parameters=init_parameters,
            energy=100,
            energy_rate={
                "fly": 30,
                "swim": 10
            }
        )
