from django.http import HttpResponse
from django.shortcuts import render, redirect
import pickle
import sklearn
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def predict_result(request):
    output = {'res' : 'none'}
    try:
        print("inside try")
        Goiter = int(request.GET.get('goiter'))
        FTI_measured = int(request.GET['FTI_measured'])
        T4U_measured = int(request.GET['T4U_measured'])
        T3_measured = int(request.GET['T3_measured'])
        query_hypothyroid = int(request.GET['query_hypothyroid'])
        psych = int(request.GET['psych'])
        thyroid_surgery = int(request.GET['thyroid_surgery'])
        on_thyroxine = int(request.GET['on_thyroxine'])
        sex = int(request.GET['sex'])
        query_hyperthyroid = int(request.GET['query_hyperthyroid'])
        pregnant = int(request.GET['pregnant'])
        tumor = int(request.GET['tumor'])
        T3 = float(request.GET['T3'])
        TSH = float(request.GET['TSH'])
        TT4 = float(request.GET['TT4'])
        FTI = float(request.GET['FTI'])
        print("get Done")

        pickled_model = pickle.load(open(BASE_DIR/'model.pkl', 'rb'))

        si1 = [[Goiter,FTI_measured,T4U_measured,T3_measured,query_hypothyroid,psych,thyroid_surgery,on_thyroxine,sex,query_hyperthyroid,pregnant,tumor,T3,TSH,TT4,FTI]]
        result = pickled_model.predict(si1)

        s = "Still trying to predict"

        if result[0] == 0:
            s = "Congrats! Thyroid Not Detected."
        else:
            s = "Sorry! It's Thyroid."
        print(s)
        output['res'] = s
    except:
        pass
    return render(request, 'index.html', output)

def home_page(request):
    return render(request, 'index.html')