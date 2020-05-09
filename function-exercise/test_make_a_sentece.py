from make_a_sentence import generate, compare, get_best_sentence

def test_generate_to_return_28_chars_sentence():
    assert len(generate()) == 28


def test_compare():
    sentence = "methizzzzzzzzzzzzzzzzzzzzzzz"
    assert compare(sentence) == 17.86


def get_best_sentence():
    pass