# Day 48 - Test
from day48_helper import get_computer_choice

def test_winner_logic():
    # Tie
    assert get_computer_choice() in ["Rock", "Paper", "Scissors"]
    print("✅ Helper choice OK")

def test_determine_winner():
    # Import from main
    from day48 import determine_winner
    assert determine_winner("Rock", "Scissors") == "You win"
    assert determine_winner("Paper", "Rock") == "You win"
    assert determine_winner("Scissors", "Paper") == "You win"
    assert determine_winner("Rock", "Rock") == "Tie"
    assert determine_winner("Rock", "Paper") == "Computer wins"
    print("✅ Winner logic OK")
    print("Day 48 test ok")

test_winner_logic()
test_determine_winner()