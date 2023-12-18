import requests

url = 'http://localhost:9695/predict'

customer = {'age': 27,
 'income': 52584,
 'loanamount': 60095,
 'creditscore': 767,
 'monthsemployed': 110,
 'numcreditlines': 3,
 'interestrate': 2.1,
 'loanterm': 60,
 'dtiratio': 0.9,
 'education': 0,
 'employmenttype': 0,
 'maritalstatus': 1,
 'hasmortgage': 0,
 'hasdependents': 1,
 'loanpurpose': 3,
 'hascosigner': 0}

response = requests.post(url, json=customer).json()

print(customer)
print(response)

if response['Defaulted'] == True:
    print('Customer will default the loan')
else:
    print('Great news! Customer will not default the loan')