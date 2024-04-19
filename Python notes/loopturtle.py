import turtle

# Initialize turtle
turtle.showturtle()
turtle.shape("turtle")

# Initial length and angle
length = 10
angle = 90

# Draw square spiral
for _ in range(16):  # Repeat 16 times
    turtle.forward(length + length)  # Move forward
    turtle.right(angle)  # Turn right
    length += 10  # Increase length by 10

# Keep the window open
turtle.done()
