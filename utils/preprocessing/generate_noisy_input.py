"""
Author : Tanishq Vyas

This file aims at getting the clean input audio and mixing it with a noise audio in order to generate the noisy input

"""

from scipy.io import wavfile
import os


class InputGenerator:

	def __init__(self, clean_path, noise_path, input_path, distortion = 0.1):

		self.clean_path = clean_path
		self.noise_path = noise_path
		self.input_path = input_path
		self.distortion = distortion


	# Function to fetch all the audio files from a folder
	# Argument is the folder path
	# Return a list of all the files
	def fetch_all_files(self, path):
		
		audio_list = []

		for filename in os.listdir(path):

			# Sampling rate in samples per sec, numpy array of data
			fs, data = wavfile.read(os.path.join(path, filename))
			
			# checking if return value is valid
			if data is not None:
				audio_list.append([fs,data])

		return audio_list

	# Function to generate random noise audio
	def generate_random_noise_audio(self, path, duration):
		pass


	# Function to generate noisy input data
	def generate_noisy_input(self):
		
		# List of final noisy input data
		input_data_list = []

		# Get all the clean audios
		clean_audio_list = self.fetch_all_files(self.clean_path)

		# Iterate over each individual audio and generate corresponding noisy input
		for audio in clean_audio_list:
			pass

		return input_data_list



if __name__ == '__main__':
	
	# test your functions here
	pass

		