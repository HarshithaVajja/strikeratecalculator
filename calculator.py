#Batting strike rate Calculator
#Runs per 100 balls

# Display a welcome message
print("Welcome to the batting strike rate Calculator created by HarshithaVajja ")  

 # Get the batsman's name from the user
name=input("please enter the name of the batsman ") 

 # Get the runs scored as input (string)
r=input("please enter the Runs scored by the batsman ") 

 # Get the balls played as input (string)
b=input("please enter the number of Balls played by the batsman ") 

 # Convert the runs scored and balls played to integers
r=int(r) 

# Convert the balls played from string to integer
b=int(b) 

# Calculate the batting average 
avg=r/b 

# Calculate the strike rate
sr=avg*100

# Display the batsman's name and strike rate
print("The strike rate of",name,"is",sr) 
