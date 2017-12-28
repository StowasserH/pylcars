import pyaudio
import wave


class Sound():
    def set_sound_file(self, sound_file):
        self.sound_file = sound_file

    def play_sound(self):
        if self.sound_file:
            self.sound(self.sound_file)

    def __init__(self):
        self.sound_file = None
        self.wav = None

    def __del__(self):
        if self.wav:
            self.wav.terminate()

    def sound(self, file):
        if self.wav:
            CHUNK = 256
            wf = wave.open(file, 'rb')

            # define callback (2)
            def callback(in_data, frame_count, time_info, status):
                data = wf.readframes(frame_count)
                return (data, pyaudio.paContinue)

            # open stream using callback (3)
            stream = self.wav.open(format=self.wav.get_format_from_width(wf.getsampwidth()),
                                   channels=wf.getnchannels(),
                                   rate=wf.getframerate(),
                                   output=True,
                                   frames_per_buffer=CHUNK,
                                   stream_callback=callback)
            stream.start_stream()

    def setPlay_sound(self, play_sound=True):
        if self.wav:
            self.wav.terminate()
            self.wav = None
        if play_sound:
            self.wav = pyaudio.PyAudio()
