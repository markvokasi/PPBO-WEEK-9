from collections import namedtuple

def tambah_method(cls):
    def tampilkan_info(self):
        print(f"Nama : {self.nama}")
        print("Nama anak :")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")
    cls.tampilkan_info = tampilkan_info
    return cls

@tambah_method
class Orang(namedtuple("Orang", "nama anak")):
    pass

john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john)
print(id(john.anak))

john.anak.append("Tina")
print(john)
print(id(john.anak))

print()
john.tampilkan_info()
