from make_a_sentence import generate, compare, get_best_string

def test_generate_to_return_28_chars_sentence():
    assert len(generate()) == 28


def test_compare():
    sentence = "methizzzzzzzzzzzzzzzzzzzzzzz"
    assert compare(sentence) == 5/28 


def test_get_best_string():
    score_string = {
        1/28: "mzzzzzzzzzzzzzzzzzzzzzzzzzzz",
        2/28: "mezzzzzzzzzzzzzzzzzzzzzzzzzz",
        3/28: "metzzzzzzzzzzzzzzzzzzzzzzzzz",
        4/28: "methzzzzzzzzzzzzzzzzzzzzzzzz",
        5/28: "methizzzzzzzzzzzzzzzzzzzzzzz"
    }
    assert get_best_string(score_string) == (0.17857142857142858, 'methizzzzzzzzzzzzzzzzzzzzzzz')
