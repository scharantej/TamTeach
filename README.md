## Flask Application Design for Teaching Beginner Tamil

### HTML Files

**index.html (Homepage)**
- Contains introductory text and links to Tamil learning modules.

**modules/basic_vocabulary.html**
- Basic Tamil vocabulary, such as greetings and common words.

**modules/grammar_basics.html**
- Fundamental grammar rules of Tamil, including sentence structure and tenses.

**modules/pronunciation_guide.html**
- Detailed guide on Tamil pronunciation, including audio and visual aids.

**modules/cultural_insights.html**
- Cultural context and insights about Tamil heritage and tradition.

### Routes

**app.py**

**@app.route('/')**
def index():
    """Homepage route, displays the introduction and module links"""
    return render_template('index.html')

**@app.route('/modules/basic_vocabulary')**
def basic_vocabulary():
    """Displays the basic Tamil vocabulary module"""
    return render_template('modules/basic_vocabulary.html')

**@app.route('/modules/grammar_basics')**
def grammar_basics():
    """Displays the grammar basics module"""
    return render_template('modules/grammar_basics.html')

**@app.route('/modules/pronunciation_guide')**
def pronunciation_guide():
    """Displays the pronunciation guide module"""
    return render_template('modules/pronunciation_guide.html')

**@app.route('/modules/cultural_insights')**
def cultural_insights():
    """Displays the cultural insights module"""
    return render_template('modules/cultural_insights.html')