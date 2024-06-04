def gen_psw(n):
    psw = ''
    for i in range(1, n):
         for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                psw += str(i) + ' ' + str(j) + ', '
    return psw
for n in range(3, 21):
    psw = gen_psw(n)
    psw = psw[:-1]
    print(f'{n} - {psw[:-1]}')


