from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

moveType = 0        # 운동 모양
x = 400             # 캐릭터 x좌표
y = 90              # 캐릭터 y좌표
moveDirection = 0   # 사각운동 좌표
countCircle = 0     # 원운동 각도
r = 300               # 원운동 반지름

while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    # 사각운동
    if moveType == 0:
        if moveDirection == 0:
            x = x + 2
            character.draw_now(x, y)
            if x > 800:
                x = 800
                moveDirection += 1
            if x == 400-2:  # moveType 변화(temp)
                x = 400
                moveType += 1
        elif moveDirection == 1:
            y = y + 2
            character.draw_now(x, y)
            if y > 600:
                y = 600
                moveDirection += 1
        elif moveDirection == 2:
            x = x - 2
            character.draw_now(x, y)
            if x < 0:
                x = 0
                moveDirection += 1
        elif moveDirection == 3:
            y = y - 2
            character.draw_now(x, y)
            if y < 90:
                y = 90
                moveDirection = 0     
        
    # 원 운동
    else:
        countCircle += 1
        x = r * math.cos((countCircle-90) / 180 * math.pi)+400    # 각도가 270도에서 시작하도록 countCircle에 -90을 적용
        y = r * math.sin((countCircle-90) / 180 * math.pi)+390
        character.draw_now(x, y)      
        if countCircle > 360:    # moveType 변화
            countCircle = 0
            moveType = 0
            x = 400
            y = 90
        

    
close_canvas()
