# Required libraries for the program
import pymysql
import pandas as pd
import json
import streamlit as st
import requests
import psycopg2
import plotly.express as px
from PIL import Image
import emoji

 # Connection Parameters
connection = pymysql.connect(
         host = 'localhost', user = 'root',
         password = '12345', database = 'Phonepe')
print("connection = ", connection)
cursor = connection.cursor()
print("cursor = ", cursor)

#Creating a Home page

icon = Image.open('C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/LOGO.png') 
st.set_page_config(page_icon=icon,page_title="PhonePe Project",
        layout="wide",
        initial_sidebar_state="expanded")


page=st.sidebar.radio("Navigation",["Home","Business Case Study"])
if page=="Home":
        st.header(":blue[PhonePe Data Analysis📈]")
        st.title("PhonePe Pulse"); st.write(":blue[THE BEAT OF PROGRESS]")
        col1,col2,col3= st.columns((1,2,1))

        with col2:
         st.video("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/vid.mp4",autoplay=True,muted=True)
         st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        st.header(":blue[PhonePe Pulse]",divider='blue')
        st.header("Introduction")
        st.markdown(""" The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem.
                      """)
        st.header("Guide")
        st.write("This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.")
        st.markdown("   ")
        colp,col4,col5,col6=st.columns((1,2,2,1))
        with col4:
            st.image("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/1.jpg")
        with col5:
            st.header("Aggregated")
            st.write("Aggregated values of various payment categories" \
            "         as shown under Categories section")
        coli,col7,col8,col9=st.columns((1,2,2,1))
        with col7:
            st.image("Phonepay_project/3.jpg")
        with col8:
             st.header("Map")
             st.write("Total values at the State and District levels ")
        coll,col10,col11,col12=st.columns((1,2,2,1))
        with col10:
            st.image("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/2.jpg")
        with col11:
              st.header("Top")
              st.write("Totals of top States / Districts / Postal Codes")
elif page =="Business Case Study":
    st.header("Business Case Study")


    # Create a drop-down for 5 scenario based
    selected_option = st.selectbox("Select any Question", ['1. Decoding Transaction Dynamics on PhonePe', '2. Device Dominance and User Engagement Analysis',
                                                        '3. Insurance Penetration and Growth Potential Analysis','4.Transaction Analysis Across States and Districts',
                                                        '5.User Registration Analysis'])

    if selected_option == '1. Decoding Transaction Dynamics on PhonePe':
        st.write(" ")
        st.write(" ")
        st.subheader('Total Transaction Amount Analysis')
        col1, col2 = st.columns(2)
        with col1:
         year = st.selectbox("*Year*", options=list(range(2018, 2025)))
        with col2:
         Quarter = st.selectbox("Quarter", options=[1,2,3,4])
        col1,col2 = st.columns(2)
        # Overall State Data - Transactions Amount
        with col1:
            st.markdown("### :violet[Overall State Data - Transactions Amount]")
            url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
            response= requests.get(url)
            data1= json.loads(response.content)
            state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
            state_names_tra.sort()

                    
            year= int(year)
            cursor.execute(f"select States, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transaction where Years = {year} and Quarter = {Quarter} group by States order by States")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['States', 'Total_Transactions', 'Total_amount'])
            df1.Total_amount = df1.Total_amount.astype(int)
            df1.Total_Transactions = df1.Total_Transactions.astype(int)
                        
            fig = px.choropleth(df1,geojson=data1,
                            featureidkey='properties.ST_NM',
                            locations='States',
                            color='Total_amount',
                            color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
 # Overall State Data - Transactions count
        with col2:
            st.markdown("###  :violet[Overall State Data - Transactions Count]")
                    
            fig1 = px.choropleth(df1,geojson=data1,
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Total_Transactions',
                        color_continuous_scale='sunset')

            fig1.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig1,use_container_width=True)

       
    # PIE CHART - PAYMENT TYPE
        st.subheader('Payment Method Popularity')
        col3,col4=st.columns(2)     
        with col3:         
        
            year= int(year)       
            cursor.execute(f"select Transaction_type as Payment_Category, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_Transaction_Amount from aggregated_transaction where Years= {year} and Quarter = {Quarter} group by Transaction_type order by Transaction_type ")
            df = pd.DataFrame(cursor.fetchall(), columns=['Payment_Category','Total_Transactions','Total_Transaction_Amount'])
        
            fig2 = px.pie(
                df,
                names="Payment_Category",
                values="Total_Transactions",
                title="Distribution of Total Transaction Count",
                hole=0.4, # To create a donut chart
                labels={"Payment_Category": "Payment_Category"},
            ) 
            st.plotly_chart(fig2)
        
        with col4:         
            fig3 = px.pie(
                df,
                names="Payment_Category",
                values="Total_Transaction_Amount",
                title="Distribution of Total Transaction Amount",
                hole=0.4, # To create a donut chart
                labels={"Payment_Category": "Payment_Category"},
            )
            st.plotly_chart(fig3)

        #LINE CHART -TRANSACTION TYPE
        st.subheader('Transactions by State and Payment_Category')
        cursor.execute(f"select States,Transaction_type,sum(Transaction_count) as Total_Transaction_count, sum(Transaction_amount) as Total_Transaction_Amount from aggregated_transaction group by States,Transaction_type order by States,Total_Transaction_count DESC")
        df1 = pd.DataFrame(cursor.fetchall(), columns=['States','Transaction_type','Total_Transaction_count','Total_Transaction_Amount'])
        state_options=df1['States'].unique()
        selected_state=st.selectbox("Select state",state_options)
        ddf=df1[df1['States']==selected_state]
        
        fig = px.line(ddf,
                     title=f'Transaction Amount Distribution in {selected_state}',
                     x="Transaction_type",
                     y="Total_Transaction_Amount",markers=True
                    )
        st.plotly_chart(fig,use_container_width=True)

