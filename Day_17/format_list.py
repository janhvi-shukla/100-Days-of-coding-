l=[[4,5,"Sameer","Sameer","Sameer"],[346,7,3426,76],[34657,"Jadhav",74557,45,6],23095,'ineuron']
l.append([67,67])
l.append([55,55])
l.insert(3,3+6j)
l

for i in l:
    if type(i)==list:
        for j in i:
            if type(j)== str:
                print (" got {} string at {} location".format(j,i))
                i.remove(j)
                print(i)
