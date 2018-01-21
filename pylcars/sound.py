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
        self.streams=[]

    def __del__(self):
        if self.wav:
            self.wav.terminate()

    def sound(self, file):
        #first close old, allready played sounds:
        for stream in self.streams:
            if not stream.is_active():
                stream.stop_stream()
                stream.close()
                self.streams.remove(stream)
        if self.wav:
            chunk = 256
            wf = wave.open(file, 'rb')

            # define callback (2)
            def callback(in_data, frame_count, time_info, status):
                data = wf.readframes(frame_count)
                return data, pyaudio.paContinue

            # open stream using callback (3)
            stream = self.wav.open(format=self.wav.get_format_from_width(wf.getsampwidth()),
                                   channels=wf.getnchannels(),
                                   rate=wf.getframerate(),
                                   output=True,
                                   frames_per_buffer=chunk,
                                   stream_callback=callback,
                                   )# start=True)
            self.streams.append(stream)

    def setPlay_sound(self, play_sound=True):
        if self.wav:
            self.wav.terminate()
            self.wav = None
        if play_sound:
            self.wav = pyaudio.PyAudio()
