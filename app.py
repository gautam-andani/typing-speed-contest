from flask import Flask, request, render_template, current_app, g, redirect
import time
import Levenshtein as minimum_edit_distance
import new_para as paragraphs

app = Flask(__name__)

@app.route('/')
def home() -> 'redirect':
    time.sleep(1.5)
    return redirect('/entry')


@app.route('/entry')
def entry() -> 'html':
    task = paragraphs.random_para_generator(40)   #generates random paragraph of 40 words using openai
    return render_template('entry.html', task=task, the_title='Welcome to my site!')


@app.route('/result', methods=['GET', 'POST'])
def result() -> 'html':

    user_input = request.form["text"]
    completion_time = int(request.form['completion_time'])
    words_typed = len(str(user_input).split(' '))
    distance = minimum_edit_distance.distance(user_input, task)

    # Calculate accuracy (assuming the length of actual_task_text is non-zero)
    accuracy = (1 - (distance / len(task))) * 100
    accuracy=round(accuracy,2)
    typing_speed = words_typed/completion_time*60
    
    return render_template('results.html',the_title='Gautam',completion_time=completion_time, accuracy=accuracy, task=task, user_input=user_input, typing_speed=typing_speed)


if __name__ == '__main__':
    app.run(debug=True)
