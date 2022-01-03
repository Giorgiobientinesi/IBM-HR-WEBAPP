import pickle
import datetime as dt
import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np

loaded_model = pickle.load(open("Logistic_Regression_AI1.sav", 'rb'))
#TITLE OF THE WEB APP
st.write("""
# HR IBM Employment Attrition App
This app estimates the **Attrition** your employees!
""")

st.sidebar.header('Insert the Employee Info')

#SIDEBAR OF THE WEB APP. THIS TAKES THE INPUT OF THE USER(ETF AND WEIGHTS)
Age = st.sidebar.slider('Age', 0, 100, 18)

Overtime = st.sidebar.selectbox(
    'Does He/She work more than Standard?',
    (["Yes","No"])
)

MIncome = st.sidebar.slider('Montlhy Income', 0, 20000, 2500)

PercentSalaryHike = st.sidebar.slider('Salary Hike(in%)', 0, 1, 0)
YearsAtCompany = st.sidebar.slider('Years At Company', 0, 30, 0)

JobRole = st.sidebar.selectbox(
    'Job Role',
    (["Sales Executive","Laboratory Technician","Manufacturing Director","Research Scientist","Sales Representative","Manager","Research Director","Healthcare Representative","Human Resources"])
)

JobInvolvement = st.sidebar.slider('Job Involvement', 0, 5, 0)
StockOptionLevel = st.sidebar.slider('Stock Option Level', 0, 2, 0)
EducationField = st.sidebar.selectbox('Education Field',
    (["Life Sciences","Medical","Marketing","Technical Degree","Human Resources","Other"])
)
WorkLifeBalance = st.sidebar.slider('Work Life Balance', 0, 5, 0)


Age1 = []
Age1.append(Age)

Overtime1 = []
Overtime1.append(Overtime)

MIncome1 = []
MIncome1.append(MIncome)


PercentSalaryHike1 = []
PercentSalaryHike1.append(PercentSalaryHike)

YearsAtCompany1 = []
YearsAtCompany1.append(YearsAtCompany)
JobRole1 = []
JobRole1.append(JobRole)
JobInvolvement1 = []
JobInvolvement1.append(JobInvolvement)
StockOptionLevel1 = []
StockOptionLevel1.append(StockOptionLevel)
EducationField1 = []
EducationField1.append(EducationField)
WorkLifeBalance1 = []
WorkLifeBalance1.append(WorkLifeBalance)


df = pd.DataFrame()
df["Age"] = Age1
df["OverTime"] = Overtime1
df["Montlhy Income"] = MIncome1
df["PercentSalaryHike"] = PercentSalaryHike1
df["YearsAtCompany"] = YearsAtCompany1
df["JobRole"] = JobRole1
df["JobInvolvement"] = JobInvolvement1
df["StockOptionLevel"] = StockOptionLevel1
df["EducationField"] = EducationField1
df["WorkLifeBalance"] = WorkLifeBalance1

df['JobRole'] = df['JobRole'].map({'Sales Executive': 0, 'Laboratory Technician': 1, 'Manufacturing Director': 2, 'Research Scientist': 3, 'Sales Representative': 4, 'Manager': 5, 'Research Director': 6, 'Healthcare Representative': 7, 'Human Resources': 8})
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
df['EducationField'] = df['EducationField'].map({'Life Sciences': 0, 'Medical': 1, "Marketing": 2, "Technical Degree": 3, "Human Resources": 4, "Other": 5})

pred = loaded_model.predict(df)

st.subheader('Employee Info')
st.write(df)

st.subheader('Attrition prediction')

if pred==1:
    st.write("The Employee is estimated to leave the Company")
else:
    st.write("The Employee is estimated to **NOT** leave the Company")

