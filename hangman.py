from random import * # 랜덤 모듈 import
words1 = ["apple", "korea", "letter"] # 리스트에 영어 단어 후보를 나열
words2 = ["umbrella", "surprise", "together"]

difficulty = int(input("난이도를 고르세요 (1또는 2):  "))
if difficulty == 1:
    reallist = words1
elif difficulty == 2:
    reallist = words2


word = choice(reallist) # 랜덤으로 단어 중 1개를 선택
print("answer : " + word) # 참고용으로 정답 출력 (실제 게임에서는 지우기)
letters = "" # 플레이어가 지금까지 입력한 알파벳들 저장

def print_hangman(count):
    if count <= 6:
        hangman='O/|\/\\'[:count] + ' '[count:]
        print(" +---+\n | |\n %c |\n %c%c%c |\n %c %c |\n |\n========" %tuple(list(hangman)))

count = 0
while True:
    result = [ x if x in letters else '_' for x in word]
    print(' '.join(result))

    if ''.join(result) == word:
        print("Success")
        break

    letter =input("Input letter > ") # 플레이어로부터 한 글자씩 입력
    if letter not in letters: # 입력값 중에 포함되어 있지 않다면
        letters += letter # 새로 입력받은 글자를 입력값에 추가

    if letter in word: # 입력한 글자가 제시 단어에 포함되었다면
        print("Correct")
        count+= 1
        #print_hangman(count)
    else: # 포함되어있지 않다면
        print("Wrong")
        #count += 1
        print_hangman(count)
