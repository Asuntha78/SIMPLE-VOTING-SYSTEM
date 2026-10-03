# Simple Election Voting System

# Number of candidates
number_of_candidates = int(input("Enter the number of candidates:"))

print()

# Candidates
candidates = []

times = 1
while times <= number_of_candidates:
    candidate = str(input(f"Enter candidate {times} name:"))
    candidates.append(candidate)
    times += 1

print()

# Vote counter
votes = []
times = 1
while times <= number_of_candidates:
    votes.append(0)
    times += 1

# Candidate list
print("Candidates:")
times = 1
while times <= number_of_candidates:    
    print(f"{times}-{candidates[times-1]}")
    times += 1

print()

# Voting
while True:
    vote = input("Enter your vote (or type 'stop' to finish):")

    if vote == "stop":
        break

    if vote == "":
        print("Please enter a candidate number")
        continue

    vote = int(vote)

    if 1 <= vote <= number_of_candidates:
        votes[vote - 1] += 1
        print("Vote recorded")
    else:
        print("Invalid candidate")

print()

# Results
print("Results:")

times = 1
while times <= number_of_candidates:
    print(f"{candidates[times - 1]}: {votes[times - 1]} votes")
    times += 1

print()

# Ranking
print("Final Ranking:")

ranked = []

rank = 1

while rank <= number_of_candidates:

    highest_votes = -1
    highest_index = -1

    times = 0

    while times < number_of_candidates:

        if times not in ranked and votes[times] > highest_votes:
            highest_votes = votes[times]
            highest_index = times

        times += 1

    if rank == 1:
        place = "1st"
    elif rank == 2:
        place = "2nd"
    elif rank == 3:
        place = "3rd"
    else:
        place = f"{rank}th"

    print(f"{place} Place: {candidates[highest_index]} ({highest_votes} votes)")

    ranked.append(highest_index)

    rank += 1

print()

# Finding the winner

highest_votes = 0
winner = ""

times = 0

while times < number_of_candidates:
    if votes[times] > highest_votes:
        highest_votes = votes[times]
        winner = candidates[times]

    times += 1

print()

# Display winner
print("Winner:")
print(f"{winner} with {highest_votes} votes")