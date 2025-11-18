from calculator_pkg_ex_jp.file_calculator import FileCalculator
# from ..file_calculator import FileCalculator


def test_file_calculator():
    assert FileCalculator().sum_file() == 6
