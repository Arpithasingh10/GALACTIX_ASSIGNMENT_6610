## Dataset Overview

The dataset used in this task is a custom HR Attrition dataset created to
simulate real-world employee records. Each row represents an employee,
and the dataset includes both numerical and categorical attributes such
as age, department, job role, income, work-life balance, and attrition
status. The dataset contains more than 50 records and reflects common
data quality issues typically found in HR systems.

---

## Data Issues Identified

### 1. Missing Values
Some records contain missing values in columns like MonthlyIncome,
WorkLifeBalance, Attrition, and JobRole. These missing values represent
realistic situations such as incomplete employee surveys, confidential
salary information, or data entry omissions.

### 2. Duplicate Records
Duplicate rows were found in the dataset, where the same employee record
appeared more than once. This can happen in real organizations due to
system synchronization issues or repeated data entry.

### 3. Mixed Data Types
The dataset contains mixed data types, including numerical values
(Age, MonthlyIncome, YearsAtCompany), categorical values (Department,
JobRole, Gender, Attrition), and missing values. This combination reflects
typical enterprise HR data.

### 4. Outliers
Certain records contain extreme values, such as very high MonthlyIncome,
large YearsAtCompany, and invalid WorkLifeBalance values. These outliers
may represent senior executives, long-tenured employees, or data entry
errors and were intentionally included to simulate real-world anomalies.

---

## Data Handling Approach

Missing values were handled using a statistical imputation approach.
Numerical columns were filled with their mean values, while categorical
columns were filled using the most frequently occurring value. This
approach helps retain maximum data while maintaining reasonable values.

Duplicate records were removed using a custom rule without hardcoding
column names, ensuring that the solution remains reusable for other
datasets.

Outliers were detected using the Interquartile Range (IQR) method for all
numeric columns. This method provides a simple and effective way to
identify extreme values without making assumptions about data
distribution.

Numeric columns were normalized using Min-Max scaling to bring values
into a common range. This helps prevent features with large values from
dominating analysis and improves downstream processing.

---

## Conclusion

This dataset demonstrates common real-world data quality challenges such
as missing values, duplicates, mixed data types, and outliers. The
implemented Python utilities were designed to automatically detect and
handle these issues in a reusable and scalable manner, without relying on
hardcoded column names.
