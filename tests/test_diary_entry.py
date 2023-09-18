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