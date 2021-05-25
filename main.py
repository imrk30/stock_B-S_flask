from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def calorie():
    if request.method == 'POST':
        exchange = request.form['exchange']
        sname = request.form['sname']
        bp = request.form['bp']
        sp = request.form['sp']
        qty = request.form['qty']
        exchange = exchange.upper().strip()
        sname = sname.upper().strip()
        end = float(sp) - float(bp)
        total = end * int(qty)
            
        # show = 'Exchange '+exhange.upper().strip()+' Stock '+sname.upper().strip()+' Profit/Loss '+str(total)

        return render_template('result.html',
        exchange=exchange,
        sname=sname,
        total=total)
    else:
        return 'Sorry !!'

if __name__ == '__main__':
   app.run(debug=True)