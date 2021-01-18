# Contoh Penggunaan Nested loop
# Catatan: Penggunaan modulo kondisional mengasumsikan nilai nol sebagai TRUE(benar) dan nol sebagai FALSE(salah)

i = 2
while(i < 10):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break
        j = j + 1
    if(j>i/j):
        print(i, "is prime")
        i = i + 1

    print("Good Bye!")