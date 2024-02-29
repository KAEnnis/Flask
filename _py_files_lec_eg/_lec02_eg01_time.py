# Prompt the user for input
seconds = int(input("Enter an integer for seconds: "))

# Get minutes and remaining seconds
minutes          = 0    # Find minutes in seconds
remaining_seconds = 0   # Seconds remaining
print(seconds, "seconds is", minutes,  
    "minutes and", remaining_seconds, "seconds")


#TASK: Now alter to import time and use time.time()
#       instead of user input of seconds
# import time

# currentTime = time.time() # Get current time

# # Obtain the total seconds since midnight, Jan 1, 1970
# totalSeconds = int(currentTime)

# # Get the current second 
# currentSecond = totalSeconds % 60 

# # Obtain the total minutes
# totalMinutes = totalSeconds // 60 

# # Compute the current minute in the hour
# currentMinute = totalMinutes % 60

# # Obtain the total hours
# totalHours = totalMinutes // 60

# # Compute the current hour
# currentHour = totalHours % 24

# # Display results
# print("Current time is", currentHour, ":", 
#     currentMinute, ":", currentSecond, "GMT")
