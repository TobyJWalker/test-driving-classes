import pytest
from lib.music_tracker import MusicTracker

def test_music_tracker_initiation():
    tracker = MusicTracker()
    assert tracker._tracks == []

def test_music_tracker_add_number():
    with pytest.raises(TypeError) as e:
        tracker = MusicTracker()
        tracker.add_track(1)
    assert str(e.value) == 'Track must be a string'

def test_music_tracker_add_none():
    with pytest.raises(TypeError) as e:
        tracker = MusicTracker()
        tracker.add_track(None)
    assert str(e.value) == 'Track must be a string'

def test_music_tracker_add_empty_string():
    with pytest.raises(ValueError) as e:
        tracker = MusicTracker()
        tracker.add_track("")
    assert str(e.value) == 'Track must not be empty'

def test_music_tracker_add_space():
    with pytest.raises(ValueError) as e:
        tracker = MusicTracker()
        tracker.add_track(" ")
    
def test_music_tracker_add_track():
    tracker = MusicTracker()
    tracker.add_track("track")
    assert tracker._tracks == ["track"]

def test_music_tracker_add_multiple_tracks():
    tracker = MusicTracker()
    tracker.add_track("track1")
    tracker.add_track("track2")
    assert tracker._tracks == ["track1", "track2"]

def test_music_tracker_list_empty_track():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

def test_music_tracker_list_tracks():
    tracker = MusicTracker()
    tracker.add_track("track1")
    tracker.add_track("track2")
    assert tracker.list_tracks() == ["track1", "track2"]