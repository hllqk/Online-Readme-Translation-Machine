from flask import Flask,render_template,request
from include.index import *
app = Flask('app')
@app.route('/')
def hello_world():
  return render_template('index.html')
@app.route('/result',methods=['POST'])
def result():
  r=request.form['readme']
  translate(r)
  #print('翻译完成，前往out.txt查看')
  return render_template('out.html')

app.run(host='0.0.0.0', port=8080,debug = True)
