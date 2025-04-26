# Step 1: Setup TTS with gTTS
import os
from gtts import gTTS
import pygame
import time

def text_to_speech_with_gtts(input_text, output_filepath):
    language = 'en'

    # Generate speech
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Play using pygame
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(output_filepath)
        pygame.mixer.music.play()
        print("Playing audio...")

        # Wait while audio is playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        pygame.mixer.music.unload()
        pygame.mixer.quit()
    except Exception as e:
        print(f"Error during playback: {e}")

# Example usage
input_text = "Hi, How are you???"
output_filepath = "gtts_testing_autoplay.mp3"
text_to_speech_with_gtts(input_text, output_filepath)

