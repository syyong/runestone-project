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


def get_best_string(score_string):
    best_score = max(score_string.keys())
    return best_score, score_string[best_score]


def run():
    count = 0
    score_string = {}
    sentence = generate()
    while compare(sentence) < 1:
        sentence = generate()
        score = compare(sentence)
        score_string[score] = sentence
        if count == 1000:
            print(get_best_string(score_string))
            score_string = {}
            count = 0
        count += 1
    

if __name__ == "__main__":
    run()