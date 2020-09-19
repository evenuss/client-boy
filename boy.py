import random

print('========   MY PYTHON PROGRAM   ========')
print('                 V0.1                  ')

userInput = input('Masukan 4 nomor :')

# l = [int(i) for i in l]


while True:
    l = userInput.split(',')
    sf = random.shuffle(l)
    # print(l)
    ops = ['+','-','*','/']
    random.shuffle(ops)
    rops1 = random.choice(ops)
    rops2 = random.choice(ops)
    rops3 = random.choice(ops)
    opf = "("+l[0]+rops1+l[1]+")"+rops2+l[2]+rops3+l[3]
    # print(opf)
# while True:
    op = eval((l[0]+rops1+l[1])+rops2+l[2]+rops3+l[3])
    if op == 24:
        print(opf)
        print(op)
        print('find')
        break
    else:
        print(opf)





# print(b)
# print(l)