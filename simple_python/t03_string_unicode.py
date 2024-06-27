print('26\u00B0')
print('26\N{DEGREE SIGN}')

# in the following, \N is not expanded 
print(r'26\u00B0\n')

print()

print('we spent \u20ac1.23M for an original C\u00e9zanne')
print("Romance in F\u266F Major")
print()
data = ['\U0001F95A', '\U0001F414']
print("unsorted:", data)
print("sorted:", sorted(data))
