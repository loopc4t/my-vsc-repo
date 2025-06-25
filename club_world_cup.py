import random
from teams import brasileirao, laliga, premier_league, serie_a, bundesliga, ligue_1, liga_pro

# Step 1: Combine all teams
all_teams = brasileirao + laliga + premier_league + \
    serie_a + bundesliga + ligue_1 + liga_pro

# Step 2: Assign strengths (example: 1-10 scale)
# You can customize this to be more accurate later
team_strengths = {
    "Real Madrid": 10,
    "Manchester City": 10,
    "Bayern Munich": 9,
    "Barcelona": 9,
    "Paris Saint-Germain": 9,
    "Juventus": 8,
    "Liverpool": 8,
    "Palmeiras": 8,
    "Flamengo": 7,
    "River Plate": 7,
    # Default for all others
}
# Add default strength 5 for teams not listed
for team in all_teams:
    if team not in team_strengths:
        team_strengths[team] = 5

# Step 3: Match creation


def create_match():
    team1 = random.choice(all_teams)
    team2 = random.choice(all_teams)
    while team1 == team2:
        team2 = random.choice(all_teams)
    return team1, team2

# Step 4: Score generation based on team strength


def weighted_score(strength):
    # More strength = more chance of higher scores
    return min(round(random.gauss(mu=strength / 2, sigma=1)), 5)


def random_results(team1, team2):
    strength1 = team_strengths[team1]
    strength2 = team_strengths[team2]

    score_1 = max(0, weighted_score(strength1))
    score_2 = max(0, weighted_score(strength2))

    print(f"{team1} {score_1} vs {score_2} {team2}")


# Test it
team1, team2 = create_match()
random_results(team1, team2)
