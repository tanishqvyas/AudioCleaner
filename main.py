import os

# Coustom imports
from utils.preprocessing.generate_noisy_input import InputGenerator


# Paths for respective data folders
clean_audio_path = os.path.join("data", "clean")
noise_audio_path = os.path.join("data", "noise")
input_audio_path = os.path.join("data", "input")
audio_plot_path  = os.path.join("data", "plots")


obj = InputGenerator(clean_audio_path, noise_audio_path, input_audio_path, audio_plot_path)

obj.generate_noisy_input(os.path.join(clean_audio_path, "dev"), os.path.join(input_audio_path, "dev"))

obj.generate_noisy_input(os.path.join(clean_audio_path, "test"), os.path.join(input_audio_path, "test"))

obj.generate_noisy_input(os.path.join(clean_audio_path, "train"), os.path.join(input_audio_path, "train"))