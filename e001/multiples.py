def sum_of_multiples(divisor1, divisor2, threshold):
    return sum(number for number in range(1, threshold) if number % divisor1 == 0 or number % divisor2 == 0)
