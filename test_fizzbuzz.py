from fizzbuzz import fizzbuzz

def test_given_1_should_return_1() -> None :
    assert fizzbuzz(1) == 1

def test_given_2_should_return_2() -> None :
    assert fizzbuzz(2) == 2 

def test_given_3_should_return_fizz() -> None :
    assert fizzbuzz(3) == 'fizz' 

