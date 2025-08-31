PhonePe Transaction Insights

Introduction
PhonePe has become one of the most popular digital payment platforms in India, with millions of users relying on it for their day-to-day transactions. The app is known for its simplicity, user-friendly interface, and fast and secure payment processing. It has also won several awards and accolades for its innovative features and contributions to the digital payments industry.

We create a web app to analyse the Phonepe transaction and users depending on various Years, Quarters, States, and Types of transaction and give a Geographical and Geo visualization output based on given requirements.

" Disclaimer:-This data between 2018 to 2023 in INDIA only "

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/402c296b-8029-4d83-8198-598fd6a44329" /># Archana--Project-1-Phonepe
eveloper Guide
1. Tools install
visual studio code.
MySQL workbench 8.0 CE
2.Import Libraries
Database Interaction
pymysql
psycopg2

Data Handling & Analysis
pandas
json
tomllib

Web Development & APIs
streamlit
requests

Visualization
plotly.express
plotly.graph_objects

Image Processing
PIL (Pillow library - from PIL import Image)

Miscellaneous/Utility
emoji
3. E T L Process
a) Extract data
The extraction phase involves reading data from a specified directory structure.
b) Process and Transform the data
Process the data by using Python algorithms and transform the processed data into DataFrame format.
c) Load data
Finally, create a connection to the MySQL server and create a Database and stored the Transformed data in the MySQL server
4. E D A Process and Frame work
a) Access MySQL DB
Create a connection to the MySQL server and access the specified MySQL DataBase by using pymysql library
b) Filter the data
Filter and process the collected data depending on the given requirements by using SQL queries
c) Visualization
Finally, create a Dashboard by using Streamlit and applying selection and dropdown options on the Dashboard and show the output are Geo visualization, bar chart, and Dataframe Table
User Guide
Step 1.
Select any one option fron All India or State wise or Top Ten categories.
Step 2.
Select any one option fron Transaction or User.
Step 3.
Select any Year, Quarter and additional required option.
Step 4.
Finally, You get the Geo Visualization Analysis or Bar chart Analysis and Table format Analysis.3
