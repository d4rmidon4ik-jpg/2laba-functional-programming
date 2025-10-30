def prime_numbers_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for number in range(2, limit + 1):
        if is_prime(number):
            yield number

primes = prime_numbers_generator(50)
print("Простые числа до 50:", list(primes))
