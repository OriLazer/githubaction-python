from src.maths_operations import add, subtract, multiply, divide, power, square_root, factorial, fibonacci, is_prime

def test_add(): # Test for add function
    assert add(2,3) == 5
    assert add(0,0) == 0
    assert add(-1,-1) == -2
    assert add(1,2) == 3

def test_subtract(): # Test for subtract function
    assert subtract(5,3) == 2
    assert subtract(0,0) == 0
    assert subtract(-1,1) == -2
    assert subtract(3,1) == 2

def test_multiply(): # Test for multiply function
    assert multiply(2,3) == 6
    assert multiply(0,0) == 0
    assert multiply(-1,-1) == 1
    assert multiply(1,2) == 2

def test_divide(): # Test for divide function
    assert divide(6,3) == 2
    assert divide(0,1) == 0
    assert divide(-1,-1) == 1
    assert divide(2,1) == 2
    assert divide(1,0) == float('inf')

def test_power(): # Test for power function
    assert power(2,3) == 8
    assert power(0,0) == 1
    assert power(-1,1) == -1
    assert power(2,0) == 1

def test_square_root(): # Test for square_root function
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root(1) == 1
    assert square_root(9) == 3
    assert square_root(-1) == float('nan')
    assert square_root(4.9) == 2.2

def test_factorial(): # Test for factorial function
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(-1) == 'Error: Factorial is not defined for negative numbers'

def test_fibonacci(): # Test for fibonacci function
    assert fibonacci(5) == 5
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(3) == 2
    assert fibonacci(-1) == 'Error: Fibonacci is not defined for negative numbers'

def test_is_prime(): # Test for is_prime function
    assert is_prime(5) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(-1) == False

# Run the test using the command: pytest tests/test_operations.py