import pytest
from lib.grammar_stats import *

def test_grammar_stats_text_not_string():
    stats = GrammarStats()
    with pytest.raises(TypeError) as e:
        stats.check(None)
    assert str(e.value) == "text must be a string"

def test_grammar_stats_first_letter_capital():
    stats = GrammarStats()
    assert stats.check("Hello!") == True

def test_grammar_stats_first_letter_not_capital():
    stats = GrammarStats()
    assert stats.check("hello!") == False

def test_grammar_stats_last_char_punctuation():
    stats = GrammarStats()
    assert stats.check("Hello!") == True

def test_grammar_stats_last_char_not_punctuation():
    stats = GrammarStats()
    assert stats.check("Hello") == False