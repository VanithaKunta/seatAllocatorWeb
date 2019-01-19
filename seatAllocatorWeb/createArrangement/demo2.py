import xlsxwriter
import math
import time
from django.shortcuts import render
from createArrangement.views import getobjects1,getobjects2,getobjects3,deletion
#import final_algorithm1
from createArrangement import final_algorithm1
from .final_algorithm1 import result
def result2():
    utilised = final_algorithm1.result(request=None).utilised_rooms.copy()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    timestr1 = timestr + '.xlsx'
    workbook = xlsxwriter.Workbook(timestr1)
    for i in range(len(utilised)):
        worksheet = workbook.add_worksheet()
        r = 1
        c = 4
        id = final_algorithm1.result(request=None).utilised_rooms[i]
        rows = final_algorithm1.row[id]
        columns = final_algorithm1.column[id]
        worksheet.set_column(0, 15, 14)
        worksheet.set_default_row(22)
        worksheet.set_default_row(hide_unused_rows=True)
        cell_format = workbook.add_format({'bold': True, 'align': 'center', 'font_color': 'red', 'font_size': 15})
        worksheet.write(r, c, "ROOM ID", cell_format)
        worksheet.write(r, c + 1, final_algorithm1.result(request=None).room_id_sorted_new[i], cell_format)
        worksheet.write(r + 1, c, "CAPACITY", cell_format)
        worksheet.write(r + 1, c + 1, final_algorithm1.utilised_rooms_capacity[i], cell_format)
        r += 4
        c = 0
        c1 = c
        r1 = r
        countr = 0
        countc = 0
        countcc = 0
        countrr = 1
        l = -1
        l1 = -1
        c2 = c
        for m in range(columns - 1):
            worksheet.set_column(c2 + 2, c2 + 2, 3)
            c2 += 3
        # worksheet.add_table(r1, c1, r1+rows-1, 3*c1, {'header_row': False, 'banded_rows': False, 'banded_columns': True})
        for j in range(len(final_algorithm1.sections_capacity)):
            for k in range(final_algorithm1.room_sections_capacity[i][j]):
                if k is not None:
                    l += 1
                    number = final_algorithm1.result(request=None).room_section_rollnos[i][l]
                    while number >= 1000000:
                        number //= 10
                    number1 = number % 10
                    if number1 == 7:
                        cell_format1 = workbook.add_format(
                            {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                             'font_color': 'red', 'border_color': 'red', 'border': 1})
                        worksheet.write(r, c, final_algorithm1.result(request=None).room_section_rollnos[i][l], cell_format1)
                    elif number1 == 5:
                        cell_format2 = workbook.add_format(
                            {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                             'font_color': 'blue', 'border_color': 'blue', 'border': 1})
                        worksheet.write(r, c, final_algorithm1.result(request=None).room_section_rollnos[i][l], cell_format2)
                    elif number1 == 6:
                        cell_format3 = workbook.add_format(
                            {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                             'font_color': 'green', 'border_color': 'green', 'border': 1})
                        worksheet.write(r, c, final_algorithm1.result(request=None).room_section_rollnos[i][l], cell_format3)
                    else:
                        cell_format4 = workbook.add_format(
                            {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                             'border': 1})
                        worksheet.write(r, c, final_algorithm1.result(request=None).room_section_rollnos[i][l], cell_format4)
                    countr += 1
                    r += 2
                    if rows % 2 is not 0:
                        if countrr == 2 and countr == rows // 2:
                            c += 3
                            countc += 1
                            countr = 0
                            r = r1 + 1
                            if countc == columns:
                                c = c1 + 1
                                countc = 0
                                countcc += 1
                                if countcc == 2:
                                    r = r1 + 1
                                    c = c1
                                    countrr = 1
                                    countcc = 0
                        else:
                            if countr == math.ceil(rows / 2):
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1
                            if countc == columns:
                                c = c1 + 1
                                countc = 0
                                countcc += 1
                                if countcc == 2:
                                    r = r1 + 1
                                    c = c1
                                    countrr += 1
                                    countcc = 0
                    else:
                        if countrr == 2 and countr == math.ceil(rows / 2):
                            c += 3
                            countc += 1
                            countr = 0
                            r = r1 + 1
                            if countc == columns:
                                c = c1 + 1
                                countc = 0
                                countcc += 1
                                if countcc == 2:
                                    r = r1 + 1
                                    c = c1
                                    countrr = 1
                                    countcc = 0
                        else:
                            if countr == math.ceil(rows / 2):
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1
                            if countc == columns:
                                c = c1 + 1
                                countc = 0
                                countcc += 1
                                if countcc == 2:
                                    r = r1 + 1
                                    c = c1
                                    countrr += 1
                                    countcc = 0
            l1 += k + 1
            l = l1
    workbook.close()
    deletion()
    #return render(request, 'createArrangement/index4.html')
#result()