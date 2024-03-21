
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modules/basic_vocabulary')
def basic_vocabulary():
    return render_template('modules/basic_vocabulary.html')

@app.route('/modules/grammar_basics')
def grammar_basics():
    return render_template('modules/grammar_basics.html')

@app.route('/modules/pronunciation_guide')
def pronunciation_guide():
    return render_template('modules/pronunciation_guide.html')

@app.route('/modules/cultural_insights')
def cultural_insights():
    return render_template('modules/cultural_insights.html')

if __name__ == '__main__':
    app.run(debug=True)
