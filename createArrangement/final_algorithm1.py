from createArrangement.views import getobjects1,getobjects2,getobjects3,deletion
from django.shortcuts import render
import xlsxwriter
import math
import time
def result(request):
    getobjects2()
    getobjects1()
    getobjects3()
    path = 'C:\\Users\\Vanitha\\Downloads\\seatAllocatorWeb\\file1.py'
    l1 = list()
    fp1 = open(path, 'r')
    for line in fp1:
        for word in line.split():
            l1.append(word)
    print(l1)
    path = 'C:\\Users\\Vanitha\\Downloads\\seatAllocatorWeb\\file2.py'
    l2 = list()
    fp2 = open(path, 'r')
    for line in fp2:
        for word in line.split():
            l2.append(word)
    print(l2)
    path = 'C:\\Users\\Vanitha\\Downloads\\seatAllocatorWeb\\file3.py'
    l3 = list()
    fp3 = open(path, 'r')
    for line in fp3:
        for word in line.split():
            l3.append(word)
    print(l3)
    d=0
    row = list()
    column = list()
    room_id = list()
    rooms_capacity = list()
    Rooms = int(l1[d])
    d=d+1
    #print("enter no.of rows and columns in each room: ")
    for i in range(int(Rooms)):
        #print('row[', i, ']: ', end=" ")
        r1 = int(l1[d])
        d = d + 1
        #print('column[', i, ']: ', end=" ")
        c1 = int(l1[d])
        d = d + 1
        #print('room_id[', i, ']: ', end=" ")
        rid = l1[d]
        d = d + 1
        row.append(r1)
        column.append(c1)
        room_id.append(rid)
        cap1 = int(r1) * int(c1) * 2
        rooms_capacity.append(cap1)

    # DICTIONARY WHICH HAS ROOM_ID AS KEYS AND ROOM_CAPACITY AS COLUMNS
    stutuple = tuple
    z = list(zip(room_id, rooms_capacity))
    print(z)
    myl = sorted(z, key=lambda z: z[1])
    #print("sorted list:", myl)
    room_id_sorted = list()
    for k in range(len(room_id)):
        room_id_sorted.append(myl[k][0])
    print(room_id_sorted)

    initial_array = rooms_capacity.copy()
    rooms_capacity.sort()
    #print('total capacity: ', sum(rooms_capacity))

    # SECTIONS AND STUDENTS INPUT
    dept_name = list()
    dept_sections = list()
    sections_capacity = list()
    starting_rollno = list()
    ending_rollno = list()
    removing_rollno = list()
    roll_numbers = []
    section_name = list()
    s=0
    departments = int(l2[s])
    s=s+1
    #print(
        #'enter department name, no.of sections, section_names, capacity, starting_rollno, ending_rollno of each section')
    for i in range(int(departments)):
        #print('dept_name[', i, ']: ', end=" ")
        dept_names = l2[s]
        s=s+1
        dept_name.append(dept_names)
        #print('sections[', i, ']: ', end=" ")
        sect = int(l2[s])
        s=s+1
        dept_sections.append(sect)
        for j in range(sect):
            #print('section_name[', i, '][', j, ']: ', end=" ")
            sect_name = l2[s]
            s = s + 1
            section_name.append(sect_name)
            #print('section_capacity[', i, '][', j, ']: ', end=" ")
            sect_cap = int(l2[s])
            s=s+1
            sections_capacity.append(sect_cap)
            #print('starting_rollno[', i, '][', j, ']: ', end=" ")
            start_no = int(l2[s])
            s = s + 1
            starting_rollno.append(start_no)
            #print('ending_rollno[', i, '][', j, ']: ', end=" ")
            end_no = int(l2[s])
            s = s + 1
            ending_rollno.append(end_no)
            #print('(y/n) Do you want to remove any no. between starting and ending roll_no?: ')
            removing = l2[s]
            s=s+1
            if removing == 'y':
                #print('how many numbers do you want to remove?: ')
                numbers = int(l2[s])
                s=s+1
                for i in range(0, numbers):
                    #print('enter number to be removed')
                    removing_no = int(l2[s])
                    s=s+1
                    removing_rollno.append(removing_no)

    missing_rollno = [[] for i in range(len(sections_capacity))]
    g=0
    #print('(y/n) Do you want to add any missing roll numbers?: ')
    missing = l3[g]
    g=g+1
    if missing == 'y':
        #print('how many sections do you want to add numbers to?')
        sections = int(l3[g])
        g=g+1
        for i in range(0, sections):
            #print('which section?')
            n = int(l3[g])
            g=g+1
            #print('how many numbers do you want to add to this section?')
            number = int(l3[g])
            g=g+1
            for i in range(0, number):
                #print('enter no. to be added')
                no = int(l3[g])
                g+1
                missing_rollno[n - 1].append(no)
    #print("missing_rollno: ", missing_rollno)
    for i in range(len(sections_capacity)):
        roll_numbers.append([])
        p = starting_rollno[i]
        q = ending_rollno[i]
        for j in range(p, q + 1):
            roll_numbers[i].append(j)
            for k in removing_rollno:
                if j == k:
                    roll_numbers[i].remove(j)
        for k in missing_rollno[i]:
            roll_numbers[i].append(k)
    #print('roll numbers: ', roll_numbers)
    b = sum(rooms_capacity)
    c = sum(sections_capacity)
    extras = b - c
    #print('extra seats: ', extras)
    RoomNo = 1
    es = extras
    ur = []
    value = []

    def rd(es, ur, rno):
        while es < rooms_capacity[rno] and rno >= 0:
            rno = rno - 1
            if rno < 0:
                return
        ur.append(rno)
        es = es - rooms_capacity[rno]
        if es >= rooms_capacity[0]:
            rno -= 1
            if rno >= 0:
                value = rd(es, ur, rno)
        value = ur
        return value

    emptyr = []
    if es < 0:
        print('Rooms are not sufficient')
    else:
        rno = len(rooms_capacity) - 1
        emptyr = rd(es, ur, rno)
        empty = list()
        if emptyr is not None:
            for i in emptyr:
                empty.append(i)
            #print('empty rooms: ', empty)
            size = len(emptyr)
            for i in range(size):
                extras = extras - rooms_capacity[ur[i]]
            #print('seats unoccupied in selected rooms: ', extras)
        else:
            p=0
            #print('empty rooms: ', emptyr)
            #print('empty seats: ', extras)
    room_id_sorted_new = list()
    utilised_rooms = list()
    utilised_rooms_capacity = list()
    section_capacity_notfilled = list()
    room_empty_seats = list()
    roll_numbers_duplicate = roll_numbers.copy()

    if es >= 0:
        if emptyr is not None:
            for i in range(0, Rooms):
                flag = 0
                for j in emptyr:
                    if i == j:
                        flag = 1
                        break
                if flag == 0:
                    utilised_rooms.append(i)
        else:
            utilised_rooms = list(range(Rooms))
        if emptyr is not None:
            for i in range(0, Rooms):
                flag = 0
                for j in emptyr:
                    if i == j:
                        flag = 1
                        break
                    if flag == 0:
                        room_id_sorted_new.append(room_id_sorted[i])
        else:
            room_id_sorted_new = room_id_sorted
        #print('utilised rooms: ', utilised_rooms)
        #print('utilised room ids: ', room_id_sorted_new)

        for i in utilised_rooms:
            utilised_rooms_capacity.append(rooms_capacity[i])
        #print('capacity of utilised rooms: ', utilised_rooms_capacity)

        length = len(utilised_rooms_capacity)

        final_utilised_capacity = utilised_rooms_capacity.copy()
        room_sections_capacity = [[] for i in range(len(utilised_rooms))]
        for k in range(len(utilised_rooms)):
            for i in range(len(sections_capacity)):
                j = sections_capacity[i] // len(utilised_rooms)
                if final_utilised_capacity[k] >= j:
                    room_sections_capacity[k].append(j)
                    # sections_capacity[i] -= final_utilised_capacity[k]
                    final_utilised_capacity[k] -= j
                else:
                    if final_utilised_capacity[k] >= 0:
                        room_sections_capacity[k].append(final_utilised_capacity[k])
                        final_utilised_capacity[k] -= rooms_capacity[k]
                    else:
                        room_sections_capacity[k].append(0)
        for i in range(len(utilised_rooms)):
            if sum(room_sections_capacity[i]) >= utilised_rooms_capacity[i]:
                room_empty_seats.append(0)
            else:
                room_empty_seats.append(utilised_rooms_capacity[i] - sum(room_sections_capacity[i]))

        for i in range(len(sections_capacity)):
            if sections_capacity[i] == sum(int(x[i]) for x in room_sections_capacity):
                section_capacity_notfilled.append(0)
            else:
                diff = sections_capacity[i] - sum(int(x[i]) for x in room_sections_capacity)
                section_capacity_notfilled.append(diff)
        for j in range(len(section_capacity_notfilled)):
            if section_capacity_notfilled[j] is not 0:
                for k in range(len(room_empty_seats)):
                    if room_empty_seats[k] is not 0:
                        if room_empty_seats[k] >= section_capacity_notfilled[j]:
                            room_empty_seats[k] -= section_capacity_notfilled[j]
                            room_sections_capacity[k][j] += section_capacity_notfilled[j]
                            section_capacity_notfilled[j] -= section_capacity_notfilled[j]
                        else:
                            diff = section_capacity_notfilled[j] - room_empty_seats[k]
                            room_sections_capacity[k][j] += room_empty_seats[k]
                            section_capacity_notfilled[j] -= room_empty_seats[k]
                            room_empty_seats[k] -= room_empty_seats[k]
                    if section_capacity_notfilled[j] is 0:
                        break
        #print('capacity of all sections in each room: ', room_sections_capacity)
        #print('section capacity not filled: ', section_capacity_notfilled)
        #print('empty seats in each room: ', room_empty_seats)
        # room_sections_capacity = list()
        room_section_rollnos = [[] for i in range(len(utilised_rooms))]
        for i in range(0, len(utilised_rooms)):
            for j in range(0, len(sections_capacity)):
                k = room_sections_capacity[i][j]
                for l in range(k):
                    room_section_rollnos[i].append(roll_numbers_duplicate[j][l])
                while k > 0:
                    roll_numbers_duplicate[j].remove(roll_numbers_duplicate[j][0])
                    k -= 1
        print("room_section_rollnos: ", room_section_rollnos)
        row.sort()
        column.sort()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        timestr1 = timestr + '.xlsx'  # NAME TO BE GIVEN TO EXCEL SHEET
        workbook = xlsxwriter.Workbook(timestr1)  # TO GENERATE WORKBOOK
        for i in range(len(utilised_rooms)):
            worksheet = workbook.add_worksheet()  # TO ADD SHEET TO WORKBOOK FOR EACH ROOM
            r = 1
            c = 4
            id = utilised_rooms[i]
            rows = row[id]
            columns = column[id]
            worksheet.set_column(0, 15, 14)
            worksheet.set_column('O:XFD', None, None, {'hidden': True})  # TO HIDE UNUSED COLUMNS
            worksheet.set_default_row(22)
            worksheet.set_default_row(hide_unused_rows=True)  # TO HIDE UNUSED ROWS
            cell_format = workbook.add_format({'bold': True, 'align': 'center', 'font_color': 'red', 'font_size': 12})
            worksheet.write(r, c, "ROOM ID", cell_format)
            worksheet.write(r, c + 1, room_id_sorted_new[i], cell_format)
            worksheet.write(r + 1, c, "CAPACITY", cell_format)
            worksheet.write(r + 1, c + 1, utilised_rooms_capacity[i], cell_format)
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
            for j in range(len(sections_capacity)):
                for k in range(room_sections_capacity[i][j]):
                    if k is not None:
                        l += 1
                        number = room_section_rollnos[i][l]
                        while number >= 1000000:
                            number //= 10
                        number1 = number % 10
                        if number1 == 7:
                            cell_format1 = workbook.add_format(
                                {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                                 'font_color': 'red', 'border_color': 'red', 'border': 1})
                            worksheet.write(r, c, room_section_rollnos[i][l], cell_format1)
                        elif number1 == 5:
                            cell_format2 = workbook.add_format(
                                {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                                 'font_color': 'blue', 'border_color': 'blue', 'border': 1})
                            worksheet.write(r, c, room_section_rollnos[i][l], cell_format2)
                        elif number1 == 6:
                            cell_format3 = workbook.add_format(
                                {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                                 'font_color': 'green', 'border_color': 'green', 'border': 1})
                            worksheet.write(r, c, room_section_rollnos[i][l], cell_format3)
                        else:
                            cell_format4 = workbook.add_format(
                                {'bold': True, 'align': 'center', 'font_size': 12, 'num_format': '000000000000',
                                 'border': 1})
                            worksheet.write(r, c, room_section_rollnos[i][l], cell_format4)
                        countr += 1
                        r += 2
                        if rows % 2 is not 0:  # WHEN NO.OF ROWS IS ODD
                            if countr == math.ceil(rows / 2) and countrr != 2:
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1
                                if countc == columns:
                                    c = c1 + 1
                                    r = r1 + 1
                                    countc = 0
                                    countcc += 1
                            elif countr == rows // 2 and countcc == 1 and countrr != 2:
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1 + 1
                                if countc == columns:
                                    countc = 0
                                    countcc += 1
                                    if countcc == 2:
                                        r = r1 + 1
                                        c = c1
                                        countrr += 1
                                        countcc = 0
                            if countr == math.ceil(rows / 2) and countrr == 2:
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
                                    countrr = 1
                                    countcc = 0
                            elif countr == rows // 2 and countcc == 0 and countrr == 2:
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1 + 1
                                if countc == columns:
                                    c = c1 + 1
                                    r = r1
                                    countc = 0
                                    countcc += 1
                                if countcc == 2:
                                    r = r1 + 1
                                    c = c1
                                    countrr = 1
                                    countcc = 0
                        else:  # WHEN NO.OF ROWS IS EVEN
                            if countrr == 2 and countr == math.ceil(rows / 2) and countcc == 1:
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1
                                if countc == columns:
                                    c = c1 + 1
                                    r = r1
                                    countc = 0
                                    countcc += 1
                                    if countcc == 2:
                                        r = r1 + 1
                                        c = c1
                                        countrr = 1
                                        countcc = 0
                            elif countrr == 2 and countr == math.ceil(rows / 2):
                                c += 3
                                countc += 1
                                countr = 0
                                r = r1 + 1
                                if countc == columns:
                                    c = c1 + 1
                                    r = r1
                                    countc = 0
                                    countcc += 1
                                    if countcc == 2:
                                        r = r1 + 1
                                        c = c1
                                        countrr = 1
                                        countcc = 0
                            else:
                                if countr == math.ceil(rows / 2) and countcc == 1:
                                    c += 3
                                    countc += 1
                                    countr = 0
                                    r = r1 + 1
                                elif countr == math.ceil(rows / 2):
                                    c += 3
                                    countc += 1
                                    countr = 0
                                    r = r1
                                if countc == columns:
                                    c = c1 + 1
                                    r = r1 + 1
                                    countc = 0
                                    countcc += 1
                                    if countcc == 2:
                                        r = r1 + 1
                                        c = c1
                                        countrr += 1
                                        countcc = 0
                l1 += k + 1
                l = l1
        workbook.close()  # CLOSE WORKBOOK
        deletion()
    return render(request, 'createArrangement/index4.html')

#result()