# score_file = open("score.txt", "w", encoding="utf8")    # open(파일이름, 쓰기, 인코딩)
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")    # open(파일이름, 덮어쓰기, 인코딩)
# score_file.write("과학: 80\n")
# score_file.write("코딩: 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")      # open(파일이름, 읽기, 인코딩)
# print(score_file.read())
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")      # open(파일이름, 읽기, 인코딩)
# print(score_file.readline())                               # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")