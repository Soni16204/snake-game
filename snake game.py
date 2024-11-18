# Simple Snake Game in python 3
#Import necessary liabaries
import turtle#used for grapical interface
 
import time#used for controlling time delay
 
import random#used to generate random numbers
 
 
 
 
delay = 0.1 
 
 
 
 
# Score
 
score = 0
 
high_score = 0
 
 
 
 
# Set up the screen
 
wn = turtle.Screen() # creating a screen object
 
wn.title("Snake Game") #set the title of the window
 
wn.bgcolor("green") # set the background color of the window
 
wn.setup(width=600, height=600) #set the size of the window
 
wn.tracer(0) # Turns off the screen updates
 
 
 
 
# Snake head of squre 
 
head = turtle.Turtle() #create the turtle for the snake head
 
head.speed(0) #set the speed of snake to the fastest
 
head.shape("square") # set the shape of the head
 
head.color("black") #set the color of the head
 
head.penup() # lift the pen so it does'nt drow line
 
head.goto(0,0) #position the head at the center of the screen
 
head.direction = "stop" # set the direction of the head
 
 
 
 
# Snake foood
 
food = turtle.Turtle() # create the turtle object for the food
 
food.speed(0) # set the speed of food to the fastest
 
food.shape("circle") # set the shape of food
 
food.color("red") # set the color of the food
 
food.penup() # lift the pen so it does'nt draw line
 
food.goto(0,100) # position the at the random spot of the screen
 
 
# create a list to store the snake's body segments
 
segments = [] 
 
 
 
 
# Pen for writing score 
 
pen = turtle.Turtle() #create turtle object for scrore
 
pen.speed(0) # set speed 
 
pen.shape("square") # set the color of the text
 
pen.color("white") # set the color of the text
 
pen.penup() # lift the pen so it does'nt draw line
 
pen.hideturtle() # hide the turtle
 
pen.goto(0, 260) #position the pen at the top of the screen 
 
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
 # display the score
 
 
 
# Functions for moments and stuff
 
def go_up():
 
  if head.direction != "down": # prevent the snake from going in the oposite direction
 
      head.direction = "up" #change direction to "up"
 
 
 
 
def go_down():
 
  if head.direction != "up":#prevent the snake from going in the oposite direction
 
      head.direction = "down"#change direction to "down"
 
 
 
 
def go_left():
 
  if head.direction != "right":#prevent the snake from going in the oposite direction
 
      head.direction = "left"#change direction to "left"
 
 
 
 
def go_right():
 
  if head.direction != "left":# prevent the snake from going in the oposite direction
 
      head.direction = "right"#change direction to "right"
 
 
 
# function to move the snake based on its direction
def move():
 
  if head.direction == "up":#if the direction is up
 
      y = head.ycor()#get the current y-coordinates of the head
 
      head.sety(y + 20)#move the head 20 units to the upward
 
 
 
 
  if head.direction == "down":#if the direction is down
 
      y = head.ycor()#get the current y-coordinates of the head
 
      head.sety(y - 20)#move the head 20 units to the downward
 
 
 
 
  if head.direction == "left":#if the direction is left
 
      x = head.xcor()#get the current x-coordinates of the head
 
      head.setx(x - 20)#move the head 20 units to the leftward
 
 
 
 
  if head.direction == "right":#if the direction is right
 
      x = head.xcor()#get the current x-coordinates of the head
 
      head.setx(x + 20)#move the head 20 units to the rightward
 
 
 
 
# Keyboard bindings/setting up keyboards keys
 
wn.listen() # listen for keypress events
 
wn.onkeypress(go_up, "w") # when "w" is pressed , call the go_up
 
wn.onkeypress(go_down, "s")# when "s" is pressed , call the go_down
 
wn.onkeypress(go_left, "a")# when "a" is pressed , call the go_left
 
wn.onkeypress(go_right, "d")# when "d" is pressed , call the go_right
 
 
 
 
# Main game loop
 
while True:
 
  wn.update()#update the screen
 
 
 
 
  # Check for a collision with the bodr
 
  if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:#if the snake hits the edge
 
      time.sleep(1)#pause the game for one second
 
      head.goto(0,0)# reset the snake head position to the center
 
      head.direction = "stop"# stop the snake moment
 
 
 
 
      # Hide the segments
 
      for segment in segments:
 
          segment.goto(1000, 1000)
 
     
 
      # Clear the segments list
 
      segments.clear()
 
 
 
 
      # Reset the score
 
      score = 0
 
 
 
 
      # Reset the delay
 
      delay = 0.1
 
 
 
      # update the score display
      pen.clear()#clear the old score
 
      pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
 
 
 
 
 
 
 
  # Check for a collision with the food
 
  if head.distance(food) < 20:#if the snake is close the food 
 
      # Move the food to a random spot
 
      x = random.randint(-290, 290)
 
      y = random.randint(-290, 290)
 
      food.goto(x,y)#move the food to the new coordinates
 
 
 
 
      # Add a segment
 
      new_segment = turtle.Turtle()#create new turtle object for the segment
 
      new_segment.speed(0)#set the speed 
 
      new_segment.shape("square")#set the shape of segment
 
      new_segment.color("grey")#set the color of the segment
 
      new_segment.penup()#lift the pen so it does'nt draw line 
 
      segments.append(new_segment)#add the new segment
 
 
 
 
      # Shorten the delay
 
      delay -= 0.001
 
 
 
 
      # Increase the score
 
      score += 10
 
 
 
      # update the high score
      if score > high_score:
 
          high_score = score
 
     
      # update the score display
      pen.clear()#clear the old score
 
      pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
 
 
 
 
  # Move the end segments first in reverse order
 
  for index in range(len(segments)-1, 0, -1):#loop through segment in reverse order
 
      x = segments[index-1].xcor()#get the x-coordinates of the previous segment
 
      y = segments[index-1].ycor()#get the y-coordinates of the previous segment
 
      segments[index].goto(x, y)#move the current segment to the position of the previous one
 
 
 
 
  # Move segment 0 to where the head is
 
  if len(segments) > 0:
 
      x = head.xcor()#get thex-coordinates of the head
 
      y = head.ycor()#get they-coordinates of the head
 
      segments[0].goto(x,y)#move the first segment to the head's position
 
 
 
 
  move()  # move the snake based on its direction
 
 
 
 
  # Check for head collision with the body segments
 
  for segment in segments:
 
      if segment.distance(head) < 20:#if a segment is closed to the head
 
          time.sleep(1)#pause the game for one second
 
          head.goto(0,0)#reset the snake head position to the center
 
          head.direction = "stop"#stop the snake movement
 
     
 
          # Hide the segments
 
          for segment in segments:
 
              segment.goto(1000, 1000)#move each segment offscreen 
 
     
 
          # Clear the segments list
 
          segments.clear()
 
 
 
 
          # Reset the score
 
          score = 0
 
 
 
 
          # Reset the delay
 
          delay = 0.1
 
     
 
          # Update the score display
 
          pen.clear()#clear the old score
 
          pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
 
 
 
 
  time.sleep(delay)
 
 
 
 
wn.mainloop()