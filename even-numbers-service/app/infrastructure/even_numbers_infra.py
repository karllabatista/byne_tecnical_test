from app.domain.exceptions.is_not_even_exception import IsNotEvenException
class EvenNumbersInfra:

    def calculate(self,number:int):

        try:
            if number % 2 == 0:
                return True
        
        except Exception as error:
            raise IsNotEvenException("The number is not even") from error