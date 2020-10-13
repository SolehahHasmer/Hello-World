
from flask import Flask, render_template #import Flask and rendere_template method from flask

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html') #call html file from template folder

if __name__ == '__main__':
  app.run()
