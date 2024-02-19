import os

def check_and_create_utility_folders():
	current_working_directory = os.path.abspath(os.getcwd())
	output_dir = os.path.join(current_working_directory, 'output')
	input_dir = os.path.join(current_working_directory, 'input')

	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)

	if not os.path.isdir(input_dir):
		os.mkdir(input_dir)
	
	print(os.path.isdir(output_dir))
	print(os.path.isdir(input_dir))
	print(current_working_directory)

if __name__ == "__main__":
	check_and_create_utility_folders()