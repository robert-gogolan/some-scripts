#this script is using ffmpeg, make sure you install the ffmpeg and you have it in PATH (for windows)
import os;

path_is = 'D:/BrainRolls/PROJECTS/Multimedia_2017.06.20_Jaguar/assets/360/'
output_dir = 'D:/BrainRolls/PROJECTS/Multimedia_2017.06.20_Jaguar/assets/360/resized'

os.mkdir(output_dir)
for filename in os.listdir(path_is):
	if filename.endswith('.jpg'):
		print('processing file: ',filename)
		#use this for scale
		os.system('ffmpeg -i ' + path_is + filename + ' -vf scale=1280:720 D:/BrainRolls/PROJECTS/Multimedia_2017.06.20_Jaguar/assets/360/resized/' + filename)
		#use this for crop
		#os.system('ffmpeg -i ' + path_is + '/' + filename + ' -vf crop=1000:300:0:420 ' + output_dir + '/' + filename)
	else:
		print('not a jpg')