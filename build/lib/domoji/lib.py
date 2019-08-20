import requests
import json
import sys
from terminaltables import AsciiTable
from crayons import *

def get_emoji_domain(query):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get('https://xn--i-7iq.ws/emojidomain/{}?format=json'.format(query), headers=headers)
    return response.json()

def convert_json_to_table(response):
    table_data = [
        ['Available', 'ASCII Domain', 'Price']
    ]
    ascii_domain = response['theAsciiDomain']
    if response['available'] == False:
        table_data.append([
            str(red('False', bold=True)), ascii_domain, 'Check GoDaddy.com'
        ])
        table = AsciiTable(table_data, 'Results')
        return table.table
    else:
        for result in response['results']:
            if result['available']:
                available = green('True', bold=True)
            else:
                available = red('False', bold=True)
            table_data.append([
                str(available), result['domain'], result.get('price') if result.get('price') is not None else 'null'
            ])
        table = AsciiTable(table_data, 'Results')
        return table.table

def menu():
    sys.stdout.flush()
    print(blue('\nDomoji v1.1\nCreated by @maxbridgland\n', bold=True))
    print(white('Easily find emoji domains from the command line. Uses i❤️.ws API for domains.', bold=True))
    print(white('Domains may be available for other tLDs like .com, .org, .co, etc. Check GoDaddy.com for full results.', bold=True))
    while True:
        cont = True
        print(green('\nPlease enter the domain with emojis you\'d like:', bold=True))
        query = input('\n~ ')
        print(yellow('\nSearching for available domains with: {}'.format(query), bold=True))
        response = get_emoji_domain(query)
        print(convert_json_to_table(response))
        while True:
            print('\nWould you like to search for another domain? [Y\\n]')
            answer = input('\n~ ').lower()
            if answer == 'y':
                break
            elif answer == 'n':
                cont = False
                break
            else:
                print('\nUnknown Choice')
        if not cont:
            break