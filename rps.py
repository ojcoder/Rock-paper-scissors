print("Welome to Rock Paper Scissors")
player1score=0
player2score=0
x=0
while x<10000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    x=x+1
    player1_answer = str(input("Player 1: Rock Paper or Scissors? "))
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    player2_answer=str(input("Player 2: Rock paper scissors?"))

    if player1_answer=="rock" and player2_answer=="paper":
        print("Player 2 wins the round!")
        player2score=player2score+1
    
    if player1_answer=="rock" and player2_answer=="scissors":
        print("Player 1 wins the round!")
        player1score=player1score+1
    
    if player1_answer=="rock" and player2_answer=="rock":
        print("Tie!")
    
    if player1_answer=="paper" and player2_answer=="paper":
        print("Tie!")
    
    if player1_answer=="paper" and player2_answer=="scissors":
        print("Player 2 wins the round!")
        player2score=player2score+1
    
    if player1_answer=="paper" and player2_answer=="rock":
        print("Player 1 wins the round!")
        player1score=player1score+1
    
    if player1_answer=="scissors" and player2_answer=="paper":
        print("Player 1 wins the round!")
        player1score=player1score+1
    
    if player1_answer=="scissors" and player2_answer=="rock":
        print("Player 2 wins the round!")
        player2score=player2score+1
    
    if player1_answer=="scissors" and player2_answer=="scissors":
        print("Tie!")
    
    if player2score==2:
        print("Player 2 wins the game!")
        break
        
    if player1score==2:
        print("Player 1 wins the game!")
        break
  
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
