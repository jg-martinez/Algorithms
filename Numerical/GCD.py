def GCD (A, B):
    while (B != 0):
        remainder = A % B
        A = B
        B = remainder
    return A

print GCD(60, 24)
