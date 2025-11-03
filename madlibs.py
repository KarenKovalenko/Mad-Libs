def main():

    user_pick = int(input(
        "Which story do you want? Enter the number 1-3, or '4' for random story.Enter 5 for exit.\n"
        "1.Hospital\n2.Camping\n3.Castle\n4.Random story\n5.Exit: "))

    if user_pick > 5 or user_pick < 1:
        print("The number must be 1, 2, 3, 4 or 5")

        user_pick = int(input(
            "Which story do you want? Enter the number 1-3, or '4' for random story.Enter 5 for exit.\n"
            "1.Hospital\n2.Camping\n3.Castle\n4.Random story\n5.Exit: "))

    if user_pick == 1:
        print_hospital_story()
    elif user_pick == 2:
        print_camping_story()
    elif user_pick == 3:
        print_castle_story()
    elif user_pick == 4:
        random_story()
    elif user_pick == 5:
        print('Goodbye')


def print_hospital_story():
    while True:
        try:
            number = int(input('Input a number: '))
            break
        except ValueError:
            print('There should be a number here.')
    measure_of_time = input('Input measure of time: ')
    mode_of_transportation = input('Input mode of transportation: ')
    adjective = input('Input adjective: ')
    adjective2 = input('Input another adjective: ')
    noun = input('Input a noun: ')
    color = input('Input a color: ')
    part_of_the_body = input('Input part of the body: ')
    verb = input('Input a verb: ')
    while True:
        try:
            number2 = int(input('Input a number: '))
            break
        except ValueError:
            print('There should be a number here.')
    noun2 = input('Input a noun: ')
    noun3 = input('Input a noun: ')
    part_of_the_body2 = input('Input part of the body: ')
    verb2 = input('Input a verb: ')
    noun4 = input('Input a noun: ')
    adjective3 = input('Input another adjective: ')
    silly_word = input('Input a silly word: ')
    noun5 = input('Input a noun: ')

    return print('Here is the story that you created.\n '
                 ''f"""It was about {number} {measure_of_time} ago when I arrived at the hospital 
        in a {mode_of_transportation}. The hospital is a/an {adjective} place, 
        there are a lot of {adjective2} {noun} here. There are nurses here who have 
        {color} {part_of_the_body}. If someone wants to come into my room 
        I told them that they have to {verb} first. I have decorated my room with {number2} 
        {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their
        {part_of_the_body2}. I heard that all doctors {verb2} {noun4} every day for breakfast. 
        The most {adjective3} thing about being in the hospital is the {silly_word} {noun5} !""")


def print_camping_story():
    person_name = input('Input a proper noun (Person Name: ')
    noun = input('Input a noun: ')
    adjective = input('Input adjective (Feeling): ')
    verb = input('Input a verb: ')
    adjective2 = input('Input another adjective (Feeling) : ')
    animal = input('Input a animal: ')
    verb2 = input('Input a verb: ')
    color = input('Input a color: ')
    verb3 = input('Input a verb (ending in ing): ')
    adverb = input('Input adverb (ending in ly): ')
    while True:
        try:
            number = int(input('Input a number: '))
            break
        except ValueError:
            print('There should be a number here.')
    measure_of_time = input('Input measure of time: ')
    color2 = input('Input a color: ')
    animal2 = input('Input a animal: ')
    while True:
        try:
            number2 = int(input('Input a number: '))
            break
        except ValueError:
            print('There should be a number here.')
    silly_word = input('Input a silly word: ')
    noun2 = input('Input a noun: ')

    return print('Here is the story that you created.\n '
                 ''f"""This weekend I am going camping with {person_name}. 
         I packed my lantern, sleeping bag, and {noun}. I am so {adjective} to {verb} in a tent. 
         I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous. 
         While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} 
         lake is great for {verb3}. Then we will {adverb} hike through 
         the forest for {number} {measure_of_time}. If I see a {color2} {animal2} while hiking, I am going 
         to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast 
         {noun2} around the campfire!!""")


def print_castle_story():
    person_name = input('Input a proper noun (Person Name: ')
    adjective = input('Input adjective: ')
    color = input('Input a color: ')
    animal = input('Input a animal: ')
    place = input('Input thr place: ')
    adjective2 = input('Input another adjective: ')
    magical_creature = input('Input the magical creature (Plural): ')
    adjective3 = input('Input another adjective: ')
    magical_creature2 = input('Input the magical creature (Plural): ')
    room = input('Input the room in a house: ')
    noun = input('Input a noun: ')
    noun2 = input('Input a noun: ')
    noun3 = input('Input a noun(Plural): ')
    adjective4 = input('Input adjective: ')
    noun4 = input('Input a noun(Plural): ')
    while True:
        try:
            number = int(input('Input a number: '))
            break
        except ValueError:
            print('There should be a number here.')
    measure_of_time = input('Input measure of time: ')
    verb = input('Input a verb (ending in ing): ')
    adjective5 = input('Input adjective: ')
    noun5 = input('Input a noun: ')

    return print('Here is the story that you created.\n '
                 ''f"""Dear {person_name}, I am writing to you from a {adjective} 
        castle in an enchanted forest. I found myself here one day after going for a ride 
        on a {color} {animal} in {place}. There are {adjective2} {magical_creature}
        and {adjective3} {magical_creature2} here! In the {room} there is 
        a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} and 
        dream of {adjective4} {noun4}. It feels as though I have lived here for 
        {number} {measure_of_time}. I hope one day you can visit, although the only way to get
        here now is {verb} on a {adjective5} {noun5}!!""")


def random_story():
    import random

    story = random.randint(1, 3)
    if story == 1:
        print_hospital_story()
    elif story == 2:
        print_camping_story()
    else:
        print_castle_story()


main()
