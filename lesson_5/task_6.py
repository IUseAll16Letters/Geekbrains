"""6. Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
"""
FILE_NAME = 'task_6.txt'


with open(FILE_NAME, 'r', encoding='utf-8') as F:
    """Creating result subjects dictionary"""
    subjects_duration = {}
    for line in F.readlines():
        """Optional- added primitive cleaner in case of typos"""
        if ':' in line:
            subj = line[:line.index(':')].strip("' ")
            working_hours = line[line.index(':')+1:].replace('(', ' ').split()
            subjects_duration[subj] = sum(int(item) for item in working_hours if item.isdigit())

print(subjects_duration)
