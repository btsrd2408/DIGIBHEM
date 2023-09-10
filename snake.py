import turtle
import random
import time

# Set up the game screen
screen = turtle.Screen()
screen.title("Snake Game Project")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#7393B3")

# Draw boundaries
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.pensize(4)
border_pen.penup()
border_pen.goto(-350, 357)
border_pen.pendown()
for _ in range(4):
    border_pen.forward(700)
    border_pen.right(90)
border_pen.hideturtle()

# Initialize the game
score = 0
delay = 0.1
food_collection = []

# Create snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Create food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(30, 30)

# Display score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-240, 290)
score_display.write("Score: ", align="center", font=("calibri", 25, "bold"))

# Movements
def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up":
        snake.direction = "down"

def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)

# User input
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Game loop
while True:
    screen.update()

    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        score += 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("calibri", 25, "bold"))
        delay -= 0.001

        # Add new food to collection
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("white")
        new_food.penup()
        food_collection.append(new_food)

    # Move snake's body
    for index in range(len(food_collection) - 1, 0, -1):
        food_collection[index].goto(food_collection[index - 1].pos())

    # Move first body segment to where the head is
    if len(food_collection) > 0:
        food_collection[0].goto(snake.pos())

    # Move the snake
    snake_move()

    # Collision detection and game over
    if (
        snake.xcor() > 340
        or snake.xcor() < -340
        or snake.ycor() > 340
        or snake.ycor() < -340
    ):
        time.sleep(1)
        screen.clear()
        screen.bgcolor("black")
        score_display.goto(0, 0)
        score_display.write(
            "Game Over\nYour Score: {}".format(score),
            align="center",
            font=("calibri", 30, "bold"),
        )
        break

    # Check for collision with snake's body
    for foods in food_collection:
        if foods.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("magenta")
            score_display.goto(0, 0)
            score_display.write(
                "Game Over\nYour Score: {}".format(score),
                align="center",
                font=("calibri", 30, "bold"),
            )
            break

    time.sleep(delay)

# Cleanup
turtle.bye()
