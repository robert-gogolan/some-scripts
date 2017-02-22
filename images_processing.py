import os;

path_to_input_folder = ''
path_to_output_folder = ''

os.mkdir(output_dir)

for filename in os.listdir(path_to_input_folder):
	if filename.endswith('.png'):
		print('processing file: ',filename)
		#use this for scale
		#os.system('ffmpeg -i ' + path_to_input_folder + '/' + filename + ' -vf scale=1280:720 ' + path_to_output_folder + '/' + filename)
		
		#use this for crop
		os.system('ffmpeg -i ' + path_to_input_folder + '/' + filename + ' -vf crop=1000:300:0:420 ' + path_to_output_folder + '/' + filename)
	else:
		print('not a png')