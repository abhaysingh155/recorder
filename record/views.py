from django.shortcuts import render, redirect
import sounddevice as sd
from scipy.io.wavfile import write
from django.contrib import messages

# Create your views here.
def record(request):
	return render(request, "base.html")

def startRecording(request):

	fs = 44100  # this is the frequency sampling; also: 4999, 64000
	seconds = 30  # Duration of recording
	 
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	sd.wait()  # Wait until recording is finished
	write('static/output.mp3', fs, myrecording)  # Save as WAV file

	messages.add_message(request, messages.INFO, 'Recording has been stored as "output.mp3" !!!')
	return render(request, "base.html")

