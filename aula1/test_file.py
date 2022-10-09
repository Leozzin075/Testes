import program


def test_even():
    # Arrange
    a = 10
    b = 20

    # Act
    result = program.sum_values(a, b)

    # Assert
    assert result == 30
