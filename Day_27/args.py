test=("fdsfdsf" , 234,[3,4,5,6,7,8] , [5,7,7,8,9])
def test(*args):
    l = []
    for i in args:
        if type(i) == list:
            
            l = l + i
    return l 
