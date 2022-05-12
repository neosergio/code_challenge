from my_app.calculate import calculate_max_area


def test_calculate_max_area():
    result_1 = calculate_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    result_2 = calculate_max_area([1, 1])
    assert isinstance(result_1, int)
    assert isinstance(result_2, int)
    assert result_1 == 49
    assert result_2 == 1


def test_calculate_max_area_with_invalid_list():
    result_1 = calculate_max_area(["test"])
    result_2 = calculate_max_area([1])
    result_3 = calculate_max_area([])
    assert result_1 == 0
    assert result_2 == 0
    assert result_3 == 0
