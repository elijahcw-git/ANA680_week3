# UCI Wine Quality Prediction using Random Forests

## Overview

This project is developed to predict wine quality in the UCI Wine Quality dataset using a Random Forest classifier. The objective is to achieve a model accuracy of 62% by selecting specific variables from the dataset that are most relevant for the prediction.

## Features Used for Prediction

The model uses the following features from the UCI Wine Quality dataset:

- Alcohol (`alcohol`)
- Density (`density`)
- Chlorides (`chlorides`)
- Volatile Acidity (`volatile acidity`)
- Total Sulfur Dioxide (`total sulfur dioxide`)

## Tools and Libraries

The model is developed using Python and makes use of the following libraries:

- scikit-learn (`sklearn`): For implementing the Random Forest algorithm.
- pandas: For data manipulation and analysis.

## Model Training

The Random Forest model is trained on the UCI Wine Quality dataset using `scikit-learn`. The dataset is processed and divided into training and test sets. The selected features are carefully chosen to ensure that the most relevant predictors are used for the model.

## Model Evaluation

The performance of the model is assessed based on its accuracy in predicting wine quality. The target is to achieve a model accuracy of 62%.



---

This README provides an overview of the UCI Wine Quality prediction project using Random Forests. For more details and code implementation, refer to the associated Python notebook.
