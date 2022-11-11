from random import randrange
_i = 0
while _i < 1000:
    score = 0
    doors = ['A', 'B', 'C']

    # Guess random between A, B and C
    def guess_door(known_door:str):
        if not known_door:
            return doors[randrange(0, len(doors))]
        else:
            return known_door

    first_guess_door = guess_door(None)
    print(first_guess_door)

    response = input()
    response_door,reponse_prize = response.split(' ')

    if "1" in response:
        print(guess_door(response.split(' ')[0]))
    else:
        second_guess_door = list(set(doors) - set([response_door, first_guess_door]))[0]
        print(second_guess_door)
    
    score = input()

    _i += 1
