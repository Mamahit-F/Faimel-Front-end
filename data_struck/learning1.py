A = set([1, 2, 3, 4, 5])
B = set([5, 6, 7, 1, 2, 3,])
Union = A | B
irisan = A & B
irisan.discard(1)
selisih = B - A

print("Gabungan: ", Union)
print("Irisan: ", irisan)
print("selisih: ", selisih)