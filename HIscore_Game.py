import random

def game():
    print("You are Playing The Game...")
    Score = random.randint(1,100)
    # Fetch The High_score
    with open ("High_Score.txt","r") as F:
        High_score = F.read()
        if High_score != "":
            High_score = int(High_score)
        else:
            High_score = 0

    print(f"Your Score:{Score}")
    if Score > High_score:     
    # Write This High_Score To This File 
        with open("High_Score.txt","w") as F:
            F.write(str(Score))
    return Score                   

# Call The game Function
game() 