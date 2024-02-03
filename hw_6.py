def read_votes_from_file(file):
    votes = {}

    with open('input.txt', 'r') as file:
        for line in file:
            last_name, votes_count = line.strip().split()
            votes_count = int(votes_count)

            if last_name in votes:
                votes[last_name] += votes_count
            else:
                votes[last_name] = votes_count

    return votes

