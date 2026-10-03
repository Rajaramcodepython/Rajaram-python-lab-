#find the touple maximum number of common element 
tuples = [(1, 2, 3), (2, 3, 4), (2, 3, 5), (1, 4, 5)]

common = set(tuples[0])

for t in tuples[1:]:
    common = common.intersection(t)

print("Common elements:", common)
print("Number of common elements:", len(common))