#BAR CHART -QUATER WISE TRANSACTION AMOUNT
        st.title("Trend Analysis")
        year = st.selectbox("*Year*", options=list(range(2018, 2025)),key=year)
        cursor.execute(f"select Years,Quarter, sum(Transaction_amount) as Total_Transaction_Amount from aggregated_transaction where Years= {year} group by Quarter order by Quarter ")
        df = pd.DataFrame(cursor.fetchall(), columns=['Years','Quarter','Total_Transaction_Amount'])
       
        fig5 = px.bar(
            df,
            x='Quarter',
            y='Total_Transaction_Amount',
            title=f'Transaction Amount Distribution in {year}',
            orientation='v'
        )
        fig5.update_traces(width=0.4)
        
     # Update the x-axis layout
        fig5.update_layout(xaxis = dict(
                tickmode = 'array',
                tickvals = [1,2,3,4]
            
))
        st.plotly_chart(fig5)

    if selected_option == '2. Device Dominance and User Engagement Analysis':

        col1, col2 = st.columns(2)
        with col1:
         year = st.selectbox("*Year*", options=list(range(2018, 2025)))
        with col2:
         Quarter = st.selectbox("Quarter", options=[1,2,3,4])
        
        # Overall State Data - User Analysis
        col1,col2=st.columns(2)
        with col1:
            st.markdown("## :violet[All State Data - Total users ]")
            url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
            response= requests.get(url)
            data1= json.loads(response.content)
            state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
            state_names_tra.sort()

            year= int(year)
            cursor.execute(f"select States, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {year} and Quarter = {Quarter} group by States order by States")
            df1 = pd.DataFrame(cursor.fetchall(), columns=['States', 'Total_Users','Total_Appopens'])
            df1.Total_Users = df1.Total_Users.astype(int)
            df1.Total_Appopens = df1.Total_Appopens.astype(int)
            
            
            figi = px.choropleth(df1,geojson=data1,
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Total_Users',
                        color_continuous_scale='sunset')

            figi.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(figi,use_container_width=True)
        with col2:
         col3,col4 = st.columns(2) 
         if (year==2019 and Quarter==1) or (year==2018):

          st.subheader(f":red[**No one used App in {year}- Quarter{Quarter} **]")
         else:
            st.markdown("## :violet[AllState Data - Total Appopens]")
            fige = px.choropleth(df1,geojson=data1,
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Total_Appopens',
                        color_continuous_scale='sunset')

            fige.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fige,use_container_width=True)

       
        # BAR CHART USERS - DISTRICT WISE DATA            
        
        st.subheader('Users Across Different Regions')
        
        cursor.execute(f"select States,Years,quarter,District,sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {year} and Quarter = {Quarter} group by States, District,Years,Quarter order by States,District")
            
        df = pd.DataFrame(cursor.fetchall(), columns=['States','Years', 'quarter', 'District', 'Total_Users','Total_Appopens'])
        df.Total_Appopens = df.Total_Appopens.astype(int)
        state_options=df['States'].unique()
        selected_state=st.selectbox("Select state",state_options)
        ddf=df[df['States']==selected_state]
        
        col1,col2=st.columns(2)
        with col1:   
          fig = px.bar(ddf,
                        title=f'Total Registered Users in {selected_state}',
                        x="District",
                        y="Total_Users",
                        orientation='v',
                        )
          st.plotly_chart(fig,use_container_width=True)
        with col2:
         
         col3,col4 = st.columns(2) 
         if (year==2019 and Quarter==1) or (year==2018):

          st.subheader(f":red[**No one used App in {year}- Quarter{Quarter} **]")
         else:
          fig12 = px.bar(ddf,
                        title=f'Total App open in {selected_state}',
                        x="District",
                        y="Total_Appopens",
                        )
          fig12.update_traces(width=0.4)
          st.plotly_chart(fig12,use_container_width=True)

