import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard - Data Analysis Final Project")
st.markdown('<div style="text-align: justify;">Welcome to Awan ML-15\'s Analysis Dashboard! Go to the sidebar to navigate to a specific section.</div>', unsafe_allow_html=True)

import streamlit as st

airdata_Gucheng_df=pd.read_csv('./main_data.csv')

# Function to navigate to a specific section

def task_objective():
    st.markdown(
        """
    ## Kriteria 1: Menggunakan Salah Satu dari Dataset yang Telah Disediakan
    Pada proyek ini, Anda harus melakukan proses analisis menggunakan salah satu dari beberapa dataset berikut.

    - Bike Sharing Dataset 
    - E-Commerce Public Dataset 
    - Air Quality Dataset 

    ## Kriteria 2: Melakukan Seluruh Proses Analisis Data
    Mirip seperti berbagai materi latihan yang telah dibahas sebelumnya, Anda harus melakukan seluruh proses analisis data mulai dari mendefinisikan pertanyaan hingga membuat kesimpulan dari hasil analisis. Selain itu, proyek analisis data yang Anda buat harus memenuhi ketentuan berikut.

    - Minimal terdapat 2 buah pertanyaan bisnis (pertanyaan analisis) yang ingin dijawab melalui proses analisis data. Pertanyaan tersebut haruslah efektif sesuai dengan materi Mendefinisikan Pertanyaan Untuk Explorasi Data.
    - Minimal terdapat 2 buah visualisasi data untuk menjawab pertanyaan bisnis yang telah dibuat.

    ## Kriteria 3: Proses Analisis Dibuat dalam Notebook yang Rapi
    Pada submission ini, Anda harus mengerjakan proyek analisis data menggunakan templat proyek yang telah disediakan. Tujuannya supaya proyek yang dibuat terdokumentasi dengan rapi. Templat yang dimaksud dapat diakses pada tautan berikut: [templat notebook](#).

    ## Kriteria 4: Membuat Dashboard Sederhana Menggunakan Streamlit
    Setelah melakukan proses analisis, selanjutnya Anda wajib membuat dashboard sebagai media untuk menyampaikan hasil analisis data secara interaktif. Pada proyek ini, Anda dapat membuat dashboard dengan Streamlit mirip seperti materi latihan sebelumnya. Selain itu, pastikan bahwa dashboard Anda buat dapat berjalan dengan lancar di local.

"""
    )

def question_1():

    correlation_matrix = airdata_Gucheng_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3','TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()

    def figure_1():
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])

        # Resample data to monthly averages for PM2.5 and PM10
        data_time_series_PM2_5 = airdata_Gucheng_df[['date', 'PM2.5']].set_index('date').resample('M').mean()
        data_time_series_PM10 = airdata_Gucheng_df[['date', 'PM10']].set_index('date').resample('M').mean()

        # Create the plots
        fig, ax = plt.subplots(figsize=(15, 6))

        # Plot PM2.5 data
        ax.plot(data_time_series_PM2_5.index, data_time_series_PM2_5['PM2.5'], label='PM2.5', color='blue')

        # Plot PM10 data
        ax.plot(data_time_series_PM10.index, data_time_series_PM10['PM10'], label='PM10', color='green')

        # Set plot titles and labels
        plt.title('Monthly Average Concentrations of PM2.5 and PM10')
        plt.xlabel('Date')
        plt.ylabel('Concentration')
        plt.legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

    import streamlit as st

    st.subheader("**Question 1**")
    st.markdown('<div style="text-align: justify;">Considering the health risks outlined by cdc.gov, where PM2.5 poses threats to human lungs and blood, while PM10 affects the eyes, nose, and throat, how do the levels of PM2.5 and PM10 fluctuate throughout the year in Gucheng, China?</div>', unsafe_allow_html=True)
    st.subheader("**Answer**")
    st.markdown(
    '''
    <div style="text-align: justify;">Firstly, I'll utilize the correlation matrix to discern the relationships between PM2.5 and PM10 levels with other variables in the dataset. This will help uncover any significant associations or dependencies between air pollution levels and other factors.</div>
    ''',
    unsafe_allow_html=True
    )

    st.write("**Correlation Matrix:**")
    st.write(correlation_matrix)
    st.markdown(
    '''
    <div style="text-align: justify;">Following this, I proceed to visualize the PM2.5 and PM10 levels throughout the year to identify any discernible trends or patterns in air pollution levels over time. This visualization will offer insights into the temporal variability of air pollution and help uncover any seasonal or long-term trends.</div>
    ''',
    unsafe_allow_html=True
    )

    st.write("**Monthly Average Concentrations of PM2.5 and PM10:**")
    figure_1()

    st.markdown(
    '''
    <div style="text-align: justify;">Based on the data depicted in the chart, a robust correlation is evident between PM2.5 and PM10 levels, indicating a closely intertwined relationship between these two pollutants. This correlation suggests that as PM2.5 levels increase, so do PM10 levels, and conversely, a decrease in PM2.5 levels corresponds with a decrease in PM10 levels.</div>
    ''',
    unsafe_allow_html=True
    )

    st.markdown(
    '''
    <div style="text-align: justify;">The visual representation reveals a consistent pattern in which both PM2.5 and PM10 levels exhibit notable increases towards the end and beginning of each year. However, it's worth noting that in the year 2015, the rise in PM2.5 and PM10 levels is not as pronounced compared to other years. This deviation from the overall trend underscores the potential influence of specific environmental or meteorological factors unique to that particular year. Further investigation into the underlying reasons behind this anomaly could provide valuable insights into the dynamics of air pollution fluctuations over time.</div>
    ''',
    unsafe_allow_html=True
    )

