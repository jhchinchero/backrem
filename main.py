from tkinter import Tk, Label, Button, ttk, filedialog, DISABLED, NORMAL, Scale, HORIZONTAL,DoubleVar
import time
import os
import threading
from PIL import Image, ImageTk

from back_rem_ import back_rem
from compress_image import compress_image_

basedir = os.path.dirname(__file__)



class Window():
	def __init__(self):
		self.window = Tk()
		self.window.title("Backrem")
		self.window.geometry("520x240")
		path_icono = Image.open(os.path.join(basedir, 'icono.ico'))
		icono = ImageTk.PhotoImage(path_icono)
		self.window.iconphoto(True, icono)
	
		btn_open_file = Button(self.window, text="Abrir imágenes",command=self.open_files)
		btn_open_file.place(x=20, y=10)

		self.label_log_img = Label(self.window, text="")
		self.label_log_img.place(x=20, y=50)

		self.btn_remove = Button(self.window, text="Remover fondo", command=self.background_remove, state=DISABLED)
		self.btn_remove.place(x=20, y=150)
		self.label_time_remove = Label(self.window, text="")
		self.label_time_remove.place(x=20, y=180)
		self.btn_ = Button(self.window, text="Comprimir imágenes", state=DISABLED, command=self.com_img)
		self.btn_.place(x=150, y=150)

		self.label_time_compress = Label(self.window, text="")
		self.label_time_compress.place(x=150, y=180)

		self.val = DoubleVar()
		self.length_input = Scale(self.window,state=DISABLED, variable = self.val, from_=10, to=95, orient=HORIZONTAL, length= 200)
		self.length_input.place(x=150, y=100)
		self.length_input.set(50)
		


		self.window.mainloop()
	def com_img(self):
		directory = filedialog.askdirectory()
		print(directory)

		thread = threading.Thread(target=compress_image_, args=(self.data_image,directory, self.val, self.label_time_compress,))
		thread.start()		

	def background_remove(self):
		directory = filedialog.askdirectory()
		print(directory)


		thread = threading.Thread(target=back_rem, args=(self.data_image,directory, self.label_time_remove,))
		thread.start()	
	def open_files(self):
		filename = filedialog.askopenfiles()
		if len(filename) == 0:
			self.label_log_img.config(text=f"Imagen no encontrado")
		else:
			self.data_image = filename
			self.label_log_img.config(text=f"Imagenes encontradas {len(filename)}")
			self.btn_remove.configure(state=NORMAL)
			self.btn_.configure(state=NORMAL)
			self.length_input.configure(state=NORMAL)
			self.length_input.set(50)
			



if __name__ == '__main__':
	Window()