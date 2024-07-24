def fibonacci_sequence(count):
    a, b = 0, 1
    fibonacci_numbers = []
    for _ in range(count):
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers
