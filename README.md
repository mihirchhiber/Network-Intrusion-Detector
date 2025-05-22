# Network Intrusion Detector

## Overview

Network Intrusion Detector is a scalable, machine learning-based network intrusion detection system (NIDS) designed to identify anomalous or malicious network activity in large-scale environments. Leveraging the distributed computing power of Apache Spark (PySpark), the project preprocesses, encodes, and models network connection data to accurately classify events as normal or anomalous, enabling real-time or batch detection of potential security threats.

## Key Features

- **Data Preprocessing:**  
  Cleans and prepares network connection data, handling missing values, duplicates, and irrelevant features to optimize model performance.

- **Feature Engineering:**  
  Encodes categorical variables using `StringIndexer` and `OneHotEncoder`, normalizes numerical features, and assembles them into feature vectors suitable for machine learning.

- **Model Training:**  
  Utilizes a Random Forest classifier for robust anomaly detection, with iterative tuning of hyperparameters (number of trees, depth) to balance performance and complexity.

- **Feature Selection:**  
  Employs feature importance analysis to reduce dimensionality, retaining only the most informative features and improving efficiency.

- **Evaluation:**  
  Assesses model accuracy, AUC, and F1 score, achieving high detection rates (accuracy ~97.5%, AUC ~0.998, F1 ~0.975) even after feature reduction.

- **Model Persistence:**  
  Saves the trained model for deployment or future inference tasks.

## Use Cases

- Real-time or batch detection of intrusions in enterprise or cloud networks.
- Automated monitoring for financial fraud or other security anomalies.
- Scalable analytics for large network traffic datasets.

## Tech Stack Used

- Apache Spark (PySpark)
- PySpark SQL         
- PySpark MLlib
- Pandas
- RandomForestClassifier
- Python 3.11

