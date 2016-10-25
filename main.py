#
# pygame.mixer.init	—	initialize the mixer module
# pygame.mixer.pre_init	—	preset the mixer init arguments
# pygame.mixer.quit	—	uninitialize the mixer
# pygame.mixer.get_init	—	test if the mixer is initialized
# pygame.mixer.stop	—	stop playback of all sound channels
# pygame.mixer.pause	—	temporarily stop playback of all sound channels
# pygame.mixer.unpause	—	resume paused playback of sound channels
# pygame.mixer.fadeout	—	fade out the volume on all sounds before stopping
# pygame.mixer.set_num_channels	—	set the total number of playback channels
# pygame.mixer.get_num_channels	—	get the total number of playback channels
# pygame.mixer.set_reserved	—	reserve channels from being automatically used
# pygame.mixer.find_channel	—	find an unused channel
# pygame.mixer.get_busy	—	test if any sound is being mixed
# pygame.mixer.Sound	—	Create a new Sound object from a file or buffer object
# pygame.mixer.Channel	—	Create a Channel object for controlling playback
#
#
import pygame;
import sys;
from processes import *;
from classes import *;

score=0;
WIDTH,HEIGHT=(640,360);
pygame.init();
pygame.mixer.init();
screen=pygame.display.set_mode((WIDTH,HEIGHT),0,32);
pygame.display.set_caption('FLY Game');
clock=pygame.time.Clock();#clock object
FPS=24;
total_frames=0;
background=pygame.image.load('images\\forest.jpg');
bug=Bug(0,HEIGHT-40,"images\\bug.png");

#
s=pygame.mixer.Sound('music\\loop.wav');
s.play(-1)


font=pygame.font.SysFont("consolas,arial",20);
def score_to_screen():
    screen_text=font.render('SCORE:'+str(score),True,(255,200,0));
    screen.blit(screen_text,(10,10));
while True:
    screen.blit(background, (0, 0));
    #PROCESSES
    score_plus=processes(bug,FPS,total_frames);
    score+=score_plus;
    # PROCESSES


    # LOGIC

    bug.motion(WIDTH,HEIGHT);
    Fly.update_all(WIDTH,HEIGHT,FPS,screen);
    BugProjectile.movement(WIDTH);
    total_frames+=1;
    # LOGIC


    # DRAW

    BaseClass.allsprites.draw(screen);
    BugProjectile.List.draw(screen);
    score_to_screen()
    pygame.display.flip();
    # DRAW

    clock.tick(FPS);



pygame.quit();
pygame.mixer.quit();
