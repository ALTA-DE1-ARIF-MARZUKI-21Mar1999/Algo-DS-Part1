def primeX(x):
    
    if x <= 0:
        return False
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2

    while count < x:
        if is_prime(num):
            count += 1
        if count < x:
            num += 1
    
    return num

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29