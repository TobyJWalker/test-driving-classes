class MusicTracker():
    def __init__(self):
        self._tracks = []
    
    def add_track(self, track):
        if type(track) != str:
            raise TypeError('Track must be a string')
        elif track == "" or track.isspace():
            raise ValueError('Track must not be empty')
        self._tracks.append(track)
    
    def list_tracks(self):
        return self._tracks