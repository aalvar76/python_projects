import os
from PIL import Image

CURRENT_WORKING_DIRECTORY = os.path.abspath(os.getcwd())
INPUT_DIR = os.path.join(CURRENT_WORKING_DIRECTORY, 'input')
OUTPUT_DIR = os.path.join(CURRENT_WORKING_DIRECTORY, 'output')

def check_if_input_folder_exists(input_dir):
	if not os.path.isdir(input_dir):
		print("Input folder does not exist, creating one...")
		print("Please locate your images inside this folder.")
		os.mkdir(input_dir)
		
def get_files_from_input_folder(input_dir):
	img_files_names = os.listdir(input_dir)
	img_files_paths = [os.path.join(input_dir, x) for x in img_files_names]
	return img_files_paths

def convert_to_png_and_save(image_path, output_dir):
	head, tail = os.path.split(image_path)
	img = Image.open(image_path)

	# if not OUTPUT DIR create one
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)

	output_file_name = '.'.join(tail.split('.')[:-1])
	output_file_name = f'{output_file_name}.png'
	img.save(os.path.join(output_dir, output_file_name), format="PNG", optimize=True, keep=True)

def run_converter(input_dir, output_dir):
	check_if_input_folder_exists(input_dir)
	images_paths = get_files_from_input_folder(input_dir)
	for img_path in images_paths:
		convert_to_png_and_save(img_path, output_dir)

if __name__ == "__main__":
	try:
		run_converter(INPUT_DIR, OUTPUT_DIR)
	except Exception as ex:
		print("There has been an exception running the script!")
		print(ex)
		print("We apologize for the inconveniences!")
	
	