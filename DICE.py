# ● \u25CF
# ┌ \u250C
#  ─ \U2500
# ┐ \U2510
# │ \U2502
# └ \U2514
# ┘ \U2518

#● ┌ ─ ┐ │ └ ┘
import random
art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

all_dice = []
sum = 0
num_of_dice = int(input("Enter the dice number: "))

for die in range(num_of_dice):
    all_dice.append(random.randint(1, 6))

# PRINT VERTICALLY
# for die in range(num_of_dice):3
#    for line in dice_art.get(dice[die]):
#        print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in all_dice:
        print(art.get(die)[line], end="")
    print()

for die in all_dice:
    sum += die
print(f"Sum: {sum}")