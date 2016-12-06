
easy_question = "__1__ is a transparent and nearly colorless chemical substance that is the main constituent of Earth's streams, lakes, and oceans, and the fluids of most living organisms. \n" \
                "Its chemical formula is H2O, meaning that its molecule contains one __2__ and two hydrogen atoms, \n" \
                "that are connected by covalent bonds. __1__ strictly refers to the liquid state of that substance, \n" \
                "that prevails at standard ambient temperature and pressure; but it often refers also to its solid state (__3__) or its gaseous state (__4__ or water vapor). \n" \
                "It also occurs in nature as snow, glaciers, ice packs and icebergs, clouds, fog, dew, aquifers, and atmospheric humidity."

easy_answers = [
    'Water',
    'oxygen',
    'ice',
    'steam']


medium_question = "\nThe __1__ is the star at the center of the Solar System.\n "\
                  "It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process.\n"\
                  "It is by far the most important source of energy for life on __2__.\n"\
                  "Its diameter is about 109 times that of __2__, and its mass is about 330,000 times that of __2__, accounting for about 99.86% of the total mass of the Solar System.\n"\
                  "About three quarters of the __1__\'s mass consists of __3__ (~73%); the rest is mostly __4__ (~25%), with much smaller quantities of heavier elements, including oxygen, carbon, neon, and iron."
                  
                  
medium_answers = [
    'Sun',
    'Earth',
    'hydrogen',
    'helium'
    ]
hard_question = "\n__1__ employs techniques and theories drawn from many fields within the broad areas of mathematics, statistics, __2__(OR),\n"\
                "information science, and __3__(CS), including signal processing, probability models, __4__ learning, statistical learning, data __5__, \n"\
                "database, data engineering, pattern recognition and learning, visualization, predictive analytics, uncertainty modeling, data warehousing, data compression, \n"\
                "computer programming, __6__ intelligence, and high performance computing.\n"\
                "Methods that scale to __7__ data are of particular interest in data science, although the discipline is not generally considered to be restricted to such __7__ data, \n"\
                "and __7__ data technologies are often focused on organizing and preprocessing the data instead of analysis. \n"\
                "The development of machine learning has enhanced the growth and importance of data science."

hard_answers = [
    'Data science',
    'operation research',
    'computer science',
    'machine',
    'mining',
    'artificial',
    'big']


def get_level():
    '''
    This function is designed to take player's input and specify the level of the game.
    :return: will return a string as player types in.
    '''
    display = 'Please choose the level of the game.\n'
    display += 'Please choose from "easy", "medium" or "hard".\n'
    level_list = ['easy', 'medium', 'hard']
    input_level = raw_input(display).lower()    # in case the input are not in lower case
    while input_level not in level_list:
        print 'Invalid choice, please choose your game level again.\n'
        input_level = raw_input(display).lower()    # input level again
    print 'OK! '+ input_level + ' is chosen.'
    return input_level


def get_question_and_answers(level):
    '''
    obtain the pair of question and answers

    :param level: a string with 3 levels
    :return: a pair of corresponding question and answer
    '''
    if level == 'easy':
        return (easy_question, easy_answers)
    if level == 'medium':
        return (medium_question, medium_answers)
    if level == 'hard':
        return (hard_question, hard_answers)
    raise ValueError('Invalid input level. Please double check.')


def display_question(question, target_blank, chances_left, max_tries):
    '''
    Output the prompt for player.

    :param question: the question chosen previously, a long string
    :param target_blank: string, constructed inside update_question
    :param chances_left: num, number of chances left
    :param max_tries: num, number of the total available chances
    :return: str, question with related prompt
    '''

    last_chance_indicator = 1
    prompt = '\nThe current paragraph reads as such:\n{}\n\n'
    prompt += 'What should be substituted in for {}? '
    prompt = prompt.format(question, target_blank)
    if chances_left == max_tries:
        return prompt
    new_prompt = ''
    if chances_left > last_chance_indicator:
        new_prompt += "Let's try again; you have {} tries left!\n\n"
    else:
        new_prompt += 'You only have {} try left!\n\n'
    return new_prompt.format(chances_left) + prompt



def update_question(question, blank_num, answer, max_attempts):
    '''
    Update the displaying question according to player's guesses.

    :param question: a long string, the chosen question with unfilled blanks.
    :param blank_num: integer, specifying the number of the blank.
    :param answer: list of the answers.
    :param max_attempts: integer, the total number of chances
    :return: tuple, containing updated question and blank number
    '''

    last_chance_indicator = 1
    chances_left = max_attempts
    target_blank = '__' + str(blank_num) + '__'
    prompt = display_question(question, target_blank, chances_left, max_attempts)
    player_guess = raw_input(prompt).lower()
    while player_guess != answer.lower() and chances_left > last_chance_indicator:
        chances_left -= 1
        prompt = display_question(question, target_blank, chances_left, max_attempts)
        player_guess = raw_input(prompt).lower()
    if chances_left > last_chance_indicator:
        print '\nCorrect!\n'
        return (question.replace(target_blank, answer), blank_num + 1)
    else:
        return (None, blank_num + 1)



def find_max_guesses():
    '''
    Let player become able to choose the number of maximum tries.

    :return: num, number of total guesses as player specifies.
    '''
    display = 'Please specify maximum number of guesses.\n'
    times = raw_input(display).lower()

    return times


def play_game():
    '''
    The main function that controls the flow of the game

    :return: logical, indicating win or loss. 
    '''
    difficulty = get_level()
    (question, answers) = get_question_and_answers(difficulty)
    max_guesses = int(find_max_guesses())
    current_blank = 1
    while current_blank <= len(answers):
        (question, current_blank) = update_question(question, current_blank, answers[current_blank - 1], max_guesses)
        if question is None:
            print "You've failed too many straight guesses!  Game over!"
            return False
    print question + '\nYou won!\n'
    return True



play_game()

