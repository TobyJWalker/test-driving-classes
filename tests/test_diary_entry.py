import pytest
from lib.diary_entry import *

def test_diary_entry_title_not_string():
    with pytest.raises(TypeError) as e:
        entry = DiaryEntry(None, "contents")
    assert str(e.value) == "title must be a string"

def test_diary_entry_content_not_string():
    with pytest.raises(TypeError) as e:
        entry = DiaryEntry("title", None)
    assert str(e.value) == "contents must be a string"

def test_diary_entry_format():
    entry = DiaryEntry("My Title", "These are the contents")
    assert entry.format() == "My Title: These are the contents"

def test_diary_entry_count_five_words():
    entry = DiaryEntry("My Title", "One two three four five")
    assert entry.count_words() == 5

def test_diary_entry_count_no_words():
    entry = DiaryEntry("My Title", "")
    assert entry.count_words() == 0