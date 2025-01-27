

# 🌍 Air Quality Prediction System  

This project focuses on **predicting air quality** in urban and industrial settings, emphasising the harmful effects of pollution from various sources like fuel combustion, power generation, and transportation. It employs machine learning algorithms to forecast air quality indices based on key pollutants such as particulate matter (PM2.5), ammonia, NOx, carbon monoxide, and sulfur dioxide. The goal is to assess the air quality to enhance public health and well-being, especially in smart cities.

---

## 🚀 **Overview of the Project**

With increasing pollution levels in cities, it's crucial to predict and monitor air quality to safeguard the health of residents. The **Air Quality Index (AQI)** is a key metric used to measure pollution levels and their impact on human health. This project uses **machine learning algorithms**, specifically **Random Forest** and **Decision Tree Regression**, to predict air quality based on multiple factors such as particulate matter, ammonia, NOx, ozone, carbon monoxide, sulfur dioxide, nitrogen dioxide, Benzene, and Toluene. 

### **Key Highlights**  
- **Machine Learning Models**: Random Forest and Decision Tree Regression used to forecast AQI.  
- **Performance Comparison**: Model evaluation using **RMSE**, **MAE**, **MSE**, and **R2 score** to determine which algorithm delivers better accuracy.  
- **Web Application**: A web page is built using **Flask** to check the air quality directly through the user interface.  

---

## 🧑‍💻 **Methodology**  

The methodology followed in this project is:

1. **Data Preprocessing**: Collect and clean the dataset containing pollution levels of various gases and AQI values.  
2. **Model Training**: Train machine learning models (Random Forest and Decision Tree Regression) on the preprocessed dataset.  
3. **Evaluation**: Compare the models using metrics like RMSE, MAE, and R2 score.  
4. **Web Deployment**: Use **Flask** to create a web interface for users to check air quality online.  

![Methodology Flow](https://github.com/user-attachments/assets/cf15111b-8758-46ba-ae1f-2aa5314e6616)

---

## 📊 **Results**

### **Model Comparison**  

- **Random Forest**: 
   - Lower RMSE, MAE, and MSE than the Decision Tree model.  
   - Higher **R2 scores**, indicating better prediction accuracy.
- **Decision Tree**: 
   - Higher RMSE, MAE, and MSE than Random Forest.  
   - Lower R2 scores.

The **Random Forest algorithm** outperforms the **Decision Tree algorithm** in predicting air quality with better accuracy and lower error metrics.

![Model Comparison Results](https://github.com/user-attachments/assets/7a5d8b76-8fd0-44da-a281-92e22b6b9642)

---

## 🖼️ **Screenshots**

Below are the screenshots of the **web interface** that allows users to check air quality predictions:

![Screenshot 1](https://github.com/user-attachments/assets/11df9028-a096-4a87-9f19-b3fee0fa1f71)

![Screenshot 2](https://github.com/user-attachments/assets/ef8fae18-c143-4430-80d5-02b985b68059)

![Screenshot 3](https://github.com/user-attachments/assets/6e2149a7-b6a5-4dbf-a9f9-975cbcb1f1e7)

---

## 🧰 **Technologies Used**

- **Machine Learning**:  
   - **Random Forest**  
   - **Decision Tree Regression**
- **Web Development**:  
   - **Flask**  
- **Data Analysis and Visualization**:  
   - **Python**  
   - **NumPy**  
- **Other Tools**:  
   - **Jupyter Notebook (Google Colab)**  
   - **Spyder**  

![Technologies Used](https://github.com/user-attachments/assets/a19f6847-706a-4943-b3e6-72b4af614026)

---

## 🔧 **Tools / IDE**  

- **Jupyter Notebook (Google Colab)**: Used for training the models.  
- **Spyder**: Used for model deployment and testing on the local system.  

To use these tools, simply install **Anaconda**.

---

## 📋 **Software Requirements**

- **Python**: 3.7.7  
- **NumPy**: 1.18.5  
- **Flask**: 1.1.2  

---

## 🚀 **Setup and Installation**

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-username/air-quality-prediction.git  
   cd air-quality-prediction  
   ```  

2. **Install Required Libraries**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the Web Application**:  
   ```bash  
   python app.py  
   ```  

4. **Access the Application**:  
   Open your browser and navigate to **http://127.0.0.1:5000/** to view the air quality predictions.

---

## 📈 **Future Improvements**

- **Data Sources**: Integrate real-time data for continuous air quality monitoring.  
- **Mobile App**: Build a mobile application for users to access the air quality index on the go.  
- **Advanced Models**: Experiment with other regression models and deep learning techniques to further improve prediction accuracy.

---

## 📫 **Contact**  
Feel free to reach out if you have any questions or feedback!  
- **Email**: [rashmithapadmashetti1819@gmail.com](mailto:rashmithapadmashetti1819@gmail.com)  
- **LinkedIn**: [Rashmitha Padmashetti](https://www.linkedin.com/in/rashmithapadmashetti/)  

