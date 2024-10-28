OVERVIEW OF THE PROJECT

Assessing air quality holds significant importance in contemporary urban and industrial settings due to the pervasive impact of pollution stemming from various sources such as fuel combustion,
power generation, and transportation. The increasing concentrations of harmful gases present a considerable threat to the well-being of residents in smart cities, underscoring the critical need for effective systems for predicting and monitoring air quality. Pollutants including particulate matter 2.5, ammonia, NOx, ozone, carbon monoxide, sulfur dioxide, nitrogen dioxide, Benzene, and Toluene, as well as metrics like AQI and AQI_bucket, are utilized in formulating the air quality index. To predict the air quality index, we employ machine learning algorithms. Regression methods, such as random forest and decision tree regression, are used to forecast air quality. These models are compared using evaluation metrics and execution time derived from the dataset. The random forest algorithm achieves better accuracy than the other two models. Additionally, I used the FLASK model to create the web page to check the air quality on the web page itself.

METHODOLOGY

![image](https://github.com/user-attachments/assets/cf15111b-8758-46ba-ae1f-2aa5314e6616)

Results

Listed all of the evaluation criteria for both techniques. root mean square error, mean absolute error, and mean square error are lower for the random forest method than the decision tree method, whereas the R2 scores are higher. As we know, R2 scores are higher for a better model, while the other metrics are lower. Therefore, we can conclude from the results that the random forest
algorithm predicts air quality better than the decision tree algorithm.

![image](https://github.com/user-attachments/assets/7a5d8b76-8fd0-44da-a281-92e22b6b9642)


Screenshots of the project

![image](https://github.com/user-attachments/assets/11df9028-a096-4a87-9f19-b3fee0fa1f71)


![image](https://github.com/user-attachments/assets/ef8fae18-c143-4430-80d5-02b985b68059)


![image](https://github.com/user-attachments/assets/6e2149a7-b6a5-4dbf-a9f9-975cbcb1f1e7)







Technologies Used
![image](https://github.com/user-attachments/assets/a19f6847-706a-4943-b3e6-72b4af614026)


Tools / IDE

I used Jupyter NoteBook (Google Colab) for model training. used spyder for model deployment on the local system. To use Jupyter NoteBook and Spyder, just install anaconda.

Software Requirments

Python == 3.7.7

NumPy == 1.18.5

Flask == 1.1.2





