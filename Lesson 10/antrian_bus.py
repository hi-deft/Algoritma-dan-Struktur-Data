class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return "Queue: " + " ← ".join(self.items)

# Simulasi
halte = Queue()
siswa = ["Andi", "Budi", "Cici", "Dedi", "Eni", "Farah", "Gani"]

for s in siswa:
    halte.enqueue(s)

# Siswa yang naik bus pertama
naik_bus = []
for _ in range(5):
    naik_bus.append(halte.dequeue())

siswa_tersisa = halte.items

print("Siswa yang naik bus pertama:", naik_bus)
print("Siswa yang menunggu:", siswa_tersisa)