def question_2():

    correlation_matrix = airdata_Gucheng_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3','TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()

    def figure_1():
        # Assuming airdata_Gucheng_df is your DataFrame containing the relevant data

        # Convert date columns to datetime
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])

        # Resample data to monthly averages
        data_time_series = airdata_Gucheng_df[['date', 'PM10', 'PM2.5', 'SO2', 'NO2', 'CO', 'O3']].set_index('date').resample('M').mean()

        # Create a figure and axes object
        fig, ax = plt.subplots(figsize=(15, 6))

        # Plot the data on the axes
        ax.plot(data_time_series.index, data_time_series['PM10'], label='PM10', color='black')
        ax.plot(data_time_series.index, data_time_series['PM2.5'], label='PM2.5', color='blue')
        ax.plot(data_time_series.index, data_time_series['SO2'], label='SO2', color='orange')
        ax.plot(data_time_series.index, data_time_series['NO2'], label='NO2', color='green')
        ax.plot(data_time_series.index, data_time_series['CO'], label='CO', color='red')
        ax.plot(data_time_series.index, data_time_series['O3'], label='O3', color='purple')

        # Set plot titles and labels
        ax.set_title('Monthly Average Concentrations of Air Pollutants')
        ax.set_xlabel('Date')
        ax.set_ylabel('Concentration')
        ax.legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

    def figure_2():

        # Convert date columns to datetime
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
        fig.suptitle('Monthly Average Concentrations of Air Pollutants', fontsize=15)

        # PM2.5 and PM10
        data_time_series_PM10 = airdata_Gucheng_df[['date', 'PM10']].set_index('date').resample('M').mean()
        data_time_series_PM2_5 = airdata_Gucheng_df[['date', 'PM2.5']].set_index('date').resample('M').mean()
        date_time_series_SO2 = airdata_Gucheng_df[['date', 'SO2']].set_index('date').resample('M').mean()
        datetime_series_NO2 = airdata_Gucheng_df[['date', 'NO2']].set_index('date').resample('M').mean()

        axes[0].plot(data_time_series_PM10.index, data_time_series_PM10['PM10'], label='PM10', color='black')
        axes[0].plot(data_time_series_PM2_5.index, data_time_series_PM2_5['PM2.5'], label='PM2.5', color='blue')
        axes[0].plot(date_time_series_SO2.index, date_time_series_SO2['SO2'], label='SO2', color='orange')
        axes[0].plot(datetime_series_NO2.index, datetime_series_NO2['NO2'], label='NO2', color='green')
        axes[0].set_title('PM2.5, PM10, SO2, NO2 ')
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Concentration')
        axes[0].legend()

        # CO
        data_time_series_CO = airdata_Gucheng_df[['date', 'CO']].set_index('date').resample('M').mean()

        axes[1].plot(data_time_series_CO.index, data_time_series_CO['CO'], label='CO', color='red')
        axes[1].set_title('CO')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Concentration')
        axes[1].legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

    def figure_3():
        # Convert date columns to datetime
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])
        data_time_series = airdata_Gucheng_df[['date', 'PM10', 'PM2.5', 'SO2', 'NO2', 'CO', 'O3']].set_index('date').resample('M').mean()

        # Create a figure
        fig, ax = plt.subplots(figsize=(15, 6))

        # Plot the data
        ax.plot(data_time_series.index, data_time_series['PM10'], label='PM10', color='black')
        ax.plot(data_time_series.index, data_time_series['PM2.5'], label='PM2.5', color='blue')
        ax.plot(data_time_series.index, data_time_series['SO2'], label='SO2', color='orange')
        ax.plot(data_time_series.index, data_time_series['NO2'], label='NO2', color='green')
        # ax.plot(data_time_series.index, data_time_series['CO'], label='CO', color='red')
        ax.plot(data_time_series.index, data_time_series['O3'], label='O3', color='purple')

        # Set plot titles and labels
        ax.set_title('Monthly Average Concentrations of Air Pollutants')
        ax.set_xlabel('Date')
        ax.set_ylabel('Concentration')
        ax.legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

    def figure_4():
        # Convert the index to a DatetimeIndex
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])
        airdata_Gucheng_df.set_index('date', inplace=True)

        # Slice the DataFrame for the years 2014 to 2015 and select columns PM2.5 and O3
        filtered_data = airdata_Gucheng_df["2013":"2015"][['PM2.5','O3']]

        # Create the plot
        fig, ax = plt.subplots(figsize=(15, 8))
        filtered_data.plot(ax=ax, linewidth=3, fontsize=15)

        # Set plot titles and labels
        plt.title('PM2.5 and O3 levels throughout the year', fontsize=15)
        plt.xlabel('Year', fontsize=15)
        plt.ylabel('Concentration', fontsize=15)

        # Display the plot in Streamlit
        st.pyplot(fig)

    def figure_5():
        
        # Convert date columns to datetime
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])

        # Slice the DataFrame for the years 2013 to 2015 and select columns PM10 and O3
        filtered_data = airdata_Gucheng_df["2013":"2015"][['PM10','O3']]

        # Create the plot
        fig, ax = plt.subplots(figsize=(15, 8))
        filtered_data.plot(ax=ax, linewidth=3, fontsize=15)

        # Set plot titles and labels
        plt.title('PM10 and O3 levels throughout the year', fontsize=15)
        plt.xlabel('Year', fontsize=15)
        plt.ylabel('Concentration', fontsize=15)

        # Display the plot in Streamlit
        st.pyplot(fig)

    st.subheader("**Question 2**")
    st.markdown('<div style="text-align: justify;">What correlations occur between PM2.5 and PM10 with SO3, NO2, CO, and O3 in Gucheng, China?</div>', unsafe_allow_html=True)
    st.subheader("**Answer**")
    st.markdown(
        '''
        <div style="text-align: justify;">As usual, we can begin by examining the correlation matrix to identify any correlations between PM2.5 and PM10 levels and other variables. Following this, we can visualize the data to enhance our understanding of the observed trends.</div>    
    ''', unsafe_allow_html=True)

    st.write("**Correlation Matrix:**")
    st.write(correlation_matrix)

    st.markdown(
        '''
        <div style="text-align: justify;">By correlating the data and visualizing it, we can gain a deeper insight into the relationship between PM2.5 and PM10 levels and their variations throughout the year, helping us better understand the underlying patterns and potential factors influencing air pollution levels.</div>    
    ''', unsafe_allow_html=True)

    st.write("**Monthly Average Concentrations of Air Pollutants:**")
    figure_1()

    st.markdown(
        '''
        <div style="text-align: justify;">To improve the visualization and facilitate easier comparison, we can split the CO data from the other variables. This will allow us to examine the relationships between PM2.5 and PM10 levels and other variables separately, making it easier to identify patterns and correlations. By separating the CO data, we can create side-by-side visualizations that provide a clearer understanding of the relationships between air pollutants and other factors.</div>
    ''', unsafe_allow_html=True)
    figure_2()

    st.markdown(
        '''
        <div style="text-align: justify;">While the correlation matrix doesn't show a significant correlation with O3, it's worth noting that the chart depicts a consistent trend among CO, PM2.5, and PM10 levels. Additionally, NO2 and SO2 exhibit a somewhat parallel pattern in the visualization. This observation sheds light on why CO demonstrates a strong correlation with both PM2.5 and PM10. By visually comparing these variables, we can better understand their interrelationships and the potential factors driving air pollution levels.</div>
    ''', unsafe_allow_html=True)

    st.markdown(
        '''
        <div style="text-align: justify;">This is how it looks if O3 is included in the comparison. The correlation matrix doesn't indicate a significant correlation with O3, hence it's not included in the comparison. However, the chart illustrates a consistent trend among CO, PM2.5, and PM10, with NO2 and SO2 displaying a somewhat parallel pattern. This observation helps clarify why CO demonstrates a strong correlation with both PM2.5 and PM10.</div>
    ''', unsafe_allow_html=True)

    st.write("**Monthly Average Concentrations of Air Pollutants:**")
    figure_3()

    st.markdown(
        '''
        <div style="text-align: justify;">While the correlation matrix might not indicate a significant correlation between PM2.5 and PM10 with O3, it's essential to analyze their relationships in more detail. We can create visualizations specifically focusing on the variations of PM2.5 and PM10 levels alongside O3 levels over time. This detailed comparison will allow us to uncover any potential patterns or correlations that might not be evident from the correlation matrix alone. By exploring these relationships, we can gain a better understanding of how different pollutants interact and contribute to air quality dynamics.</div>
    ''', unsafe_allow_html=True)

    st.write("**PM2.5 and O3 levels throughout the year:**")
    figure_4()

    st.markdown(
        '''
        <div style="text-align: justify;">The chart illustrates that PM2.5 levels are predominantly high during winter months, whereas O3 levels peak during summer months. This seasonal variation in occurrence explains why O3 doesn't exhibit a significant correlation with PM2.5. The contrasting patterns between PM2.5 and O3 underscore their distinct sources and behaviors, with PM2.5 being more influenced by wintertime emissions and O3 by summertime photochemical reactions. This detailed observation helps elucidate the lack of a strong correlation between PM2.5 and O3 in the dataset.</div>
    ''', unsafe_allow_html=True)

    st.write("**PM10 and O3 levels throughout the year:**")
    figure_5()

    st.markdown(
        '''
        <div style="text-align: justify;">Indeed, PM10 exhibits a similar seasonal pattern to PM2.5, with both pollutants showing higher levels during winter months. As for O3, its occurrence peaks mainly during summer. This discrepancy in seasonal trends explains why O3 doesn't demonstrate a significant correlation with PM10. The contrasting patterns between PM10 and O3, driven by different sources and atmospheric conditions, contribute to the lack of a strong correlation between these pollutants in the dataset.</div>
    ''', unsafe_allow_html=True)

