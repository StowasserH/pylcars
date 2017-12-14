# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, QtSvg
import pyaudio
import wave

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Gui(QtGui.QMainWindow):
    default_style = "border: none;\nbackground: #000;\n"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(self.mainWindowSize)
        MainWindow.setStyleSheet(self.default_style)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


    def sound(self, file):
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

    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)
        # self.defaultStyle=_fromUtf8("border: none;\nbackground: #000;\n")
        # "background-image: url(:/AddButton.png);"
        # "background-repeat: no-repeat;"
        # "background-position: center center"

        self.mainWindowSize = QtCore.QSize(800, 480)
        self.setupUi(self)
        self.wav = pyaudio.PyAudio()

    def __del__(self):
        self.wav.terminate();
