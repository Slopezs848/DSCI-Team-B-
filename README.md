# DSCI-Team-B-

**Modeling for Autistic Spectrum Disorder Screening Data for Children Dataset**


**Project Overview:** This project aims to develop a machine learning-based application for early autism detection in children, using a dataset introduced by Fadi Fayez Thabtah from the Department of Digital Technology at the Manukau Institute of Technology. The application leverages behavioral and demographic features to accurately predict autism spectrum disorder (ASD) traits, supporting timely intervention and improved long term outcomes. 


**Data Set Description:** This dataset contains information related to the screening of autistic spectrum disorder (ASD) in children with 292 instances and 21 attributes, including 10 behavioural scores and other demographic information. . It includes various demographic and behavioral features that are used to identify potential ASD cases.


**Behavioral Scores include:**

- **A1_Score:** Integer - The answer code for the first question in the AQ-10-Child questionnaire (0 or 1).

- **A2_Score:** Integer - The answer code for the second question in the AQ-10-Child questionnaire (0 or 1).

- **A3_Score:** Integer - The answer code for the third question in the AQ-10-Child questionnaire (0 or 1).

- **A4_Score:** Integer - The answer code for the fourth question in the AQ-10-Child questionnaire (0 or 1).

- **A5_Score:** Integer - The answer code for the fifth question in the AQ-10-Child questionnaire (0 or 1).

- **A6_Score:** Integer - The answer code for the sixth question in the AQ-10-Child questionnaire (0 or 1).

- **A7_Score:** Integer - The answer code for the seventh question in the AQ-10-Child questionnaire (0 or 1).

- **A8_Score:** Integer - The answer code for the eighth question in the AQ-10-Child questionnaire (0 or 1).

- **A9_Score:** Integer - The answer code for the ninth question in the AQ-10-Child questionnaire (0 or 1).

- **A10_Score:** Integer - The answer code for the tenth question in the AQ-10-Child questionnaire (0 or 1).


**Demographic Information includes:**

- **age:** Integer - Age of the individual in years.

- **gender:** Categorical - Gender of the individual (Male or Female).

- **ethnicity:** Categorical - List of common ethnicities in text format.

- **jaundice:** Binary - Whether the individual was born with jaundice (yes or no).

- **autism:** Binary - Whether any immediate family member has a pervasive developmental disorder (PDD) (yes or no).

- **country_of_res:** Categorical - List of countries in text format.

- **used_app_before:** Binary - Whether the user has used a screening app before (yes or no).

- **result:** Integer - The final score obtained based on the scoring algorithm of the screening method used.

- **age_desc:** Categorical - Description of the age category.

- **relation:** Categorical - The person completing the test (Parent, self, caregiver, medical staff, clinician, etc.).

- **Target Variables, class:** Binary - The target variable indicating whether the individual is classified as having ASD (yes or no).

**Source:** Thabtah, F. (2017). Autistic Spectrum Disorder Screening Data for Children [Dataset]. UCI Machine Learning Repository. Retrieved from https://doi.org/10.24432/C5659W.


**Machine Learning Models Used:**

- **Support Vector Machine (SVM)** - Effective for high-dimensional data with clear decision boundaries

- **XGBoost** - High-speed, scalable gradient boosting algorithm for complex data patterns

- **Logistic Regression** - Simple, interpretable baseline model for binary classification


project_structure/
│
├── Code/                  
│   ├── Data Preparation/               
|   ├── Exploratory Data Analysis/
│   └── Models/         
│
├── Data/             
|   ├── Untouched Data/             
|   ├── Cleaned Data/
|   ├── Data Encoded/
│   └── Feature Importance/ 
│
├── Documentation_and_Presentations/                 
│   ├── Autism Screening Child Data Description/  
│   ├── EDA Presentation/   
│   ├── Final Capstone Presentation/ 
│   ├── Final EDA/   
│   ├── Final ML/ 
│   ├── Project Proposal/ 
|
├── Literature_Survey/               
│             
│
├── UI_Photos/                
│
└── README.md             

**Installation**
To run this application follow these steps:

1. Clone the repository
```bash
git clone https://github.com/Slopezs848/DSCI-Team-B-
```
2. Installed required libraries 
```bash
pip install -r requirements.txt
```
3. Run the streamlit app: 
```bash
streamlit run streamlit_app.py
```
4. Choose your input and hit the predict button. 


**The structure of this repository is designed to provide a clear and organized view of the project's data preparation, model development, and user interface stages. This layout makes it easy for users to navigate through the different phases of the project, whether they are interested in the raw data, code implementation, or the deployed application. Each section is clearly labeled, allowing users to quickly locate the specific component or stage they want to explore.**
