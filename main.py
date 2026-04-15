# 1
class Universitet:
    def __init__(self, n, sh, t):
        self.nomi = n
        self.shahar = sh
        self.talabablar_soni = t

a = Universitet("TATU", "Toshkent", 20000)
print(a.nomi, a.shahar, a.talabablar_soni)

b = Universitet("SamDU", "Samarqand", 15000)
print(b.nomi, b.shahar, b.talabablar_soni)

# 2
class Film:
    def __init__(self, n, j, d, r):
        self.nomi = n
        self.janr = j
        self.davomiyligi = d
        self.reytingi = r

a = Film("Inception", "fantastik", 148, 9)
print(a.nomi, a.janr, a.davomiyligi, a.reytingi)

b = Film("Titanic", "darma", 195, 8)
print(b.nomi, b.janr, b.davomiyligi, b.reytingi)

# 3
class Dokon:
    def __init__(self, n, m, t):
        self.nomi = n
        self.manzil = m
        self.turi = t

a = Dokon("Korzinka","Toshkent", "supermarket")
print(a.nomi, a.manzil, a.turi)

b = Dokon("Havas", "Samarqand", "market")
print(b.nomi, b.manzil, b.turi)

# 4
class Hayvon:
    def __init__(self, n, t, y, r):
        self.nomi = n
        self.turi = t
        self.yili = y
        self.rangi = r

a = Hayvon("Rex", "it", 3, "qora")
print(a.nomi, a.turi, a.yili, a.rangi)

b = Hayvon("Mushukcha", "mushuk", 2, "oq")
print(b.nomi, b.turi, b.yili, b.rangi)

c = Hayvon("Simba", "sher", 5, "sariq")
print(c.nomi, c.turi, c.yili, c.rangi)

# 20
class Kompuyuter:
    def __init__(self, p, o, d, n):
        self.protsessor = p
        self.operativ_xotira = o
        self.disk = d
        self.narx = n

a = Kompuyuter("Intel i5", "8GB", "512GB SSD", 700)
print(a.protsessor, a.operativ_xotira, a.disk, a.narx)

b = Kompuyuter("Intel i7", "16GB", "1TB SSD", 12000)
print(b.protsessor, b.operativ_xotira, b.disk)
