import pandas as pd
from faker import Faker

fake = Faker()
num_records = 1000

# Main function that executes the other functions for creating each table
def main():
    taxpayers()
    dependents()
    income()
    deductions()
    credits()
    payments()
    refunds()
    amount_owed()
    print("All CSV files have been saved successfully.")
    
def taxpayers():
    # Adjust the settings to display all columns
    pd.set_option('display.max_columns', None)
    # Generate data for Taxpayers
    taxpayers_data = {
        'taxpayer_id': [i for i in range(1, num_records + 1)],
        'first_name': [fake.first_name() for _ in range(num_records)],
        'last_name': [fake.last_name() for _ in range(num_records)],
        'birth_date' : [fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(num_records)],
        'ssn': [fake.ssn() for _ in range(num_records)],
        'filing_status': [fake.random_element(elements=(
            'Single', 'Married Filing Jointly', 'Married Filing Separately', 
            'Head of Household', 'Qualifying Widow(er) with Dependent Child')) for _ in range(num_records)],
        'address': [fake.street_address() for _ in range(num_records)],
        'city': [fake.city() for _ in range(num_records)],
        'state': [fake.state_abbr() for _ in range(num_records)],
        'zip_code': [fake.zipcode() for _ in range(num_records)],
        'email': [fake.email() for _ in range(num_records)],
        'phone_number': [fake.phone_number() for _ in range(num_records)],
        'employer_name': [fake.company() for _ in range(num_records)],
        'employer_address': [fake.address() for _ in range(num_records)],
        'job_title': [fake.job() for _ in range(num_records)],
        'employment_start_date': [fake.date_this_decade() for _ in range(num_records)],
        'employment_end_date': [fake.date_this_decade() if fake.boolean() else '' for _ in range(num_records)],
        'tax_return_id': [i for i in range(1, num_records + 1)],
        'tax_year': [fake.year() for _ in range(num_records)],
        'filing_date': [fake.date_this_year() for _ in range(num_records)],
        'return_type': [fake.random_element(elements=(
            'Individual', 'Joint', 'Amended', 'Head of Household', 
            'Qualifying Widow(er) with Dependent Child', 
            'Married Filing Separately', 'Estate', 'Trust', 
            'Non-Resident Alien', 'Resident Alien', 
            'Partial Year Resident', 'Final Return', 'Business', 
            'Partnership', 'Corporation')) for _ in range(num_records)],
        'income_source': [fake.random_element(elements=(
            'Salary', 'Dividends', 'Rental', 'Business', 'Other', 'Interest Income', 
            'Capital Gains', 'Pensions', 'Social Security', 'Royalties', 
            'Unemployment Benefits', 'Alimony', 'Annuities', 'Freelance Income', 
            'Grants', 'Investment Income', 'Licensing Fees', 'Consulting Fees', 
            'Prize Winnings', 'Scholarships', 'Inheritance', 
            'Rent from Personal Property')) for _ in range(num_records)],
        'income_frequency': [fake.random_element(elements=('Monthly', 'Yearly')) for _ in range(num_records)],
        'taxable_amount': [round(fake.random_number(digits=5), 2) for _ in range(num_records)],
        'deduction_category': [fake.random_element(elements=(
            'Education','Health', 'Mortgage',
            'Other','Charitable Contributions','State Taxes Paid',
            'Local Taxes Paid','Business Expenses','Medical Expenses',
            'Investment Expenses','Home Office','Retirement Contributions',
            'Childcare Expenses','Casualty and Theft Losses','Moving Expenses')) for _ in range(num_records)],
        'deduction_description': [fake.text(max_nb_chars=50) for _ in range(num_records)],
        'credit_description': [fake.text(max_nb_chars=50) for _ in range(num_records)],
        'credit_eligibility': [fake.random_element(elements=('Eligible', 'Not Eligible')) for _ in range(num_records)],
        'payment_date': [fake.date_this_year() for _ in range(num_records)],
        'payment_method': [fake.random_element(elements=(
            'Bank Transfer', 'Check', 'Credit Card', 'Debit Card',
            'Cash', 'Electronic Funds Transfer (EFT)', 'PayPal',
            'Wire Transfer', 'Money Order', 'Cryptocurrency',
            'Direct Deposit', 'Digital Wallet', 'Apple Pay',
            'Google Pay', 'Gift Card')) for _ in range(num_records)],
        'refund_date': [fake.date_this_year() for _ in range(num_records)],
        'refund_reason': [fake.random_element(elements=(
            'Overpayment', 'Adjustment', 'Error', 'Refundable Credit',
            'Incorrect Filing', 'Duplicate Payment', 'Penalty Adjustment',
            'Account Correction', 'Payment Error', 'Miscellaneous')) for _ in range(num_records)],
        'amount_owed_due_date': [fake.date_this_year() for _ in range(num_records)],
        'amount_owed_reason': [fake.random_element(elements=(
            'Underpayment', 'Penalty', 'Interest', 'Late Filing',
            'Late Payment', 'Error in Return', 'Additional Tax Liability',
            'Amended Return', 'Adjustment', 'Other')) for _ in range(num_records)],
        'property_type': [fake.random_element(elements=(
            'Home', 'Land', 'Commercial', 'Rental', 'Vacation',
            'Investment', 'Agricultural', 'Industrial', 'Multi-family', 'Other')) for _ in range(num_records)],
        'property_value': [round(fake.random_number(digits=6), 2) for _ in range(num_records)],
        'mortgage_interest_paid': [round(fake.random_number(digits=5), 2) for _ in range(num_records)],
        'taxpayer_occupation': [fake.job() for _ in range(num_records)],
        'previous_year_income': [round(fake.random_number(digits=5), 2) for _ in range(num_records)],
        'state_tax_refund': [round(fake.random_number(digits=4), 2) for _ in range(num_records)],
        'local_tax_refund': [round(fake.random_number(digits=4), 2) for _ in range(num_records)],
        'estimated_tax_payments_made': [round(fake.random_number(digits=4), 2) for _ in range(num_records)],
        'tax_liability': [round(fake.random_number(digits=5), 2) for _ in range(num_records)]
    }
    taxpayers_df = pd.DataFrame(taxpayers_data)
    taxpayers_df.to_csv('taxpayers.csv')

