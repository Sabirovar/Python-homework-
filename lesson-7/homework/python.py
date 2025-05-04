# 1. is_prime(n) funksiyasi

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 2.  digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(24))   
print(digit_sum(502))  
print(digit_sum(1234)) 

# 3. Ikki sonning darajalari

def powers_of_two(N):
    k = 1
    result = []
    while 2 ** k <= N:
        result.append(2 ** k)
        k += 1
    print(*result)

powers_of_two(10)
