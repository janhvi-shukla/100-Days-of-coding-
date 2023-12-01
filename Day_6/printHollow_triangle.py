rows = 3
columns = 6

# Loop through number of rows
for i in range(rows):
    
    # Loop through number of columns
    for j in range(columns):
        
        # Printing Pattern
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
