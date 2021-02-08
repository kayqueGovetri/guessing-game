import random


def play():
    print_first_message()
    secret_number = random.randrange(1, 101)
    points = 1000
    total_attempts = calculate_total_attempts()

    for game_round in range(1, total_attempts + 1):
        print("Round {} in {}".format(game_round, total_attempts))

        shot = capture_shot()

        if shot < 1 or shot > 100:
            print("You must enter a number between 0 and 100")
            continue

        hit = shot == secret_number
        bigger = shot > secret_number
        smaller = shot < secret_number

        if hit:
            print("You got it right!")
            break
        else:
            points = shot_error(bigger, smaller, secret_number, shot, points)

    print("Total points: {}".format(points))
    print("Finish game")


def print_first_message():
    print("*********************************")
    print("***Welcome the guessing game!****")
    print("*********************************")


def calculate_total_attempts():
    print("What is the level of difficulty??")
    print("(1) Easy (2) Normal (3) Hard")

    level = int(input("Set the difficulty level: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    return total_attempts


def capture_shot():
    shot_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", shot_str)
    return int(shot_str)


def shot_error(bigger, smaller, secret_number, shot, points):
    if bigger:
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif smaller:
        print("Você errou! O seu chute foi menor do que o número secreto.")
    lost_points = abs(secret_number - shot)
    return points - lost_points


if __name__ == "__main__":
    play()
