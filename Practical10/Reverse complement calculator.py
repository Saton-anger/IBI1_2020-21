
x = input('input the sequence: ')
def con_com(a):
    seq = a.upper()
    code = {"A": 'T', "T": 'A', "C": 'G', "G": 'C'}
    com = ''
    for i in range(len(seq)):
        a = code[seq[i]]
        com = com + a
    return com
result = con_com(x)   # how this function can be called
print(result[::-1])

