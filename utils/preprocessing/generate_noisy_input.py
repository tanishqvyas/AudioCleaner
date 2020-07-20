"""
Author : Tanishq Vyas

This file aims at getting the clean input audio and mixing it with a noise audio in order to generate the noisy input

"""

import os
import math
import random

# Plotting the audio
from matplotlib import pyplot as plt
import numpy as np
import wave
import sys


from scipy.io import wavfile
from pydub import AudioSegment
from pydub.playback import play


# Audio duration
import wave
import contextlib
from mutagen.mp3 import MP3

# For dataset generation
import numpy as np
import soundfile as sf
import csv


class InputGenerator:

	def __init__(self, clean_path, noise_path, input_path, plot_path, distortion = 0.1):

		self.clean_path = clean_path
		self.noise_path = noise_path
		self.input_path = input_path
		self.plot_path  = plot_path
		self.distortion = distortion


	# Function to fetch all the audio files from a folder
	# Argument is the folder path
	# Return a list of names of all the files (extension included)
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


	# Function to get the length of the audio file
	def get_audio_duration_wav(self, path):


		with contextlib.closing(wave.open(path,'r')) as f:
			
			frames = f.getnframes()
			rate = f.getframerate()
			duration = frames / float(rate)
			print(duration)

			return duration

	# Function to get audio length for mp3 file
	def get_audio_duration_mp3(self, path):

		audio = MP3(path)
		return audio.info.length


	def get_noise_audio(self, duration, count):

		pass


	# Function to generate noisy input data
	def generate_noisy_input(self, source_path, destination_path):
		
		print("GENERATING NOISY INPUT FOR ", source_path)


		# List of final noisy input data
		input_data_list = []

		# Get all the clean audios
		clean_audio_list = self.fetch_all_file_names(source_path)
		num_of_clean_audios = len(clean_audio_list)
		print("Clean audio fetching completed. There are : ", num_of_clean_audios, " audio files")


		# Get all the noise audios
		noise_audio_list = self.fetch_all_file_names(self.noise_path)
		print("Noisy audio fetching completed")
		num_of_noise_audio = len(noise_audio_list)
		noise_index = 0


		# Iterate over each individual audio and generate corresponding noisy input
		for i in range(num_of_clean_audios):
			
			print("Generating noisy audio for : ", clean_audio_list[i])

			# Fetching the clean audio & it's duration
			original_audio = AudioSegment.from_file(os.path.join(source_path, clean_audio_list[i]))
			# clean_audio_duration = self.get_audio_duration(os.path.join(source_path, clean_audio_list[i]))
			print("Fetched ", clean_audio_list[i])

			# Fetching the noise audio
			noise_audio = AudioSegment.from_file(os.path.join(self.noise_path, noise_audio_list[noise_index]))
			noise_index = (noise_index+1)%num_of_noise_audio


			combined = original_audio.overlay(noise_audio)

			if(i % 2 == 0):

				noise2 = AudioSegment.from_file(os.path.join(self.noise_path, noise_audio_list[random.randint(0,num_of_noise_audio-1)]))
				combined = combined.overlay(noise2)

			combined.export(os.path.join(destination_path, clean_audio_list[i]), format='wav')
			print("Noisy input generated succesfully for : ", clean_audio_list[i], "\n\n")




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
		plt.title(folder_path +" : "+filename)
		fig = plt.gcf()
		plt.show()

		if(wanna_save):

			fig.savefig(os.path.join(self.plot_path, filename + ".png"))

	@staticmethod
	def strutil(num):
		if(num <= 9):
			return '0' + str(num)
		else:
			return str(num)

	def generate_csv(self):
		for i in range(1, 25):
			data_clean, samplerate = sf.read('R:/Work/Flipkart/Dataset/CLEAN/clean/clean/sp'+ strutil(i)+'.wav')
			data_dirty, samplerate = sf.read('R:/Work/Flipkart/Dataset/DIRTY/babble_0dB/0dB/sp' + strutil(i)+'_babble_sn0.wav')

			with open('sound_x_train_big.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				np.savetxt(f, data_dirty, delimiter = ",")

			with open('sound_y_train_big.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				np.savetxt(f, data_clean, delimiter = ",")



		for i in range(25, 31):
			data_clean, samplerate = sf.read('R:/Work/Flipkart/Dataset/CLEAN/clean/clean/sp'+ strutil(i)+'.wav')
			data_dirty, samplerate = sf.read('R:/Work/Flipkart/Dataset/DIRTY/babble_0dB/0dB/sp' + strutil(i)+'_babble_sn0.wav')

			with open('sound_x_test_big.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				np.savetxt(f, data_dirty, delimiter = ",")

			with open('sound_y_test_big.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				np.savetxt(f, data_clean, delimiter = ",")




if __name__ == '__main__':
	
	pass






