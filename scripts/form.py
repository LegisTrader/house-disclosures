import requests
from bs4 import BeautifulSoup
'''
Testing beautful soup to submit forms, need to grease out this function so i can use it to iterate through the full list of reps
'''
def submit_form(first_name, filing_year, doc_type, state):
    url = 'https://disclosures-clerk.house.gov/FinancialDisclosure/FinancialDisclosure'
    
    # Send a GET request to fetch the form page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the form on the page
    form = soup.find('form', {'action': '/FinancialDisclosure/FinancialDisclosure'})
    
    # Extract the necessary form fields
    last_name_field = form.find('input', {'name': 'LastName'})
    filing_year_field = form.find('input', {'name': 'FilingYear'})
    doc_type_field = form.find('input', {'name': 'DocType'})
    state_field = form.find('select', {'name': 'StateCD'})
    
    # Set the form field values
    last_name_field['value'] = last_name
    filing_year_field['value'] = filing_year
    doc_type_field['value'] = doc_type
    
    # Find the selected state option
    state_option = state_field.find('option', string=state)
    state_option['selected'] = 'selected'
    
    # Create a dictionary with the form data
    form_data = {
        last_name_field['name']: last_name_field['value'],
        filing_year_field['name']: filing_year_field['value'],
        doc_type_field['name']: doc_type_field['value'],
        state_field['name']: state_option['value']
    }
    
    # Submit the form
    submit_url = url + form['action']
    response = requests.post(submit_url, data=form_data)
    
    return response.text

# Example data for iteration
data = [
    {'last_name': 'Pelosi', 'filing_year': '2022', 'doc_type': 'P', 'state': 'Alabama'},
    {'last_name': 'Warnock', 'filing_year': '2021', 'doc_type': 'C', 'state': 'California'},
    {'last_name': 'Cortez', 'filing_year': '2023', 'doc_type': 'P', 'state': 'New York'}
]

# Iterate through the data and submit the form for each set of values
for item in data:
    result = submit_form(item['last_name'], item['filing_year'], item['doc_type'], item['state'])
    print(result)
    print('---')