def question_3():
    correlation_matrix = airdata_Gucheng_df[['PM2.5','TEMP', 'PRES']].corr()
    
    def figure_1():
        # Convert date columns to datetime
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])

        # Resample data to monthly averages
        data_time_series = airdata_Gucheng_df[['date', 'PM2.5', 'TEMP', 'PRES']].set_index('date').resample('M').mean()

        # Create the subplots
        fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))
        fig.suptitle('Monthly Average Concentrations', fontsize=15)

        # Plot PM2.5 data
        axes[0].plot(data_time_series.index, data_time_series['PM2.5'], label='PM2.5', color='blue')
        axes[0].set_title('PM2.5')
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Concentration')
        axes[0].legend()

        # Plot Temperature data
        axes[1].plot(data_time_series.index, data_time_series['TEMP'], label='Temperature', color='orange')
        axes[1].set_title('Temperature')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Temperature')
        axes[1].legend()

        # Plot Pressure data
        axes[2].plot(data_time_series.index, data_time_series['PRES'], label='Pressure', color='green')
        axes[2].set_title('Pressure')
        axes[2].set_xlabel('Date')
        axes[2].set_ylabel('Pressure')
        axes[2].legend()

        # Adjust layout
        plt.tight_layout()

        # Display the plot in Streamlit
        st.pyplot(fig)
    
    def figure_2():
       
        # Convert the date columns to datetime
        airdata_Gucheng_df['date'] = pd.to_datetime(airdata_Gucheng_df[['year', 'month', 'day', 'hour']])

        # Set the date column as the index
        airdata_Gucheng_df.set_index('date', inplace=True)

        # Slice the DataFrame for the years 2013 to 2017 and select the required columns
        filtered_data = airdata_Gucheng_df["2013":"2017"][["month","PM2.5","TEMP","PRES","DEWP"]]

        # Group by month and aggregate
        grouped_data = filtered_data.groupby('month').agg({'PM2.5':['min','max'], 'TEMP':['min','max'],'PRES':['min','max']})

        # Display the grouped data in a Streamlit table
        st.write(grouped_data)

    import streamlit as st

    st.subheader("**Question 3**")
    st.markdown('<div style="text-align: justify;">What correlations exist between the levels of PM2.5 the variables of TEMP and PRES in Gucheng, China?</div>', unsafe_allow_html=True)
    st.subheader("**Answer**")
    st.markdown(
    '<div style="text-align: justify;">Certainly, let\'s proceed with analyzing the correlation between PM2.5 levels and temperature (TEMP) as well as atmospheric pressure (PRES) using a correlation matrix. Following this, visualization of the data is needed to gain a deeper understanding of the observed trends and relationships between PM2.5 levels and these atmospheric variables. This approach will help elucidate any potential correlations and provide insights into the impact of temperature and pressure on PM2.5 levels.</div>',
    unsafe_allow_html=True
    )

    st.write("**Correlation Matrix:**")
    st.write(correlation_matrix)
    st.write("**Monthly Average Concentrations of Air Pollutants**")
    figure_1()

    st.markdown(
    '<div style="text-align: justify;">From the charts provided, it appears that temperature exhibits an inverse correlation with both PM2.5 levels and atmospheric pressure. To delve deeper into this relationship, let\'s group the data by month and analyze the concentration of PM2.5 levels, temperature, and pressure for each month individually. This detailed analysis will allow us to better understand the variations in air pollutant levels in relation to temperature and pressure fluctuations throughout the year.</div>',
    unsafe_allow_html=True
    )

    st.write("**Grouped Data by Month**")
    figure_2()

    st.markdown(
    '<div style="text-align: justify;">Based on the information gleaned from the charts and tables, it\'s clear that there exists a negative correlation between temperature and pressure. This relationship indicates that as temperature rises, pressure tends to decrease, and conversely, as temperature falls, pressure tends to increase. Conversely, a positive correlation is evident between PM2.5 levels and pressure, as depicted in the chart. This implies that higher pressure conditions correspond to elevated PM2.5 levels. These observations offer valuable insights into the intricate interactions between atmospheric variables and air pollutant levels, underscoring the multifaceted dynamics that shape air quality.</div>',
    unsafe_allow_html=True
    )

