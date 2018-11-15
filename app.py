from flask import Flask, send_file
from github3 import GitHub, login
import xlsxwriter
import io
app = Flask(__name__)

@app.route('/<username>')
def spreadhseet(username):

    token = ''

    gh = login(token=token)

    #print('Retrieving all repositories by: ' + u + '\n')
    reps = gh.repositories_by(username=username)

    #print('Preparing the spreadsheet...')
    output = io.BytesIO()
    # Prep OSS Contribution Spreadsheet
    file_name = 'Own-Time-Contributions.xlsx'
    wkbook = xlsxwriter.Workbook(output, {'in_memory': True})
    sheet = wkbook.add_worksheet()

    # column width
    sheet.set_column("A:A", 20)
    sheet.set_column("B:B", 20)
    sheet.set_column("C:C", 20)
    sheet.set_column("D:D", 20)
    sheet.set_column("E:E", 20)
    sheet.set_column("E:E", 20)

    # Bold for headers

    bold = wkbook.add_format({'bold': True})

    # Header Titles

    vmwcontrib = '''
    Does contributing to the project fundamentally compete with an existing VMware product/project? (Yes/No/Maybe)
    '''
    otherparties = '''
    Are there other parties of interest? (Y/N, If Y then who?)
    '''

    sheet.write('A1', 'Project Name', bold)
    sheet.write('B1', 'Project Description', bold)
    sheet.write('C1', vmwcontrib, bold)
    sheet.write('D1', otherparties, bold)
    sheet.write('E1', 'Link to the project site', bold)
    sheet.write('F1', 'Which license(s) governs this project?', bold)

    # populate data. Skipping columsn that need human supervision
    row = 1
    for r in reps:
        sheet.write(row, 0, r.name)
        sheet.write(row, 1, r.description)
        sheet.write(row, 4, r.html_url)
        try:
            lic = r.license().license.name
        except Exception:
            lic = ''
        sheet.write(row, 5, lic)
        row += 1

    wkbook.close()
    output.seek(0)

    return send_file(output, attachment_filename=file_name)