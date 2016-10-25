import pygame;
pygame.init();


font=pygame.font.Font(None,25);
text_color=(255,215,0);
text_backgound_seleted=(176,196,222);
text_color_selected=(255,0,0);
backgound_color=(0,0,255);
def message_to_screen(msg,x,y,selected):
    if selected:
        screen_text=font.render(msg,True,text_color_selected,text_backgound_seleted);
    else:
        screen_text = font.render(msg,True,text_color);
    gameDisplay.blit(screen_text,(x,y));

running=True;


gameDisplay=pygame.display.set_mode((640,480));
select_index=0;
op1={"msg":' Options..     F1 ',"x":100,"y":100,"enable":False};
op2={"msg":' File...           F2 ','x':100,"y":120,"enable":False};
op3={"msg":' Source ...     F3 ','x':100,"y":140,"enable":False};
op4={"msg":' Settings      F4 ','x':100,"y":160,"enable":False};
op5={"msg":' Exit....      F5 ','x':100,"y":180,"enable":False};


arr_option=[op1,op2,op3,op4,op5];

def clear_allselected():
    for op in arr_option:
        op["enable"]=False;
def moveSelection(dx):
    global  select_index;
    select_index+=dx;
    if (select_index)>len(arr_option):
        select_index=1
    elif (select_index<1):
        select_index=len(arr_option);

    print(select_index)
    clear_allselected();
    if dx!=-2:
        arr_option[select_index-1]["enable"]=True;

    else:
        select_index=0;


def drawOptions():
    for op in arr_option:
        message_to_screen(op["msg"],op["x"],op["y"],op["enable"]);

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False;
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                moveSelection(1)
            elif event.key==pygame.K_UP:
                moveSelection(-1);
            elif event.key==pygame.K_ESCAPE:
                moveSelection(-2);
    gameDisplay.fill(backgound_color);
    drawOptions();
    pygame.display.update();
pygame.quit();