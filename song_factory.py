from playlist import MusicTrack, Podcast


class SongFactory:
    def create_song(self, song_type, title, artist, duration):
        if song_type == "song":
            return MusicTrack(title, artist, duration)
        elif song_type == "podcast":
            return Podcast(title, artist, duration)
        else:
            raise ValueError("Invalid song type.")