#immport libraries
import requests
import csv,os,datetime,pprint

#User Input
#Api = raw_input("Enter your API Key: ")
Keywords = raw_input('Search keywords separated by comma. These keywords will be used to find authors that match all these keywords. Matching is done on First name, Last Name, Email, Publication name, social media accounts. Enter Keywords: ')
#Query Parameters for API Call
query_params = { 'ClientKey': 'P81UUQrjaIK2QL2/PScQ2GK2AjII1dKSG2vRsiih7v3ANm1XhabJifBzS81Eqqe1RZPyQEi6lpR3O/arGjYEtg==',
                 'SearchKeywords': Keywords,
                 'format': 'csv'
                 }

endpoint = 'http://api.mblast.com/search/authors'

#Save .CSV Response
with open('output.csv', 'wb') as handle:
    response = requests.get(endpoint, params =query_params, stream=True)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
print("Complete")
