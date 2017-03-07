# -*- coding: utf-8 -*-
import cocos
import random
class Testgame(cocos.layer.Layer):
    # pass
    def __init__(self):
        super(Testgame,self).__init__()
        # self.logo = cocos.sprite.Sprite()
        # self.logo.position = 550,400
        # self.add(self.logo,9999)
        txt = cocos.text.Label(u'最棒了最棒了')
        txt.position = 300,200
        self.add(txt)

        self.ppx = cocos.sprite.Sprite('ppx_rush1.png')
        self.ppx.position = 200,300
        self.add(self.ppx)

        self.speed_x = 3
        self.speed_y = 3
        self.schedule(self.update)

    def update(self,dt):
        self.ppx.x += self.speed_x
        if self.ppx.x > 600:
            self.speed_x = -(1+4*random.random())
        elif self.ppx.x < 0:
            self.speed_x = 3

        self.ppx.y += self.speed_y
        if self.ppx.y > 480:
            self.speed_y = -3
        elif self.ppx.y <0:
            self.speed_y = 3

cocos.director.director.init(caption=u'测试')
cocos.director.director.run(cocos.scene.Scene(Testgame()))
