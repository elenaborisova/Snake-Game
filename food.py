import config

x = (random(config.SCREEN_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
y = (random(config.SCREEN_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
food_pos = [x, y]
food_img = None


def show():
    image(food_img, food_pos[0], food_pos[1], config.SCALE, config.SCALE)
    

def reset():
    x = (random(config.SCREEN_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
    y = (random(config.SCREEN_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
    food_pos[0] = x
    food_pos[1] = y
