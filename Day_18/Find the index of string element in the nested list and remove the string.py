l = [[1, 2, 3]
 [11, 12, 'b', 'b', 'b'],
 [21, 't', 223],
 [4, 5, 6],
 [7, 8, 9],
 'demo',
 12.5]

for i in l:
    if type(i) == list:
        j=0
        while j < len(i):
            if type(i[j]) is str:
                print("Index of string {} is :".format(i[j]),j)
            j = j +1
        j=0
        while j < len(i):
            if type(i[j]) is str:
                print("The string in the nested list is '{}'".format(i[j]))
                i.remove(i[j])
                continue
            j = j +1
print("List after removal of string from nested list is\r",l,'\n')