#LINE CHART - BRAND WISE 
        st.subheader('Device Analysis')
        cursor.execute(f"select States,Brands,sum(Transaction_count) as Total_Transaction_count from aggregated_user group by States,Brands order by States,Total_Transaction_count DESC")
        df1 = pd.DataFrame(cursor.fetchall(), columns=['States','Brands','Total_Transaction_count'])
        state_options=df1['States'].unique()
        selected_state=st.selectbox("Select state",state_options,key='select state')
        ddf=df1[df1['States']==selected_state]
        
        fig11 = px.line(ddf,
                     title=f'Brands used in {selected_state}',
                     x="Brands",
                     y="Total_Transaction_count",markers=True
                    )
        st.plotly_chart(fig11,use_container_width=True)

#BAR CHART TOTAL APP OPENS-QUARTER WISE
        st.title("Trend Analysis")
        year = st.selectbox("*Year*", options=list(range(2018, 2025)),key=year)
        cursor.execute(f"select Years,Quarter, sum(Appopens) as Total_Appopens from map_user where Years= {year} group by Quarter order by Quarter ")
        df = pd.DataFrame(cursor.fetchall(), columns=['Years','Quarter','Total_Appopens'])
       
        fig22 = px.bar(
            df,
            x='Quarter',
            y='Total_Appopens',
            title=f'Total appopens in {year} Quarter wise Distribution',
            orientation='v'
        )
        fig22.update_traces(width=0.4)
        fig22.update_layout(xaxis = dict(
                tickmode = 'array',
                tickvals = [1,2,3,4],
            
))
        st.plotly_chart(fig22)
        
