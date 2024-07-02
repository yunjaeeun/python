# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")  # end = " " -> 줄바꿈 되지 않게
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")  # end = " " -> 줄바꿈 되지 않게
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C","C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")