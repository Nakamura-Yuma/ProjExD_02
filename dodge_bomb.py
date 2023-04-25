import pygame as pg
import sys
import random

delta = {                   #練習Ⅳ
        pg.K_UP:(0, -1),    #練習Ⅳ
        pg.K_DOWN:(0, +1),  #練習Ⅳ
        pg.K_LEFT:(-1, 0),  #練習Ⅳ
        pg.K_RIGHT:(+1, 0), #練習Ⅳ
    }                       #練習Ⅳ  


def check_bound(scr_rct:pg.Rect, obj_rct:pg.Rect) -> tuple[bool, bool]: #練習Ⅴ
    '''
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数1:画面Surfaceのrect
    引数2:こうかとん、または、爆弾Surfaceのrect
    戻り値:横方向、縦方向のはみ出し判定結果(画面内:True/画面外:False)
    '''
    yoko, tate = True, True #練習Ⅴ
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: #練習Ⅴ
        yoko = False #練習Ⅴ
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: #練習Ⅴ
        tate = False #練習Ⅴ
    return yoko, tate #練習Ⅴ


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img2 = pg.image.load("ex02/fig/3.png")
    kk_img2 = pg.transform.flip(kk_img, True, True)
    kk_rct = kk_img.get_rect() #練習Ⅳ
    kk_rct2 = kk_img2.get_rect()
    kk_rct.center = 900, 400 #練習Ⅳ

    fonto = pg.font.Font(None, 80)
    txt = fonto.render("Deth", True, 255, 255, 255)

    bb_img = pg.Surface((20, 20)) #練習Ⅰ
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10) #練習Ⅰ
    bb_img.set_colorkey((0, 0, 0)) #練習Ⅰ
    x, y = random.randint(0, 1600), random.randint(0, 900) #練習Ⅱ
    #screen.blit(bb_img, [x, y]) #練習Ⅱ
    vx, vy = +1, +1 #練習Ⅲ
    bb_rct = bb_img.get_rect() #練習Ⅲ
    bb_rct.center = x, y #練習Ⅲ
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()#練習Ⅳ
        for k, mv in delta.items():   #練習Ⅳ
            if key_lst[k]:            #練習Ⅳ
                kk_rct.move_ip(mv)    #練習Ⅳ
        if check_bound(screen.get_rect(), kk_rct) != (True, True): #練習Ⅴ
            for k, mv in delta.items(): #練習Ⅴ
                if key_lst[k]: #練習Ⅴ 
                    kk_rct.move_ip(-mv[0], -mv[1]) #練習Ⅴ


        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct) #練習Ⅳ
        bb_rct.move_ip(vx, vy) #練習Ⅲ
        yoko, tate = check_bound(screen.get_rect(), bb_rct) #練習Ⅴ
        if not yoko: #練習Ⅴ
            vx *= -1 #練習Ⅴ
        if not tate: #練習Ⅴ
            vy *= -1 #練習Ⅴ
        screen.blit(bb_img, bb_rct) #練習Ⅲ
        if kk_rct.colliderect(bb_rct): #練習Ⅵ
            screen.blit(kk_img2, kk_rct)
            return screen.blit(txt, [300, 200])
            for i in range(900-y):
                kk_rct2.move_ip(0, 1)   #練習Ⅵ


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()