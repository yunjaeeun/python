# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 :

# 1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

for i in range(1, 51):
    score_file = open("{0} 주차 주간보고.txt".format(i), "w", encoding="utf8")    # open(파일이름, 쓰기, 인코딩)
    print("부서 : ", file=score_file)
    print("이름 : ", file=score_file)
    print("업무 요약 : ", file=score_file)
    score_file.close()

# for i in range(1, 51):
#     with open("{0} 주차 주간보고.txt".format(i), "w", encoding="utf8") as report_file:    # open(파일이름, 쓰기, 인코딩)
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("부서 : \n")
#         report_file.write("이름 : \n")
#         report_file.write("업무 요약 : ")