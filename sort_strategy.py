class MusicSortStrategy:
    def sort(self, songs):
        pass


class SortByTitleStrategy(MusicSortStrategy):
    def sort(self, songs):
        return sorted(songs, key=lambda x: x.title)


class SortByArtistStrategy(MusicSortStrategy):
    def sort(self, songs):
        return sorted(songs, key=lambda x: x.artist)