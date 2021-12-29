x,y = map(int,input().split())
s = input()
print(s[:x-1]+s[x-1:y][::-1]+s[y:])