
#make a list of start and stop positions for each number
#make a list of the positions of the symbols

#import the txt and read using numpy

with open('day3.txt') as f:
    data = f.readlines()
    symbols = []
    gears = []
    numbers_start =[]
    numbers_stop = [] 
    total = 0
    total2 = 0
    #make the lists of the positions of the symbols
    for i in range(len(data)):
        onNumber = False
        for j in range (len(data[i])) :
            char = data[i][j]
            if char.isdigit() == False and char != '.' and char != ' ' and char != '\n':
                symbols.append([i,j])
            #make the lists of the start and stop positions for each number
            if(onNumber == False and char.isdigit() == True):
                numbers_start.append([i,j])
                onNumber = True
            if(onNumber == True and char.isdigit() == False):
                numbers_stop.append([i,j-1])
                onNumber = False
        if(onNumber == True):
            numbers_stop.append([i, len(data[i]) - 1])    
    #make the list of sybol index -> number of words adjacent to it
    for i in range (len(symbols)):
        gears.append([])
    
    #now add the number to the total if it is adjacent to a symbol
    
    for i in range(len(numbers_start)):
        #get the row of the number
        add = False
        row = numbers_start[i][0]
        #get the column of the number start and end
        start = numbers_start[i][1]
        stop = numbers_stop[i][1]
        #get the number
        number = int(data[row][start:stop+1])
        #check if the number is adjacent to a symbol - in row above, same row, or row below
        for j in range(start-1, stop+2):
        #for each number, check if it is adjacent to a symbol and mark that symbol as ++
            if [row,j] in symbols: 
                symbol_index = symbols.index([row, j])
                gears[symbol_index].append(number)
                add = True
            if [row-1,j] in symbols:
                symbol_index = symbols.index([row-1, j])
                gears[symbol_index].append(number)
                add = True
            if [row+1,j] in symbols:
                symbol_index = symbols.index([row+1, j])
                gears[symbol_index].append(number)
                add = True
        if add == True:
            total += number
    #count numbers adj to each symbol
    #for each symbol, check if it is a start and adjacent to 2 numbers
    #if yes, add their product to the total
    for i in range(len(symbols)):
        x_axis = symbols[i][1]
        y_axis = symbols[i][0]
        if len(gears[i]) == 2 and data[y_axis][x_axis] == '*':
            total2 += gears[i][0] * gears[i][1]
        
    print(total2)
