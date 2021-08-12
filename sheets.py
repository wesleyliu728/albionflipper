import gspread
from oauth2client.service_account import ServiceAccountCredentials
import data as dat
import time


def grabData():
    #Here add in the name of your spreadsheet
    Name = 'EXAMPLE NAME'
    #Here copy the name of your json file containing your scope
    json = 'EXAMPLE NAME'






    startnums = [3,48,93,138,183]
    arr = dat.getData()
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(json,scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open(Name)
    sheets = spreadsheet.worksheets()
    for x in range(len(arr)):
        for i in range(5):
            runes= arr[x][i]._runes
            items = arr[x][i]._items
            sheet = sheets[i]
            startervalue = startnums[x]
            set1 = startervalue
            set1b = set1+8
            set2 = set1b + 3
            set2b = set2 + 8
            set3 = set2b + 3
            set3b = set3 + 8
            set4 = set3b + 3
            set4b = set4 + 8
            sheet = sheets[i]
            sheetdata = sheet.batch_get(['A{}:A{}'.format(set1,set1b),'C{}:C{}'.format(set1,set1b),'E{}:E{}'.format(set1,set1b),'A{}:A{}'.format(set2,set2b),'C{}:C{}'.format(set2,set2b),'E{}:E{}'.format(set2,set2b),'A{}:A{}'.format(set3,set3b),'C{}:C{}'.format(set3,set3b),'E{}:E{}'.format(set3,set3b),'A{}:A{}'.format(set4,set4b),'C{}:C{}'.format(set4,set4b),'E{}:E{}'.format(set4,set4b)])
            array = []
            for j in sheetdata:
                temp = []
                for u in j:
                    temp.append([items[u[0]]])
                array.append(temp)
            update = [{'range':'B{}:B{}'.format(set1,set1b),'values':array[0]},{'range':'D{}:D{}'.format(set1,set1b),'values':array[1]},{'range':'F{}:F{}'.format(set1,set1b),'values':array[2]},{'range':'B{}:B{}'.format(set2,set2b),'values':array[3]},{'range':'D{}:D{}'.format(set2,set2b),'values':array[4]},{'range':'F{}:F{}'.format(set2,set2b),'values':array[5]},{'range':'B{}:B{}'.format(set3,set3b),'values':array[6]},{'range':'D{}:D{}'.format(set3,set3b),'values':array[7]},{'range':'F{}:F{}'.format(set3,set3b),'values':array[8]},{'range':'B{}:B{}'.format(set4,set4b),'values':array[9]},{'range':'D{}:D{}'.format(set4,set4b),'values':array[10]},{'range':'F{}:F{}'.format(set4,set4b),'values':array[11]}]
            sheet.batch_update(update)
            pog = list(runes.values())
            for l in range(4):
                sheet.update_cell(3+x,13+l,pog[l])
        time.sleep(100)