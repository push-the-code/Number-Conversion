def bin_to_dec (str):
    dec = 0
    for i in range(len(str)):
        num = int(str[i])
        dec += num * pow(2, i)
    print(dec)
    
bin_to_dec("110011")
