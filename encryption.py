string = input("what is the message ")
key =int(input"what is the numer of the key ") 
encryption = ""

for i in range(0,len(string)):
    x = ord(string[i])
    if x in range(97, 123):
        x += key
        if x > 122:
            x = 96 + x - 122
    


    encryption += chr(x)

print(encryption)




print(decryption)

for i in range(0,len(string)):
    x = ord(string[i])
    if x in range(97, 123):
        x -= key
        if x > 122:
            x = 96 + x - 122
    


    encryption += chr(x)