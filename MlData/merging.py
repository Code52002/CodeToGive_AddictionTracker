# -*- coding: utf-8 -*-
"""Merging.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14uaEApXRVzvOmK8Eohc9B_WhPjzbFndf
"""

import sys
import json

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings("ignore")

# read the array from the subprocess args
json_string = sys.argv[1]
# Parse the JSON string into a Python object
json_object = json.loads(json_string)

# Access the values from the JSON object
addictionType = json_object['type']
user_response = json_object['data']

# addictionType = "alcohol"
# user_response = [0, 0, 0, 0, 0, 0, 0]

# print(addictionType, user_response)

# Define a function to train the K-means model on a given dataset
def train_kmeans_model(dataset):
    # Extract the features and addiction intensity values
    features = dataset.iloc[:, :].values
    addiction_intensities = dataset.iloc[:, :].values.reshape(-1, 1)

    # Calculate the addiction intensity as the average of the user's responses
    addiction_intensities = np.mean(features, axis=1).reshape(-1, 1)

    # Apply feature scaling
    scaler_f = StandardScaler()
    scaler_a = StandardScaler()
    features_scaled = scaler_f.fit_transform(features)
    addiction_intensities_scaled = scaler_a.fit_transform(addiction_intensities)

    # Train the K-means model
    n_clusters = 3
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans_model.fit(np.hstack((features_scaled, addiction_intensities_scaled)))

    return kmeans_model, scaler_f, scaler_a


def predict_counselor_needed(user_response, kmeans_model, scaler_f, scaler_a):
    # Calculate the addiction intensity as the average of the user's responses
    intensity = np.mean(user_response)

    # Scale the addiction intensity using the same scaler used for training
    intensity_scaled = scaler_a.transform([[intensity]])
    # print(intensity_scaled)
    # Reshape the user response and intensity_scaled to have 2 dimensions
    user_response_reshaped = np.array(user_response).reshape(1, -1)
    user_response_reshaped = scaler_f.transform(user_response_reshaped)
    # print(user_response_reshaped)
    # Predict the addiction intensity cluster
    cluster_label = kmeans_model.predict(
        np.hstack((user_response_reshaped, intensity_scaled))
    )

    return cluster_label


