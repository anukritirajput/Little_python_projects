from game_data import data
from art import logo
from art import vs
import random
play=True
def compare(A,B):
  print(f"Compare A:{data[A]['name']},a {data[A]['description']},from {data[A]['country']}")
  print(vs)
  print(f"Compare B:{data[B]['name']},a {data[B]['description']},from {data[B]['country']}")
  choice=input(print("Who has more no. of followers?Type 'A' or 'B':"))
  if(data[A]['follower_count']>data[B]['follower_count']):
    correct='A'
  else:
    correct='B'
  if choice==correct:
    return True
  else:
    return False
  
c=0  
while play==True:
  print(logo)

  n1 = random.randint(0,50)
  n2 = random.randint(0,50)
  play=compare(n1,n2)
  if play==True:
    c+=1
    print("you are right, current score =",c)
  else:
    print("sorry, wrong answer, Final score =",c)


  
