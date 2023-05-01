from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("The Snake")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.newfood()
        snake.evolve()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_on = False
        score.game_over()
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()


