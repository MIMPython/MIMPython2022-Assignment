def print_filename(name, week_id, assignment_id):
    # Both week_id and assignment_id are 1 or 2-digit numbers
    limit = range(1, 100)
    if week_id in limit and assignment_id in limit:
        w_id = str(week_id)
        a_id = str(assignment_id)
        if week_id < 10:
            w_id = '0' + w_id
        if assignment_id < 10:
            a_id = '0' + a_id

        print(f'week{w_id}_assignment{a_id}_{name}.py')
    else:
        print('week id or assignment id is out of range.')


print_filename('PhungThiThuAn', 2, 1)
# week02_assignment01_PhungThiThuAn.py

print_filename('PhungThiThuAn', 19, 8)
# week19_assignment08_PhungThiThuAn.py

print_filename('PhungThiThuAn', 100, 2)
# week id or assignment id is out of range.
