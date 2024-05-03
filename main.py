from tkinter import Tk, Label, Button, ttk, filedialog, DISABLED, NORMAL
import time
import os
import threading

from back_rem_ import back_rem

class Window():
	def __init__(self):
		self.window = Tk()
		self.window.title("Backrem")
		self.window.geometry("500x220")

	
		btn_open_file = Button(self.window, text="Abrir imágenes",command=self.open_files)
		btn_open_file.place(x=20, y=10)

		self.label_log_img = Label(self.window, text="")
		self.label_log_img.place(x=20, y=100)

		self.btn_remove = Button(self.window, text="Remover fondo", command=self.background_remove, state=DISABLED)
		self.btn_remove.place(x=20, y=150)
		self.label_time_remove = Label(self.window, text="")
		self.label_time_remove.place(x=20, y=180)
		self.btn_ = Button(self.window, text="Comprimir imágenes", state=DISABLED)
		self.btn_.place(x=150, y=150)
		


		self.window.mainloop()

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
			



if __name__ == '__main__':
	Window()