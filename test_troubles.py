from troubles import sanitize_string


def test_sanitize_string():
    base_string = 'nnmmmnmnnmnnm5'
    exclude = 'nnmmjhfhgf'
    max_len = 5
    expected_result = ['5']
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result


def test_sanitize_zero_string():
    base_string = ''
    exclude = 'nnmmjhfhgf'
    max_len = 5
    expected_result = []
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result

def test_sanitize_overload_string():
    base_string = '1' * 500
    print(base_string)
    exclude = 'nnmmjhfhgf'
    max_len = 5
    expected_result = ['500']
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result