# Database Management System & Analytics for Tax Services Business

<p align="center">
  <img src="imagenes/cover.jpg" />
</p>

---

## Contents
1. [Title](#title)
2. [Description](#description)1
3. [Project Structure](#project-structure)
6. [Directory Structure](#directory-structure)
3. [Installation](#installation)
4. [Introduction](#introduction)
5. [Objectives](#objectives)
7. [Data Description](#data-description)
    - RDMS (Relational Database Management System)
    - Metadata
    - Table and Field Details
9. [Methodology](#methodology)
10. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
11. [Predictive Modeling](#predictive-modeling)
12. [Results and Discussion](#results-and-discussion)
13. [Conclusions and Recommendations](#conclusions-and-recommendations)
14. [Contributions](#contributions)
15. [License](#license)
16. [Contact](#contact)

---

## Description
This project focuses on creating a database management system (DBMS) and a set of data analytics tools specifically designed to optimize tax services in the United States. Using advanced data science techniques, the project aims to enhance the efficiency and accuracy of the tax filing process, addressing the challenges faced by both taxpayers and tax service providers.

The project is built on a relational database that includes detailed tables on taxpayers, dependents, income, deductions, credits, payments, refunds, and amounts owed. A synthetic dataset is used to simulate real-world scenarios, enabling analysis and solution development without compromising data privacy.

In addition to creating the DBMS, the project includes exploratory data analysis (EDA) to identify key patterns and relationships in tax data. Based on these analyses, predictive models are developed to forecast future behaviors and optimize decision-making in tax management.

The project is modular and organized into several documents detailing system development, data analysis, and answers to specific business questions. A detailed guide for system installation and usage is also provided, facilitating its implementation in real-world environments.

## **Project Structure**
Description of the documents and directories included in the project.
- `README.md`: General project description.
- `1_Database and Analytics Framework Development.ipynb`: Project Development - Part 1.
- `2_Analysis_and_Business_Questions_Answers.ipynb`: Project Development - Part 2.
- `images/`: Directory containing images used in the documents.
- `tables/`: Directory containing data tables used in the analyses.
- `scripts/`: Directory containing scripts for project execution, including exploratory data analysis and predictive modeling.
- `data/`: Directory containing raw and processed datasets used for analysis and modeling.

## **Directory Structure**
<pre>
your_project/
│
├── README.md
├── 1_Laboratory_Creation_and_Database_Management_System.ipynb
├── 2_Analysis_and_Business_Questions_Answers.ipynb
├── images/
│   ├── cover.jpg
│   ├── taxpayer_table1.png
│   ├── taxpayer_table2.png
│   ├── taxpayer_table3.png
│   ├── taxpayer_table4.png
│   ├── taxpayer_table5.png
│   ├── dependents_table.png
│   ├── income_table.png
│   ├── deductions_table.png
│   ├── credits_table.png
│   ├── payments_table.png
│   ├── refunds_table.png
│   ├── amountowed_table.png
│
├── tables/
│   ├── taxpayers.csv
│   ├── dependents.csv
│   └── imcome.csv
│   └── deductions.csv
│   └── credits.csv
│   └── payments.csv
│   └── refunds.csv
│   └── amountowed.csv
├── scripts/
│   ├── main.py
│   ├── eda.py
│   └── modeling.py
│   └── train.py
│   └── test.py
│   └── ...
└── data/
    ├── raw_data.csv
    ├── cleaned_data.csv
    └── ...
</pre>

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aronds/tax_services_analytics.git
2. Install the dependencies:
`pip install -r requirements.txt
## Usage
python main.py
## **Introduction**

**Background**
The tax collection system in the United States is complex and presents multiple challenges for both taxpayers and tax services.

**Context and Relevance of the Problem**
This project aims to improve the efficiency and accuracy of the tax filing process using advanced data analysis techniques.

**Scope**
Optimization of tax services using data analysis and predictive modeling.

**Limitations**
Availability and quality of data.

## **Objectives**
* Create a controlled artificial ecosystem for problem simulation.
* Perform exploratory data analysis (EDA) to identify patterns and answer initial questions.
* Create specific datasets to address business questions.
* Develop predictive models based on EDA findings.
* Evaluate the effectiveness of different classification and regression models.

## **Data Description**
For practical purposes, we have created a synthetic dataset that allows us to skip previous processes such as data cleaning. This saves time, processing, and resources, enabling us to focus on analysis and solutions. In a real data environment, some of the necessary tasks would include:

- Data cleaning to remove inconsistencies and errors.
- Data validation to ensure accuracy.
- Data transformation to meet analysis requirements.
- Among other errors:
  * Inconsistencies in personal data:
    - Solution: Implement data validations when entering information, such as format checks for SSNs and addresses.
  * Duplicate records:
    - Solution: Use unique keys and referential integrity controls to prevent record duplication.
  * Incorrect tax calculations:
    - Solution: Develop verification algorithms to automatically recalculate taxes based on entered data and compare them with IRS calculations.
  * Data security:
    - Solution: Encrypt sensitive data and restrict access to personal data only to authorized personnel.
  * Errors in income and deduction categorization:
    - Solution: Create dropdown lists with predefined options for income and deduction types, minimizing categorization errors.
  * Data updates:
    - Solution: Implement a version control system to maintain a history of data changes and allow restoration of previous versions if necessary.

---
## RDMS (Relational Database Management System)
**Taxpayers and Dependents**

<table>
    <tr>
        <td>
            <pre>
+------------------------+
|  Taxpayers             |
+------------------------+
| taxpayer_id PK         |
| first_name             |
| last_name              |
| ssn                    |
| filing_status          |
| address                |
| city                   |
| state                  |
| zip_code               |
| email                  |
| phone_number           |
| employer_name          |
| employer_address       |
| job_title              |
| employment_start_date  |
| employment_end_date    |
| tax_return_id          |
| tax_year               |
| filing_date            |
| return_type            |
| income_source          |
| income_frequency       |
| taxable_amount         |
| deduction_category     |
| deduction_description  |
| credit_description     |
| credit_eligibility     |
| payment_date           |
| payment_method         |
| refund_date            |
| refund_reason          |
| amount_owed_due_date   |
| amount_owed_reason     |
| property_type          |
| property_value         |
| mortgage_interest_paid |
| taxpayer_occupation    |
| previous_year_income   |
| state_tax_refund       |
| local_tax_refund       |
| estimated_tax_payments_made |
| tax_liability          |
+------------------------+
            </pre>
        </td>
        <td>
            <pre>
+----------------------+
|  Dependents          |
+----------------------+
| taxpayer_id FK       |
| dependent_id PK      |
| first_name           |
| last_name            |
| ssn                  |
| relationship         |
| qualifies_for_credit |
+----------------------+
            </pre>
        </td>
    </tr>
</table>

---

**Income and Deductions**

<table>
    <tr>
        <td>
            <pre>
+---------------+
|   Income      |
+---------------+
| IncomeID PK   |
| TaxpayerID FK |
| IncomeType    |
| Amount        |
+---------------+
            </pre>
        </td>
        <td>
            <pre>
+-----------------+
| Deductions      |
+-----------------+
| TaxpayerID FK   |
| DeductionID PK  |
| DeductionType   |
| Amount          |
+-----------------+
            </pre>
        </td>
    </tr>
</table>

---

**Credits and Payments**

<table>
    <tr>
        <td>
            <pre>
+---------------+
|   Credits     |
+---------------+
| CreditID PK   |
| TaxpayerID FK |
| CreditType    |
| Amount        |
+---------------+
            </pre>
        </td>
        <td>
            <pre>
+-----------------+
| Payments        |
+-----------------+
| TaxpayerID FK   |
| PaymentID PK    |
| PaymentType     |
| Amount          |
+-----------------+
            </pre>
        </td>
    </tr>
</table>

---

**Refunds and Amounts Owed**

<table>
    <tr>
        <td>
            <pre>
+---------------+
|  Refunds      |
+---------------+
| RefundID PK   |
| TaxpayerID FK |
| RefundAmount  |
+---------------+
            </pre>
        </td>
        <td>
            <pre>
+-----------------+
| AmountsOwed     |
+-----------------+
| TaxpayerID FK   |
| AmountOwedID PK |
| Amount          |
+-----------------+
            </pre>
        </td>
    </tr>
</table>

## Metadata
**System Summary**
- **Number of Tables**: 8
- **Total Columns**: 68
- **Estimated Total Rows (with synthetic data)**: 1000 per table (adjustable as needed)

## Table and Field Details

#### Table: Taxpayers
**Description**: Stores basic information about taxpayers.

**Columns**: 42
- **taxpayer_id**: `INT` (Primary Key) - Unique identifier for the taxpayer.
- **first_name**: `VARCHAR(50)` - Taxpayer's first name.
- **last_name**: `VARCHAR(50)` - Taxpayer's last name.
- **ssn**: `CHAR(11)` - Social Security Number of the taxpayer.
- **filing_status**: `VARCHAR(50)` - Filing status (e.g., Single, Married Filing Jointly).
- **address**: `VARCHAR(100)` - Taxpayer's address.
- **city**: `VARCHAR(50)` - Taxpayer's city.
- **state**: `CHAR(2)` - Taxpayer's state.
- **zip_code**: `CHAR(5)` - Taxpayer's postal code.
- **email**: `VARCHAR(100)` - Taxpayer's email.
- **phone_number**: `VARCHAR(15)` - Taxpayer's phone number.
- **employer_name**: `VARCHAR(100)` - Employer's name.
- **employer_address**: `VARCHAR(100)` - Employer's address.
- **job_title**: `VARCHAR(50)` - Taxpayer's job title.
- **employment_start_date**: `DATE` - Employment start date.
- **employment_end_date**: `DATE` - Employment end date.
- **tax_return_id**: `INT` - Tax return identifier.
- **tax_year**: `INT` - Fiscal year.
- **filing_date**: `DATE` - Filing date.
- **return_type**: `VARCHAR(50)` - Return type (e.g., Individual, Joint, Amended).
- **income_source**: `VARCHAR(50)` - Source of income.
- **income_frequency**: `VARCHAR(10)` - Income frequency (Monthly, Annual).
- **taxable_amount**: `DECIMAL(10, 2)` - Taxable amount.
- **deduction_category**: `VARCHAR(50)` - Deduction category.
- **deduction_description**: `VARCHAR(100)` - Description of the deduction.
- **credit_description**: `VARCHAR(100)` - Description of the credit.
- **credit_eligibility**: `VARCHAR(20)` - Credit eligibility (Eligible, Not Eligible).
- **payment_date**: `DATE` - Payment date.
- **payment_method**: `VARCHAR(50)` - Payment method.
- **refund_date**: `DATE` - Refund date.
- **refund_reason**: `VARCHAR(50)` - Reason for the refund.
- **amount_owed_due_date**: `DATE` - Due date for amount owed.
- **amount_owed_reason**: `VARCHAR(50)` - Reason for the amount owed.
- **property_type**: `VARCHAR(50)` - Type of property.
- **property_value**: `DECIMAL(10, 2)` - Property value.
- **mortgage_interest_paid**: `DECIMAL(10, 2)` - Mortgage interest paid.
- **taxpayer_occupation**: `VARCHAR(50)` - Taxpayer's occupation.
- **previous_year_income**: `DECIMAL(10, 2)` - Previous year's income.
- **state_tax_refund**: `DECIMAL(10, 2)` - State tax refund.
- **local_tax_refund**: `DECIMAL(10, 2)` - Local tax refund.
- **estimated_tax_payments_made**: `DECIMAL(10, 2)` - Estimated tax payments made.
- **tax_liability**: `DECIMAL(10, 2)` - Tax liability.
![](imagenes/taxpayer_table1.png)
![](imagenes/taxpayer_table2.png)
![](imagenes/taxpayer_table3.png)
![](imagenes/taxpayer_table4.png)
![](imagenes/taxpayer_table5.png)
---
#### Table: Dependents
**Description**: Stores information about taxpayers' dependents.

**Columns**: 7
- **dependent_id**: `INT` (Primary Key) - Unique identifier for the dependent.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **first_name**: `VARCHAR(50)` - Dependent's first name.
- **last_name**: `VARCHAR(50)` - Dependent's last name.
- **ssn**: `CHAR(11)` - Social Security Number of the dependent.
- **relationship**: `VARCHAR(50)` - Relationship of the dependent to the taxpayer.
- **qualifies_for_credit**: `BOOLEAN` - Indicates if the dependent qualifies for tax credits.
![](imagenes/dependents_table.png)
---
#### Table: Income
**Description**: Stores information about taxpayers' income.

**Columns**: 4
- **income_id**: `INT` (Primary Key) - Unique identifier for the income.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **income_type**: `VARCHAR(50)` - Type of income.
- **amount**: `DECIMAL(10, 2)` - Amount of income.
![](imagenes/income_table.png)
---
#### Table: Deductions
**Description**: Stores information about taxpayers' deductions.

**Columns**: 4
- **deduction_id**: `INT` (Primary Key) - Unique identifier for the deduction.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **deduction_type**: `VARCHAR(50)` - Type of deduction.
- **amount**: `DECIMAL(10, 2)` - Amount of deduction.
![](imagenes/deductions_table.png)
---
#### Table: Credits
**Description**: Stores information about taxpayers' tax credits.

**Columns**: 4
- **credit_id**: `INT` (Primary Key) - Unique identifier for the credit.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **credit_type**: `VARCHAR(50)` - Type of credit.
- **amount**: `DECIMAL(10, 2)` - Amount of credit.
![](imagenes/credits_table.png)
---
#### Table: Payments
**Description**: Stores information about payments made by taxpayers.

**Columns**: 4
- **payment_id**: `INT` (Primary Key) - Unique identifier for the payment.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **payment_type**: `VARCHAR(50)` - Type of payment.
- **amount**: `DECIMAL(10, 2)` - Amount of payment.
![](imagenes/payments_table.png)

#### Table: Refunds
**Description**: Stores information about refunds received by taxpayers.

**Columns**: 3
- **refund_id**: `INT` (Primary Key) - Unique identifier for the refund.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **refund_amount**: `DECIMAL(10, 2)` - Amount of the refund.
![](imagenes/refunds_table.png)
---
#### Table: Amounts Owed
**Description**: Stores information about amounts owed by taxpayers.

**Columns**: 3
- **amount_owed_id**: `INT` (Primary Key) - Unique identifier for the amount owed.
- **taxpayer_id**: `INT` (Foreign Key) - Identifier of the associated taxpayer.
- **amount**: `DECIMAL(10, 2)` - Amount owed.
![](imagenes/amountowed_table.png)
---
## **Methodology**
   - Description of the methods and techniques used in this phase of the project.
## **Exploratory Data Analysis (EDA)**
   - Description and visualization of the data.
   - Types of deductions and credits.
   - Income distribution charts.
   - Heatmaps to identify correlations.
## **Initial Results**
   - Preliminary findings from the analysis.
   - Identification of income patterns by state.
   - Correlations between types of deductions and credits.
## **Predictive Modeling**
   - Description of the models used, their training, and evaluation.
## **Validation and Evaluation**
   - Results of cross-validation and evaluation metrics.
## **Results and Discussion**
   - Interpretation of the obtained results.
   - Results of cross-validation and evaluation metrics.
   - Comparison with previous studies.
   - Implications of the findings.
## **Conclusions and Recommendations**
   - Main conclusions of the project:
   - Recommendations for practical implementation and future work:
   This project creates a solid foundation for managing and analyzing tax services data, using a structured approach and synthetic data to ensure privacy and information security. The system allows for the identification and resolution of common issues in the tax services industry, providing a robust platform for ongoing analysis and improvements.
   
## **Contributions**
   To contribute, please open an issue or submit a pull request.
## **License**
   This project is licensed under the MIT License.
## **Contact**
   For more information, contact Arom Antinao at coregroup.proyect@gmail.com
