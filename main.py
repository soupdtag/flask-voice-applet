from flask import Flask, request, render_template, redirect
import os
import speech_recognition as sr

app = Flask(__name__)

# STEP 1: record user input
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<turkId>/<filenum>/record')
def record(turkId, filenum):
	return render_template('recorder.html', name=turkId, num=filenum)


# STEP 2: upload user input
@app.route('/<turkId>/<filenum>/upload', methods=['GET', 'POST'])
def upload(turkId, filenum):
	filename = os.path.join(os.path.expanduser('~'),'turktasks',turkId,str(filenum)+'.wav')
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	audio_data = request.files['audio_data']
	audio_data.save(filename)
	print("upload complete.")
	return ('', 202)


# STEP 3: validate user input
@app.route('/<turkId>/<filenum>/validate', methods=['GET', 'POST'])
def validate(turkId, filenum):
#	filename = os.path.join(os.path.expanduser('~'),'turktasks',turkId,str(filenum)+'.wav')
#	snr = v1(filename)		# signal-to-noise ratio
#	transc = v2(filename)		# transcription of audio file
#	accuracy = v3(filename)		# how much the transcript aligns with the ground truth
	print("redirecting to validate")
	return redirect("/" + turkId + "/" + filenum + "/complete")
#	return redirect("/" + turkId + "/" + filenum + "/complete")
#	return redirect(url_for(complete(turkId, filenum))

## 1 - signal/noise ratio
#def v1(f):

## 2 - google speech api transcription
#def v2(f):

## 3 - comparison w/ transcript
#def v3(f):


# STEP 4: data collection complete; return validation key (scrambled turkId) to worker
@app.route('/<turkId>/<filenum>/complete')
def complete(turkId, filenum):
	print("arrived at complete")
	return 'Thanks! Please click the \'Submit\' button to proceed.'

if __name__ == "__main__":
	app.run()