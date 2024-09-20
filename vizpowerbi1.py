import streamlit as st
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

url3 = "https://bit.ly/SalarySurveyHRDBCT3"
url4 = "https://bit.ly/VisualizationEstimatedSalarySurvey"
url5 = "https://bit.ly/3WGmBUv"

st.markdown("""
This dashboard is inspired by the results of a salary survey, indicating that the data used is not real, but randomly generated. The reason for this is that the salary data available in the survey only includes the Q1, Median, and Q3 figures. I felt that this data would be insufficient for my practice, so I opted to use randomly generated salary data instead.
""")

st.markdown("""
The randomly generated data was created based on several considerations:
a) Assuming that the generated data follows a normal distribution.
b) Assuming that the sample median can be estimated as the same as the sample mean.
c) Since the parameters require the number of data points, the mean, and the standard deviation (SD), the SD value was obtained using the formula SD = (Interquartile Range / 1.35).
d) To prevent the salary values from being negative or too low, I decided to set a limit that the generated salary values should not be negative and should not deviate too far from the Q1 value.
e) Finally, I used RStudio to help generate this data, with some assistance from ChatGPT when errors occurred.

There is a new column replacing the Q1, Median, and Q3 values, called "estimated salary." Additionally, there is a new column to check whether the salary obtained is above or below the 2024 minimum wage (UMP) for each province.
""")
st.markdown("""
Here is a sample image from my visualization results.
            """)
st.image("Visualization Sample.jpeg")

video_file = open('demo.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.markdown("""
If you interested more, you can download the file that i provided below:
            """)
st.markdown("""Salary Survey HRDBACOT Document Result:         
            %s
            """ % url3)

st.markdown("""Visualization of Estimated Salary Survey with Power BI:
            %s
            """ % url4)

st.markdown("""Cleaned Dataset of Estimated Salary Survey:        
            %s
            """ % url5)
