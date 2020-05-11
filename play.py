# encoding: utf-8
import os
import random
import sys

import pygame
from pygame.locals import *

# 初始位置.
CONST_STARTING_1P_POS_X = 8
CONST_STARTING_1P_POS_Y = 8
CONST_STARTING_2P_POS_X = 56
CONST_STARTING_2P_POS_Y = 40

# 視窗大小.
canvas_width = 800
canvas_height = 600

# 遊戲區大小.
game_area_width  = 64
game_area_height = 48

# 顏色.
block = (0,0,0)             # 黑.
green = (38, 220, 22)       # 綠.

# 遊戲區陣列.
gameAreaArray =[[0]*game_area_height for i in range(game_area_width)]

# 除錯訊息.
debug_message = False

#-------------------------------------------------------------------------
# 1P開始位置.
game1P_x = CONST_STARTING_1P_POS_X
game1P_y = CONST_STARTING_1P_POS_Y
# 前進方向.
# 0:上 1:下 2:左 3:右.
game1P_direction = 1

#-------------------------------------------------------------------------
# 2P開始位置.
game2P_x = CONST_STARTING_2P_POS_X
game2P_y = CONST_STARTING_2P_POS_Y
# 前進方向.
# 0:上 1:下 2:左 3:右.
game2P_direction = 0

# 分數.
score1P = 0
score2P = 0

# 玩家失敗.
# 0:無.
# 1:1P.
# 2:2P.
playFial = 0

# 每秒執行主迴圈次數.
fps = 8

# 重新開始時間.
restartTime = 0

# 遊戲模式.
# 0:遊戲結束.
# 1:遊戲中.
gameMode = 0

# 1P或2P移動
# 1P:True.
# 2P:False.
move = True

#-------------------------------------------------------------------------
# 函數:秀字.
#-------------------------------------------------------------------------
def showFont( text, x, y, color):
    global canvas
    text = font_24.render(text, True, color) 
    canvas.blit( text, (x,y))

#-------------------------------------------------------------------------
# 函數:判斷邊界-1P.
#-------------------------------------------------------------------------
def ifBoundary1P(direction):
    global gameAreaArray, game1P_x, game1P_y, playFial, score2P
    
    # 判斷邊界.
    if(game1P_x > game_area_width-2):
        game1P_x = game_area_width-1
    elif(game1P_x < 1):
        game1P_x = 0
    if(game1P_y > game_area_height-2):
        game1P_y = game_area_height-1
    elif(game1P_y < 1):
        game1P_y = 0

    # 設定失敗.
    if(gameAreaArray[game1P_x][game1P_y] != 0):
        playFial = 1
        gameAreaArray[game1P_x][game1P_y] = 2
        # 加對方分數.
        score2P += 1
    else:
        # 箭頭.            
        if(direction==0):
            gameAreaArray[game1P_x][game1P_y] = 10
        elif(direction==1):
            gameAreaArray[game1P_x][game1P_y] = 11                
        elif(direction==2):
            gameAreaArray[game1P_x][game1P_y] = 12
        elif(direction==3):
            gameAreaArray[game1P_x][game1P_y] = 13            

#-------------------------------------------------------------------------
# 函數:判斷邊界-2P.
#-------------------------------------------------------------------------
def ifBoundary2P(direction):
    global gameAreaArray, game2P_x, game2P_y, playFial, score1P
    
    # 判斷邊界.
    if(game2P_x > game_area_width-2):
        game2P_x = game_area_width-1
    elif(game2P_x < 1):
        game2P_x = 0
    if(game2P_y > game_area_height-2):
        game2P_y = game_area_height-1
    elif(game2P_y < 1):
        game2P_y = 0

    # 設定失敗.
    if(gameAreaArray[game2P_x][game2P_y] != 0):
        playFial = 2
        gameAreaArray[game2P_x][game2P_y] = 2
        # 加對方分數.
        score1P += 1
    else:
        # 箭頭.            
        if(direction==0):
            gameAreaArray[game2P_x][game2P_y] = 20
        elif(direction==1):
            gameAreaArray[game2P_x][game2P_y] = 21                
        elif(direction==2):
            gameAreaArray[game2P_x][game2P_y] = 22
        elif(direction==3):
            gameAreaArray[game2P_x][game2P_y] = 23

#-------------------------------------------------------------------------
# 函數:重新開始遊戲.
#-------------------------------------------------------------------------
def restart():
    global gameAreaArray, game1P_x, game1P_y, game2P_x, game2P_y, playFial
    global game1P_direction, game2P_direction

    # 初始遊戲區陣列.
    for y in range(game_area_height):
        for x in range(game_area_width):
            gameAreaArray[x][y] = 0

    # 1P開始位置.
    game1P_x = CONST_STARTING_1P_POS_X
    game1P_y = CONST_STARTING_1P_POS_Y
    # 前進方向.
    game1P_direction = 1

    # 2P開始位置.
    game2P_x = CONST_STARTING_2P_POS_X
    game2P_y = CONST_STARTING_2P_POS_Y
    # 前進方向.
    game2P_direction = 0

    # 玩家失敗.
    playFial = 0

