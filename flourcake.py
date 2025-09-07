flour, sugar = list(map(int, input().split()))
flourNeed = 100
sugarNeed = 50
cake = 0
while True:
   if flour < flourNeed or sugar < sugarNeed:
       break
   else:
       flour -= flourNeed
       sugar -= sugarNeed
       cake += 1
print(cake, flour, sugar)
