import os

# Coustom imports
from utils.preprocessing.generate_noisy_input import InputGenerator


# Paths for respective data folders
clean_audio_path = os.path.join("data", "clean")
noise_audio_path = os.path.join("data", "noise")
input_audio_path = os.path.join("data", "input")


obj = InputGenerator(clean_audio_path, noise_audio_path, input_audio_path)

obj.generate_noisy_input()

# obj.play_audio(os.path.join(clean_audio_path, "name.wav"))
