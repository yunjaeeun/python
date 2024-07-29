lst = [55 ,7, 78, 12, 42]

def bubble_sort(numbers, n):
    # numbers : 정렬하고 싶은 대상
    # n : 배열(리스트)의 길이

    # i번 자리의 주인 정하기 (n-1 ~ 1)
    for i in range(n-1, 0, -1):
        # 맨 앞에서 두개씩 비교 하면서 큰게 뒤로 오도록 자리 바꾸기
        for j in range(0, i):
            # 자리 바꾸는 조건
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers

print(bubble_sort(lst, 5))