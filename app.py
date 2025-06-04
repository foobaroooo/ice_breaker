from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from ice_breaker import ice_breaker_with

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    summary_and_facts, profile_pic_url = ice_breaker_with(name)
    
    return jsonify({
        'summary_and_facts': summary_and_facts.content,
        'picture_url': profile_pic_url,
    })
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)

