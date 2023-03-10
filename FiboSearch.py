# Nama : Muslim Nur Wahid
# NIM : 2209116070
# Kelas : Sistem Informasi B '22

def fib(w):
    if w < 1:
        return 1
    elif w == 1:
        return 1
    else:
        return fib(w-1) + fib(w-2)
def FiboSearching(Gojo, Satoru):
    w = 0
    while fib(w) < len(Gojo):
        w = w + 1
    offset = -1
    for v in range(len(Gojo)):
        if type(Gojo[v]) == list:
            output1 = FiboSearching(Gojo[v], Satoru)
            if output1 == -1:
                Gojo[v] = "berhasil"
            else:
                print(Satoru, "di Index", int(v), "pada kolom", output1)
                exit()
    while (fib(w) > 1):
        mnw = min(offset + fib(w-2), len(Gojo) - 1)
        if (Satoru > Gojo[mnw]):
            w = w-1
            offset = mnw
        elif (Satoru < Gojo[mnw]):
            w = w-2
        else:
            return mnw
    if (fib(w-1) and Gojo[offset + 1] == Satoru):
        return offset + 1
    return -1

data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print(data)
c = input("Masukkan nama yang ingin kamu cari : ")
output = FiboSearching(data, c)
if output == -1:
    print(c, "tidak ada")
else:
    print(c, "di Index", output)