from gui_files.svg import *

DICE_CAPTION = "Black n Beige"

def draw_dice(num):
    if num == 1:
        width, height = 100, 100
        graphic = create_graphic(width, height)
        draw_rect(graphic, 0, 0, 100, 100, fill="#d2b55b", stroke="black")
        draw_circle(graphic, 22, 22, 7, stroke="black", fill="black")

    elif num == 2:
        width, height = 100, 100
        graphic = create_graphic(width, height)
        draw_rect(graphic, 0, 0, 100, 100, fill="#black", stroke="black")
        draw_circle(graphic, 22, 22, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 32, 32, 5, stroke="#d2b55b", fill="#d2b55b")



    elif num == 3:
        width, height = 100, 100
        graphic = create_graphic(width, height)
        draw_rect(graphic, 0, 0, 100, 100, fill="#d2b55b", stroke="black")
        draw_circle(graphic, 22, 22, 5, stroke="black", fill="black")
        draw_circle(graphic, 32, 32, 5, stroke="black", fill="black")
        draw_circle(graphic, 42, 42, 5, stroke="black", fill="black")


    elif num == 4:
        width, height = 100, 100
        graphic = create_graphic(width, height)
        draw_rect(graphic, 0, 0, 100, 100, fill="black", stroke="black")
        draw_circle(graphic, 22, 22, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 32, 32, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 42, 42, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 52, 52, 5, stroke="#d2b55b", fill="#d2b55b")

    elif num == 5:
        width, height = 100, 100
        graphic = create_graphic(width, height)
        draw_rect(graphic, 0, 0, 100, 100, fill="#d2b55b", stroke="black")
        draw_circle(graphic, 22, 22, 5, stroke="black", fill="black")
        draw_circle(graphic, 32, 32, 5, stroke="black", fill="black")
        draw_circle(graphic, 42, 42, 5, stroke="black", fill="black")
        draw_circle(graphic, 52, 52, 5, stroke="black", fill="black")
        draw_circle(graphic, 62, 62, 5, stroke="black", fill="black")

    elif num == 6:
        width, height = 100, 100
        graphic = create_graphic(width, height)
        draw_rect(graphic, 0, 0, 100, 100, fill="black", stroke="black")
        draw_circle(graphic, 22, 22, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 32, 32, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 42, 42, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 52, 52, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 62, 62, 5, stroke="#d2b55b", fill="#d2b55b")
        draw_circle(graphic, 72, 72, 5, stroke="#d2b55b", fill="#d2b55b")

    return graphic
