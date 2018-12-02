#!/usr/bin/python3
# trackPackage.py
#doesn't work need to use api

from bs4 import BeautifulSoup
import argparse
import requests

parser = argparse.ArgumentParser(description='Learn latest status of postal package.')
parser.add_argument('package', metavar='AB123456789CD', type=str, help='Tracking number of package')

args = parser.parse_args()

res = requests.get(f'https://tools.usps.com/go/TrackConfirmAction?tLabels={args.package}', headers={'User-agent': 'Mozilla/5.0'})
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
status = soup.select('div.expected_delivery p')
print(status[0].getText())