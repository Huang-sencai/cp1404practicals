import random
def main():
    score_number=float(input("Enter score: "))
    if score_number < 0 or score_number > 100:
       return 0
    elif score_number >= 90:
      return 1
    elif score_number >= 50:
        return 2
    else:
       return 3




number=main()
if number==0:
    print("Invalid score")
elif number==1:
    print("Excellent")
elif number==2:
    print("Passable")
else:
    print("Bad")
score=random.randint(-25, 125)
if score<0 or score>100:
    print("Invalid score")
elif score>=90:
        print("Excellent")
elif score>=50:
        print("Passable")
else:
        print("Bad")