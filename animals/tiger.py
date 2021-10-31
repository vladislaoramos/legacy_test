from .animal import Animal


class Tiger(Animal):
    def __init__(self, name: str = "Tiger", init_parameters: dict = None):
        super().__init__(
            name=name,
            init_parameters=init_parameters,
            energy=100,
            energy_rate={
                "swim": 40,
                "run": 20
            }
        )
