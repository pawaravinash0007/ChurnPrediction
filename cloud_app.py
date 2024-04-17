import streamlit as st
import pandas as py 
import numpy as np 
import pickle 

grid_search = pickle.load(open("test.pkl", "rb"))

def predict(data):
  grid_search = pickle.load(open("test.pkl", "rb"))
  return grid_search.predict(data)

st.title('CHURN PREDICTION')
st.header("Telecom Retention")

col1,col2,col3 = st.columns(3)

with col1:
	st.text("SeniorCitizen")
	sc = st.slider('sc',0,2,2)

	st.text("Tenure")
	tenure = st.slider("Tenure", 1.0,72.0,1.0)

	st.text("MonthlyCharges")
	mc = st.slider("MonthlyCharges", 1.0,120.0,1.0)

	st.text("TotalCharges")
	tc = st.slider("TotalCharges", 1.0,10000.0,1.0)
	
with col2:
	st.text("InternetService_Fiber optic")
	iff = st.radio("InternetService_Fiber optic", ('Yes','No'))

	st.text("InternetService")
	isn = st.radio("InternetService", ('Yes','No'))

	st.text("OnlineSecurity")
	osy = st.radio("OnlineSecurity",('Yes','No'))

	
	st.text("OnlineBackup")
	oby = st.radio("OnlineBackup", ('Yes','No'))

	st.text("DeviceProtection")
	dy = st.radio("DeviceProtection", ('Yes','No'))

	st.text("TechSupport")
	ty = st.radio("TechSupport",('Yes','No'))

	st.text("StreamingTV")
	sty = st.radio("StreamingTV", ('Yes','No'))
	 
	st.text("StreamingMovies")
	smy = st.radio("StreamingMovies", ('Yes','No'))
	 
with col3: 
	st.text("Contract_One year")
	c1 = st.selectbox("Contract_One year",('Yes','No'))
	 
	st.text("Contract_Two year")
	c2 = st.selectbox("Contract_Two year", ('Yes','No'))
	 
	st.text("PaperlessBilling")
	pby = st.selectbox("PaperlessBilling", ('Yes','No'))
	 
	st.text('Payment')        
	pay=st.selectbox("Payment Option",["Credit Card","Electronics Check","Mailed Check"]) 

 





st.text('')
if st.button("Predict Churners"):
	iff=1 if iff=='Yes' else 0
	isn=1 if isn=='Yes' else 0
	osy=1 if osy=='Yes' else 0
	oby=1 if oby =='Yes' else 0
	dy=1 if dy=='Yes' else 0
	ty=1 if ty=='Yes' else 0
	sty=1 if sty=='Yes' else 0
	smy=1 if smy=='Yes' else 0
	c1=1 if c1=='Yes' else 0
	c2=1 if c2=='Yes' else 0
	pby=1 if pby=='Yes' else 0


	
	for i in ["Credit Card","Electronics Check","Mailed Check"]:
		if i=='Credit Card' or 'Electronics Check' or 'Mailed Check':
			pay=1
		else:
			pay=0


	input_data = np.array([[sc,tenure,mc,tc,iff,isn,1,osy,1,oby,1,dy,1,ty,1,sty,1,smy,c1,c2,pby,pay,1,1]])
	result = predict(input_data)
	st.write(result[0])
	
st.markdown("This code is develope by WBL Team : Viraj")
