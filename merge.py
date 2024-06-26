import pandas as pd

# Load datasets
aug_train = pd.read_csv('aug_train.csv')
aug_test = pd.read_csv('aug_test.csv')
ibm_hiring = pd.read_csv('IBM_Hiring.csv')

# Select relevant columns from aug_train and aug_test
aug_train_relevant = aug_train[['enrollee_id', 'city', 'city_development_index', 'gender', 'relevent_experience',
                                'enrolled_university', 'education_level', 'major_discipline', 'experience', 
                                'company_size', 'company_type', 'last_new_job', 'training_hours', 'target']]

aug_test_relevant = aug_test[['enrollee_id', 'city', 'city_development_index', 'gender', 'relevent_experience',
                              'enrolled_university', 'education_level', 'major_discipline', 'experience', 
                              'company_size', 'company_type', 'last_new_job', 'training_hours']]

# Select relevant columns from IBM_Hiring
ibm_hiring_relevant = ibm_hiring[['Age', 'Attrition', 'BusinessTravel', 'Department', 'EducationField', 'Gender', 
                                  'JobRole', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime', 
                                  'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole', 
                                  'YearsSinceLastPromotion', 'YearsWithCurrManager']]

# Combine aug_train and aug_test datasets
combined_aug = pd.concat([aug_train_relevant, aug_test_relevant], ignore_index=True)

# Assuming enrollee_id is the key to merge with ibm_hiring_relevant (this may need to be adjusted based on actual keys)
# Merge combined_aug with ibm_hiring_relevant based on a common key
# Here we assume Gender, EducationField, and city are common columns for merging

# Align column names for merging purposes (if necessary)
ibm_hiring_relevant.rename(columns={'Gender': 'gender', 'EducationField': 'education_level'}, inplace=True)

# Merge the datasets
combined_data = pd.merge(combined_aug, ibm_hiring_relevant, on=['gender', 'education_level'], how='left')

# Save the combined dataset
combined_data.to_csv('Main_Dataset.csv', index=False)

print(combined_data.head())
