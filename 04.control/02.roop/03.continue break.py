absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        print("{0} 학생은 결석입니다.".format(student))
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지.")
        break
    print("{0}, 책을 읽어봐".format(student))