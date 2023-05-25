from openpyxl import load_workbook

wb = load_workbook('D:/Copy of Names, Ids .xlsx')

sheet = wb.active


def branch(bits_id):
    if bits_id[6] == 'P' and bits_id[7] == 'S':
        if bits_id[4] == 'A' and bits_id[5] == 'A':
            return 'ECE'
        elif bits_id[4] == 'A' and bits_id[5] == '1':
            return  'Chemical'
        elif bits_id[4] == 'A' and bits_id[5] == '2':
            return 'Civil'
        elif bits_id[4] == 'A' and bits_id[5] == '3':
            return 'EEE'
        elif bits_id[4] == 'A' and bits_id[5] == '4':
            return 'Mechanical'
        elif bits_id[4] == 'A' and bits_id[5] == '5':
            return 'B pharma'
        elif bits_id[4] == 'A' and bits_id[5] == '7':
            return 'CS'
        elif bits_id[4] == 'A' and bits_id[5] == '8':
            return 'ENI'
        elif bits_id[4] == 'A' and bits_id[5] == 'B':
            return 'manufacturing'
        elif bits_id[4] == 'B' and bits_id[5] == '1':
            return 'Msc Bio'
        elif bits_id[4] == 'B' and bits_id[5] == '2':
            return 'Msc chem'
        elif bits_id[4] == 'B' and bits_id[5] == '3':
            return 'Msc eco'
        elif bits_id[4] == 'B' and bits_id[5] == '4':
            return 'msc maths'
        elif bits_id[4] == 'B' and bits_id[5] == '5':
            return 'Msc physics'
    else:
        if bits_id[4] == 'B' and bits_id[5] == '1':
            str = 'Msc Bio'
        elif bits_id[4] == 'B' and bits_id[5] == '2':
            str = 'Msc chem'
        elif bits_id[4] == 'B' and bits_id[5] == '3':
            str = 'Msc eco'
        elif bits_id[4] == 'B' and bits_id[5] == '4':
            str = 'msc maths'
        elif bits_id[4] == 'B' and bits_id[5] == '5':
            str =  'Msc physics'
        if bits_id[6] == 'A' and bits_id[7] == 'A':
            return str + ' + ECE'
        if bits_id[6] == 'A' and bits_id[7] == '1':
            return str + ' + Chemical'
        if bits_id[6] == 'A' and bits_id[7] == '2':
            return str + ' + Civil'
        if bits_id[6] == 'A' and bits_id[7] == '3':
            return str + ' + EEE'
        if bits_id[6] == 'A' and bits_id[7] == '4':
            return str + ' + Mechanical'
        if bits_id[6] == 'A' and bits_id[7] == '5':
            return str + ' + B pharma'
        if bits_id[6] == 'A' and bits_id[7] == '7':
            return str + ' + CS'
        if bits_id[6] == 'A' and bits_id[7] == '8':
            return str + ' + ENI'
        if bits_id[6] == 'A' and bits_id[7] == 'B':
            return str + ' + manufacturing'


def email(bits_id):
    mail = 'f2022' + bits_id[8:12] + '@pilani.bits-pilani.ac.in'
    return mail


result = []
for i in range(2, 24):
    dict = {}
    x = sheet['A' + str(i)]
    y = sheet['B' + str(i)]
    dict['name'] = y.value
    dict['bits_id'] = x.value
    dict['branch'] = branch(x.value)
    dict['bits_email'] = email(x.value)
    result.append(dict)


print(result)

