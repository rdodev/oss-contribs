from github3 import GitHub, login
import xlsxwriter
from lib.functions import populate_sheet

u = input('Please enter your github username: ')

#you can obtain a personal api token for your github account. Make sure it's read access only where applicable.
token=''
gh = login(token=token)

print('Retrieving all repositories by: ' + u + '\n')
reps = gh.repositories_by(username=u)
reps = filter(lambda x: x.archived is False, reps)

print('Preparing the spreadsheet...')

# Prep OSS Contribution Spreadsheet
file_name = 'Own-Time-Contributions.xlsx'
wkbook = xlsxwriter.Workbook(file_name)
populate_sheet(reps, wkbook)
wkbook.close()

print('File named {} has been saved in the current directory.'.format(file_name))