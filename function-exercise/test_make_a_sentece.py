from make_a_sentence import generate, compare

def test_generate_to_return_28_chars_sentence():
    assert len(generate()) == 28


def test_compare():
    sentence = "methizzzzzzzzzzzzzzzzzzzzzzz"
    assert compare(sentence) == 5/28 
