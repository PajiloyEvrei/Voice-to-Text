import json  
import pyaudio
import keyboard as keyb
import speech_recognition as sr
from tkinter import *
import time
from pynput import keyboard
from tkinter import ttk
import os 
import getpass

FB = False
SB = False
ready = False
Ready = False
ASG = True
root = Tk()

p = pyaudio.PyAudio()
def listen():
	r = sr.Recognizer()

	with sr.Microphone(device_index = 1) as source:
		audio = r.listen(source)

	query = r.recognize_google(audio, language = 'ru-RU')
	return query.lower()

def Record(self): 
	for text in listen():
		keyb.write(f'{text.lower()}')


root['bg']= 'black'
root.title('Речь  --> Текст')
root.wm_attributes('-alpha',1)
root.geometry('175x100')
root.resizable(width=False, height=False)

canvas = Canvas(root,width=250,height=110)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

Forbtn = Entry(frame,bg='white', state=DISABLED, width=15)
Forbtn.grid(row=0,column=0)

def NR():
	global Ready
	Ready = False
	if ASG is True:
		btn.configure(text='назначить', bg='#FAEBD7', command=Assign, width=10)
	else:
		btn.configure(text='assign', bg='#FAEBD7', command=Assign, width=10)
	global ABTN
	ABTN.pop(0)
	if len(Forbtn.get()) == 2:
		root.bind(f'<{Forbtn.get()[1]}>', Record)
	elif len(Forbtn.get()) == 4:
		root.bind(f'<KeyPress-{Forbtn.get()[1]}>', FB_pressed)
		root.bind(f'<KeyPress-{Forbtn.get()[3]}>', SB_pressed)
		root.bind(f'<KeyRelease-{Forbtn.get()[1]}>', FB_released)
		root.bind(f'<KeyRelease-{Forbtn.get()[3]}>', SB_released)
def Check():
	if FB is True and SB is True:
		Record(1)
def FB_pressed(event):
	global FB
	FB = True
	Check()
def SB_pressed(event):
	global SB
	SB = True
	Check()
def FB_released(event):
	global FB
	FB = False
	Check()
def SB_released(event):
	global SB
	SB = False
	Check()
def onKeyPress(event):
	global ABTN
	if Ready is True:
		Forbtn.configure(state=NORMAL)
		Forbtn.insert("0",f'+{event.keysym}')
		Forbtn.configure(state=DISABLED)
		ABTN = Forbtn.get().split("+")
		if len(Forbtn.get()) >= 4:
			NR()
def Assign():
	global Ready
	if len(Forbtn.get()) == 2:
		root.unbind(f'<{Forbtn.get()[1]}>')
	elif len(Forbtn.get()) == 4:
		root.unbind(f'<{Forbtn.get()[1]}>')
		root.unbind(f'<{Forbtn.get()[3]}>')
	Ready = True
	Forbtn.configure(state=NORMAL)
	Forbtn.delete("0", END)
	Forbtn.configure(state=DISABLED)
	if ASG is True:
		btn.configure(text='подтвердить', bg='#FAEBD7', command=NR, width=10)
	else:
		btn.configure(text='confirm', bg='#FAEBD7', command=NR, width=10)
root.bind('<KeyPress>', onKeyPress)
btn = Button(frame, text='назначить', bg='#FAEBD7', command=Assign, width=10)
btn.grid(row=1,column=0,stick='we')



AutorunActive = False
USER_NAME = getpass.getuser()
def autorun():
	global AutorunActive
	def add_to_startup(file_path=r"C:\\Users\\%s\\Desktop\\program\\VoiceToText.py"% USER_NAME):
		bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
		with open(bat_path + '\\' + "open.bat", 'w+') as bat_file:
			bat_file.write(r'start "name" %s' % file_path )
	add_to_startup()
	AutorunActive = True
def DELautorun():
	global AutorunActive
	if AutorunActive is True:
		os.remove(r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\open.bat' % USER_NAME)
		AutorunActive = False

label_Auto= Label(frame, text='Автозапуск',bg='white')
label_Auto.grid(row=2,column=0)
Abtn = Button(frame, text='ВКЛ', bg='#FAEBD7', width=4, height=1, command=autorun)
Abtn.grid(row=2,column=1)
Dbtn = Button(frame, text='ВЫКЛ', bg='#FAEBD7', width=4, height=1, command=DELautorun)
Dbtn.grid(row=2,column=2)

def RU():
	global ASG
	Abtn.configure(text='ВКЛ')
	Dbtn.configure(text='ВЫКЛ')
	label_Lang.configure(text='Язык')
	label_Auto.configure(text='Автозапуск')
	btn.configure(text='назначить')
	ASG = True
def ENG():
	global ASG
	Abtn.configure(text='ON')
	Dbtn.configure(text='OFF')
	label_Lang.configure(text='Language')
	label_Auto.configure(text='Autorun')
	btn.configure(text='assign')
	ASG = False

label_Lang= Label(frame, text='Язык',bg='white')
label_Lang.grid(row=3,column=0)
Rbtn = Button(frame, text='RU', bg='#FAEBD7', width=4, height=1,command=RU)
Rbtn.grid(row=3,column=1)
Ebtn = Button(frame, text='ENG', bg='#FAEBD7', width=4, height=1,command=ENG)
Ebtn.grid(row=3,column=2)
root.mainloop()
