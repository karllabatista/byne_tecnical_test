from fastapi import APIRouter,HTTPException
from starlette import status
from app.use_case.even_numbers_use_case import EvenNumberUseCase
from app.infrastructure.even_numbers_infra import EvenNumbersInfra
from app.domain.exceptions.is_not_even_exception import IsNotEvenException


router = APIRouter()

@router.get("/check_number")
def is_even_number():
    try:
        infra =  EvenNumbersInfra()

        use_case = EvenNumberUseCase(infra)
        result = use_case.execute()
        return result.json()
        # return HTTPException(status_code=status.HTTP_200_OK,detail=)
    except IsNotEvenException :
        raise  HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="The number is not Even")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Erro to calculate number")

