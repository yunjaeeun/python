# for wating_no in range(5):      # 0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(wating_no))

# for wating_no in range(1, 6):      # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(wating_no))

starbucks =["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 한줄 for문
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]    # students에 있는 값에 100씩 더함
print(students)

student = ["Iron man", "Thor", "Groot"]
student = [len(i) for i in student]
print(student)