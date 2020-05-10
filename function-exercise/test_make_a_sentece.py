from make_a_sentence import generate, compare, get_best_string

def test_generate_to_return_28_chars_sentence():
    assert len(generate()) == 28


def test_compare():
    sentence = "methizzzzzzzzzzzzzzzzzzzzzzz"
    assert compare(sentence) == 17.86


def test_get_best_string():
    strings_scores = {
        3.57: "mzzzzzzzzzzzzzzzzzzzzzzzzzzz",
        7.14: "mezzzzzzzzzzzzzzzzzzzzzzzzzz",
        10.71: "metzzzzzzzzzzzzzzzzzzzzzzzzz",
        14.29: "methzzzzzzzzzzzzzzzzzzzzzzzz",
        17.86: "methizzzzzzzzzzzzzzzzzzzzzzz"
    }
    assert get_best_string(strings_scores) == "methizzzzzzzzzzzzzzzzzzzzzzz"
