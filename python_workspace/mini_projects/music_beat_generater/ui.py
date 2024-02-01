# 프로그램 UI 생성 모듈
# 작성 일시: 2022-12-14
# 작성 내용: 최초 작성

from tkinter import *
from tkinter.ttk import Combobox, Progressbar
import pygame

Genre_String = ["pop", "hiphop", "jazz", "etc"]


class ProgramUI(Frame):
    def __init__(self):
        super().__init__()

        self.player = None
        self.pb = None
        self.generate_button = None
        self.is_music_playing = False
        self.music_sound = pygame.mixer.Sound('sample.wav')
        self.init_ui()

    def init_ui(self):
        self.master.title("Beat Generator")
        self.master.resizable(False, False)
        self.window_align_center()
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()

        # 음원(비트) 생성 프레임 구성
        generate_frame = Frame(self.master, width=width, height=height / 2)
        generate_frame.pack()

        Label(generate_frame, text="Genre option").grid(row=0, column=0)

        genre_options = Combobox(generate_frame, height=5, values=Genre_String, state='readonly')
        genre_options.set("Select Genre")
        genre_options.grid(row=1, column=0)

        self.generate_button = Button(generate_frame, text='gen')
        self.generate_button.grid(row=1, column=1)

        # 생성된 음원(비트) 결과 확인 프레임 구성
        result_frame = Frame(self.master, width=width, height=height / 2)
        result_frame.pack()

        Label(result_frame, text="play").grid(row=0, column=0)

        # 음원 재생기 생성

        self.player = Frame(result_frame, width=200, height=20, bg='red')
        self.player.grid(row=1,column=0)
        play = Button(self.player, text="▶", command=self.music_start_pause)  # ∥와 바뀐다
        play.grid(row=0, column=0)

        stop = Button(self.player, text="■", command=self.music_stop)
        stop.grid(row=0, column=1)

        self.pb = Progressbar(self.player, orient='horizontal', mode='indeterminate', length=100)
        self.pb.grid(row=0, column=2)


    def window_align_center(self):
        w = 300
        h = 500

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def music_start_pause(self):
        if not self.is_music_playing: # 음악이 재생 중이지 않으면
            # 음원(비트)재생 및 버튼 swap
            self.pb.start()
            self.is_music_playing = True
        else:
            # 음원(비트) 일시정지 및 버튼 swap
            self.pb.stop()
            self.is_music_playing = False


    def music_stop(self):
        pass