#-------------------------------------------------------------------------
# 主程式.
#-------------------------------------------------------------------------
if __name__=='__main__':
    # 初始.
    pygame.init()
    # 顯示Title.
    pygame.display.set_caption(u"封鎖線遊戲")
    # 建立畫佈大小.
    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    #canvas = pygame.display.set_mode((canvas_width, canvas_height),pygame.DOUBLEBUF and pygame.FULLSCREEN)
    
    # 時脈.
    clock = pygame.time.Clock()

    # 設定字型.
    font_24 = pygame.font.Font("Fonts/Cascadia.ttf", 24)

    # 重新開始遊戲.
    restart()

    # 1P位置.        
    gameAreaArray[game1P_x][game1P_y] = 11
    # 2P位置.        
    gameAreaArray[game2P_x][game2P_y] = 20

    #-------------------------------------------------------------------------    
    # 主迴圈.
    #-------------------------------------------------------------------------
    running = True
    while running:
        # 每秒執行fps次
        clock.tick(fps)

        #---------------------------------------------------------------------
        # 判斷輸入.
        #---------------------------------------------------------------------
        for event in pygame.event.get():
            # 離開遊戲.
            if event.type == pygame.QUIT:
                running = False
            # 判斷按下按鈕
            if event.type == pygame.KEYDOWN:
                # 判斷按下ESC按鈕
                if event.key == pygame.K_ESCAPE:
                    running = False
                # 除錯訊息開關.
                elif event.key == pygame.K_p:
                    debug_message = not debug_message

                # 0:遊戲結束.
                if gameMode == 0:
                    # 開始遊戲.
                    if event.key == pygame.K_RETURN:
                        # 初始分數.
                        score1P = 0
                        score2P = 0
                        # 重新開始遊戲.
                        restartTime = 0
                        restart()   
                        # 設定開始遊戲.
                        gameMode = 1

                # 1:遊戲中.
                elif gameMode == 1:
                    #-----------------------------------------------------------------
                    # 1P-上.
                    if event.key == pygame.K_w:
                        game1P_direction = 0
                    #-----------------------------------------------------------------
                    # 1P-下.
                    elif event.key == pygame.K_s:
                        game1P_direction = 1
                    #-----------------------------------------------------------------
                    # 1P-左.
                    elif event.key == pygame.K_a:
                        game1P_direction = 2
                    #-----------------------------------------------------------------
                    # 1P-右.
                    elif event.key == pygame.K_d:
                        game1P_direction = 3

                    #-----------------------------------------------------------------
                    # 2P-上.
                    if event.key == pygame.K_UP:
                        game2P_direction = 0
                    #-----------------------------------------------------------------
                    # 2P-下.
                    elif event.key == pygame.K_DOWN:
                        game2P_direction = 1
                    #-----------------------------------------------------------------
                    # 2P-左.
                    elif event.key == pygame.K_LEFT:
                        game2P_direction = 2
                    #-----------------------------------------------------------------
                    # 2P-右.
                    elif event.key == pygame.K_RIGHT:
                        game2P_direction = 3

        #--------------------------------------------------------------------- 
        # 繪製畫面.   
        #---------------------------------------------------------------------    
        # 清除畫面.
        canvas.fill(block)

        #--------------------------------------------------------------------- 
        # 遊戲模式.
        # 0:遊戲結束.
        if gameMode == 0:
            # 清除顯示區.
            for y in range(18,24):
                for x in range(25,40):
                    gameAreaArray[x][y] = 3
            # 顯示GameOver與雙方分數.
            showFont( "GAME", 380, 240, green)
            showFont( "OVER", 380, 262, green)
            showFont( str(score1P), 340, 262, green)
            showFont( str(score2P), 460, 262, green)

        #--------------------------------------------------------------------- 
        # 1:遊戲中.
        elif gameMode == 1:
            #--------------------------------------------------------------------- 
            # 邏輯運算.   
            #---------------------------------------------------------------------    
            # 還沒分出勝負.
            if (playFial == 0):
                # 
                if(move):
                    # 1P位置.        
                    gameAreaArray[game1P_x][game1P_y] = 1
                    # 1P前進方向.
                    # 0:上.
                    if (game1P_direction == 0):
                        game1P_y -= 1
                    # 1:下.
                    elif (game1P_direction == 1):
                        game1P_y += 1
                    # 2:左.
                    elif (game1P_direction == 2):
                        game1P_x -= 1
                    # 3:右.
                    elif (game1P_direction == 3):
                        game1P_x += 1
                    # 1P判斷邊界.
                    ifBoundary1P(game1P_direction)
                else:
                    # 2P位置.        
                    gameAreaArray[game2P_x][game2P_y] = 1
                    # 2P前進方向.
                    # 0:上.
                    if (game2P_direction == 0):
                        game2P_y -= 1
                    # 1:下.
                    elif (game2P_direction == 1):
                        game2P_y += 1
                    # 2:左.
                    elif (game2P_direction == 2):
                        game2P_x -= 1
                    # 3:右.
                    elif (game2P_direction == 3):
                        game2P_x += 1
                    # 1P判斷邊界.
                    ifBoundary2P(game2P_direction)
                move = not move

            # 分出勝負.
            else:
                # 1P失敗，閃爍失敗處.
                if(playFial==1):
                    if(gameAreaArray[game1P_x][game1P_y]==2):
                        gameAreaArray[game1P_x][game1P_y] = 3
                    else:
                        gameAreaArray[game1P_x][game1P_y] = 2
                # 2P失敗，閃爍失敗處.
                elif(playFial==2):
                    if(gameAreaArray[game2P_x][game2P_y]==2):
                        gameAreaArray[game2P_x][game2P_y] = 3
                    else:
                        gameAreaArray[game2P_x][game2P_y] = 2

                # 重新開始遊戲時間.
                restartTime += 1
                if((restartTime / fps) == 3):
                    # 判斷遊戲結束.
                    if(score1P >=6 or score2P >= 6):
                        # 設定遊戲結束.
                        gameMode = 0
                    else:
                        restartTime = 0
                        restart()   # 重新開始遊戲.

            if (playFial > 0):    
                # 1P失敗，2P閃爍分數.
                if(playFial==1):
                    if(gameAreaArray[game1P_x][game1P_y]==2):                    
                        showFont( str(score2P), ((CONST_STARTING_2P_POS_X)*12)+15, ((CONST_STARTING_2P_POS_Y + 2)*12), green)
                    showFont( str(score1P), ((CONST_STARTING_1P_POS_X)*12)+15, ((CONST_STARTING_1P_POS_Y - 2)*12), green)                    
                # 2P失敗，1P閃爍分數.
                elif(playFial==2):
                    if(gameAreaArray[game2P_x][game2P_y]==2):
                        showFont( str(score1P), ((CONST_STARTING_1P_POS_X)*12)+15, ((CONST_STARTING_1P_POS_Y - 2)*12), green)
                    showFont( str(score2P), ((CONST_STARTING_2P_POS_X)*12)+15, ((CONST_STARTING_2P_POS_Y + 2)*12), green)

        #--------------------------------------------------------------------- 
        # 繪製外框.
        gameAreaArray[32][0]=6
        for x in range(game_area_width):
            if(gameAreaArray[x][0]==0):
                gameAreaArray[x][0] = 1
            if(gameAreaArray[x][game_area_height-1]==0):
                gameAreaArray[x][game_area_height-1] =  1
        for y in range(game_area_height):
            if(gameAreaArray[0][y]==0):
                gameAreaArray[0][y] = 1
            if(gameAreaArray[game_area_width-1][y]==0):
                gameAreaArray[game_area_width-1][y] = 1

        #--------------------------------------------------------------------- 
        # 繪製遊戲區.
        ix = 15
        iy = 2
        for y in range(game_area_height):
            for x in range(game_area_width): 
                # 方塊.
                if(gameAreaArray[x][y]==1):
                    showFont( u"▨", ix, iy, green)
                # 死亡.
                elif(gameAreaArray[x][y]==2):                
                    showFont( u"▦", ix, iy, green)
                # 空白.
                elif(gameAreaArray[x][y]==3):
                    showFont( u"⠀", ix, iy, green)
                elif(gameAreaArray[x][y]==6):
                    showFont( u"6", ix, iy, green)
                # 1p-上箭頭.
                elif(gameAreaArray[x][y]==10):
                    showFont( u"▴", ix, iy, green)
                # 1p-下箭頭.
                elif(gameAreaArray[x][y]==11):
                    showFont( u"▾", ix, iy, green)
                # 1p-左箭頭.
                elif(gameAreaArray[x][y]==12):
                    showFont( u"◂", ix, iy, green)
                # 1p-右箭頭.
                elif(gameAreaArray[x][y]==13):
                    showFont( u"▸", ix, iy, green)
                # 2p-上箭頭.
                elif(gameAreaArray[x][y]==20):
                    showFont( u"▵", ix, iy, green)
                # 2p-下箭頭.
                elif(gameAreaArray[x][y]==21):
                    showFont( u"▿", ix, iy, green)
                # 2p-左箭頭.
                elif(gameAreaArray[x][y]==22):
                    showFont( u"◃", ix, iy, green)
                # 2p-右箭頭.
                elif(gameAreaArray[x][y]==23):
                    showFont( u"▹", ix, iy, green)

                # 除錯.
                if(debug_message):
                    if(gameAreaArray[x][y]!=0):
                        # 顯示陣列編碼.
                        showFont( str(gameAreaArray[x][y]), ix, iy, (255, 0, 0))
                        # 顯示FPS.
                        showFont( u"FPS:" + str(int(clock.get_fps())), 8, 2, (255, 255, 255))

                ix+=12
            ix = 15
            iy+=12

        # 更新畫面.
        pygame.display.update()

    # 離開遊戲.
    pygame.quit()
    quit()