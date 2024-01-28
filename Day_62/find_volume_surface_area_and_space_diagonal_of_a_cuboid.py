import math
 
 
# function to calculate
# Surface area
def find_surafce_area(l, b, h):
     
    # formula of surface_area = 2(lb + bh + hl)
    Surface_area = 2 * ( l * b + b * h + h * l)
     
    # Display surface area
    print(Surface_area)
 
# function to find the
# Volume of rectangular 
# prism
def find_volume(l, b, h):
     
    # formula to calculate
    # volume = (l * b*h)
    Volume = (l * b * h)
     
    # Display volume
    print(Volume)
    categories Most Used
 School Programming
 Aptitude
 Re
def find_space_diagonal(l, b, h):
     
    # formula to calculate
    # Space diagonal = square_root(l**2 + b**2 + h**2)
    Space_diagonal = math.sqrt(l**2 + b**2 + h**2)
     
    # display space diagonal
    print(Space_diagonal)
     
# Driver Code
l = 90
b = 6
h = 56
 
# surface area
# function call
find_surafce_area(l, b, h)
 
# volume function call
find_volume(l, b, h)
     
# Space diagonal function call
find_space_diagonal(l, b, h)