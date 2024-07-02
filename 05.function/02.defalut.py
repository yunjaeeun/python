# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))    # \ -> 줄바꿈
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
          .format(name, age, main_lang))    # \ -> 줄바꿈

profile("유재석")
profile("김태호", 25, "자바")