# Day 40 - Test
def approximate_play(target):
    guesses = 0
    for g in range(1, 101):
        guesses += 1
        if g == target:
            return guesses
    return 999  # should never hit

def test_game_logic():
    assert 1 <= approximate_play(50) <= 100
    assert 1 <= approximate_play(1) <= 100
    assert 1 <= approximate_play(100) <= 100
    print("✅ Guess logic approx OK")
    print("Day 40 test ok")

test_game_logic()