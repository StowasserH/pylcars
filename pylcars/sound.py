"""Audio playback functionality for LCARS interface.

This module provides sound playing capabilities for the LCARS interface using
PyAudio for real-time audio streaming. It manages multiple concurrent audio streams
and handles WAV file playback with proper resource cleanup.
"""
import pyaudio
import wave
from typing import Optional, List, Callable, Tuple, Any


class Sound:
    """Audio playback manager for LCARS interface sounds.

    Manages WAV file playback through PyAudio with support for multiple
    concurrent audio streams. Handles resource allocation and cleanup for
    audio playback.

    Attributes:
        sound_file: Path to the sound file to play.
        wav: PyAudio instance for audio playback.
        streams: List of active audio streams.
    """
    sound_file: Optional[str]
    wav: Optional[pyaudio.PyAudio]
    streams: List[pyaudio.Stream]

    def set_sound_file(self, sound_file: str) -> None:
        """Set the sound file to be played.

        Args:
            sound_file: Path to the WAV sound file.
        """
        self.sound_file = sound_file

    def play_sound(self) -> None:
        """Play the configured sound file.

        Plays the sound file set via set_sound_file(). Does nothing if no
        sound file has been configured.
        """
        if self.sound_file:
            self.sound(self.sound_file)

    def __init__(self) -> None:
        """Initialize the Sound player.

        Sets up empty state for sound playback. PyAudio instance is created
        on demand when sound playback is enabled.
        """
        self.sound_file = None
        self.wav = None
        self.streams = []

    def __del__(self) -> None:
        """Clean up PyAudio resources on object destruction.

        Closes all active streams and terminates the PyAudio instance
        to prevent resource leaks.
        """
        try:
            # Close all streams first
            for stream in self.streams:
                try:
                    if stream.is_active():
                        stream.stop_stream()
                    stream.close()
                except Exception:
                    pass

            # Then terminate PyAudio
            if self.wav:
                self.wav.terminate()
        except Exception:
            # Suppress exceptions in __del__ to prevent issues during shutdown
            pass

    def sound(self, file: str) -> None:
        """Play a WAV audio file.

        Opens the specified WAV file and plays it asynchronously using a
        PyAudio stream. Automatically cleans up finished streams before
        opening a new one.

        Args:
            file: Path to the WAV file to play.

        Raises:
            wave.Error: If the WAV file is invalid or cannot be read.
            FileNotFoundError: If the file does not exist.
        """
        # Clean up inactive streams using list comprehension to avoid modifying list during iteration
        self.streams = [s for s in self.streams if s.is_active()]

        # Close any remaining inactive streams
        for stream in self.streams:
            try:
                if not stream.is_active():
                    stream.stop_stream()
                    stream.close()
            except Exception:
                pass

        if not self.wav:
            return

        try:
            chunk: int = 256
            wf: wave.Wave_read = wave.open(file, 'rb')

            # define callback (2)
            def callback(in_data: bytes, frame_count: int, time_info: Any, status: Any) -> Tuple[bytes, int]:
                data: bytes = wf.readframes(frame_count)
                return data, pyaudio.paContinue

            # open stream using callback (3)
            stream: pyaudio.Stream = self.wav.open(
                format=self.wav.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                frames_per_buffer=chunk,
                stream_callback=callback,
            )
            self.streams.append(stream)
            # Note: wf is kept open because the callback still needs it during playback
        except (FileNotFoundError, wave.Error) as e:
            print(f"Error playing sound '{file}': {e}")

    def set_play_sound(self, play_sound: bool = True) -> None:
        """Enable or disable sound playback capability.

        Initializes or terminates the PyAudio instance based on the desired state.
        When disabled, cleans up all active streams and the PyAudio instance.

        Args:
            play_sound: True to enable sound playback, False to disable (default: True).
        """
        # Clean up all existing streams
        for stream in self.streams:
            try:
                if stream.is_active():
                    stream.stop_stream()
                stream.close()
            except Exception:
                pass
        self.streams = []

        # Terminate PyAudio if it's running
        if self.wav:
            try:
                self.wav.terminate()
            except Exception:
                pass
            self.wav = None

        # Initialize PyAudio if requested
        if play_sound:
            try:
                self.wav = pyaudio.PyAudio()
            except Exception as e:
                print(f"Error initializing PyAudio: {e}")
                self.wav = None
