class EvenNumberUseCase:

    def __init__(self,number:int):
        self.number = number


    def execute(self) -> bool:
        
        return self.calculate(self.number)

        