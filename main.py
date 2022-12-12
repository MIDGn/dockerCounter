from flask import Flask
import socket

app = Flask('app')

counter = 0

@app.route('/')
def show_stat():
  global counter
  return str(counter)

@app.route('/stat')
def increment():
  global counter
  counter += 1
  return str(counter)

@app.route('/about')
def hello():
  html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
  return html.format(name="Георгий", hostname=socket.gethostname())

app.run(host='0.0.0.0', port=8080)