# Contoh Menghapus pada Dictionary

dict = {'Name' : 'Maulana Ali Hanafiah', 'Age' : 21, 'Class' : 'Last'}

del dict['Name'] # Hapus entri dengan key 'Name'
dict.clear()     # Hapus semua entri
del dict         # Hapus Dictionary yang ada

print("dict['Name']: ", dict['Name'])
print("dict['School']: ", dict['School'])