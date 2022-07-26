from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')






@app.route('/predictAction', methods=['POST'])
def predictAction():
    if request.method == 'POST':
            gre_score=float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            research = request.form['research']
        #model = pickle.load(open('stroke_new.pkl','wb'))

        


        filename='Admission.Predictor_model(3).pkl'
        loaded_model = pickle.load(open(filename, 'rb'))

        array = [[gre_score,toefl_scoreuniversity_rating,sop,lor,cgpa,research]]

        array = [np.array(array[0],dtype = 'float64')]
        pred_admin = model.predict(array)
        result = int(pred_admin[0])
        str=""
        if result==0:
           return render_template('nochance.html',prediction=round(100*prediction[0]))
        else:
           return render_template('chance.html',prediction=round(100*prediction[0]))
        return render_template('predict.html',a = str)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)