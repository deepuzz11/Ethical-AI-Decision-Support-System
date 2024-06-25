import pandas as pd

# Load datasets
aug_train = pd.read_csv('aug_train.csv')
aug_test = pd.read_csv('aug_test.csv')
ibm_hiring = pd.read_csv('IBM_Hiring.csv')


# Merge aug_train and aug_test based on common keys
combined_aug = pd.concat([aug_train, aug_test], ignore_index=True)

# Check columns in combined_aug and ibm_hiring to find common keys
print(combined_aug.columns)
print(ibm_hiring.columns)

# Example: Merge using 'city' and 'education_level' from combined_aug
# and 'Department' and 'EducationField' from ibm_hiring
combined_data = pd.merge(combined_aug, ibm_hiring, left_on=['city', 'education_level'], right_on=['Department', 'EducationField'], how='left')

# Perform additional preprocessing and feature engineering as needed
# Example: Calculate tenure
combined_data['tenure'] = combined_data['YearsAtCompany'] - combined_data['YearsInCurrentRole']

# Save or further analyze the combined dataset
combined_data.to_csv('Main_Dataset.csv', index=False)