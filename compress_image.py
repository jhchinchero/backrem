from PIL import Image
import os
import uuid

def compress_image_(input, output, qua, label_time_compress):
	value = int(qua.get())
	for image in input:
		label_time_compress.configure(text=f"Comprimiendo imagen {image.name}")
		input_img = Image.open(image.name)
		output_img = input_img.save(os.path.join(output, f"{uuid.uuid1()}.png"), optimize=True, quality=value)
	label_time_compress.configure(text="Compresión terminada")