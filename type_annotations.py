from typing import Mapping

# Type Annotations


def sum_two_numbers(a: int, b: int) -> int:
    "Retorna a soma ded a e b."
    return a + b


results: Mapping[str, int] = {
    "result10": sum_two_numbers(5, 5),
    "result256": sum_two_numbers(250, 6)
}
