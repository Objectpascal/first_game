import pygame,sys;
import classes;
import random;

# PROCESSES
from classes import Fly


def processes(bug,fps,totoalframes):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                classes.BugProjectile.Fire=not classes.BugProjectile.Fire;
    #key testing
    keys=pygame.key.get_pressed();
    if keys[pygame.K_a]:
        bug.velx=-5;
        bug.image = pygame.image.load('images\\Bugflipped.png');
        bug.going_right=False;

    elif keys[pygame.K_d]:
        bug.velx=5;
        bug.image = pygame.image.load('images\\bug.png');
        bug.going_right = True;
    elif keys[pygame.K_w]:
        bug.jumping=True;


    elif keys[pygame.K_SPACE]:

        def direction():
            if bug.going_right:
                p.velx = 8;
            else:
                p.image = pygame.transform.flip(p.image, True, False)
                p.velx = -8;
        if (classes.BugProjectile.Fire):
            sound=pygame.mixer.Sound('music\\f2.ogg');
            sound.play();
            p=classes.BugProjectile(bug.rect.x,bug.rect.y,"images\\projectiles\\fire.png");
        else:
            sound = pygame.mixer.Sound('music\\f1.ogg');
            sound.play();
            p=classes.BugProjectile(bug.rect.x,bug.rect.y,"images\\projectiles\\frost.png");
        direction();
    spawn(fps,totoalframes);
    collisions();


    # key testing
def spawn(FPS,totoal_frams):
    four_seconds=FPS*4;
    if totoal_frams%four_seconds==0:
        r=random.randint(1,2);
        x=1;
        if r==2:
            x=640-40;
        fly=classes.Fly(x,130,"images\\fly.png");


def collisions():
    # #frezz flyes
    # for fly in classes.Fly.List:
    #     if pygame.sprite.spritecollide(fly,classes.BugProjectile.List,False):
    #         if classes.BugProjectile.Fire:
    #             fly.health-=fly.half_health;
    #         else:
    #             fly.velx=0;
    #
    #
    #
    # for proj in classes.BugProjectile.List:
    #     if pygame.sprite.spritecollide(proj,classes.Fly.List,False):
    #        proj.destroy()
    #
    #     # fly_proj=pygame.sprite.spritecollide(fly,classes.BugProjectile.List,True);
    #     # if len(fly_proj)>0:
    #     #     for hit in fly_proj:
    #     #         fly.health-=fly.half_health;

    for fly in classes.Fly.List:
        projectiles=pygame.sprite.spritecollide(fly,classes.BugProjectile.List,True);
        for project in projectiles:
            if project.fire:
                fly.health-=2*fly.half_health;
                fly.image=pygame.image.load('images\\burnt_fly.png');
            else:
                fly.itsfrozen=True;
                if fly.velx>0:
                    fly.image=pygame.image.load('images\\frozen_fly.png');
                elif fly.velx<0:
                    fly.image=pygame.image.load('images\\frozen_fly.png');
                    fly.image=pygame.transform.flip(fly.image,True,False);
                fly.velx=0;
# PROCESSES