#SCENARIO 3
    if selected_option == '3. Insurance Penetration and Growth Potential Analysis':

        col1, col2 = st.columns(2)
        with col1:
         year = st.selectbox("*Year*", options=list(range(2020, 2025)),key='yearselect')
        with col2:
         Quarter = st.selectbox("Quarter", options=[1,2,3,4],key='Quarterselect')
        col3,col4 = st.columns(2) 
        if year==2020 and Quarter==1:
         st.subheader(f":green[No one took Insurance Policy in 2020 - Quarter 1 ]")
        else:
         with col3:
            st.markdown("## :violet[All State Data -  Insurance Count ]")
            url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
            response= requests.get(url)
            data1= json.loads(response.content)
            state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
            state_names_tra.sort()

            year= int(year)
            cursor.execute(f"select States, sum(Insurance_count) as Total_Insurance_count, sum(Insurance_amount) as Total_Insurance_Amount from aggregated_insurance where Years = {year} and Quarter = {Quarter} group by States order by States")
            df3 = pd.DataFrame(cursor.fetchall(), columns=['States', 'Total_Insurance_count','Total_Insurance_Amount'])
            df3.Total_Insurance_count = df3.Total_Insurance_count.astype(int)
            df3.Total_Insurance_Amount = df3.Total_Insurance_Amount.astype(int)
            
            
            figq = px.choropleth(df3,geojson=data1,
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Total_Insurance_count',
                        color_continuous_scale='sunset')

            figq.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(figq,use_container_width=True)

         with col4:
            st.markdown("## :violet[All State Data - Insurance Amount  ]")
            figw = px.choropleth(df3,geojson=data1,
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Total_Insurance_Amount',
                        color_continuous_scale='sunset')

            figw.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(figw,use_container_width=True)

    
        # BAR CHART POLICY - DISTRICT WISE DATA            
        
        st.subheader('Policy Taken Across Different Regions')
        cursor.execute(f"select States,Years,quarter,District,sum(Insurance_count) as Total_Insurance_count, sum(Insurance_amount) as Total_Insurance_Amount from map_insurance where Years = {year} and Quarter = {Quarter} group by States, District,Years,Quarter order by States,District")
        df4 = pd.DataFrame(cursor.fetchall(), columns=['States','Years', 'quarter', 'District', 'Total_Insurance_count','Total_Insurance_Amount'])
        state_options=df4['States'].unique()
        selected_state=st.selectbox("Select state",state_options,key='State')
        df5=df4[df4['States']==selected_state]
        col3,col4 = st.columns(2) 
        if year==2020 and Quarter==1:
         st.subheader(f":green[No one took Insurance Policy in 2020 - Quarter 1 ]")
        else:
         col1,col2=st.columns(2)
         with col1:   
            fig21 = px.bar(df5,
                        title=f'Total Insurance policy members in {selected_state}',
                        x="District",
                        y="Total_Insurance_count",
                        orientation='v',
                        )
            fig21.update_traces(width=0.4)
            st.plotly_chart(fig21,use_container_width=True)
         with col2:
            fig7= px.bar(df5,
                        title=f'Total Insurance Amount in {selected_state}',
                        x="District",
                        y="Total_Insurance_Amount",
                        )
            fig7.update_traces(width=0.4)
            st.plotly_chart(fig7,use_container_width=True)

#BAR CHART QUARTER WISE -TOTAL INSURANCE AMOUNT
        st.title("Trend Analysis")
        year = st.selectbox("*Year*", options=list(range(2020, 2025)),key=year)
        cursor.execute(f"select Years,quarter,sum(Insurance_amount) as Total_Insurance_Amount from map_insurance where Years = {year} group by Quarter order by Quarter")        
        df = pd.DataFrame(cursor.fetchall(), columns=['Years', 'Quarter','Total_Insurance_Amount'])
       
        fig8 = px.bar(
            df,
            x='Quarter',
            y='Total_Insurance_Amount',
            title=f'Total Insurance Amount in {year} Quarter wise Distribution',
            orientation='v'
        )
        fig8.update_traces(width=0.4)
        fig8.update_layout(xaxis = dict(tickmode = 'array',tickvals = [1,2,3,4],
            
))
        st.plotly_chart(fig8)
#SCENARIO 4      
    if selected_option == '4.Transaction Analysis Across States and Districts':
        
        col1,col2=st.columns(2)
        with col1:
         year = st.selectbox("*Year*", options=list(range(2018, 2025)),key="year_selector")
        with col2:
         Quarter = st.selectbox("Quarter", options=[1,2,3,4],key="quarter_selector")
        tab1,tab2,tab3 = st.tabs(["***Top States***","***Top Districts***","***Top Pincodes***" ])

        with tab1:
