import random

# Lists of random values for each attribute
first_name = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
              "Lisa", "Nancy", "Betty", "Sandra", "Margaret", "Ashley", "Kimberley", "Emily", "Donna", "Michelle",
              "Carol", "Amanda", "Melissa", "Deborah", "Stephanie", "Dorothy", "Rebecca", "Sharon", "Laura", "Cynthia",
              "Amy", "Kathleen", "Angela", "Shirley", "Brenda", "Emma", "Anna", "Pamela", "Nicole", "Samantha",
              "Katherine", "Christine", "Helen", "Debra", "Rachel", "Carolyn", "Janet", "Maria", "Catherine",
              "Heather", "Diane", "Olivia", "Julie", "Joyce", "Victoria", "Ruth", "Virginia", "Lauren", "Kelly",
              "Christina", "Joan", "Evelyn", "Judith", "James", "Robert", "John", "Michael", "David", "William",
              "Richard", "Joseph", "Thomas", "Christopher", "Charles", "Daniel", "Matthew", "Anthony", "Mark",
              "Donald", "Steven", "Andrew", "Paul", "Joshua", "Kenneth", "Kevin", "Brian", "George", "Timothy",
              "Ronald", "Jason", "Edward", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan",
              "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Alexander",
              "Patrick", "Frank", "Raymond", "Jack", "Dennis", "Jerry"]

last_name = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
             "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
             "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez",
             "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Nelson", "Carter", "Mitchell",
             "Turner", "Phillips", "Reed", "Campbell", "Parker", "Evans", "Morris", "Ross", "Rivera", "Bennett",
             "Foster", "Gray", "Simmons", "Russell", "Hayes", "Coleman", "Brooks", "Powell", "Wood", "Jenkins",
             "Perry", "Bell", "Murphy", "Cooper", "Howard", "Long", "Diaz", "Collins", "Butler", "Rivera",
             "Gonzales", "Ward", "Torres", "Sanders", "Bryant", "Reed", "Ortiz", "Henderson", "Tucker", "Cox",
             "Ramirez", "James", "Price", "Coleman", "Jenkins", "Baker", "Simpson", "Stevens", "Martinez",
             "Kelly", "Richardson", "Mitchell", "Hughes", "Ellis", "Nelson", "Powell", "Harrison", "Wood",
             "Bryant", "Hudson", "Graham", "Kennedy", "Wells", "Porter", "Hunt", "Holmes", "Fisher", "Watson",
             "Warren", "Sullivan", "Adams", "Fox", "Hayes", "Barnes", "Perry", "Morales", "Castro", "Ortiz",
             "Todd", "Shepherd", "Becker", "Bridges", "Peterson", "Reid", "Fernandez", "Ware", "Holden", "Knox",
             "Ferreira", "Gomez", "O'Connor", "Guzman", "Yu", "Li", "Sazuki", "Watanabe", "Holloway", "Jennings",
             "Copeland", "Banks", "Schneider", "Reyes", "Woods", "Foley", "Marsh", "Stuart", "Freeman", "Keller",
             "Takayama", "Itabashi", "Suyama", "Shimizu", "Ruiz", "Pearson", "Wolf", "Burton", "Cartwright",
             "Deckow", "Hyatt", "Sanford", "Wisozk", "Kertzmann", "Kiehn", "Armstrong", "Hamill", "Murray",
             "Stokes", "Runte", "Emmerich", "Gutmann", "Bauch", "Farrell", "Dach", "Marks", "Spencer",
             "Harrington", "Haughey", "O'Donnellan", "O'Kieran", "O'Hurley", "Mullen", "Grehan", "Vazquez",
             "Baumann", "Vasconcelos", "Pires", "Harper", "Burns", "Chambers"

             ]

majors = [
    "Computer Science", "Information Technology", "Software Engineering", "Electrical Engineering", "Mechanical Engineering",
    "Civil Engineering", "Architecture", "Biology", "Biochemistry", "Physics",
    "Chemistry", "Environmental Science", "Mathematics", "Statistics", "Economics",
    "Finance", "Accounting", "Business Administration", "Marketing", "Management",
    "International Relations", "Political Science", "Psychology", "Sociology", "Anthropology",
    "History", "Philosophy", "Linguistics", "English Literature", "Creative Writing",
    "Journalism", "Film and Media Studies", "Graphic Design", "Fine Arts", "Music",
    "Theater", "Education", "Nursing", "Public Health", "Medicine (Pre-Med)",
    "Law (Pre-Law)", "Criminal Justice", "Social Work", "Agriculture", "Food Science",
    "Animal Science", "Sports Science", "Astronomy", "Data Science", "Artificial Intelligence"
]


ages = list(range(17, 46))  # Ages from 17 to 45

# Assign weights: higher for 17–21, lower after that
weights = [
    10,  # 17
    20,  # 18
    25,  # 19
    25,  # 20
    20,  # 21
    10,  # 22
    6,   # 23
    4,   # 24
    3,   # 25
    2,   # 26
    2,   # 27
    2,   # 28
    2,   # 29
    2,   # 30
    1,   # 31
    1,   # 32
    1,   # 33
    1,   # 34
    1,   # 35
    0.8,  # 36
    0.8,  # 37
    0.8,  # 38
    0.5,  # 39
    0.5,  # 40
    0.4,  # 41
    0.4,  # 42
    0.4,  # 43
    0.3,  # 44
    0.3  # 45
]

dormitories = [
    "Maple Hall", "Oak Hall", "Pine Residence", "Cedar Lodge", "Willow House",
    "Birch Hall", "Aspen Residence", "Elm Hall", "Magnolia House", "Redwood Dorm"
]

clubs = [
    "Drama Club", "Chess Club", "Robotics Club", "Photography Club", "Music Band",
    "Debate Society", "Hiking Club", "Anime Club", "Coding Club", "Gaming Society",
    "Environmental Club", "Dance Crew", "Film Club", "Sports Club", "Art Society",
    "Volunteer Club", "Entrepreneurship Club", "Psychology Club", "Cultural Exchange Club", "Book Club",
    "LGBTQ+ Alliance", "Meditation Club", "Finance Club", "Math Club", "Public Speaking Club"
]


first = random.choice(first_name)
last = random.choice(last_name)
major = random.choice(majors)
age = random.choices(ages, weights=weights, k=1)[0]
dormitory = random.choice(dormitories)
num_of_clubs = random.randint(0, 3)
student_clubs = random.sample(clubs, num_of_clubs)

print(f"Name: {first} {last}")
print(f"Major: {major}")
print(f"Age: {age}")
print(f"Dormitory: {dormitory}")
print("Student Club(s):")
for club in student_clubs:
    print(club)
