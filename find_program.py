import sys
import os
import re
import json

DATABASE = [
    {
        "file": "dendrogram_products.py",
        "slips": ["Slip 1 (p.3, Q1)", "Slip 14 (p.16, Q1)", "Slip 23 (p.25, Q1)"],
        "algorithm": "Hierarchical Clustering / Dendrogram",
        "dataset": "Product DataFrame (Price, Rating, Number of Sales)",
        "keywords": ["dendrogram", "products", "product_name", "price", "rating", "number_of_sales", "hierarchical", "clustering", "similar products"],
        "question": "Create a dataframe containing information about different products such as Price, Rating, and Number of Sales. Generate a Dendrogram to group similar products based on their characteristics."
    },
    {
        "file": "pca_feature_extraction.py",
        "slips": ["Slip 1 (p.3, Q2)", "Slip 8 (p.10, Q2)", "Slip 21 (p.23, Q2_OR)"],
        "algorithm": "Feature Selection & PCA (Principal Component Analysis)",
        "dataset": "Loan_application.csv",
        "keywords": ["loan", "loan_application", "loan_status", "feature selection", "feature extraction", "pca", "principal component analysis", "debt_ratio", "credit_score"],
        "question": "Create a suitable dataset named Loan_application.csv containing at least 10 records with the attributes Application_ID, Age, Income, Credit_Score, Loan_Amount, Employment_Years, Debt_Ratio, and Loan_Status. Write a Python program to perform Feature Selection and Feature Extraction (PCA)."
    },
    {
        "file": "kmeans_clustering.py",
        "slips": ["Slip 1 (p.3, Q2_OR)"],
        "algorithm": "K-Means Clustering",
        "dataset": "Iris Dataset (Built-in)",
        "keywords": ["iris", "kmeans", "k-means", "clustering", "k = 3", "centroids", "cluster centroids", "datapoints"],
        "question": "Using the built-in Iris dataset, apply K-Means clustering with K = 3. Plot the datapoints, visualize the clusters with different colors, and display the cluster centroids."
    },
    {
        "file": "data_discretization_equal_width.py",
        "slips": ["Slip 2 (p.4, Q1)"],
        "algorithm": "Data Discretization (Equal Width Binning)",
        "dataset": "age_records (Person_ID, Age)",
        "keywords": ["age_records", "age", "discretization", "equal width", "binning", "cut", "person_id"],
        "question": "Write a Python program to create an age_records DataFrame containing the attributes Person_ID and Age for suitable sample records. Perform Data Discretization on the Age attribute using Equal Width Binning. Display the original and discretized data."
    },
    {
        "file": "linear_regression_youtube.py",
        "slips": ["Slip 2 (p.4, Q2)"],
        "algorithm": "Linear Regression",
        "dataset": "YouTube Video Dataset (USvideos.csv)",
        "keywords": ["youtube", "video", "views", "likes", "linear regression", "scatter plot", "regression line", "predict views"],
        "question": "Apply Linear Regression on a YouTube Video dataset to predict video views using relevant video attributes. Visualize the relationship between the predictor and target variable using a scatter plot and regression line."
    },
    {
        "file": "apriori_association_rules.py",
        "slips": ["Slip 2 (p.4, Q2_OR)", "Slip 10 (p.12, Q2_OR)"],
        "algorithm": "Apriori Association Rule Mining",
        "dataset": "Learning Activities Dataset (10 transactions: Video Lecture, Quiz, Assignment, Discussion Forum, Certificate)",
        "keywords": ["apriori", "frequent itemsets", "association rules", "video lecture", "quiz", "assignment", "discussion forum", "certificate", "support 0.2", "support 0.3", "support 0.4"],
        "question": "Create the following dataset in python. Apply the Apriori algorithm to generate frequent itemsets and association rules. Repeat the process with different minimum support values (0.2, 0.3, 0.4)."
    },
    {
        "file": "box_plot_outliers.py",
        "slips": ["Slip 3 (p.5, Q1)", "Slip 19 (p.21, Q1)"],
        "algorithm": "Box Plot / Outlier Detection",
        "dataset": "Vehicles DataFrame (Fuel_Efficiency, Engine_Power, Vehicle_Weight, Engine_Size, Acceleration)",
        "keywords": ["vehicles", "box plot", "box plots", "fuel_efficiency", "engine_power", "outlier", "outliers", "5 records"],
        "question": "Create a dataframe containing information about different vehicles such as Fuel_Efficiency, Engine_Power, Vehicle_Weight, Engine_Size, and Acceleration. Add 5 records in dataframe, including outlier. Create Box Plots for Fuel Efficiency and Engine Power and identify outliers."
    },
    {
        "file": "linear_regression_salary.py",
        "slips": ["Slip 3 (p.5, Q2)", "Slip 8 (p.10, Q2_OR)"],
        "algorithm": "Simple Linear Regression",
        "dataset": "Salary Dataset (Salary_Data.csv)",
        "keywords": ["salary", "yearsexperience", "years of experience", "simple linear regression", "regression line", "mse", "mean squared error"],
        "question": "Consider the Salary Dataset. Apply Simple Linear Regression to predict salary based on years of experience. Split the data into training and testing sets, plot the regression line, and evaluate the model using Mean Squared Error."
    },
    {
        "file": "random_forest_heart_disease.py",
        "slips": ["Slip 3 (p.5, Q2_OR)", "Slip 19 (p.21, Q2_OR)"],
        "algorithm": "Random Forest Classification",
        "dataset": "Heart Disease Dataset (heart.csv)",
        "keywords": ["heart disease", "random forest", "heart.csv", "presence", "accuracy", "confusion matrix", "precision", "recall", "f1-score"],
        "question": "Apply the Random Forest algorithm on the Heart Disease dataset to predict the presence or absence of heart disease. Preprocess the data, evaluate the model using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix."
    },
    {
        "file": "pie_chart_payment_methods.py",
        "slips": ["Slip 4 (p.6, Q1)"],
        "algorithm": "Pie Chart",
        "dataset": "Payment Methods (UPI, Credit Card, Debit Card, Cash, Net Banking)",
        "keywords": ["pie chart", "payment method", "payment_methods", "upi", "credit card", "debit card", "cash", "net banking", "customers"],
        "question": "A survey was conducted to determine the preferred payment method among customers: payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Cash', 'Net Banking'], customers = [150, 80, 60, 40, 30]. Create a Pie Chart to represent percentage of customers using each method."
    },
    {
        "file": "logistic_regression_gaming.py",
        "slips": ["Slip 4 (p.6, Q2)", "Slip 13 (p.15, Q2_OR)"],
        "algorithm": "Logistic Regression",
        "dataset": "Online Gaming Dataset (online_gaming_behavior_dataset.csv)",
        "keywords": ["gaming", "online gaming", "casual", "professional", "daily play time", "achievements unlocked", "in-game purchases", "gaming level", "logistic regression"],
        "question": "Apply Logistic Regression on an Online Gaming dataset to classify players as Casual or Professional gamers based on features such as daily play time, achievements unlocked, in-game purchases, and gaming level. Evaluate with Accuracy, Precision, Recall, F1-Score, and Confusion Matrix."
    },
    {
        "file": "kmeans_clustering_ecommerce.py",
        "slips": ["Slip 4 (p.6, Q2_OR)", "Slip 11 (p.13, Q2_OR)"],
        "algorithm": "K-Means Clustering",
        "dataset": "E-Commerce Customer Dataset (Mall_Customers.csv)",
        "keywords": ["e-commerce", "customer", "ecommerce", "mall_customers", "kmeans", "k-means", "segment", "annual income", "spending score"],
        "question": "Apply the K-Means Clustering algorithm on the given E-commerce Customer dataset. Read the dataset using Python, inspect and preprocess data, select numerical features, segment customers and display clusters."
    },
    {
        "file": "label_encoding.py",
        "slips": ["Slip 5 (p.7, Q1)"],
        "algorithm": "Label Encoding",
        "dataset": "customer_DataFrame (Customer_ID, Gender, City, Membership_Type)",
        "keywords": ["customer_dataframe", "label encoding", "customer_id", "gender", "city", "membership_type", "categorical"],
        "question": "Write a Python program to create a customer_DataFrame with suitable attributes such as Customer_ID, Gender, City, and Membership_Type. Perform label encoding technique on appropriate categorical attributes. Display before and after."
    },
    {
        "file": "venn_diagram_streaming.py",
        "slips": ["Slip 5 (p.7, Q2)", "Slip 22 (p.24, Q2)"],
        "algorithm": "Venn Diagram & Pie Chart",
        "dataset": "Streaming Customers (Netflix & Amazon Prime)",
        "keywords": ["netflix", "amazon prime", "venn diagram", "pie chart", "both services", "streaming"],
        "question": "Generate a DataFrame containing customer information for Netflix and Amazon Prime users. Create a Venn diagram and a Pie chart to show customers using only Netflix, only Amazon Prime, and both services."
    },
    {
        "file": "knn_spam.py",
        "slips": ["Slip 5 (p.7, Q2_OR)", "Slip 12 (p.14, Q2_OR)"],
        "algorithm": "K-Nearest Neighbors (KNN)",
        "dataset": "Spambase Dataset (spambase.csv)",
        "keywords": ["knn", "k-nearest neighbors", "spam", "non-spam", "spambase", "emails", "accuracy", "confusion matrix"],
        "question": "Use the K-Nearest Neighbors (KNN) algorithm to classify emails as spam or non-spam using the Spambase dataset. Preprocess data, train KNN classifier, evaluate using accuracy, confusion matrix, precision, recall, and F1-score."
    },
    {
        "file": "scatter_plot_cars.py",
        "slips": ["Slip 6 (p.8, Q1)"],
        "algorithm": "Scatter Plot",
        "dataset": "Cars DataFrame (model, engine size, fuel efficiency)",
        "keywords": ["car model", "engine size", "fuel efficiency", "scatter plot", "cars", "litres", "km/l"],
        "question": "Create a DataFrame containing the car model, engine size (in litres), and fuel efficiency (in km/L) for given cars. Create a scatter plot to visualize relationship between engine size and fuel efficiency."
    },
    {
        "file": "linear_regression_sports.py",
        "slips": ["Slip 6 (p.8, Q2)"],
        "algorithm": "Simple Linear Regression",
        "dataset": "Sports Performance Dataset (collegiate_athlete_injury_dataset.csv)",
        "keywords": ["sports", "sports performance", "training hours per week", "performance score", "simple linear regression", "r2 score", "scatter graph", "regression line"],
        "question": "Use the Sports Performance dataset to develop a Simple Linear Regression model to predict Performance Score based on Training Hours Per Week. Evaluate model using R2 score and plot scatter graph with regression line."
    },
    {
        "file": "knn_customers.py",
        "slips": ["Slip 6 (p.8, Q2_OR)"],
        "algorithm": "K-Nearest Neighbors (KNN)",
        "dataset": "Customer Dataset (Mall_Customers.csv)",
        "keywords": ["knn", "customer dataset", "segments", "classify customers", "mall_customers", "accuracy", "confusion matrix"],
        "question": "Implement a KNN classifier on the given Customer dataset. Preprocess the data and classify customers into different segments. Evaluate the model using Accuracy and Confusion Matrix."
    },
    {
        "file": "bar_chart_courses.py",
        "slips": ["Slip 7 (p.9, Q1)", "Slip 25 (p.27, Q1)"],
        "algorithm": "Bar Chart",
        "dataset": "Courses Enrollment (BCA, BBA, B.Com, B.Sc, BA)",
        "keywords": ["bar chart", "courses", "students", "bca", "bba", "b.com", "b.sc", "ba", "enrolled"],
        "question": "Consider dataset representing students enrolled in different courses: courses = ['BCA', 'BBA', 'B.Com', 'B.Sc', 'BA'], students = [60, 45, 75, 50, 35]. Create a Bar Chart to visualize students enrolled in each course."
    },
    {
        "file": "knn_student_grading.py",
        "slips": ["Slip 7 (p.9, Q2)", "Slip 23 (p.25, Q2_OR)"],
        "algorithm": "K-Nearest Neighbors (KNN)",
        "dataset": "Student Grading Dataset (Students_Grading_Dataset.csv)",
        "keywords": ["knn", "k-nearest neighbors", "student dataset", "student grading", "performance categories", "accuracy", "precision", "recall", "f1-score", "confusion matrix"],
        "question": "Implement a K-Nearest Neighbors (KNN) classifier on the given Student Grading dataset to classify students into different performance categories. Preprocess data, train/test, and evaluate using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix."
    },
    {
        "file": "apriori_groceries.py",
        "slips": ["Slip 7 (p.9, Q2_OR)", "Slip 15 (p.17, Q2_OR)", "Slip 25 (p.27, Q2_OR)"],
        "algorithm": "Apriori Market Basket Analysis",
        "dataset": "Groceries Dataset (7 transactions: Basmati Rice, Toor Dal, Atta, etc.)",
        "keywords": ["groceries", "market basket analysis", "apriori", "items purchased", "basmati rice", "toor dal", "turmeric powder", "cooking oil", "atta", "sugar", "support 0.3", "support 0.4"],
        "question": "Write a Python program to perform market basket analysis on the Groceries dataset using the Apriori algorithm. Preprocess categorical transaction data, generate frequent itemsets and association rules. Repeat using minimum support 0.3 and 0.4."
    },
    {
        "file": "geospatial_visualization.py",
        "slips": ["Slip 8 (p.10, Q1)"],
        "algorithm": "Geospatial Visualization",
        "dataset": "Earthquakes Dataset (Latitude, Longitude, Depth, Magnitude)",
        "keywords": ["earthquakes", "geospatial", "latitude", "longitude", "depth", "magnitude", "map", "color"],
        "question": "Create a suitable dataset containing information about earthquakes using Latitude, Longitude, Depth, and Magnitude. a. Create a Geospatial Visualization on a map. b. Use color to represent magnitude."
    },
    {
        "file": "min_max_scaling.py",
        "slips": ["Slip 9 (p.11, Q1)"],
        "algorithm": "Min-Max Scaling",
        "dataset": "Product DataFrame (Product_ID, Price, Quantity_Sold, Discount, Revenue)",
        "keywords": ["min-max scaling", "min_max_scaling", "product dataframe", "quantity_sold", "discount", "revenue", "minmaxscaler"],
        "question": "Write a Python program to create a product DataFrame with attributes Product_ID, Price, Quantity_Sold, Discount, and Revenue. Apply Min-Max Scaling data transformation technique and display transformed data."
    },
    {
        "file": "logistic_regression_smartphones.py",
        "slips": ["Slip 9 (p.11, Q2)", "Slip 11 (p.13, Q2)"],
        "algorithm": "Logistic Regression",
        "dataset": "Smartphone Dataset (Mobile Price Prediction / train.csv)",
        "keywords": ["smartphones", "smartphone", "price categories", "ram", "storage", "battery capacity", "camera resolution", "logistic regression", "price_range"],
        "question": "Apply Logistic Regression to classify smartphones into different price categories using specifications such as RAM, storage, battery capacity, and camera resolution. Assess model using Accuracy, F1-Score, and Confusion Matrix."
    },
    {
        "file": "word_cloud_books.py",
        "slips": ["Slip 9 (p.11, Q2_OR)", "Slip 20 (p.22, Q2)"],
        "algorithm": "Venn Diagram & Word Cloud",
        "dataset": "Books Dataset (Book Title, Author, Publication Year, Rating)",
        "keywords": ["books", "book title", "author", "publication year", "venn diagram", "word cloud", "wordcloud", "two different time periods"],
        "question": "Create a dataset containing information about different books with attributes Book Title, Author, Publication Year, Average Rating, and Number of Ratings. a. Create a Venn Diagram comparing authors in two time periods. b. Generate Word Cloud using book titles."
    },
    {
        "file": "pie_chart_transportation.py",
        "slips": ["Slip 10 (p.12, Q1)"],
        "algorithm": "Pie Chart",
        "dataset": "Transportation Modes (Train, Bicycle, Bike, Car, Bus)",
        "keywords": ["transport", "transportation", "employees", "train", "bicycle", "bike", "car", "bus", "pie chart"],
        "question": "A company conducted a survey to determine preferred mode of transportation among employees: transport = ['Train', 'Bicycle', 'Bike', 'Car', 'Bus'], employees = [220, 60, 70, 80, 40]. Create Pie Chart representing percentage of employees."
    },
    {
        "file": "random_forest_house_prices.py",
        "slips": ["Slip 10 (p.12, Q2)"],
        "algorithm": "Random Forest Regression",
        "dataset": "Housing Dataset (housing.csv)",
        "keywords": ["housing", "house prices", "random forest regression", "random forest", "mae", "rmse", "r2 score"],
        "question": "Using the given housing dataset, develop a Random Forest Regression model to predict house prices based on available property attributes. Preprocess data, evaluate predictive performance using MAE, RMSE, and R2 Score."
    },
    {
        "file": "bar_chart_departments.py",
        "slips": ["Slip 11 (p.13, Q1)"],
        "algorithm": "Bar Chart",
        "dataset": "Departments (HR, Finance, IT, Sales, Marketing)",
        "keywords": ["departments", "organization", "hr", "finance", "it", "sales", "marketing", "bar chart", "distribution of employees"],
        "question": "An organization has recorded number of employees working in different departments such as HR, Finance, IT, Sales, and Marketing. Write a Python program to create a bar chart showing distribution of employees."
    },
    {
        "file": "histogram_titanic.py",
        "slips": ["Slip 12 (p.14, Q1)"],
        "algorithm": "Histogram & Pie Chart",
        "dataset": "Titanic Dataset (titanic.csv)",
        "keywords": ["titanic", "titanic.csv", "histogram", "passenger class", "pclass", "pie chart", "survival distribution"],
        "question": "Load the Titanic dataset (titanic.csv). Create a histogram showing the number of passengers in each passenger class. Create a Pie Chart showing the survival distribution."
    },
    {
        "file": "polynomial_regression_songs.py",
        "slips": ["Slip 12 (p.14, Q2)"],
        "algorithm": "Polynomial Regression",
        "dataset": "Songs Dataset (Spotify Raw Data / songs.csv)",
        "keywords": ["songs", "song popularity", "polynomial regression", "audio features", "danceability", "energy", "tempo", "mae", "rmse", "r2 score", "fitted curve"],
        "question": "Apply Polynomial Regression to predict song popularity using audio features such as danceability, energy, and tempo. Evaluate model using MAE, RMSE, and R2 Score, and visualize fitted curve."
    },
    {
        "file": "box_plot_sales_outliers.py",
        "slips": ["Slip 13 (p.15, Q1)"],
        "algorithm": "Box Plot / Outlier Detection",
        "dataset": "Sales Dataset (sales.csv)",
        "keywords": ["sales", "sales.csv", "retail store", "daily sales", "two months", "box plot", "outliers"],
        "question": "A retail store has recorded daily sales for two months. Create a dataframe using sales.csv file and generate a Box Plot to identify any outliers. Customize graph with title and labels."
    },
    {
        "file": "knn_wine.py",
        "slips": ["Slip 13 (p.15, Q2)"],
        "algorithm": "K-Nearest Neighbors (KNN)",
        "dataset": "Wine Dataset (Wine.csv)",
        "keywords": ["wine", "wine.csv", "knn", "k-nearest neighbors", "accuracy", "precision", "recall", "f1-score"],
        "question": "Implement the K-Nearest Neighbors (KNN) algorithm to classify the Wine dataset. Perform required data preprocessing, train and test model, evaluate performance using Accuracy, Precision, Recall, and F1-Score."
    },
    {
        "file": "polynomial_regression_car_prices.py",
        "slips": ["Slip 14 (p.16, Q2)", "Slip 24 (p.26, Q2_OR)"],
        "algorithm": "Polynomial Regression",
        "dataset": "Car Price Prediction Dataset (car_data.csv)",
        "keywords": ["car price", "car price prediction", "polynomial regression", "selling price", "vehicle age", "present price", "kilometers driven", "kms_driven", "r2 score", "fitted polynomial curve"],
        "question": "Using the Car Price Prediction dataset, apply Polynomial Regression to predict Selling Price based on Vehicle Age, Present Price, and Kilometers Driven. Evaluate using R2 Score and visualize fitted curve."
    },
    {
        "file": "one_hot_encoding.py",
        "slips": ["Slip 14 (p.16, Q2_OR)", "Slip 25 (p.27, Q2)"],
        "algorithm": "Data Integration, Label & One-Hot Encoding",
        "dataset": "Mobile Phones DataFrames",
        "keywords": ["mobile phones", "data integration", "label encoding", "one-hot encoding", "brand", "model", "operating_system", "battery_capacity", "get_dummies"],
        "question": "Create two DataFrames containing information about different mobile phones. Perform Data Integration on Model, Label Encoding on Brand, and One-Hot Encoding on Operating_System."
    },
    {
        "file": "data_discretization_equal_frequency.py",
        "slips": ["Slip 15 (p.17, Q1)"],
        "algorithm": "Data Discretization (Equal Frequency Binning)",
        "dataset": "age_records (Person_ID, Age)",
        "keywords": ["age_records", "age", "discretization", "equal frequency", "binning", "qcut", "person_id"],
        "question": "Write a Python program to create an age_records DataFrame containing attributes Person_ID and Age for suitable sample records. Perform Data Discretization on Age attribute using Equal Frequency Binning."
    },
    {
        "file": "treemap_cities.py",
        "slips": ["Slip 15 (p.17, Q2)"],
        "algorithm": "Treemap & 3D Scatter Plot",
        "dataset": "Cities DataFrame (Area, Temperature, Rainfall, Population Density)",
        "keywords": ["treemap", "3d scatter plot", "cities", "area", "average temperature", "rainfall", "population density"],
        "question": "Create a DataFrame containing information about different cities with attributes City, Area (sq. km), Average Temperature, Rainfall, and Population Density. Generate a Treemap of population density and a 3D Scatter Plot using Area, Temperature, and Rainfall."
    },
    {
        "file": "correlation_heatmap.py",
        "slips": ["Slip 16 (p.18, Q1)"],
        "algorithm": "Correlation Matrix & Heat Map",
        "dataset": "Student Performance DataFrame",
        "keywords": ["study hours", "attendance", "assignment score", "exam score", "correlation matrix", "heat map", "heatmap"],
        "question": "Create a DataFrame containing student performance data with attributes such as Study Hours, Attendance, Assignment Score, and Exam Score. Calculate correlation matrix and generate Heat Map to visualize correlation."
    },
    {
        "file": "data_transformation_scaling.py",
        "slips": ["Slip 16 (p.18, Q2)", "Slip 19 (p.21, Q2)", "Slip 23 (p.25, Q2)"],
        "algorithm": "Data Transformation (Min-Max, Standardization, Normalization)",
        "dataset": "Weather Parameters DataFrame",
        "keywords": ["temperature", "humidity", "wind speed", "pressure", "rainfall", "data transformation", "min-max scaling", "standardization", "normalization"],
        "question": "Write a Python program to create a DataFrame with attributes Temperature, Humidity, Wind Speed, Pressure, and Rainfall. Apply Min-Max Scaling, Standardization, and Normalization techniques."
    },
    {
        "file": "apriori_student_activities.py",
        "slips": ["Slip 16 (p.18, Q2_OR)", "Slip 20 (p.22, Q2_OR)"],
        "algorithm": "Apriori Association Rule Mining",
        "dataset": "Student Activities (9 transactions: Library, Seminar, Workshop, Project, Assignment)",
        "keywords": ["library", "seminar", "workshop", "project", "assignment", "apriori", "student activity", "support 0.2", "support 0.3"],
        "question": "Implement the Apriori algorithm on the given student activity dataset (9 transactions) to identify frequent itemsets and generate association rules among activities. Repeat analysis using minimum support 0.2 and 0.3."
    },
    {
        "file": "data_integration.py",
        "slips": ["Slip 17 (p.19, Q1)"],
        "algorithm": "Data Integration",
        "dataset": "student_details & academic_records",
        "keywords": ["student_details", "academic_records", "data integration", "student_id", "merge", "common attribute"],
        "question": "Write a Python program to create two DataFrames, student_details and academic_records, containing suitable student-related attributes. Perform data integration combining using Student_ID."
    },
    {
        "file": "treemap_3d_scatter_economy.py",
        "slips": ["Slip 17 (p.19, Q2)"],
        "algorithm": "Treemap & 3D Scatter Plot",
        "dataset": "Cities Economic Dataset (City, Population, GDP, Literacy Rate)",
        "keywords": ["city", "population", "gdp", "literacy rate", "treemap", "3d scatter plot", "population distribution"],
        "question": "Create a dataset containing information about different cities with attributes: City, Population, GDP, and Literacy Rate. a. Generate Treemap showing population distribution. b. Create 3D Scatter Plot using Population, GDP, and Literacy Rate."
    },
    {
        "file": "random_forest_student_grading.py",
        "slips": ["Slip 17 (p.19, Q2_OR)"],
        "algorithm": "Random Forest Classification",
        "dataset": "Student Grading Dataset (Students_Grading_Dataset.csv)",
        "keywords": ["student grading", "random forest", "performance categories", "random forest classifier", "confusion matrix", "accuracy", "precision", "recall", "f1-score"],
        "question": "Develop a Random Forest Classifier using the given Student Grading dataset to classify students into different performance categories. Evaluate using Confusion Matrix, Accuracy, Precision, Recall, and F1-Score."
    },
    {
        "file": "data_cleaning_iqr.py",
        "slips": ["Slip 18 (p.20, Q1)"],
        "algorithm": "Data Cleaning & IQR Outliers",
        "dataset": "employee_data (Emp_ID, Age, Dept, Years_Experience, Performance_Rating)",
        "keywords": ["employee_data", "emp_id", "missing values", "duplicate records", "iqr method", "outliers", "data cleaning"],
        "question": "Write a Python program to create an employee_data DataFrame with attributes Emp_ID, Age, Dept, Years_Experience, and Performance_Rating. Perform data cleaning by handling missing values, removing duplicates, and detecting outliers using IQR method."
    },
    {
        "file": "geospatial_treemap_world_cities.py",
        "slips": ["Slip 18 (p.20, Q2)", "Slip 24 (p.26, Q2)"],
        "algorithm": "Geospatial Visualization & Treemap",
        "dataset": "World Cities Dataset (worldcities.csv)",
        "keywords": ["world cities", "worldcities", "latitude", "longitude", "geospatial", "world map", "marker size", "treemap", "population distribution"],
        "question": "Consider World Cities dataset containing attributes city, country, latitude, longitude, and population. a. Create Geospatial Visualization showing locations on world map using marker size for population. b. Create Treemap to visualize population distribution."
    },
    {
        "file": "linear_regression_crop_yield.py",
        "slips": ["Slip 18 (p.20, Q2_OR)"],
        "algorithm": "Simple Linear Regression",
        "dataset": "Crop Yield Dataset (crop_yield_data.csv)",
        "keywords": ["crop yield", "rainfall", "simple linear regression", "predicting crop yield", "mae", "r2 score", "scatter plot", "regression line"],
        "question": "Use Crop Yield dataset to apply Simple Linear Regression for predicting crop yield from rainfall. Handle missing values, train/test split, evaluate using MAE and R2 Score, create Scatter Plot with Regression Line."
    },
    {
        "file": "standardization.py",
        "slips": ["Slip 20 (p.22, Q1)"],
        "algorithm": "Standardization (Z-score)",
        "dataset": "Employee Attributes DataFrame (Age, Salary, Experience, Working_Hours, Performance_Score)",
        "keywords": ["standardization", "standardscaler", "z-score", "age", "salary", "experience", "working_hours", "performance_score"],
        "question": "Write a Python program to create a DataFrame containing attributes Age, Salary, Experience, Working_Hours, and Performance_Score. Apply Standardization data transformation technique and display transformed data."
    },
    {
        "file": "correlation_heatmap_weather.py",
        "slips": ["Slip 21 (p.23, Q1)"],
        "algorithm": "Correlation Matrix & Heat Map",
        "dataset": "weather.csv (Temperature, Humidity, Rainfall, Wind Speed)",
        "keywords": ["weather", "weather.csv", "temperature", "humidity", "rainfall", "wind speed", "heat map", "heatmap", "correlation"],
        "question": "Create a dataframe using weather.csv containing values of Temperature, Humidity, Rainfall, and Wind Speed. Generate a Heat Map to visualize correlation between these weather parameters."
    },
    {
        "file": "kmeans_clustering_students.py",
        "slips": ["Slip 21 (p.23, Q2)", "Slip 22 (p.24, Q2_OR)"],
        "algorithm": "K-Means Clustering",
        "dataset": "Student Dataset (Attendance, Marks)",
        "keywords": ["attendance", "marks", "kmeans", "k-means", "k = 3", "student dataset", "centroids", "scatter plot"],
        "question": "Apply K-Means Clustering algorithm to given student dataset using Attendance and Marks as input attributes. Preprocess data, set K = 3, assign students to clusters, visualize clusters and centroids on scatter plot."
    },
    {
        "file": "normalization.py",
        "slips": ["Slip 22 (p.24, Q1)"],
        "algorithm": "Normalization (L2 / MinMax)",
        "dataset": "House Rent DataFrame (City, House_Type, House_Area, Number_of_Rooms, Monthly_Rent)",
        "keywords": ["normalization", "normalizer", "house_area", "number_of_rooms", "monthly_rent", "house_type", "city"],
        "question": "Write a Python program to create a DataFrame containing attributes City, House_Type, House_Area, Number_of_Rooms, and Monthly_Rent. Apply Normalization technique to numerical attributes and display normalized data."
    },
    {
        "file": "data_discretization_equal_width_books.py",
        "slips": ["Slip 24 (p.26, Q1)"],
        "algorithm": "Data Discretization (Equal Width Binning)",
        "dataset": "book_records (Book_ID, Book_Price)",
        "keywords": ["book_records", "book_price", "book_id", "discretization", "equal width", "binning", "cut"],
        "question": "Write a Python program to create a book_records DataFrame containing attributes Book_ID and Book_Price for suitable sample records. Perform Data Discretization on Book_Price attribute using Equal Width Binning."
    }
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return set(text.split())

def search_question(query, top_n=5):
    query_words = clean_text(query)
    scores = []
    
    for item in DATABASE:
        # Match against keywords, algorithm, dataset, question, and filename
        text_corpus = " ".join([
            item["file"],
            item["algorithm"],
            item["dataset"],
            " ".join(item["keywords"]),
            item["question"]
        ])
        corpus_words = clean_text(text_corpus)
        
        # Calculate overlap
        overlap = query_words.intersection(corpus_words)
        score = 0.0
        
        for w in overlap:
            weight = 1.0
            # Higher weights for specific technical terms
            if w in ["dendrogram", "venn", "wordcloud", "apriori", "kmeans", "knn", "logistic", "polynomial", "treemap", "iqr", "discretization", "scaling", "standardization", "normalization", "pca"]:
                weight = 3.5
            elif w in ["titanic", "gaming", "spambase", "groceries", "salary", "youtube", "athlete", "crop", "earthquake", "weather", "housing", "wine", "cars", "netflix"]:
                weight = 3.0
            score += weight
        
        # Exact phrase bonus
        if any(kw.lower() in query.lower() for kw in item["keywords"] if len(kw.split()) > 1):
            score += 4.0
        
        # Specific algorithm matches
        if item["file"].replace(".py", "") in query.lower().replace(" ", "_"):
            score += 10.0
            
        scores.append((score, item))
    
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_n]

