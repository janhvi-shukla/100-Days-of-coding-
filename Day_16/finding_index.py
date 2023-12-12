l = [[1,2,3,4],[5,6,7,"hello",8],[8,7,66],2,6]
l.append([2,3,4])
l.append(8+6j)
l.append([5,6,7])
for i in l:

  if type(i) == list:
    for j,v in enumerate(i):
      
      if type(v) == str:
        print("index of string: ",j)
        i[j]="hi"
    print(i[1])
print(l)
