import pygame

class PlayMusic(object):
    def __init__(self,musicfile,time):
        """

        :param musicfile: 音乐文件的路径
        :param time: 播放音乐的次数
        """
        self.musicfile = musicfile

        self.time=time

    def play_music(self):

        pygame.mixer.init()

        track=pygame.mixer.music.load(self.musicfile)
        pygame.mixer.music.play(self.time)





