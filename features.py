from playsound import playsound
#playing Assistant sound function
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


import sounddevice as sd
import numpy as np
import librosa
import os
from scipy.spatial.distance import euclidean
# Function to record audio
def record_audio(duration=5, sample_rate=22050):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete.")
    return audio.flatten()

# Function to extract MFCC features
def extract_features(audio, sample_rate=22050):
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

# Function to save a reference voice sample
def save_reference_voice(reference_path="reference.npy"):
    print("Record your reference voice sample.")
    audio = record_audio()
    sample_rate = 22050
    features = extract_features(audio, sample_rate)
    np.save(reference_path, features)
    print(f"Reference voice sample saved to {reference_path}")

# Function for voice authentication
def authenticate(reference_path="reference.npy"):
    flag =""
    if not os.path.exists(reference_path):
        print("Reference voice sample not found. Please save one first.")
        return False

    print("Record your voice for authentication.")
    audio = record_audio()
    sample_rate = 22050
    features = extract_features(audio, sample_rate)

    reference_features = np.load(reference_path)
    distance = euclidean(reference_features, features)
    
    threshold = 20  # Set an appropriate threshold based on experimentation
    if distance < threshold:
        print("Authentication successful.")
        return True
        flag = 1
    else:
        print("Authentication failed.")
        return False
        flag = 0
#Main menu
#if __name__ == "__main__":
#    print("1. Save reference voice")
#    print("2. Authenticate voice")
#    choice = input("Enter your choice: ")
#    if choice == "1":
#        save_reference_voice()
#    elif choice == "2":
#        authenticate()
#    else:
#        print("Invalid choice.")