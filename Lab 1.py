# Penggunaan End
print("PENGGUNAAN END")
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('y')
print('Z')
print("\n")


# Penggunaan Separator
print("PENGGUNAAN SEPARATOR")
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
print("\n")


# String Format
print("STRING SEBELUM DI FORMAT")
print(0,10**0)
print(1,10**1)
print(2,10**2)
print(3,10**3)
print(4,10**4)
print(5,10**5)
print(6,10**6)
print(7,10**7)
print(8,10**8)
print(9,10**9)
print(10,10**10)
print("\n")


# String Format
print("STRING SETELAH DI FORMAT")
print('{0:>3} {1:>16}'.format(0,10**0))
print('{0:>3} {1:>16}'.format(1,10**1))
print('{0:>3} {1:>16}'.format(2,10**2))
print('{0:>3} {1:>16}'.format(3,10**3))
print('{0:>3} {1:>16}'.format(4,10**4))
print('{0:>3} {1:>16}'.format(5,10**5))
print('{0:>3} {1:>16}'.format(6,10**6))
print('{0:>3} {1:>16}'.format(7,10**7))
print('{0:>3} {1:>16}'.format(8,10**8))
print('{0:>3} {1:>16}'.format(9,10**9))
print('{0:>3} {1:>16}'.format(10,10**10))