def display_results(query, results):
    print("=" * 80)
    print(f"QUERY: {query.strip()[:100]}...")
    print("=" * 80)
    
    if not results or results[0][0] == 0:
        print("No high-confidence match found. Please check question keywords.")
        return

    best = results[0][1]
    print(f"[*] BEST MATCHING PROGRAM: python {best['file']}")
    print(f"  Appears in : {', '.join(best['slips'])}")
    print(f"  Algorithm  : {best['algorithm']}")
    print(f"  Dataset    : {best['dataset']}")
    print("-" * 80)
    print("TOP MATCHING CANDIDATES:")
    
    for idx, (sc, item) in enumerate(results, 1):
        rel = f"(Score: {sc:.1f})"
        print(f"\n[{idx}] {item['file']} {rel}")
        print(f"    Slips     : {', '.join(item['slips'])}")
        print(f"    Algorithm : {item['algorithm']}")
        print(f"    Dataset   : {item['dataset']}")
        print(f"    Question  : {item['question'][:120]}...")
    print("=" * 80)
    print(f"To run the best match directly, execute:\n  python {best['file']}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        print("--- CS-308 Data Science Practical Program Finder ---")
        print("Paste your exam question below (or enter key phrases):")
        try:
            query = input("> ")
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
            
    if not query.strip():
        print("Empty input. Exiting.")
        sys.exit(0)
        
    top_matches = search_question(query, top_n=5)
    display_results(query, top_matches)
