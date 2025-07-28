from app.use_case.even_numbers_use_case import EvenNumberUseCase
from unittest.mock import Mock

def test_test_event_numbers_use_case():
    input_name = 2
    use_case = EvenNumberUseCase()
    use_case.number = input_name

    even_number_mock = Mock()
    even_number_mock.calculate.return_value = True

    result = use_case.execute(even_number_mock)

    assert result is True