import time

# Time solution started
start_time = time.time()

# Names txt are both located in names folder
f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Create empty list
duplicates = []
# Set method sorts iterable sequence and returns dictionary
a = set(names_1)
b = set(names_2)

# Adds sorted dictionary to list 
duplicates.append(str(a & b))

print(len(a & b), 'duplicates')

# Time solution ended
end_time = time.time()
print(f"{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