# alcohol addiction
def alcohol(user_response):
    dataset_condition1 = pd.read_csv("MlData/content/Alcohol.csv",names= ['q1', 'q2', 'q3','q4','q5','q6','q7'])
    (
        kmeans_model_condition1,
        scaler_f_condition1,
        scaler_a_condition1,
    ) = train_kmeans_model(dataset_condition1)
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition1, scaler_f_condition1, scaler_a_condition1
    )
    yes = [1, 3, 1, 1, 1, 1, 1]
    no = [0, 0, 0, 0, 0, 0, 0]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition1, scaler_f_condition1, scaler_a_condition1
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition1, scaler_f_condition1, scaler_a_condition1
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition1, scaler_f_condition1, scaler_a_condition1
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# internet addiction
def internet(user_response):
    dataset_condition2 = pd.read_csv("MlData/content/internet.csv",names= ['q1', 'q2', 'q3','q4','q5','q6','q7'])
    (
        kmeans_model_condition2,
        scaler_f_condition2,
        scaler_a_condition2,
    ) = train_kmeans_model(dataset_condition2)
    yes = [3, 2, 1, 1, 1, 1, 1]
    no = [0, 0, 0, 0, 0, 0, 0]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition2, scaler_f_condition2, scaler_a_condition2
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition2, scaler_f_condition2, scaler_a_condition2
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition2, scaler_f_condition2, scaler_a_condition2
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# poronography addiction
def pornography(user_response):
    dataset_condition3 = pd.read_csv("MlData/content/pornography.csv",names= ['q1', 'q2', 'q3','q4','q5','q6','q7'])
    (
        kmeans_model_condition3,
        scaler_f_condition3,
        scaler_a_condition3,
    ) = train_kmeans_model(dataset_condition3)
    no = [0, 0, 0, 0, 0, 0, 0]
    yes = [1, 1, 3, 3, 1, 1, 1]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition3, scaler_f_condition3, scaler_a_condition3
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition3, scaler_f_condition3, scaler_a_condition3
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition3, scaler_f_condition3, scaler_a_condition3
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# gaming addiction
def gaming(user_response):
    dataset_condition4 = pd.read_csv(
        "MlData/content/gaming.csv",
        names=["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"],
    )
    (
        kmeans_model_condition4,
        scaler_f_condition4,
        scaler_a_condition4,
    ) = train_kmeans_model(dataset_condition4)
    no = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yes = [1, 3, 1, 1, 1, 1, 1, 1, 1]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition4, scaler_f_condition4, scaler_a_condition4
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition4, scaler_f_condition4, scaler_a_condition4
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition4, scaler_f_condition4, scaler_a_condition4
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# gambling addiction
def gambling(user_response):
    dataset_condition5 = pd.read_csv(
        "MlData/content/gambling.csv", names=["q1", "q2", "q3", "q4", "q5", "q6", "q7"]
    )
    (
        kmeans_model_condition5,
        scaler_f_condition5,
        scaler_a_condition5,
    ) = train_kmeans_model(dataset_condition5)
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition5, scaler_f_condition5, scaler_a_condition5
    )
    no = [0, 0, 0, 0, 0, 0, 0]
    yes = [1, 1, 1, 1, 1, 1, 1]
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition5, scaler_f_condition5, scaler_a_condition5
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition5, scaler_f_condition5, scaler_a_condition5
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# family issues
def family(user_response):
    dataset_condition6 = pd.read_csv(
        "MlData/content/family.csv",
        names=["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"],
    )
    (
        kmeans_model_condition6,
        scaler_f_condition6,
        scaler_a_condition6,
    ) = train_kmeans_model(dataset_condition6)
    yes = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    no = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition6, scaler_f_condition6, scaler_a_condition6
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition6, scaler_f_condition6, scaler_a_condition6
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition6, scaler_f_condition6, scaler_a_condition6
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# anger issues
def anger(user_response):
    dataset_condition7 = pd.read_csv(
        "MlData/content/anger.csv", names=["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
    )
    (
        kmeans_model_condition7,
        scaler_f_condition7,
        scaler_a_condition7,
    ) = train_kmeans_model(dataset_condition7)
    yes = [2, 1, 4, 1, 1, 1, 1, 1]
    no = [0, 0, 0, 0, 0, 0, 0, 0]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition7, scaler_f_condition7, scaler_a_condition7
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition7, scaler_f_condition7, scaler_a_condition7
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition7, scaler_f_condition7, scaler_a_condition7
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition:
        return "need a counselor"
    else:
        return "can have a counselor"


# suicide
def suicide(user_response):
    s = sum(user_response) - user_response[1]
    f = user_response[1] >= 2 and s >= 5
    dataset_condition8 = pd.read_csv(
        "MlData/content/sucide.csv", names=["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
    )
    (
        kmeans_model_condition8,
        scaler_f_condition8,
        scaler_a_condition8,
    ) = train_kmeans_model(dataset_condition8)
    yes = [1, 3, 1, 1, 1, 1, 1, 1]
    no = [0, 0, 0, 0, 0, 0, 0, 0]
    counselor_condition = predict_counselor_needed(
        user_response, kmeans_model_condition8, scaler_f_condition8, scaler_a_condition8
    )
    yes_condition = predict_counselor_needed(
        yes, kmeans_model_condition8, scaler_f_condition8, scaler_a_condition8
    )
    no_condition = predict_counselor_needed(
        no, kmeans_model_condition8, scaler_f_condition8, scaler_a_condition8
    )

    # Check if the user needs a counselor based on the cluster
    if counselor_condition == no_condition:
        return "don't not need a counselor"
    elif counselor_condition == yes_condition or f:
        return "need a counselor"
    else:
        return "can have a counselor"


def switch_case(addictionType, user_response):
    res = ""
    if addictionType == "alcohol":
        res = alcohol(user_response)
    elif addictionType == "internet":
        res = internet(user_response)
    elif addictionType == "pornography":
        res = pornography(user_response)
    elif addictionType == "gaming":
        res = gaming(user_response)
    elif addictionType == "gambling":
        res = gambling(user_response)
    elif addictionType == "family":
        res = family(user_response)
    elif addictionType == "anger":
        res = anger(user_response)
    elif addictionType == "suicide":
        res = suicide(user_response)
    return res

ans = switch_case(addictionType, user_response)

print(ans)
