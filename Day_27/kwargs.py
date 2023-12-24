def test2(**kwargs):
    for i in kwargs.items():
        if type(i[1])== list :
            if "sudh" in i[1] :
                print("i am able to find your name in input data ")
                print(i[1])
    return kwargs
test18(b =6 , c = [4,5,6,7] , d = ["sudh" , "kumar " , 5.67], n = 6 + 7j)
