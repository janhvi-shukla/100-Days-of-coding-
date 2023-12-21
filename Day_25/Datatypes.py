def fun1(*args):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    for i in args:
        if type(i)==int:
            a.append(i)
        if type(i)==float:
            b.append(i)
        if type(i)==str:
            c.append(i)
        if type(i)==tuple:
            d.append(i)
        if type(i)==list:
            e.append(i)
        if type(i)==dict:
            f.append(i)
        if type(i)==bool:
            g.append(i)
    return a,b,c,d,e,f,g
