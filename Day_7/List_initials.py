l=['janhvi',4567,False,34.6,[8,5,'go']]
for i in l :
    if type(i) == list:
        n = 0
        for  j in i :
            if type(j) == int :
                n = n + j
        print(n)
                
        print(type(j))
