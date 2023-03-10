# Nama : Muslim Nur Wahid
# NIM : 2209116070
# Kelas : Sistem Informasi B '22

def jumpSearch(data, c, v):
    langkah = v**0.5
    prev = 0
    for w in range(len(data)):
        if type(data[w]) == list:  
            output1 = jumpSearch(data[int(w)], c, len(data[int(w)]))
            # if output1 == -1:
            #     data[int(w)] = "berhasil"
            # else:
            #     print(c, "di Index", int(w), "pada kolom", output1)
            #     exit()
    while data[int(min(langkah, v)-1)] < c:
        prev = langkah
        langkah += v**0.5
        if prev >= v:
            return -1
    while data[int(prev)] < c:        
        prev += 1
        if prev == min(langkah, v):
            return -1
    if data[int(prev)] == c:
        return int(prev)
    return -1

data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
v = len(data)
print(data)
c = input("Masukkan nama yang ingin kamu cari : ")
output = jumpSearch(data, c, v)
if output == -1:
    print(c, "tidak ada")
else:
    print(c, "di Index", output)