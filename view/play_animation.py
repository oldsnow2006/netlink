from tkinter import *
class Play_Animation(Label):
    def __init__(self):
        super(Play_Animation, self).__init__()
        numIdx = 5  # gif的帧数
        frames = []
        for i in range(0, 5):
            frame = PhotoImage(file='router' + str(i) + '.gif')
            frames.append(frame)

    def update(idx):
        frame = frames[idx]

        label.configure(image=frame)
        idx += 1
        if idx == numIdx:
            idx = 0
        root.after(500, update, idx)

    label = Label(root, bg='white')
    label.pack()
    root.after(0, update, 0)