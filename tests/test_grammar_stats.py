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

def test_grammar_stats_percent_good_all_correct():
    stats = GrammarStats()
    stats.check("Hello!")
    stats.check("Hello!")
    stats.check("Hello!")
    assert stats.percentage_good() == 100

def test_grammar_stats_percent_good_all_incorrect():
    stats = GrammarStats()
    stats.check("hello")
    stats.check("hello!")
    stats.check("Hello")
    assert stats.percentage_good() == 0

def test_grammar_stats_percent_half_correct():
    stats = GrammarStats()
    stats.check("Hello!")
    stats.check("hello")
    assert stats.percentage_good() == 50