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
    return score/28


def run():
    count = 0
    score_string = {}
    sentence = generate()
    best = 0
    score = compare(sentence)

    while score < 1:
        if score > best:
            if count % 1_000_000 == 0:
                print(score, sentence)
        sentence = generate()
        score = compare(sentence)
        count += 1
    

if __name__ == "__main__":
    run()