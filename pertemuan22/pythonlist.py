# List 
#==========================
# List adalah variabel yand dapat menyimpan banyak data

# fruits= ["apple," "banana", "cherry"]

Rio = ["faimel", "faith", "ralf", "jeiner", "jey", "greefine",]
print(Rio)
# Access List item
# Dimulai dari 0
print(Rio[1]) #faith
# index negtive
print(Rio[-1]) #greefine
print(Rio[-2]) #jey
# Range of index
print(Rio[1:4]) #faith, ralf, jeiner
print(Rio[:4]) #faimel, faith, ralf, jeiner
print(Rio[2:]) #ralf, jeiner, jey, greefine
print(Rio[-3:-1]) #jeiner, jey

# ceck if item exist
if "faimel" in Rio:
    print("yes")
else:
    print("No")

# change list item
Rio[2] = "banana"
print(Rio)
Rio[1:2] = ["lemon", "kiwi"]
print(Rio)
Rio.insert(2, "Manggo") #Insert di tengah
print(Rio)
Rio.append("Dragon Fruits") #Insert di akhir
print(Rio)

# Looping list
for i in Rio:
    print(i)
for i in range(len(Rio)):
    print(Rio[i])

 

