import pickle
import json
import Config
import numpy as np

class MedicalDrug():
    def __init__(self,Age,Sex,BP,Cholestrol,Na_to_K):
        self.Age = Age
        self.Sex = Sex
        self.BP = BP
        self.Cholestrol = Cholestrol
        self.Na_to_K = Na_to_K


    def load_model(self):
        with open(Config.MODEL_FILE_PATH,'rb') as f:
            self.DT_CLF_Model = pickle.load(f)

        with open(Config.JSON_FILE2_PATH,'r') as f:
            self.Final_Data = json.load(f)

        with open(Config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_drugs(self):
        self.load_model()

        Test_array = np.zeros(5)
        Test_array[0] = self.Age
        Test_array[1] = self.json_data['Sex'][self.Sex]
        Test_array[2] = self.json_data['BP'][self.BP]
        Test_array[3] = self.json_data['Cholestrol'][self.Cholestrol]
        Test_array[4] = self.Na_to_K

        print('Test array is :',Test_array)

        dt_model = self.DT_CLF_Model.predict([Test_array])

        final_dt_model = self.Final_Data[str(dt_model[0])]

        return final_dt_model