import random
import string

def generate():
    chars = [i for i in string.ascii_lowercase] + [' ']
    return ''.join([random.choice(chars) for i in range(28)])


def compare(sentence):
    goal = "methinks it is like a weasel"
    score = 0
    for i in range(28):
        if goal[i] == sentence[i]:
            score += 1
    return round(score/28*100, 2)


def get_best_sentence():
    pass


def run():
    count = 0
    while True:
        sentence = generate()
        score = compare(sentence)
        if score == 100:
            print(sentence)
            break
        elif count == 1000:
            get_best_sentence()
            print(score)
        count += 1
    

if __name__ == "__main__":
    run()