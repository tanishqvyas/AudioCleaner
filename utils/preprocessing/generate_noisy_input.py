"""
Author : Tanishq Vyas

This file aims at getting the clean input audio and mixing it with a noise audio in order to generate the noisy input

"""

import os


from matplotlib import pyplot as plt
import numpy as np
import wave
import sys


from scipy.io import wavfile
from pydub import AudioSegment
from pydub.playback import play



class InputGenerator:

	def __init__(self, clean_path, noise_path, input_path, plot_path, distortion = 0.1):

		self.clean_path = clean_path
		self.noise_path = noise_path
		self.input_path = input_path
		self.plot_path  = plot_path
		self.distortion = distortion


	# Function to fetch all the audio files from a folder
	# Argument is the folder path
	# Return a list of all the files
	def fetch_all_file_names(self, path):
		
		audio_list = []

		for filename in os.listdir(path):

			# Sampling rate in samples per sec, numpy array of data
			# fs, data = wavfile.read(os.path.join(path, filename))
			
			# checking if return value is valid
			# if data is not None:
				# audio_list.append([fs,data])
			audio_list.append(filename)

		return audio_list


	# Function to generate noisy input data
	def generate_noisy_input(self, sample_count=1):
		
		# List of final noisy input data
		input_data_list = []

		# Get all the clean audios
		clean_audio_list = self.fetch_all_file_names(self.clean_path)

		# Get all the noise audios
		noise_audio_list = self.fetch_all_file_names(self.noise_path)


		# Iterate over each individual audio and generate corresponding noisy input
		for i in range(sample_count):
			
			original_audio = AudioSegment.from_file(os.path.join(self.clean_path, clean_audio_list[i]))
			noise_audio    = AudioSegment.from_file(os.path.join(self.noise_path, noise_audio_list[i]))

			combined = original_audio.overlay(noise_audio)

			combined.export(os.path.join(self.input_path, clean_audio_list[i]), format='wav')


	# A function to play the audio
	def play_audio(self, path):

		sound = AudioSegment.from_file(path, format="wav")
		play(sound)

	# A function to plot the audio
	def plot_the_audio(self, folder_path, filename, wanna_save = False):

		samplerate, data = wavfile.read(os.path.join(folder_path, filename))

		duration = len(data)/samplerate
		time = np.arange(0,duration,1/samplerate) #time vector

		plt.plot(time,data)
		plt.xlabel('Time [s]')
		plt.ylabel('Amplitude')
		plt.title(filename)
		fig = plt.gcf()
		plt.show()

		if(wanna_save):

			fig.savefig(os.path.join(self.plot_path, filename + ".png"))



if __name__ == '__main__':
	

	# Paths for respective data folders
	clean_audio_path = os.path.join("data", "clean")
	noise_audio_path = os.path.join("data", "noise")
	input_audio_path = os.path.join("data", "input")


	obj = InputGenerator(clean_audio_path, noise_audio_path, input_audio_path)

	obj.generate_noisy_input()






		