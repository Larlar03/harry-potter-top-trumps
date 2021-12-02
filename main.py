import requests
import random


def random_student():
    student_number = random.randint(1, 79)

    url = 'http://hp-api.herokuapp.com/api/characters/students'

    response = requests.get(url)

    student_list = response.json()

    student = student_list[student_number]

    return {
        'name': student['name'],
        'house': student['house'],
        'ancestry': student['ancestry'],
        'wand': student['wand']['length'],
    }


def run():
    players_student = random_student()

    print('You have been given {} from {}'.format(players_student['name'], players_student['house']))

    opponents_student = random_student()

    print('The opponent chose {} from {}'.format(opponents_student['name'], opponents_student['house']))

    stat_choice = input('Which stat do you want to test against your opponent? (ancestry or wand_length?) ')

    players_stat = players_student[stat_choice]

    opponents_stat = opponents_student[stat_choice]

    def ancestry_stat():
        if players_stat == 'pure-blood' and opponents_stat == 'pure-blood':
            print('Draw. You are both pure-blood.')
        elif players_stat == 'pure-blood' and not opponents_stat == 'pure-blood':
            print('You win! You\'re pure-blood and the opponent is {}'.format(opponents_stat))
        elif opponents_stat == 'pure-blood' and not players_stat == 'pure-blood':
            print('You lose! You\'re {} and the opponent is pure-blood'.format(players_stat))
        elif players_stat == 'half-blood' and opponents_stat == 'half-blood':
            print('Draw. You are both half-blood.')
        elif players_stat == 'half-blood' and opponents_stat == 'muggleborn':
            print('You win! You\'re half-blood and the opponent is {}'.format(opponents_stat))
        elif players_stat == 'half-blood' and opponents_stat == 'pure-blood':
            print('You lose! You\'re {} and the opponent is pure-blood'.format(players_stat))
        elif players_stat == 'muggleborn' and opponents_stat == 'muggleborn':
            print('Draw. You are both muggleborn.')
        elif players_stat == 'muggleborn' and not opponents_stat == 'muggleborn':
            print('You lose! You\'re muggle-born and the opponent is {}'.format(opponents_stat))
        else:
            print('We don\'t have yours or your players ancestry details. Please play again')

    def wand_stat():
        if players_stat > opponents_stat:
            print('You win! Your wand length is {} and the opponents is {}.'.format(players_stat, opponents_stat))
        elif players_stat < opponents_stat:
            print('You lose! Your wand length is {} and the opponents is {}.'.format(players_stat, opponents_stat))
        elif players_stat == opponents_stat:
            print('It\'s a draw. You both have a wand length of {}'.format(players_stat))
        elif players_stat or opponents_stat == '':
            print('We don\'t have the measurements of either yours or your players wand length. Please play again.')

    def wand_or_ancestry():
        if stat_choice == 'wand':
            wand_stat()
        elif stat_choice == 'ancestry':
            ancestry_stat()

    wand_or_ancestry()


run()
