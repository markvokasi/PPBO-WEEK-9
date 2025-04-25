from collections import namedtuple

Drivers = namedtuple('Drivers', ['nama', 'tim', 'kejuaraan'])

f1 = Drivers('Max Verstappen', 'Red Bull Racing', [2021, 2022, 2023])

def tampilkan_info(data):
    print("Drivers   :", data.nama)
    print("Tim       :", data.tim)
    print("Kejuaraan :", data.kejuaraan)

tampilkan_info(f1)

