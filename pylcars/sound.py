import pyaudio
import wave
from typing import Optional, List, Callable, Tuple, Any


class Sound:
    sound_file: Optional[str]
    wav: Optional[pyaudio.PyAudio]
    streams: List[pyaudio.Stream]

    def set_sound_file(self, sound_file: str) -> None:
        self.sound_file = sound_file

    def play_sound(self) -> None:
        if self.sound_file:
            self.sound(self.sound_file)

    def __init__(self) -> None:
        self.sound_file = None
        self.wav = None
        self.streams = []

    def __del__(self) -> None:
        if self.wav:
            self.wav.terminate()

    def sound(self, file: str) -> None:
        # first close old, allready played sounds:
        for stream in self.streams:
            if not stream.is_active():
                stream.stop_stream()
                stream.close()
                self.streams.remove(stream)
        if self.wav:
            chunk: int = 256
            wf: wave.Wave_read = wave.open(file, 'rb')

            # define callback (2)
            def callback(in_data: bytes, frame_count: int, time_info: Any, status: Any) -> Tuple[bytes, int]:
                data: bytes = wf.readframes(frame_count)
                return data, pyaudio.paContinue

            # open stream using callback (3)
            stream: pyaudio.Stream = self.wav.open(format=self.wav.get_format_from_width(wf.getsampwidth()),
                                   channels=wf.getnchannels(),
                                   rate=wf.getframerate(),
                                   output=True,
                                   frames_per_buffer=chunk,
                                   stream_callback=callback,
                                   )  # start=True)
            self.streams.append(stream)

    def setPlay_sound(self, play_sound: bool = True) -> None:
        if self.wav:
            self.wav.terminate()
            self.wav = None
        if play_sound:
            self.wav = pyaudio.PyAudio()
