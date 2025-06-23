def min_kicks(s):
    # goalsA and goalsB track the confirmed scores
    goalsA = 0
    goalsB = 0
    
    # remainingA and remainingB track the number of kicks left for each team,
    # including those with known outcomes and '?' outcomes.
    remainingA = 5  # Team A has 5 kicks in total (indices 0, 2, 4, 6, 8)
    remainingB = 5  # Team B has 5 kicks in total (indices 1, 3, 5, 7, 9)
    
    for i in range(10):
        kick = s[i]
        
        # Determine which team is kicking
        team = 'A' if (i % 2 == 0) else 'B'
        
        # Decrement the count of remaining kicks for the current team
        if team == 'A':
            remainingA -= 1
        else:
            remainingB -= 1
            
        # Update scores based on known outcomes
        if kick == '1':
            if team == 'A':
                goalsA += 1
            else:
                goalsB += 1
        # For '?' outcomes, we make an assumption that would *delay* a certain win
        # This means assuming the opponent scores if it's their turn,
        # or assuming we miss if it's our turn.
        # This makes the conditions for an early win stricter.
        elif kick == '?':
            if team == 'B':
                # If Team B kicks '?', assume they score to make it harder for A to win early
                goalsB += 1
            # If Team A kicks '?', we implicitly assume they miss (goalsA remains unchanged)
            # This makes it harder for A to win early and easier for B to win early

        # Check termination conditions after each kick
        # Team A wins if their current score is greater than Team B's maximum possible score
        # (current goalsB + remaining kicks for B)
        if goalsA > goalsB + remainingB:
            return i + 1
        
        # Team B wins if their current score is greater than Team A's maximum possible score
        # (current goalsA + remaining kicks for A)
        if goalsB > goalsA + remainingA:
            return i + 1
            
    # If no winner is determined after 10 kicks, it means all 10 kicks are needed.
    return 10

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    s = input().strip()
    print(min_kicks(s))