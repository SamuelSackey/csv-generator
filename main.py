"""Main File"""
import random
from fileio import *
from values import *

NUMBER_OF_RECORDS = 10

FIELDS = "Gender,Age,Wassce Aggregate,Bece Aggregate,Preferred Program,cut-off point,Dream Job;Favorite Subject 1,Favorite Subject 2,Favorite Subject 3,Interests,Learning Style,ExtraCurricular Activities,Native Language,Secondary Language\n"

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

    # Append entry to file
    append(",".join(map(str, entry)))
