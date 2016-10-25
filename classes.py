import pygame;
import sys;
import random;
import math;

class BaseClass(pygame.sprite.Sprite):
    allsprites=pygame.sprite.Group();
    def __init__(self,x,y,image_string):
        super(BaseClass,self).__init__();
        BaseClass.allsprites.add(self);

        self.image=pygame.image.load(image_string);
        self.rect=self.image.get_rect();
        self.rect.x=x;
        self.rect.y=y;

    def destroy(self,ClassName):
        ClassName.List.remove(self);
        BaseClass.allsprites.remove(self);
        del self;

class Bug(BaseClass):
    List=pygame.sprite.Group();
    def __init__(self, x, y, image_string):
        super(Bug,self).__init__(x, y, image_string)
        Bug.List.add(self);
        self.velx=0;
        self.vely=5;
        self.going_right=True;
        self.jumping,self.go_down=False,False;
    def motion(self,WIDTH,HEIGHT):
        self.rect.x+=self.velx;
        if self.rect.x < 0:
            self.rect.x = 0;
        elif (self.rect.x + self.rect.width) > WIDTH:
            self.rect.x = WIDTH - self.rect.width;

        self.__jump(HEIGHT);

    def __jump(self,HEIGHT):
        max_jump = 50;
        if self.jumping:
            if self.rect.y < max_jump:
                self.go_down = True;

            if self.go_down:

                self.rect.y += self.vely;
                if (self.rect.y + self.rect.height) > HEIGHT:
                    self.jumping=False;
                    self.go_down=False;
            else:
                self.rect.y -= self.vely;



class Fly(BaseClass):
    List=pygame.sprite.Group();
    def __init__(self, x, y, image_string):
        super(Fly,self).__init__(x, y, image_string)
        Fly.List.add(self);
        self.velx,self.vely=random.randint(1,4),2;
        self.health=100;
        self.half_health=self.health/2;
        self.amplitude,self.period=random.randint(20,140),random.randint(4,5)/100;
        self.itsfrozen=False;
        self.totalframes=0;
        self.font=pygame.font.SysFont("consolas,arial",15);


    def fly_hite_message(self,screen):
        screen_text = self.font.render('+10', True, (255, 200, 0));
        screen.blit(screen_text, ((self.rect.x+self.rect.width/2), self.rect.y-5));


    @staticmethod
    def update_all(WIDTH,HEIGHT,FPS,scren):

        for fly in Fly.List:
            fly.totalframes+=1;
            if fly.health<=0:


                if fly.rect.y+fly.rect.height<HEIGHT:
                    fly.fly_hite_message(scren);
                    fly.rect.y+=fly.vely;
            else:
                fly.fly(WIDTH,FPS);

    def fly(self,WIDTH,FPS):
        if self.itsfrozen:
            if (self.totalframes%(FPS*10)==0):
                self.totalframes=0;
                self.velx=random.randint(1,4);
                self.itsfrozen=False;
                self.image=pygame.image.load('images\\fly.png');
        else:
            self.rect.x+=self.velx;
            if (self.rect.x<0) or ((self.rect.x+self.rect.width)>WIDTH):
                self.image=pygame.transform.flip(self.image,True,False);
                self.velx=-self.velx;

            self.rect.y=self.amplitude*math.sin(self.period*self.rect.x)+140;



class BugProjectile(pygame.sprite.Sprite):
    List=pygame.sprite.Group();
    normal_list=[];

    Fire = True;

    def __init__(self, x, y, image_string):
        super(BugProjectile,self).__init__();

        self.image = pygame.image.load(image_string);
        self.rect = self.image.get_rect();
        self.rect.x = x;
        self.rect.y = y;
        self.velx=None;
        self.fire=BugProjectile.Fire;
        try:
            last_elemnt=BugProjectile.normal_list[-1];
            if self.rect.colliderect(last_elemnt.rect):
                return ;

        except:
            pass;
        BugProjectile.List.add(self);
        BugProjectile.normal_list.append(self);


    def destroy(self):
        BugProjectile.List.remove(self);
        BugProjectile.normal_list.remove(self);
        del self;

    @staticmethod
    def movement(WIDTH):
        for projectile in BugProjectile.List:
            projectile.rect.x+=projectile.velx;



