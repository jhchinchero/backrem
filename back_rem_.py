
from rembg import remove
import cv2
import os
import uuid
import time


def back_rem(input, output_path, label_time_remove):#([], path_out, label)
	for image in input:
		#print(image.name)
		label_time_remove.config(text=f"Procesando imagen {image.name}")
		input = cv2.imread(os.path.join(image.name))
		
		output_image = remove(input)
		cv2.imwrite(os.path.join(output_path, f"{uuid.uuid1()}.png"), output_image)
	label_time_remove.config(text=f"Proceso terminado")

def test():
	print("test")