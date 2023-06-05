# # # # stri="constition of india"
# # # # lst=stri.split()
# # # # str1=""
# # # # for i in range(len(lst)):
# # # # 	str1+=" "+lst[i]
# # # # print(https://en.wikipedia.org/wiki/str1')
# # # # import requests

# # # # res = requests.get('https://reqres.in/api/users?page=2')
# # # # var=res.json().get("data")
# # # # for i in var:

# # # #     print(i["email"])
# # # # ------------
# # # # print(f'Total users: {res.json().get("data")}')
# # # # json_res = res.json()


# # # # json_res.get('total')
# # # # json_res["total"]
# # # #####
# # # import requests

# # # res = requests.get('https://weatherdbi.herokuapp.com/data/weather/hyderabad')
# # # reg=res.json()

# # # region = reg["region"]
# # # time = reg["currentConditions"]["dayhour"]
# # # print(region,time)

# # # temp = reg["currentConditions"]["temp"]["c"]
# # # precip = reg["currentConditions"]["precip"]
# # # humidity = reg["currentConditions"]["humidity"]
# # # wind = reg["currentConditions"]["wind"]["km"]
# # # print("Temperature:",temp,"Precip:",precip,"humidity:",humidity, "wind:",wind)

# # # var=res.json().get("temp")
# # # #print(reg,var)
# # # # for i in var:
# # # #     print(i)
# # import urllib
# # import json

# # serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# # while True:
# #     address = input('Enter location: ')
# #     if len(address) < 1 : break

# #     url = serviceurl + urllib.parse.urlencode({'sensor':'false',
# #        'address': address})
# #     print ('Retrieving', url)
# #     uh = urllib.request.urlopen(url)
# #     data = uh.read()
# #     print ('Retrieved',len(data),'characters')

# #     js = json.loads(str(data))


# # import json
# # import requests
# # API_URL = "https://api-inference.huggingface.co/models/gpt2"
# # headers = {"Authorization": "Bearer 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"}
# # def query(payload):
# #     data = json.dumps(payload)
# #     response = requests.request("POST", API_URL, headers=headers, data=data)
# #     return json.loads(response.content.decode("utf-8"))
# # data = query("what is NASA ")
# # print(data)


from googlesearch import search
query=input("Enter query")
sen=""
for i in search(query, tld="com", num=10,stop=10,pause=1):
    sen = sen + i + "*"
print(sen)
'''

'''
import numpy as np
import pandas as pd
import pickle
from nltk.stem import PorterStemmer
ps = PorterStemmer()
# loading model
loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
# Unpickle dataframes
symptom_severity = pd.read_pickle("symptom_severity.pkl")
disease_description = pd.read_pickle("disease_description.pkl")
disease_precaution = pd.read_pickle("disease_precaution.pkl")
def DiseasePrediction(text):
    bool_list = []
    text_token_list = text.split()
    text_token_list = [ps.stem(w) for w in text_token_list]
    text_token_set = set(text_token_list)
    print("So far done")
    for ele in symptom_severity["Symptom"]:
        ele = ele.split('_')
        ele = [ps.stem(w) for w in ele]
        ele_set = set(ele)
        flag = 0
        for i in range(len(text_token_list)):
            if (len(ele) > 1):
                if (ele_set.issubset(text_token_set)):
                    flag = 1
                else:
                    flag = 0
            else:
                if (text_token_list[i] == ele[0]):
                    flag = 1
                else:
                    flag = 0
        bool_list.append(flag)
    symptom_severity["bool_list"] = bool_list
    symptom_severity["weight_bool_list"] = symptom_severity["weight"] * symptom_severity["bool_list"]
    weight_bool_list = list(symptom_severity["weight_bool_list"])
    # Disease Prediction
    X_arr = np.array(weight_bool_list)
    is_all_zero = np.all((X_arr == 0))
    if is_all_zero:
        print("Sorry, your symptoms don't match our database.")
    else:
        y_pred = loaded_model.predict(X_arr.reshape(1, -1))
        Predicted_Disease = y_pred[0]
        disease = "We are predicitng you have: " + Predicted_Disease.upper() + "\n"
        print("WE ARE PREDICTING THAT YOU HAVE ------- ", Predicted_Disease.upper())
        # Disease Description
        for i in range(len(disease_description)):
            if (disease_description["Disease"][i] == Predicted_Disease):
                disease = disease + "Description of the disease :- \n" + disease_description["Description"][i] + "\n"
                print("DESCRIPTION OF THE DISEASE : ---- \n")
                print(disease_description["Description"][i])
        # Disease Precaution
        for i in range(len(disease_precaution)):
            if (disease_precaution["Disease"][i] == Predicted_Disease):
                disease = disease + "Precautions that can be taken:-\n"
                disease = disease + "PRECAUTION 1: " + disease_precaution["Precaution_1"][i] + "\n"
                disease = disease + "PRECAUTION 2: " + disease_precaution["Precaution_2"][i] + "\n"
                disease = disease + "PRECAUTION 3: " + disease_precaution["Precaution_3"][i] + "\n"
                disease = disease + "PRECAUTION 4: " + disease_precaution["Precaution_4"][i] + "\n"
        print(disease)
symptoms_by_user = input("Write about your SYMPTOMS: ")
DiseasePrediction(symptoms_by_user)
