#Simple Login application in python
from flask import Flask,request,render_template,abort
app=Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index',methods=('GET', 'POST'))
def index():
    if request.form["user"]=="vinil":
        return render_template('index.html',user=request.form["user"])
    else:
	    abort(404)

'''@app.route('/success')
def success():
    return redirect_template('index.html')
	'''	
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'),404

if __name__=='__main__':
    app.run(debug=True)