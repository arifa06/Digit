def digitAwal (a,b):                                    # Membuat fungsi 'digitAwal' dengan parameter
    p = a**b                                            # Melakukan operasi matematika
    p1 = str(p)                                         # Melakukan konversi tipe data
    return p1[0]                                        # Menyimpan nilai

def digitAkhir (c,d):                                   # Membuat fungsi 'digitAkhir' dengan parameter
    p = c**c                                            # Melakukan operasi matematika
    p1 = str(p)                                         # Melakukan konversi tipe data
    return p1[-1]                                       # Menyimpan nilai

print(digitAwal(10,8))                                  # Memanggil fungsi dengan argumen dan mencetak nilai
print(digitAwal(2,3))                                   # Memanggil fungsi dengan argumen dan mencetak nilai
print(digitAwal(6,3))                                   # Memanggil fungsi dengan argumen dan mencetak nilai

print()                                                 # Mencetak baris baru

print(digitAkhir(10,8))                                 # Memanggil fungsi dengan argumen dan mencetak nilai
print(digitAkhir(3,3))                                  # Memanggil fungsi dengan argumen dan mencetak nilai
print(digitAkhir(6,3))                                  # Memanggil fungsi dengan argumen dan mencetak nilai   