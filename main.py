class Number_Conversion:
    def bin_to_dec (str):
        dec = 0
        for i in range(len(str)):
            num = int(str[i])
            dec += num * pow(2, i)
        print(dec)
    
    def dec_to_bin(int):
        bin = ""
        while int > 0:
            bin += str(int % 2)
            int //= 2
        print(bin)
    
n = Number_Conversion
