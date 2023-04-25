def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

s = input("문자열을 입력하세요: ")
vowel_count = count_vowels(s)
print("모음의 개수는 {}개입니다.".format(vowel_count))