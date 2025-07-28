import random
from app.infrastructure.even_numbers_infra import EvenNumbersInfra
class EvenNumberUseCase:

    def __init__(self):
        self.number =random.randrange(10) 


    def execute(self,infra:EvenNumbersInfra) -> int:

        return infra.calculate(self.number)

        