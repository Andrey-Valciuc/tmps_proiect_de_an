class PlaylistComponent:
    def add(self, component):
        raise NotImplementedError()

    def play(self):
        raise NotImplementedError()


class MusicTrack(PlaylistComponent):
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print("Song:", self.title, "by", self.artist)


class Podcast(PlaylistComponent):
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print("Podcast:", self.title, "by", self.artist)


class LyricsDecorator(PlaylistComponent):
    def __init__(self, song, lyrics):
        self.song = song
        self.lyrics = lyrics

    def play(self):
        self.song.play()
        self.display_lyrics()

    def display_lyrics(self):
        print("Lyrics:\n", self.lyrics)


class Playlist(PlaylistComponent):
    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add(self, component):
        self.playlist.append(component)

    def play(self):
        print("Playlist:", self.name)
        for item in self.playlist:
            item.play()