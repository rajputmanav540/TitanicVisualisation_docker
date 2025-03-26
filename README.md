# Titanic Visualization App 🚢📊  

This is a **Streamlit-based web application** that visualizes the Titanic dataset.  
It provides various interactive visualizations to explore **passenger survival, class distribution, age, and gender demographics**.

---

## **🔹 Features**  
✅ Interactive visualizations using **Matplotlib & Seaborn**  
✅ Passenger survival analysis based on **gender, age, and class**  
✅ Histogram, pie charts, and bar plots for in-depth insights  
✅ User-friendly interface powered by **Streamlit**  
✅ Dockerized for seamless deployment  

---

## **🔹 Installation & Running the App**
To run this project locally, follow these steps:

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/Titanic-Visualization.git
cd Titanic-Visualization
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Streamlit App**
```bash
streamlit run app.py
```

---

## **🔹 Running the App using Docker**
This application is fully containerized using Docker. Follow these steps to run it inside a Docker container:

### **Step 1: Build the Docker Image**
```bash
docker build -t titanic-visualization .
```

### **Step 2: Run the Docker Container**
```bash
docker run -p 8501:8501 titanic-visualization
```

Now, open your browser and go to `http://localhost:8501` to access the app.

---

## **🔹 Docker Architecture Diagram**

Below is a visual representation of the Docker architecture:

![Docker Architecture](images/home_page.png)

This diagram illustrates the relationship between the key components mentioned above. The **Docker Daemon** runs on the host machine and manages the creation and execution of containers. Users interact with Docker through the **CLI**, while the images and containers reside in the system's filesystem. The **Docker registry** holds the images, making it easier for users to pull and push images from a centralized location.

---

## **🔹 Dataset**
This application utilizes the **Titanic dataset** from Kaggle. The dataset contains information about Titanic passengers, including their age, class, gender, fare, and survival status.

### **Data Columns:**
- `PassengerId` - Unique identifier for each passenger
- `Survived` - Survival status (0 = No, 1 = Yes)
- `Pclass` - Ticket class (1st, 2nd, 3rd)
- `Name` - Passenger name
- `Sex` - Gender
- `Age` - Age in years
- `SibSp` - Number of siblings/spouses aboard
- `Parch` - Number of parents/children aboard
- `Ticket` - Ticket number
- `Fare` - Passenger fare
- `Cabin` - Cabin number
- `Embarked` - Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

---

## **🔹 Contributions**
We welcome contributions! Feel free to **fork** the repository, create a new **branch**, and submit a **pull request**.

---

## **🔹 License**
This project is licensed under the **MIT License**.

---

## **🔹 Contact**
For any questions or feedback, feel free to reach out via:
- GitHub Issues
- Email: rajputmanav540@gmail.com
