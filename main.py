from flask import Flask, render_template, request
import os
import codecs

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        file = request.files['textfile']
        file.save(os.path.join(file.filename))
        with codecs.open(file.filename, 'r', 'utf-8') as f:
            file_text = f.read()
        os.remove(file.filename)
        answer = wordCounter(file_text)

    return render_template('index.html', ans= answer[0], word_count = answer[1])

def wordCounter(file_text):

    separators = ",.?!:;'/|\"@#$%^&*()_+-=1234567890\n\r"

    for symb in separators:
        file_text = file_text.replace(symb, ' ')

    file_text = file_text.lower()
    words = file_text.split(' ')
    word_list = set(words)
    word_list.remove('')

    counter = {}
    for word in words:
        counter[word] = 0

    max_count = 0
    ans_word = ''

    for word in words:
        for i in word_list:
            if i == word:
                counter[i] += 1

    for key, value in counter.items():
        if value > max_count:
            ans_word = key
            max_count = value

    return ans_word, max_count

if __name__ == '__main__':
    app.run()