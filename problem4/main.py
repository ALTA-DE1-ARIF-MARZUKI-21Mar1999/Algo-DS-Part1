def generate_primes_grid(width, height, start):

    result = ''
    current_number = start
    prime_width = 2

    for i in range(height):
        row = ''
        for j in range(width):
            while not is_prime(current_number) or current_number <= start:
                current_number += 1
            if current_number == start:
                row += str(current_number).rjust(prime_width) + ' '
            else:
                row += str(current_number).rjust(prime_width) + ' '
            current_number += 1
        result += row.strip() + '\n'
    return result

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """