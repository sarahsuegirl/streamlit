import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler


my_model=joblib.load("final_model.p")
ss=StandardScaler()

#st.write("hello,Sarah")
ex=st.radio(" The experience level",['SE','EN','EX','MI'])
et=st.selectbox("Employment Type",['Full Time','PT','CT','FL'])
#jt=st.selectbox("Job Title",['','','',''])
er=st.selectbox('Employment Residence',['US','GB','IN','CA','DE','FR','ES','GR','JP','PT','BR','PK','NL','PL','IT','RU','AE','AT','VN','TR','AU','RO','BE','sG','SI','DK','HU','NG','MX','BO','MY','TN','IE','DZ','AR','CZ','JE','LU','PR','RS','EE','CL','HK','KE','MD','CO','IR','CN','MT','UA','IQ','HN','BG','HR','PH','NZ','CH'])
st.
#jt='Data Scientist'
#er='DE'
#cl='US'
#cs='L'

#result=ss.inverse_transform(my_model.predict(ss.fit_transform([[ex,et,jt,er,cl,cs]])).reshape(-1,1).T)
st.button('Predict')
