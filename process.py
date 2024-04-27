from pydub import AudioSegment
from pydub.playback import play

def load_audio(file_path):
    """Load an audio file."""
    return AudioSegment.from_file(file_path)

def play_audio(audio):
    """Play the loaded audio."""
    play(audio)

def apply_equalization(audio, equalizer_values):
    """Apply equalization to the audio."""
    for i, value in enumerate(equalizer_values):
        audio = audio.apply_gain(value)
    return audio
