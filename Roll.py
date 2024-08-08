# Made by Jfetto 
# Roll


import random 
import time
import os

# Function for time conversion and printing out proper grammer probably a little excessive but its a fun function
def all_time(time_value):
    time = int(time_value)
    seconds = time
    minutes = 0 
    hours = 0
    if seconds >= 60 :
        minutes += 1 
        seconds -= 60
    if minutes >= 60:
        hours += 1
        minutes -= 60
   
    if hours == 1 :
        print(hours,"Hour ", end="")
    elif hours != 1 :
        print(hours, "Hours ", end="")
    if minutes == 1 :
        print(minutes,"Minute ", end="")
    elif minutes != 1 :
        print(minutes, "Minutes ",end="")
    if seconds == 1 :
            print(seconds, "Second ")
    elif seconds > 1 :
        print(seconds, "Seconds ")
    if seconds < 1 : 
        print(round(time_value, 3),"Seconds")    
    

# Initializing the range variables  n-1  
stack1 = [*range(1,10)]
stack2 = [*range(1,10)]

# shuffling the variables before the while loop starts
random.shuffle(stack1)
random.shuffle(stack2)

#counters 
iterations = 0
match = 0
tmatch = 0
start = time.time()
# Things for f(strings)
status = " Still Trying....."
if_found = "Matches Found"

# Main while loop to iterate through the zipped lists 
while tmatch < max(stack1):
    iterations += 1
    match = 0
    random.shuffle(stack1)
    random.shuffle(stack2)

    # Main while loop
    for (zip1,zip2) in zip(stack1,stack2) :
        if zip1 == zip2 :
            match += 1
            print(f"Current Status : {status} | Iterations = {iterations} | {tmatch} Matches Found " , end="\r")  
        elif zip1 != zip2:
            continue
    # clears out the match variable and gives it to tmatch
    if match > tmatch : 
        tmatch = match
        match = 0
    # changes status in the f string not really needed anymore but i like it 
    if tmatch == max(stack1):
        status = "!-Completed-!"
        #time.sleep(2)
        os.system("clear") # will only work on linux
        print (f"<(0_0<) <(0_0)> (>0_0)> ")
        print(f"{status} | Iterations = {iterations} | {tmatch}  Matches Found" , end="\r")  
   
end = time.time() - start   # end of the timer used to call into the function    


# Final print statments 

# stopping the clock for the function 
all_time(end)
print()
print("Final position for list one: ",stack1)
print("Final Position for list two: ", stack2)





     
