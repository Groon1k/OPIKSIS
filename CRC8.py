def degrees (V):
    M, polynom = 0, []
    for i in range(len(V)):
        M += 2 ** int(V[i])
    M = bin(M)[2:]
    for k in range(len(M)):
        polynom.append(int(M[k]))
    return polynom
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def idi (mes, por):
    while len(mes)>=len(por):
        if mes[0]==1:
            for j in range(len(por)):
                mes[j]=mes[j]^por[j]
        elif((mes[0]==0) and (len(mes)>=len(por))):
            mes.remove(mes[0])
    return mes
ch=text_to_bits(input()) #message to binary notation
ms, pr = [], [] #empty list for checksum #empty list for check
crc8 = degrees(input('enter your degrees of the polynomial:'))
print(crc8)
for i in range (len(ch)):
    ms.append(int(ch[i]))
    pr.append(int(ch[i]))
print(ms)
for j in range(len(crc8)-1):
    ms.append(0)
ms = idi(ms, crc8)
print(ms)
for i in range(len(ms)):
    pr.append(int(ms[i]))
pr = idi(pr, crc8)
print(pr)
