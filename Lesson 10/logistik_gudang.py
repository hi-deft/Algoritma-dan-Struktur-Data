# Implementasi Stack untuk gudang
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def __repr__(self):
        return "Stack: " + " → ".join(self.items)

# Implementasi Queue untuk truk
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def __repr__(self):
        return "Queue: " + " ← ".join(self.items)

# Simulasi
gudang = Stack()
barang_masuk = ["Sabun", "Sikat Gigi", "Shampoo"]

for b in barang_masuk:
    gudang.push(b)

# Keluarkan 2 barang untuk dikirim
truk = Queue()
for _ in range(2):
    truk.enqueue(gudang.pop())

# Barang terakhir sampai di toko (dikeluarkan dari antrian)
barang_terkirim = []
while not truk.is_empty():
    barang_terkirim.append(truk.dequeue())

print("Isi tumpukan di gudang:", gudang.items)
print("Urutan pengiriman ke toko:", " → ".join(barang_terkirim))
print("Barang terakhir sampai di toko:", barang_terkirim[-1])