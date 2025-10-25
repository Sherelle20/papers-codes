"""
Before run please delete this file spkr_59_word_60_st_1.wav 
"""
import os
import numpy as np
import wave

def stereo_to_mono(file_path, output_path, new_frame_rate=16000):
    with wave.open(file_path, 'rb') as stereo_file:
        params = stereo_file.getparams()
        num_channels, sample_width, old_frame_rate, num_frames = params[:4]

        frames = stereo_file.readframes(num_frames)
        audio_data = np.frombuffer(frames, dtype=np.int16)

        audio_data = np.reshape(audio_data, (num_frames, num_channels))

        mono_data = np.mean(audio_data, axis=1).astype(np.int16)

        with wave.open(output_path, 'wb') as mono_file:
            mono_file.setnchannels(1)
            mono_file.setsampwidth(sample_width)
            mono_file.setframerate(new_frame_rate)
            mono_file.writeframes(mono_data.tobytes())

def convert_folder_to_mono(input_folder, output_folder, new_frame_rate=16000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.wav'):
           
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            stereo_to_mono(input_path, output_path, new_frame_rate)
            print(f"Converted {filename} to mono with a sample rate of {new_frame_rate} Hz.")




input_folder = '/home/sherelle/Documents/yemba_dataset'
output_folder = '/home/sherelle/Documents/yemba_dataset_1'


convert_folder_to_mono(input_folder, output_folder)
