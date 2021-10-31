from .animal import Animal


class Fish(Animal):
    def __init__(self, name: str = "Fish", init_parameters: dict = None):
        super().__init__(
            name=name,
            init_parameters=init_parameters,
            energy=100,
            energy_rate={"swim": 5}
        )


class FlyingFish(Animal):
    def __init__(self, name: str = "FlyingFish", init_parameters: dict = None):
        super().__init__(
            name=name,
            init_parameters=init_parameters,
            energy=100,
            energy_rate={
                "swim": 5,
                "fly": 20
            }
        )
