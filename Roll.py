import random 
import time


# Function for time conversion and printing out proper grammer
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
        print(round(time_value, 3))    
    

# Initializing the range variables    
stack1 = [*range(1,6)]
stack2 = [*range(1,6)]

# shuffling the variables before the while loop starts
random.shuffle(stack1)
random.shuffle(stack2)

#counters 
iterations = 0
match = 0
tmatch = 0
start = time.time()
status = " Still Trying....."

# Main while loop to iterate through the zipped lists 
while tmatch < max(stack1):
    iterations += 1
    match = 0
    random.shuffle(stack1)
    random.shuffle(stack2)

    for (zip1,zip2) in zip(stack1,stack2) :
        if zip1 == zip2 :
            match += 1
        elif zip1 != zip2:
            continue

    if match > tmatch : 
        tmatch = match
        match = 0
    if tmatch == max(stack1):
        status = "Completed"
    
    print(f"Current Status : {status} | Iterations = {iterations} | {tmatch}  Max matches found" , end="\r")  
   
end = time.time() - start   # end of the timer used to call into the function    


# Final print statments 
print()
all_time(end)
print("Final position for list one: ",stack1)
print("Final Position for list two: ", stack2)





     
