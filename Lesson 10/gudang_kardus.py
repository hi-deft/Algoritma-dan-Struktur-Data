class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return "Stack: " + " → ".join(self.items)

# Simulasi
gudang = Stack()
kardus = ["A", "B", "C", "D", "E"]

for k in kardus:
    gudang.push(k)

# Mengeluarkan 3 kardus
for _ in range(3):
    gudang.pop()

print("Kardus tersisa di gudang (dari bawah ke atas):", gudang.items)