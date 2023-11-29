def is_leap(year):
    leap = False
    if int(year) % 4 == 0 and int(year)% 100 != 0 :
        leap = True
        return leap
    elif int(year) %  400 == 0 :
        leap = True
        return leap
    elif int(year) %4 != 0 :
        leap = False
        return leap
    
    return leap
    
    
    
    
    return leap

year = int(input())