def dependents():
    # Generate data for Dependents
    dependents_data = {
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records // 2)],
    'dependent_id': [i for i in range(1, (num_records // 2) + 1)],
    'first_name': [fake.first_name() for _ in range(num_records // 2)],
    'last_name': [fake.last_name() for _ in range(num_records // 2)],
    'ssn': [fake.ssn() for _ in range(num_records // 2)],
    'relationship': [fake.random_element(elements=(
        'Child', 'Spouse', 'Relative', 'Parent', 'Sibling',
        'Grandchild', 'Grandparent', 'Stepchild', 'Foster Child',
        'Dependent Relative', 'Other')) for _ in range(num_records // 2)],
    'qualifies_for_credit': [fake.boolean() for _ in range(num_records // 2)]
    }
    dependents_df = pd.DataFrame(dependents_data)
    # Save the DataFrame to CSV files
    dependents_df.to_csv('dependents.csv', index=False)

def income():
    # Generate data for Income
    income_data = {
    'income_id': [i for i in range(1, num_records + 1)],
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records)],
    'income_type': [fake.random_element(elements=(
        'Salary', 'Investment', 'Rental', 'Business', 'Other',
        'Dividends', 'Interest', 'Capital Gains', 'Pensions', 'Royalties',
        'Freelance', 'Consulting', 'Alimony', 'Grants', 'Royalties')) for _ in range(num_records)],
        'amount': [round(fake.random_number(digits=5), 2) for _ in range(num_records)]
    }
    income_df = pd.DataFrame(income_data)
    # Save the DataFrame to CSV files
    income_df.to_csv('income.csv', index=False)

def deductions():
    # Generate data for Deductions
    deductions_data = {
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records)],
    'deduction_id': [i for i in range(1, num_records + 1)],
    'deduction_type': [fake.random_element(elements=(
        'Charitable Donations', 'Mortgage Interest', 'Medical Expenses',
        'State and Local Taxes', 'Retirement Contributions', 'Education Expenses',
        'Home Office', 'Business Expenses', 'Investment Expenses', 'Casualty Loss',
        'Moving Expenses', 'Childcare Expenses', 'Student Loan Interest',
        'Health Savings Account', 'Medical Expenses', 'Other')) for _ in range(num_records)],
    'amount': [round(fake.random_number(digits=4), 2) for _ in range(num_records)],
    'description': [fake.text(max_nb_chars=50) for _ in range(num_records)]
    }
    deductions_df = pd.DataFrame(deductions_data)
    # Save the DataFrame to CSV files
    deductions_df.to_csv('deductions.csv', index=False)

def credits():
    # Generate data for Credits
    credits_data = {
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records)],
    'credit_id': [i for i in range(1, num_records + 1)],
    'credit_type': [fake.random_element(elements=(
        'Child Tax Credit', 'Education Credit', 'Retirement Savings Credit',
        'Earned Income Credit', 'Foreign Tax Credit', 'Adoption Credit',
        'Energy Efficient Home Credit', 'Electric Vehicle Credit',
        'American Opportunity Credit', 'Lifetime Learning Credit',
        'Premium Tax Credit', 'Residential Energy Credit',
        'Mortgage Interest Credit', 'Health Coverage Tax Credit',
        'Credit for the Elderly or Disabled', 'Other')) for _ in range(num_records)],
    'amount': [round(fake.random_number(digits=4), 2) for _ in range(num_records)],
    'eligibility': [fake.random_element(elements=('Eligible', 'Not Eligible')) for _ in range(num_records)],
    'description': [fake.text(max_nb_chars=50) for _ in range(num_records)]
    }
    credits_df = pd.DataFrame(credits_data)
    # Save the DataFrame to CSV files
    credits_df.to_csv('credits.csv', index=False)

def payments():
    # Generate data for Payments
    payments_data = {
    'payment_id': [i for i in range(1, num_records + 1)],
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records)],
    'payment_date': [fake.date_this_year() for _ in range(num_records)],
    'payment_amount': [round(fake.random_number(digits=5), 2) for _ in range(num_records)],
    'payment_method': [fake.random_element(elements=(
        'Bank Transfer', 'Credit Card', 'Debit Card', 'Check',
        'Cash', 'Wire Transfer', 'EFT', 'PayPal', 'Other')) for _ in range(num_records)],
    'payment_description': [fake.text(max_nb_chars=50) for _ in range(num_records)]
    }
    payments_df = pd.DataFrame(payments_data)
    # Save the DataFrame to CSV files
    payments_df.to_csv('payments.csv', index=False)

def refunds():
    # Generate data for Refunds
    refunds_data = {
    'refund_id': [i for i in range(1, num_records + 1)],
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records)],
    'refund_date': [fake.date_this_year() for _ in range(num_records)],
    'refund_amount': [round(fake.random_number(digits=5), 2) for _ in range(num_records)],
    'refund_reason': [fake.random_element(elements=(
        'Overpayment', 'Adjustment', 'Error', 'Credit',
        'Amended Return', 'Duplicate Payment', 'Penalty Adjustment',
        'Account Correction', 'Payment Error', 'Miscellaneous')) for _ in range(num_records)],
    'refund_description': [fake.text(max_nb_chars=50) for _ in range(num_records)]
    }
    refunds_df = pd.DataFrame(refunds_data)
    # Save the DataFrame to CSV files
    refunds_df.to_csv('refunds.csv', index=False)

def amount_owed():
    # Generate data for Amount Owed
    amount_owed_data = {
    'owed_id': [i for i in range(1, num_records + 1)],
    'taxpayer_id': [fake.random_int(min=1, max=num_records) for _ in range(num_records)],
    'owed_date': [fake.date_this_year() for _ in range(num_records)],
    'owed_amount': [round(fake.random_number(digits=5), 2) for _ in range(num_records)],
    'owed_reason': [fake.random_element(elements=(
        'Underpayment', 'Penalty', 'Interest', 'Late Payment',
        'Late Filing', 'Amended Return', 'Other')) for _ in range(num_records)],
    'owed_description': [fake.text(max_nb_chars=50) for _ in range(num_records)]
    }
    amount_owed_df = pd.DataFrame(amount_owed_data)
    # Save the DataFrame to CSV files
    amount_owed_df.to_csv('amount_owed.csv', index=False)

if __name__ == "__main__":
    main()
