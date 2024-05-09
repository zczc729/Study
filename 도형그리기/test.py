a = 10
ch = '*'



# for i in range(1, int(a / 2) + 1): #1~n까지 순서대로 반복
#     print(ch*i + " "*(a-i*2) + ch*i) #5를 넣었을 때 1별+ 10-2=8공백+ 1별
# for i in range(int((a-1) / 2), 0, -1): #n-1~1까지 내림차순 순서대로 반복(예:5넣었을 때 4~1)
#     print(ch*i + " "*(a-i*2) + ch*i) #5 넣었을 때 4별+2공백 + 4별

num = 1

for i in range(a, 0, -2):
    if i == a:
        print(ch * i)
    else:
        str1 = ''
        str1 = ' ' * num + ch * i + ' ' * num
        num += 1
        print(str1)
num = num - 1
for i in range(2, a + 1, +2):
    str1 = ''
    str1 = ' ' * num + ch * i + ' ' * num
    num -= 1
    print(str1)
