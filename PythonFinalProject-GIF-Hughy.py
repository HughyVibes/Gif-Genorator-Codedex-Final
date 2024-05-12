import imageio.v3 as iio

# disregard the different random variables among the lines of "Q1" "dcQQ", it was late and was in my own world lol

# Initial Welcoming. Choosing of animal
print('Hello!')
print('Please choose either Dog or Cat by typing their indicated number below.')

dcQQ = False

while not dcQQ:
    animalquestion = int(input('(1) - Dogs!\n(2) - Cats!\n'))

    if animalquestion == 1:
        dcQQ = True
    elif animalquestion == 2:
        dcQQ = True
    else:
        print('Invalid input. Please enter 1 for Dog or 2 for Cat.')

dcQ = True

while dcQ:
    # Different Paths of questions and generated answers / gif
    if animalquestion == 1:  # dog
        filename = ['dog-blank.jpg', 'dog-happy.jpg']
        images = []

        Q1 = True
        while Q1:
            print('Hmmmm ok, and how energetic do you feel today?')
            dogfeelingQ = int(input('(1) - Lazy\n(2) - Normal\n(3) - Pumped!\n'))

            if dogfeelingQ in [1, 2, 3]:
                moodwordhold = ['Lazy', 'Normal', 'Pumped'][dogfeelingQ - 1]
                Q1 = False
                dcQ = False
            else:
                print('Invalid input. Please enter a number between 1 and 3.')

        # creates the actual gif
        for filename in filename:
            images.append(iio.imread(filename))

        durations = [900, 400, 125]
        iio.imwrite('doggy.gif', images, duration=durations[dogfeelingQ - 1], loop=0)

        print(f'Well Chosen! Seeing that you like Dogs and are feeling {moodwordhold},\n'
              f'I have left a special suprise in your installed folder titled "doggy" that should fit your mood.')

    elif animalquestion == 2:  # Cat
        filename = ['cat-down.jpg', 'cat-angry.jpg']
        images = []

        Q2 = True
        while Q2:
            print('Hmmmm ok, and how mad are you feeling today?')
            CatfeelingQ = int(input('(1) - Mad\n(2) - Very Mad\n(3) - Rage Monster\n'))

            if CatfeelingQ in [1, 2, 3]:
                moodwordhold = ['Mad', 'Very Mad', 'Rage Monster'][CatfeelingQ - 1]
                Q2 = False
                dcQ = False
            else:
                print('Invalid input. Please enter a number between 1 and 3.')

        # creates the actual gif
        for filename in filename:
            images.append(iio.imread(filename))

        durations = [900, 400, 125]
        iio.imwrite('cat.gif', images, duration=durations[CatfeelingQ - 1], loop=0)

        print(f'Well Chosen! Seeing that you like Cats and are feeling {moodwordhold},\n'
              f'I have left a special suprise in your installed folder titled "cat" that should fit your mood.')

    else:
        print('That is not an option! Please enter a valid number.')
        dcQ = True
