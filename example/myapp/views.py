from django.shortcuts import render
import pandas as pd

def index(request):
    if request.method == 'POST' and request.FILES['fileInput']:
        file = request.FILES['fileInput']
        df = pd.read_excel(file, sheet_name='Sheet1', header=0)

        grade_df = df.groupby('grade')['value'].agg(["min", "max", "mean"]).reset_index().rename(columns={"mean": "avg"})
        email_df = df.assign(domain=df['email'].apply(lambda x: x.split("@")[1])).groupby('domain')['value'].agg("count").sort_values(ascending=False).reset_index()

        return render(request, 'result.html', {'grade_df': grade_df, 'email_df': email_df})

    return render(request, 'index.html')
