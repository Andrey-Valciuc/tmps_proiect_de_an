
class MusicLibrary:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.songs = []
            cls._instance.playlists = []
        return cls._instance

    def add_song(self, song):
        self.songs.append(song)

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def display_songs(self):
        print("Music Library:")
        for song in self.songs:
            print(song.title)

    def display_playlists(self):
        print("Playlists:")
        for playlist in self.playlists:
            print(playlist.name)

    def get_songs_longer_than(self, duration_threshold):
        return MusicDurationIterator(self.songs, duration_threshold)


class MusicDurationIterator:
    def __init__(self, songs, duration_threshold):
        self.songs = songs
        self.duration_threshold = duration_threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.songs):
            song = self.songs[self.index]
            self.index += 1
            if float(song.duration) > self.duration_threshold:
                return song
        raise StopIteration
