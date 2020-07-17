# Inbuilt Imports
import os

# Coustom imports
from utils.preprocessing.generate_noisy_input import InputGenerator



# Meta Data for process control
meta_data = {
	
	"wanna_generate_input": True,
	"num_train_samples": 10000,
	"num_dev_samples": 1120,
	"num_test_samples" : 1120,

	"wanna_train": False,
	"wanna_test": False
}





# Paths for respective data folders
clean_audio_path = os.path.join("data", "clean")
noise_audio_path = os.path.join("data", "noise")
input_audio_path = os.path.join("data", "input")
audio_plot_path  = os.path.join("data", "plots")


# Creating an object of InputGenerator class
obj = InputGenerator(clean_audio_path, noise_audio_path, input_audio_path, audio_plot_path)


# Input Data Generation
if(meta_data["wanna_generate_input"]):

	obj.generate_noisy_input(os.path.join(clean_audio_path, "dev"), os.path.join(input_audio_path, "dev"))

	obj.generate_noisy_input(os.path.join(clean_audio_path, "test"), os.path.join(input_audio_path, "test"))

	obj.generate_noisy_input(os.path.join(clean_audio_path, "train"), os.path.join(input_audio_path, "train"))