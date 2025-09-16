def ma_hoa_cong_Z26(ban_ro, khoa):
    khoa = khoa % 26   # chuẩn hóa khóa
    ban_ma = ""
    for ky_tu in ban_ro:
        if ky_tu.isalpha():
            # xác định ký tự hoa hay thường
            co_so = ord('A') if ky_tu.isupper() else ord('a')
            # công thức: (P + k) mod 26
            c = (ord(ky_tu) - co_so + khoa) % 26 + co_so
            ban_ma += chr(c)
        else:
            ban_ma += ky_tu  # giữ nguyên nếu không phải chữ cái
    return ban_ma

def giai_ma_cong_Z26(ban_ma, khoa):
    return ma_hoa_cong_Z26(ban_ma, -khoa)


# Ví dụ theo đề
ban_ro = "LeMinhThu"
khoa = 46
ban_ma = ma_hoa_cong_Z26(ban_ro, khoa)
print("Bản rõ :", ban_ro)
print("Khóa    :", khoa, "(mod 26 =", khoa % 26, ")")
print("Bản mã :", ban_ma)
print("Giải mã :", giai_ma_cong_Z26(ban_ma, khoa))
