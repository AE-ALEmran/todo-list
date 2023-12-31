from gtts import gTTS
import os

def text_to_speech(text, language='bn', output_file='output.mp3'):

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    os.system(f'start {output_file}')

if __name__ == "__main__":
    text=input('Enter the text you want:')
    text_to_speech(text)
