import random
from app.infrastructure.even_numbers_infra import EvenNumbersInfra
from app.domain.exceptions.is_not_even_exception import IsNotEvenException

class EvenNumberUseCase:

    def __init__(self):
        self.number =random.randrange(10) 


    def execute(self,infra:EvenNumbersInfra) -> int:

        try:
            result = infra.calculate(self.number)
        except Exception as error:
            raise IsNotEvenException("The number is not even") from error

        return result

        