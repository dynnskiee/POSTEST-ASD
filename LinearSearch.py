# Nama : Muslim Nur Wahid
# NIM : 2209116070
# Kelas : Sistem Informasi B '22

def linearsearch(data, c):
    for w in range(len(data)):
        if type(data[w]) == list:
            hasil_c = linearsearch(data[w], c)
            if hasil_c == -1:
                return -1
            else:
                print(f"{c} di Index {w} pada kolom {hasil_c}")
                exit()
        elif data[w] == c:
            return w
    return -1

data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print(data)
c = input("Masukkan nama yang ingin kamu cari : ")
output = linearsearch(data, c)
if output == -1:
    print(f"{c} di Index {output}")
else:
    print(f"{c} di Index {output}")