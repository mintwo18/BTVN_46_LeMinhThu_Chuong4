def caesar(plaintext: str, k: int) -> str:
    k %= 26
    kq = []
    for ch in plaintext:
        if 'A' <= ch <= 'Z':  # in hoa
            kq.append(chr((ord(ch) - 65 + k) % 26 + 65))
        elif 'a' <= ch <= 'z':  # in thường
            kq.append(chr((ord(ch) - 97 + k) % 26 + 97))
        else:
            kq.append(ch)
    return ''.join(kq)


if __name__ == "__main__":
    plaintext = "LE MINH THU"
    k = 46
    ciphertext = caesar(plaintext, k)
    
    print("Plaintext:", plaintext)
    print("k =", k, "→ k mod 26 =", k % 26)
    print("Ciphertext:", ciphertext)
