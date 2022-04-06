from flask import Flask, render_template, request
from threading import Thread

def main():
  #creates the app object
  app = Flask(__name__)
  
  
  #when / is passed as the route, return a template
  @app.route('/', methods=['GET','POST'])
  def index():
    #read https://en.wikipedia.org/wiki/POST_(HTTP)
    #for example, if you submit a form in html, a post request will be sent to the server.
    if request.method =="POST":
      #request.form is the object that contains the form data in a post request.
      
      print(request.form)
      
      #process data here
      return render_template('index.html')
    
    
  
    #default render_template
    return render_template('index.html')


  
  def run():
    #runs the app
    app.run(host='0.0.0.0', port = 8081)

  def begin():
    #creates a thread to run the app
    t= Thread(target=run)
    t.start()
  begin()

if __name__ == '__main__':
  main()