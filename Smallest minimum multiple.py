def smallest_minimum_multiple():
    num = 20
    trobat = False
    while not trobat:
        num += 1
        trobat = True
        for i in range(20,0,-1):
            if num%i != 0:
                trobat = False
                break
    return num

print(smallest_minimum_multiple())