week_days = {1: 'Mon.txt', 2: 'Tue.txt', 3: 'Wed.txt', 4: 'Thu.txt', 5: 'Sat.txt', 6: 'Sun.txt'}
day = int(input('Введите день недели,число от 1 до 7: '))
event = ''
timetable_change = int(
    input('Введите 1 чтобы прочитать расписание, 2 чтобы добавить измениния, 3 чтобы изменить расписание: '))
while timetable_change < 1 or timetable_change > 3:
    timetable_change = int(input('Ошибка, введите цифру от 1 до 3 : '))
if timetable_change == 1:
    day = int(input('Введите день недели от 1 до 7: '))
    with open(week_days[day], 'r', encoding='utf-8') as f:
        print(f.readlines())
elif timetable_change == 2:
    day = int(input('Введите день недели от 1 до 7: '))
    event = input('Какие события вы хотите добавить? ')
    with open(week_days[day], 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(event)
elif timetable_change == 3:
    day = int(input('Введите день недели от 1 до 7: '))
    event = input('Какие события вы хотите изменить? ')
    with open(week_days[day], 'w', encoding='utf-8') as f:
        f.write(event)
