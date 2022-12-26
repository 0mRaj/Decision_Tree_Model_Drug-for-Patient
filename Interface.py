from flask import Flask, render_template,request,jsonify
import Config
from Project_App.Utils import MedicalDrug

app = Flask(__name__)

########################### HOME API ####################################
@app.route('/')
def hello_flask():
    print("WELCOME to Flask")
    return jsonify({'Model':"Sucessfully builded"})

##############################################################################################

@app.route("/predict_charges")
def get_drug_medicine():
    data = request.form
    Age= eval(data['Age'])
    Sex= data['Sex']
    BP= data['BP']
    Cholestrol= data['Cholestrol']
    Na_to_K= eval(data['Na_to_K'])
    

    Drug_pred = MedicalDrug(Age,Sex,BP,Cholestrol,Na_to_K)
    Final_Drug_pred = Drug_pred.get_predicted_drugs()

    return jsonify({'Result':f"As per Given details required Medicine is :{Final_Drug_pred}"})




if __name__ == '__main__':
    app.run()