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

def test_diary_entry_wpm_not_int():
    entry = DiaryEntry("My Title", "These are the contents")
    with pytest.raises(TypeError) as e:
        entry.reading_time(None)
    assert str(e.value) == "wpm must be an integer"

def test_diary_entry_reading_time_four_words():
    entry = DiaryEntry("My Title", "These are the contents")
    assert entry.reading_time(4) == 1

def test_diary_entry_reading_time_eight_words():
    entry = DiaryEntry("My Title", "One two three four five six seven eight")
    assert entry.reading_time(4) == 2

def test_diary_entry_reading_time_no_words():
    entry = DiaryEntry("My Title", "")
    assert entry.reading_time(4) == 0