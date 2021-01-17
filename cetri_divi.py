import random
no_cik = int(input('no '))
lidz_cik = int(input('lidz '))

iespejamie = [i for i in range(no_cik, lidz_cik+1)]
print(iespejamie)
minejumi = 0
while True:
    a = random.choice(iespejamie)
    print(f'Skaitlis ir {a}')
    minejumi += 1
    atbilde = input()
    if atbilde == 'mazaks':
        iespejamie = iespejamie[0:iespejamie.index(a)]
        print(iespejamie)
    elif atbilde == 'lielaks':
        iespejamie = iespejamie[iespejamie.index(a)+1: len(iespejamie)]
        print(iespejamie)
    else:
        break
print(f'Uzminēja {minejumi} {"minējumos" if minejumi > 1 else "minējumā"}')