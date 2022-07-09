# I create a list with all numbers from 0 to 999 that are multiples of 3 or 5 and we sum all them and print the result
print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))