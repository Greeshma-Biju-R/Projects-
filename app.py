
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def index():
return render_template('index.html')
@app.route('/recognize', methods=['POST'])
def recognize_command():
data = request.get_json()
transcript = data.get('transcript', '')
command = process_transcript(transcript)
return jsonify({'message': command})
def process_transcript(transcript):
# Process the transcript to recognize commands
if 'തുറക്കുക ' in transcript:
return 'Opening...'
elif 'അടക്കുക ' in transcript:
return 'Closing...'
elif 'പിറകകോട്ട് കപോകുക ' in transcript:
return 'Going back...'
elif 'മുകനോട്ട് കപോകുക ' in transcript:
return 'Going forward...'
else:
return 'Command not recognized.'
if __name__ == '__main__':
app.run(debug=True)
