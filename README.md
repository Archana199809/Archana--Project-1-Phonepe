**PhonePe Transaction Insights**

**Introduction**

PhonePe has become one of the most popular digital payment platforms in India, with millions of users relying on it for their day-to-day transactions. The app is known for its simplicity, user-friendly interface, and fast and secure payment processing. It has also won several awards and accolades for its innovative features and contributions to the digital payments industry.

We create a web app to analyse the Phonepe transaction and users depending on various Years, Quarters, States, and Types of transaction and give a Geographical and Geo visualization output based on given requirements.

" Disclaimer:-This data between 2018 to 2023 in INDIA only "

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/402c296b-8029-4d83-8198-598fd6a44329" />


**1. Tools install**

1. visual studio code.
2. MySQL workbench 8.0 CE
   
**2.Import Libraries**

  **a) Database Interaction**
  - pymysql
  - psycopg2
  
  **b) Data Handling & Analysis**
  - pandas
  - json
  - tomllib
  
  **c) Web Development & APIs**
  - streamlit
  - requests
  
  **d) Visualization**
  - plotly.express
  - plotly.graph_objects
  
  **e) Image Processing**
  - PIL (Pillow library - from PIL import Image)
  
  **f) Miscellaneous/Utility**
  - emoji
    
**3. E T L Process**

**a) Extract data**

The extraction phase involves reading data from a specified directory structure.

**b) Process and Transform the data**

Process the data by using Python algorithms and transform the processed data into DataFrame format.

**c) Load data**

Finally, create a connection to the MySQL server and create a Database and stored the Transformed data in the MySQL server

**4. E D A Process and Frame work**

**a) Access MySQL DB**

Create a connection to the MySQL server and access the specified MySQL DataBase by using pymysql library

**b) Filter the data**

Filter and process the collected data depending on the given requirements by using SQL queries

**c) Visualization**

Finally, create a Dashboard by using Streamlit and applying selection and dropdown options on the Dashboard and show the output are Geo visualization, bar chart, and Dataframe Table

**User Guide**

The image displays a Streamlit application for "Total Transaction Amount Analysis". To use this Streamlit application, follow these steps: 

**Step 1:**

Access the Application: Open the Streamlit application in your web browser. This typically happens automatically when you run the Streamlit script, or you might navigate to a specific URL where it's deployed. 

**Step2:**

Select Year: Locate the "Year" dropdown menu, which is currently showing "2018" in the image. Click on this dropdown to select a different year if you wish to analyze data from a different period. 

**Step3:**

Select Quarter: Locate the "Quarter" input field, which is currently showing "1" in the image. You can change this value to select a specific quarter for your analysis within the chosen year. 

**Step4:**

View Analysis: After selecting the desired year and quarter, the application will automatically update the visualizations for "Overall State Data - Transactions Amount" and "Overall State Data - Transactions Count" based on your selections. 

**Step5:**

Interpret Visualizations: Examine the two map-based visualizations to understand the transaction amount and count data across different states, as depicted by the color intensity or other visual cues on the map of India.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/402c296b-8029-4d83-8198-598fd6a44329" />
