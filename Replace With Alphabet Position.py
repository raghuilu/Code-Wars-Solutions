def alphabet_position(text):
    res=""
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in text:
        if(letter.isupper() and letter in alpha):
            res+=str(ord(letter)-64)+" "
        elif(letter.islower() and letter in alpha):
            res+=str(ord(letter)-96)+" "
        else:
             continue
    return res[:-1]
