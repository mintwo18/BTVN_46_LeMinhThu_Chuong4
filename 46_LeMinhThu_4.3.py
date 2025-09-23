# Thông số RSA
p = 17
q = 23
e = 5
n = p * q          # n = 391
phi_n = (p-1)*(q-1)  # phi(n) = 352


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return g, x, y

g, x, y = extended_gcd(e, phi_n)
d = x % phi_n  # d = 141

# Thông điệp
message = "LeMinhThu"
ascii_values = [ord(c) for c in message]

# Hàm lũy thừa 
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Mã hóa
cipher_values = [mod_exp(c, e, n) for c in ascii_values]

# Giải mã
decoded_values = [mod_exp(c, d, n) for c in cipher_values]
decoded_message = ''.join(chr(c) for c in decoded_values)

print("Thông điệp ASCII:", ascii_values)
print("Mã hóa RSA:", cipher_values)
print("Giải mã:", decoded_message)
