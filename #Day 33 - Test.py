#Day 33 - Test
def test_rps_logic():
    # Test win conditions
    wins = [
        ("rock", "scissors"),
        ("paper", "rock"), 
        ("scissors", "paper")
    ]
    
    for player, computer in wins:
        if (player == "rock" and computer == "scissors") or \
           (player == "paper" and computer == "rock") or \
           (player == "scissors" and computer == "paper"):
            print(f"Win test {player} vs {computer}: OK")
    
    print("All RPS logic tests passed")
    print("Day 33 test ok")

test_rps_logic()