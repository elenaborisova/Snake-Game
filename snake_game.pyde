import config
import snake
import food
import result
import os


def end_screen():
    background(0)
    fill(255)
    textSize(64)
    text("GAME OVER", config.SCREEN_WIDTH // 5, config.SCREEN_HEIGHT // 2)
    
    if result.score > result.highscore:
        textSize(32)
        text("New High Score!", config.SCREEN_WIDTH // 3.4, config.SCREEN_HEIGHT // 5)


def setup():
    size(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    frameRate(8)
    
    if os.path.exists(config.HIGHSCORE_FILE_PATH):
        with open(config.HIGHSCORE_FILE_PATH, "r") as file:
            result.highscore = int(file.read())
            
    food.food_img = loadImage("images/apple.png")
    snake.snake_head_img = loadImage("images/snake_head.png")
    
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    result.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
        result.score += 1
        
    if snake.eats_self():
        end_screen()
        result.set_highscore()
        noLoop()
    
    
def keyPressed():
    if keyCode == UP and not config.CURR_DIRECTION == "down":
        config.CURR_DIRECTION = "up"
    elif keyCode == DOWN and not config.CURR_DIRECTION == "up":
        config.CURR_DIRECTION = "down"
    elif keyCode == RIGHT and not config.CURR_DIRECTION == "left":
        config.CURR_DIRECTION = "right"
    elif keyCode == LEFT and not config.CURR_DIRECTION == "right":
        config.CURR_DIRECTION = "left"
        
