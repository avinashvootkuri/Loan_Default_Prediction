### Loan Default Prediction (CAPSTONE PROJECT FOR MLZOOMCAMP 2023)
## Project for MLZoomcamp course Capstone-1 Loan default prediction

## Problem Statement:
One of the primary objectives of companies with financial loan services is to decrease payment defaults and ensure that individuals are paying back their loans as expected. 
Dataset consists of target variable (default 0/1) to identify if a loan with default or the payer has payed back as expetected. We will be using machince learning techniques to predict 
if an loanid is defaulted or not. Machine learning make help us with learning from past applications data and make decision in realtime which helps with reduce human effort and increases efficiency

## Dataset:
Dataset is obtained from Kaggle - https://www.kaggle.com/datasets/nikhil1e9/loan-default/data

Features
```
Index    Column_name                                Description
0       LoanID              A unique identifier for each loan.
1       Age                 The age of the borrower.
2       Income              The annual income of the borrower.
3       LoanAmount          The amount of money being borrowed.
4       CreditScore         The credit score of the borrower, indicating their creditworthiness.
5       MonthsEmployed      The number of months the borrower has been employed.
6       NumCreditLines      The number of credit lines the borrower has open.
7       InterestRate        The interest rate for the loan.
8       LoanTerm            The term length of the loan in months.
9       DTIRatio            The Debt-to-Income ratio, indicating the borrower's debt compared to their income.
10      Education           The highest level of education attained by the borrower (PhD, Master's, Bachelor's, High School).
11      EmploymentType      The type of employment status of the borrower (Full-time, Part-time, Self-employed, Unemployed).
12      MaritalStatus       The marital status of the borrower (Single, Married, Divorced).
13      HasMortgage         Whether the borrower has a mortgage (Yes or No).
14      HasDependents       Whether the borrower has dependents (Yes or No).
15      LoanPurpose         The purpose of the loan (Home, Auto, Education, Business, Other).
16      HasCoSigner         Whether the loan has a co-signer (Yes or No).
17      Default             The binary target variable indicating whether the loan defaulted (1) or not (0).
```
## Solution:
Loan default prediction is classification problem. We will exploring the various classification algorithms Logistic Regression, Decision Tree Classifier, Random Forest Classifier and Xgboost Classifier. 
Based on the evaluation metrics we will show the best performing model. 

# Running Locally:

## Prerequities: 
please check if you have python version 3.9, if not download it from the link here - https://www.python.org/downloads/release/python-390/

To run the project locally, please follow the below steps:
1. Clone the repo.
2. Install pipenv using the command  
    ```
    1. pip install pipenv
    ```
3. Run the below command, inorder to install the required packages:
    ```
   pipenv install
    ```
4. Run the below command, to activate the virtual env created with the above command:
   ```
   pipenv shell
   ```
5. Run the train.py for local reproducability.
   ``` 
    python3 train.py
    ```
   You can also used the same virtual environment to run the notebook.ipynb file.

   
# Running on Docker 
## Getting Started:
To run the project, please follow the below steps:

## Prerequisties:
- Docker: you will need to have Docker installed on your computer. 

## Installation:
1. Clone the repo.

2. Build the Docker image using the follwing command:
    ```
    docker build -t loandefault-predict .
    ```
3. Run Docker container using the below command:
    ```
    docker run -it --rm -p 9695:9695 loandefault-predict
    ```
4. Once the above statement is executed, you will be noticing, 
   starting guicorn and Listeing at: http://0.0.0.0:9695


## Prediction Service:
Once docker is up and running, you can start using the model by running the below command in a new terminal window or new tab: 
    ```
    python predict-docker.py
    ```

If you like my work above, please feel free to star it. Thank you!!
