binary = "1111"
dec = 0

for i in range(len(binary)):
    num = int(binary[i])
    dec = dec + num * pow(2, i)
    
    
print(dec)
