def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nearest_prime(n):
    if n < 2:
        return 2
    
    lower = n
    upper = n
    
    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1

n = 114514
nearest = nearest_prime(n)
print(f"距离最近的素数是 {nearest}")
