word = 'madam'
rev = []
count = 0
for i in range(len(word)):
    if word[i] == word[len(word)-1-i]:
        count += 1

print(word)
if count == len(word):
    print("입력하신 단어는 회문(Palindrome)입니다.")