def conclusion():
    st.subheader("**Conclusion**")
    st.markdown(
    '''
    - Conclusion for 1st Question

   1. **Correlation between PM2.5 and PM10 levels**: The data shows a robust correlation between PM2.5 and PM10 levels, indicating a closely intertwined relationship between these two pollutants. As PM2.5 levels increase, so do PM10 levels, and conversely, a decrease in PM2.5 levels corresponds with a decrease in PM10 levels.

   2. **Consistent seasonal pattern**: The visual representation of the data reveals a consistent pattern where both PM2.5 and PM10 levels exhibit notable increases towards the end and beginning of each year. This suggests the presence of seasonal influences or environmental factors that lead to fluctuations in air pollution levels over time.

   3. **Deviation in 2015**: However, in the year 2015, the rise in PM2.5 and PM10 levels is not as pronounced compared to other years. This deviation from the overall trend indicates the potential influence of specific environmental or meteorological factors unique to that particular year. Further investigation into the underlying reasons behind this anomaly could provide valuable insights into the dynamics of air pollution fluctuations over time.

   In conclusion, the data analysis highlights the correlation between PM2.5 and PM10 levels, the consistent seasonal pattern in air pollution levels, and the anomaly observed in 2015. These insights underscore the complexity of air pollution dynamics and the importance of continuous monitoring and analysis to understand and address environmental challenges effectively.


- Conclusion for 2nd Question

   1. **Correlation among pollutants**:
      - The correlation matrix doesn't show a significant correlation with O3.
      - CO exhibits a strong correlation with both PM2.5 and PM10, reflecting their interrelationships.
      - NO2 and SO2 display a somewhat parallel pattern, contributing to the correlation with CO, PM2.5, and PM10.

   2. **Seasonal variation**:
      - PM2.5 levels are consistently high during winter months, whereas O3 levels peak during summer months.
      - PM10 also shows higher levels during winter, while O3 peaks mainly in summer.
      - The contrasting seasonal patterns between PM2.5 and O3, as well as PM10 and O3, highlight distinct sources and behaviors driven by wintertime emissions and summertime photochemical reactions.

   3. **Lack of strong correlation with O3**:
      - The contrasting seasonal patterns between PM2.5 and O3, and PM10 and O3, contribute to the lack of a significant correlation between these pollutants.
      - This discrepancy emphasizes the importance of considering seasonal variations and distinct sources when analyzing correlations among air pollutants.

   In summary, the analysis elucidates the complex interrelationships and seasonal variations among air pollutants, highlighting the distinct behaviors of PM2.5, PM10, and O3. These insights underscore the need for comprehensive analyses that consider both correlation matrices and visual representations to better understand air pollution dynamics and their driving factors.

- Conclusion for 3rd Question

   1. **Inverse correlation between temperature and PM2.5 levels/atmospheric pressure**:
      - The charts suggest an inverse correlation between temperature and both PM2.5 levels and atmospheric pressure. As temperature increases, PM2.5 levels and atmospheric pressure tend to decrease, and vice versa.

   2. **Analysis by month**:
      - Further analysis is proposed by grouping the data by month to understand the variations in PM2.5 levels, temperature, and pressure on a monthly basis. This approach allows for a more detailed examination of how these variables fluctuate throughout the year.

   3. **Negative correlation between temperature and pressure**:
      - A negative correlation between temperature and pressure. As temperature rises, pressure tends to decrease, and as temperature falls, pressure tends to increase. This relationship is important for understanding atmospheric dynamics.

   4. **Positive correlation between PM2.5 levels and pressure**:
      - In contrast to the inverse correlation with temperature, there is a positive correlation between PM2.5 levels and pressure. Higher pressure conditions correspond to elevated PM2.5 levels. This suggests that atmospheric pressure may influence the concentration of PM2.5 pollutants.

   5. **Insights into atmospheric interactions and air quality dynamics**:
      - These observations provide valuable insights into the complex interactions between atmospheric variables and air pollutant levels. Understanding these relationships is crucial for comprehensively assessing air quality and identifying potential factors contributing to pollution levels.

   In conclusion, the text highlights the inverse correlation between temperature and both PM2.5 levels and atmospheric pressure, as well as the negative correlation between temperature and pressure. Additionally, a positive correlation is noted between PM2.5 levels and pressure. These findings underscore the importance of considering multiple environmental factors when analyzing air quality dynamics.
   
    '''
    )

def navigate_to_section(section):
    # Assuming you have defined different sections in your Streamlit app
    # You can replace these placeholders with your actual sections
    if section == "Task Objective":
        task_objective()

    elif section == "Section 1":
        question_1()

    elif section == "Section 2":
        question_2()

    elif section == "Section 3":
        question_3()

    elif section == "Conclusion":
        conclusion()


# Streamlit sidebar
st.sidebar.title("Go to Question Section")

with st.sidebar:

    st.image("https://ugc.production.linktr.ee/wnxqrf8vR4StpIow7wvi_Logo%20Dicoding%20(1).png?io=true&size=thumbnail-stack-v1_0", width=180)

# Button to navigate to Section 1
if st.sidebar.button("Task Objective"):
    navigate_to_section("Task Objective")

if st.sidebar.button("Question #1"):
    navigate_to_section("Section 1")

    # Button to navigate to Section 2
if st.sidebar.button("Question #2"):
    navigate_to_section("Section 2")

    # Button to navigate to Section 3
if st.sidebar.button("Question #3"):
    navigate_to_section("Section 3")

if st.sidebar.button("Conclusion"):
    navigate_to_section("Conclusion")


