
# imports we will use
from unittest import case
from xml.etree.ElementTree import tostring
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
# print('Loading dataset')
df = pd.read_excel('./2020-graduation_rates_public_citywide.xlsx',dtype={'% Grads': str},header=0,sheet_name='Ethnicity')
df.drop(df.index[df['% Grads'] == 's'], inplace = True)
df.drop(df.index[df['% Grads'] == '0.0' ], inplace = True)

df['% Grads'] = df['% Grads'].astype(float)

# print('A sample of 10:')
x=df.sample(10)
# print(df.sample(10))
# print(df.dtypes)
# print('Visualization')

selection = alt.selection_multi(fields=['Category'], bind='legend')

line1 = alt.Chart(df).mark_line().encode(
    x='Cohort Year:Q',
    y=alt.Y("average(% Grads):Q",scale=alt.Scale(domain=(0, 100))),
    color="Category:N",
    tooltip=['Cohort Year','average(% Grads)','Category'],
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
).add_selection(
    selection
)

line2 = alt.Chart(df).mark_line().encode(
    x='Cohort Year:Q',
    y=alt.Y("average(% Dropout):Q",scale=alt.Scale(domain=(0, 40))),
    color="Category:N",
    tooltip=['Cohort Year','average(% Dropout)','Category'],
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
).add_selection(
    selection
)


df2 = pd.DataFrame(np.array([[2007, 3, 'The Parents Involved case draws attention,  the Supreme Court published a ruling in it, and Chief Justice John Roberts Jr. wrote about stopping racial discrimination.'],
                             [2009, 2,'Two studies about the influence of racial segregation in schools are published in TAJE and TJPAM'],
                             [2014, 4,'The Civil Rights Project at UCLA released a report showing the segregation in NYC public schools. \n Councilmen moved to force the administration to address segregation. The Department of Education starts a “Diversity in Admissions” program, principals responded.'],
                             [2015, 3,'De Blasio signed the School Diversity Accountability Act into law. A study from UCB stresses long-term issues caused by segregation.']]),
                   columns=['Cohort Year', 'Number of relevant public news mentioned','Content'])

event_bar = alt.Chart(df2).mark_bar().encode(
    x=alt.X("Cohort Year:Q",scale=alt.Scale(domain=(2000, 2016))),
    y=alt.Y('Number of relevant public news mentioned:Q', scale=alt.Scale(scheme='blues')),
    tooltip= ['Cohort Year', 'Content'],
    opacity = alt.value(0.3)
).add_selection(alt.selection_multi())

vis1 =(event_bar+line1 ).resolve_scale(y='independent')|(event_bar+line2).resolve_scale(y='independent')

df3 = pd.read_excel('./2020-graduation_rates_public_citywide.xlsx',dtype={'% Grads': np.str},header=0,sheet_name='Poverty')
df3.drop(df3.index[df3['% Grads'] == 's'], inplace = True)
df3.drop(df3.index[df3['% Grads'] == '0.0' ], inplace = True)

df3['% Grads'] = df3['% Grads'].astype(float)


eco_line1 = alt.Chart(df3).mark_line().encode(
    x='Cohort Year:Q',
    y=alt.Y("average(% Grads):Q"),
    color="Category:N",
    tooltip=['Cohort Year','average(% Grads)','Category'],
)

eco_line2 = alt.Chart(df3).mark_line().encode(
    x='Cohort Year:Q',
    y=alt.Y("average(% Dropout):Q"),
    color="Category:N",
    tooltip=['Cohort Year','average(% Dropout)','Category'],
)


vis2 = (eco_line1+ event_bar).resolve_scale(y='independent') |(eco_line2+ event_bar).resolve_scale(y='independent')



st.sidebar.markdown("Select a visualization to display")
option = st.sidebar.selectbox("Graduation and dropout rates 2003-2016",['By ethnicity','By economical status','Blog Post'])
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

blog_post = read_markdown_file("readme.md")
if option == 'By economical status':
    st.title("Visualizations by Eugenia Yang")
    st.write(vis2)
elif option == 'By ethnicity':
    st.title("Visualizations by Eugenia Yang")
    st.write(vis1)
else :
    st.markdown(blog_post)
    st.write(vis1,vis2)