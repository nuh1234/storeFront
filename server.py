from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    itemCount = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    now = datetime.datetime.now()
    dateString = now.strftime("%B %d %Y %I:%M%p")
    return render_template("checkout.html", user=request.form, itemCount=itemCount, dateTime=dateString)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    