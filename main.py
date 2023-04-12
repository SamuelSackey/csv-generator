"""Main File"""
import random
from fileio import *
from values import *

NUMBER_OF_RECORDS = 10000

FIELDS = "Gender,Age,Wassce Aggregate,Bece Aggregate,Preferred Program,cut-off point,Dream Job,Favorite Subject 1,Favorite Subject 2,Favorite Subject 3,Interests,Learning Style,ExtraCurricular Activities,Native Language,Secondary Language\n"

# Create file and add filed names
write(FIELDS)

# Randomly select data values and append
for record in range(NUMBER_OF_RECORDS):
    entry = []
    # Gender
    entry.append(random.choice(gender))

    # Age
    entry.append(random.randint(12, 31))

    # Wassce Aggregate
    entry.append(random.randint(6, 55))

    # Bece Aggregate
    entry.append(random.randint(6, 55))

    # Preferred Program & Cut-off point
    program = random.choice(list(preferred_programs.items()))
    entry.append(program[0])
    entry.append(program[1])

    # Dream Job
    entry.append(random.choice(dream_jobs))

    # Favorite Subject 1, 2, 3
    favorites = subjects.copy()
    fav_1 = random.choice(favorites)

    favorites.remove(fav_1)
    fav_2 = random.choice(favorites)

    favorites.remove(fav_2)
    fav_3 = random.choice(favorites)

    entry.append(fav_1)
    entry.append(fav_2)
    entry.append(fav_3)

    # Interests
    entry.append(random.choice(interests))

    # Learning Style
    entry.append(random.choice(learning_styles))

    # ExtraCurricular Activities
    entry.append(random.choice(extracurricular))

    # Native Language
    entry.append(random.choice(native))

    # Secondary Language
    entry.append(random.choice(secondary))

    # Append entry to file
    append(",".join(map(str, entry)))
