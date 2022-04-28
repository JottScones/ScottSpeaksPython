import phone_lookup as pl
import phone_parser as pp
from pydub import AudioSegment
from pydub.playback import play
from functools import reduce
import PySimpleGUI as sg

wav_file_path   = "./wavs/"
save_voice_path = "./output/voice.wav"

def save_voice(sentence, path=save_voice_path):
    combined_sound = create_voice(sentence)
    combined_sound.export(path, format="wav")

def play_voice(sentence):
    combined_sound = create_voice(sentence)
    play(combined_sound)

def create_voice(sentence):
    wav_file_names = process_tokens(sentence_to_tokens(sentence))
    audio_list     = [audio_seg(fname) for fname in wav_file_names]
    combined_sound = reduce((lambda s1, s2: s1 + s2), audio_list)
    return combined_sound

def audio_seg(filename):
    return AudioSegment.from_wav(wav_file_path + filename)

def process_tokens(tokens):
    # Place a pause between each word then flattens
    # returns list with audio file suffix
    tokens_with_pause = [word + ["PAUSE"] for word in tokens]
    tokens_flattened  = sum(tokens_with_pause,[])

    # Remove stress tokens since not currently used in this implementation
    stresses          = ["PRIM_STRESS", "SEC_STRESS"]
    without_stresses  = [t for t in tokens_flattened if t not in stresses]

    # Add .wav suffix which is name of corresoponding audio file
    wav_file_names    = [token + ".wav" for token in without_stresses]
    return wav_file_names

def sentence_to_tokens(sentence):
    # Converts str sentence first to list of strs with phonetics of each word
    # then converts phones to a list of lists of token representations of phone
    phones   = pl.sentence_lookup(sentence)
    tokens   = list(map(pp.lex_word, phones))

    return tokens

# ------------------------------------------------------------------------------
# GUI creation
layout = [
            [sg.Text("Text to speech", font='Any 30')],
            [sg.InputText('', key="-INPUT-", font='Any 20')],
            [sg.Button("Play", size=(30,1))]
        ]
window = sg.Window("Scott says", layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Play":
        play_voice(values["-INPUT-"])

window.close()
