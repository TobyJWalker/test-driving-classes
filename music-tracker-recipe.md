
>> PURPOSE

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

>> CLASS DESIGN

class MusicTracker():
    def __init__():
        Purpose: Create a empty list of music tracks
        Input: None
        Output: None
        Errors: None
    
    def add_track():
        Purpose: Add a track to the list
        Input: track (string)
        Output: None
        Errors: TypeError, ValueError

    def list_tracks():
        Purpose: Return a list of tracks
        Input: None
        Output: tracks (list)
        Errors: None

>> TESTS

>> When initialised, the class creates an empty list from music tracks
tracker = MusicTracker()
tracker._tracks => []

>> When adding a track, raise an error if the input is not a string
tracker.add_track(1) => TypeError
tracker.add_track(None) => TypeError

>> When adding a track, raise an error if the string is empty or only space
tracker.add_track('') => ValueError
tracker.add_track(' ') => ValueError

>> When adding a track, add the track to the list
tracker.add_track('track 1')
tracker._tracks => ['track 1']
tracker.add_track('track 2')
tracker._tracks => ['track 1', 'track 2']

>> When listing tracks, return empty list if no tracks present
tracker.list_tracks() => []

>> When listing tracks, whole list of tracks is returned
tracker.add_track('track 1')
tracker.add_track('track 2')
tracker.list_tracks() => ['track 1', 'track 2']