from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1, story2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = -1

debug = DebugToolbarExtension(app)

@app.route('/madlibs')
def show_form():
    return render_template('madlibs.html')

@app.route('/story-1_form')
def show_story1_form():
    prompts = story1.prompts
    return render_template('story-1_form.html', prompts=prompts)

@app.route('/story-2_form')
def show_story2_form():
    prompts = story2.prompts
    return render_template('story-2_form.html', prompts=prompts)

@app.route('/story-1')
def show_story1():
    text = story1.generate(request.args)
    return render_template('story-1.html', text=text)

@app.route('/story-2')
def show_story2():
    text = story2.generate(request.args)
    return render_template('story-2.html', text=text)

