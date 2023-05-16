from flask import Flask, request ,render_template ,url_for
from collections import namedtuple
import openai
from apikey import apikey

openai.api_key = "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"

model = "curie:ft-personal-2023-05-14-05-52-10"
temperature = 0.5

def give_response(prompt):
    response = openai.Completion.create(
        prompt=prompt,
        model=model,
        temperature=temperature
    )
    text = response.choices[0].text
    separator = '\n'

    result = text.split(separator, 1)[0] 
    return result

app = Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def index():
    prompt = ''
    completion = ''
    if(request.method == 'POST'):
        prompt = request.form["Prompt"]
        if(prompt != ''):
            completion = give_response(prompt + '->')
        
    return render_template('index.html',prompt = prompt,completion = completion)

# @app.route('/api')
# def api():
#     user_input = request.args.get('input')
#     print(type(user_input))
#     answer = give_response(user_input+'->')
#     return '<h1>'+answer+'</h1>'



if __name__ == '__main__':
    app.run(debug=True)