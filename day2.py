from typing import List
file_path = "day2.txt"
def set_max(line: List[str]) -> int:
    #grab the max for each color in the segment and return them all multiplied together
    red_max = -1
    green_max = -1
    blue_max = -1
    for segment in line:
        segment = segment.strip()
        index = 1
        while(segment[0:index+1].isdigit()):
            index += 1
        #get the number of the color
        number = int(segment[0:index])
        #get the color
        color = segment[index+1:]
        color = color.strip()
        #set max based on color
        if("red" in color):
            if(number > red_max):
                red_max = number
        elif("green" in color):
            if(number > green_max):
                green_max = number
        elif("blue" in color):
            if(number > blue_max):
                blue_max = number
    return red_max * green_max * blue_max
def check_possible(line: List[str]):
    #take the list of string and check if each color is correct 
    for segment in line:
        segment = segment.strip()
        index = 1
        while(segment[0:index+1].isdigit()):
            index += 1
        #get the number of the color
        number = int(segment[0:index])
        #get the color
        color = segment[index+1:]
        color = color.strip()
        #set max based on color
        max = 0 
        if("red" in color):
            max = 12
        elif("green" in color):
            max = 13
        elif("blue" in color):
            max = 14
        if(number > max):
            return False
    return True
try:
    with open(file_path, "r") as file:
        total: int = 0
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        #replace : and ; with , 
        lines = [line.replace(":",",") for line in lines]
        lines = [line.replace(";",",") for line in lines]
        # Perform operations on the list of strings
        for i in range(len(lines)):
            #game number = i+1
            line = lines[i].split(",")
            #remove the first section of the list - game number
            line = line[1:]
            #check if the list is correct
            if(check_possible(line)):
                total += 1 + i
        print(total)        
except FileNotFoundError:
    print("File not found.")