#BAR CHART-TOP 10 STATES
            year= int(year)
            cursor.execute(f"select States, sum(Transaction_count) as Transaction_Count, sum(Transaction_amount) as Total_Amount from aggregated_transaction where Years = {year} and Quarter = {Quarter} group by States order by Total_Amount desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Transaction_Count','Total_Amount'])
            df.Transaction_Count = df.Transaction_Count.astype(float)

            fig = px.bar(df,
                         title='Top 10 states',
                         x="States",
                         y="Total_Amount",
                         orientation='v',
                         color_discrete_sequence=px.colors.sequential.Agsunset
                         )
            
        
            st.plotly_chart(fig,use_container_width=True)
           
        with tab2:
#BAR CHART-TOP 10 DISTRICT        
            year= int(year)
            cursor.execute(f"select District , sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total_Amount from map_transaction where Years = {year} and Quarter = {Quarter} group by District order by Total_Amount desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transaction_count','Total_Amount'])
            df[["Transaction_count","Total_Amount"]]= df[["Transaction_count","Total_Amount"]].astype(int)
            fig = px.bar(df,
                         title='Top 10 District',
                         x="District",
                         y="Total_Amount",
                         orientation='v',
                         color_discrete_sequence=px.colors.sequential.Agsunset
                         )
            st.plotly_chart(fig,use_container_width=True)

        with tab3:
            
  #BAR CHART-TOP 10 PINCODES         
            year= int(year)
            
            cursor.execute(f"select Pincodes, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_transaction where Years = {year} and Quarter = {Quarter} group by Pincodes order by Total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincodes', 'Transaction_count','Total_Amount'])
            df[["Transaction_count","Total_Amount"]]= df[["Transaction_count","Total_Amount"]].astype(int)


            fig = px.pie(df,
                         values='Total_Amount',
                         names='Pincodes',
                         title='Top 10 Pincodes',
                         color_discrete_sequence=px.colors.sequential.Agsunset,
                         hover_data=['Total_Amount'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
#SCENARIO 5        
    if selected_option == '5.User Registration Analysis':
       
        col1,col2=st.columns(2)
        with col1:
         year = st.selectbox("*Year*", options=list(range(2018, 2025)),key="year_selector")
        with col2:
         Quarter = st.selectbox("Quarter", options=[1,2,3,4],key="quarter_selector")
        tab1,tab2,tab3,tab4 = st.tabs(["***Top Brands***","***Top States***","***Top Districts***","***Top Pincodes***"])
        
        with tab1:
#BAR CHART-TOP 10 BRANDS
            if year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                cursor.execute(f"select Brands, sum(Transaction_count) as Total_Users, avg(Percentage)*100 as Avg_Percentage from aggregated_user where Years = {year} and Quarter = {Quarter} group by Brands order by Total_Users desc limit 10")
                df = pd.DataFrame(cursor.fetchall(), columns=['BrandS', 'Total_Users','Avg_Percentage'])
                fig = px.bar(df,
                             title='Top 10 Brands',
                             x="BrandS",
                             y="Total_Users",
                             orientation='v',
                             color_discrete_sequence=px.colors.sequential.Agsunset
                             )
                st.plotly_chart(fig,use_container_width=True)   
    
        with tab2:
#BAR CHART-TOP 10 STATES
            cursor.execute(f"select States, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {year} and Quarter = {Quarter} group by States order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Total_Users','Total_Appopens'])
            fig = px.bar(df,
                         title='Top 10 States',
                         x="States",
                         y="Total_Users",
                         orientation='v',
                         color_discrete_sequence=px.colors.sequential.Agsunset
                         )

            st.plotly_chart(fig,use_container_width=True)            
           
#BAR CHART - TOP 10 DISTRICTS              
        with tab3:
            
            cursor.execute(f"select District, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {year} and Quarter = {Quarter} group by District order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                         title='Top 10 District',
                         x="District",
                         y="Total_Users",
                         orientation='v',
                         color_discrete_sequence=px.colors.sequential.Agsunset
                         )
            st.plotly_chart(fig,use_container_width=True)
           
            
        with tab4:
 #PIE CHART - TOP 10 PINCODES           
            cursor.execute(f"select Pincodes, sum(RegisteredUser) as Total_Users from top_user where Years = {year} and Quarter = {Quarter} group by Pincodes order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincodes', 'Total_Users'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.pie(df,
                         values='Total_Users',
                         names='Pincodes',
                         title='Top 10 Pincodes',
                         color_discrete_sequence=px.colors.sequential.Agsunset,
                         hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
