# Scott Speaks Python App

Do you ever find yourself wanting to hear Scott's voice even when he's not around?\
If the answer is yes, then this app is for you! 😄

Steps to get up and running:
1. Pull this repo
2. Create a python venv and activate (`python -m env PATH/TO/REPO` & `source bin/activate`)
3. Download library dependencies using `pip install -r requirements.txt`
4. Run python app using `python speech_generator.py`
5. Type any sentence and you will hear it be spoken by Scott
6. *\* You may also need to install Tkinter for this to work, methods vary by os (eg. brew for Mac)*

## How does it Work?
<img width="911" alt="image" src="https://user-images.githubusercontent.com/47277374/165859297-8ee2711e-8eed-422f-af78-a36100c0d159.png">

### Phonetic Dictionary
The project makes use of the [Moby Project](https://en.wikipedia.org/wiki/Moby_Project) phonetic dictionary which is the largest phonetic database, containing 177,267 words.
The dictionary represents the pronunciation of words using a defined set of 44 phonemes (or sounds).
Using just these 44 sounds, one can piece them together to construct the sound of any word in the English language.
This is the logic behind how this speech-to-text app works. In fact you can hear me pronounce each of the 44 phonemes by browsing the `/wavs`p directory!

### Lexical Analysis
Each phoneme in the Moby dictionary is represented with a unique set of characters - 
for example the **SCHWA** phoneme (sounds like 'uh') is represented using `/-/`.
We construct a lexical grammar that declares which characters represent which phonemes and define rules for how words are constructed using phonemes.
Using this grammar we use a lexer tokenise our phonemes and match the corresponding audiofile to our token.

### Audio Concatenation
Joining Audio files is easily accomplished using the `pydub` library. It is as simple as loading the files as AudioSegments and using the `+` operator
to join them together.
