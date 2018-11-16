from flask import Flask, send_file
from github3 import GitHub, login
import xlsxwriter
import io
from lib.functions import populate_sheet
app = Flask(__name__)

@app.route('/<username>')
def spreadhseet(username):

    token = ''
    gh = login(token=token)
    reps = gh.repositories_by(username=username)
    reps = filter(lambda x: x.archived is False, reps)
    output = io.BytesIO()
    file_name = 'Own-Time-Contributions.xlsx'
    wkbook = xlsxwriter.Workbook(output, {'in_memory': True})
    populate_sheet(reps, wkbook)
    wkbook.close()
    output.seek(0)

    return send_file(output, attachment_filename=file_name)