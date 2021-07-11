#! -*- encoding:utf-8 -*-
"""
@File    :   recoder.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   录制设备声音
sounddevice, scipy
"""
import tkinter
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
from threading import Thread
from numpy import vstack

import sounddevice as sd
from scipy.io import wavfile

root = tkinter.Tk()
root.title('Recoder')
root.geometry('300x100+400+300')
root.resizable(False, False)

# 录制的秒数
length = 5
for index, device in enumerate(sd.query_devices()):
    # if '扬声器 (SPA33      spker)' in device['name']:
    if '立体声混音' in device['name']:
        sd.default.device[0] = index
        fs = int(device.get('default_samplerate', 44100))
        # fs = 44100
        showinfo("Success", "发现混音设备！")
        break
else:
    showinfo("Attention", "未发现混音设备！")

def recoder():
    sounds = []
    lbInfo['text'] = '正在录音...'
    while recording.get():
        data = sd.rec(frames=fs*length, samplerate=fs, blocking=True, channels=2)
        sounds.append(data)
    sound = vstack(sounds)
    filename = asksaveasfilename(title='保存声音', filetypes=[('wavfile', '*.wav')])
    if not filename:
        return
    if not filename.endswith('.wav'):
        filename += ".wav"
    wavfile.write(filename, fs, sound)
    lbInfo['text'] = '保存成功'

def start_recording():
    global thread_recorder
    recording.set(True)
    # 创建并启动线程
    thread_recorder = Thread(target=recoder)
    thread_recorder.start()
    buttonStop['state'] = 'normal'
    buttonStart['state'] = 'disabled'

def stop_recording():
    recording.set(False)
    buttonStop['state'] = 'disabled'
    buttonStart['state'] = 'normal'


recording = tkinter.BooleanVar(root, False)

buttonStart = tkinter.Button(root, text='开始录制', command=start_recording)
buttonStart.place(x=10, y=10, width=130, height=20)

buttonStop = tkinter.Button(root, text='停止录音', state='disabled', command=stop_recording)
buttonStop.place(x=160, y=10, width=130, height=20)

lbInfo = tkinter.Label(root, foreground='red')
lbInfo.place(x=10, y=40, width=280, height=20)

root.mainloop()