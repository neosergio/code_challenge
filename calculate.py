from typing import List


def calculate_max_area(numbers: List[int]) -> int:
    max_area = 0
    first_column = 0
    second_column = len(numbers) - 1

    while first_column < second_column:
        if numbers[first_column] <= numbers[second_column]:
            temp_max_area = numbers[first_column] * (second_column - first_column)
            first_column += 1
        else:
            temp_max_area = numbers[second_column] * (second_column - first_column)
            second_column -= 1
        if temp_max_area > max_area:
            max_area = temp_max_area

    return max_area
