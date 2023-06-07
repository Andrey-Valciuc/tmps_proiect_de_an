import os
from playlist import Playlist, LyricsDecorator
from song_factory import SongFactory
from sort_strategy import SortByTitleStrategy, SortByArtistStrategy
from music_library import MusicLibrary

class MainMenu:
    def __init__(self):
        self.library = MusicLibrary()
        self.song_factory = SongFactory()
        self.sort_strategy = SortByTitleStrategy()
        self.create_initial_data()

    def display_menu(self):
        os.system('cls')
        print("\n=== Music Library Management ===")
        print("1. Add new song")
        print("2. Display music library")
        print("3. Create new playlist")
        print("4. Display playlists")
        print("5. Sort music")
        print("6. Add component to playlist")
        print("7. Display playlist contents")
        print("8. Display songs longer than")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_new_song()
                input("Press Enter to continue...")
            elif choice == "2":
                self.display_music_library()
                input("Press Enter to continue...")
            elif choice == "3":
                self.create_new_playlist()
                input("Press Enter to continue...")
            elif choice == "4":
                self.display_playlists()
                input("Press Enter to continue...")
            elif choice == "5":
                self.sort_music()
                input("Press Enter to continue...")
            elif choice == "6":
                self.add_component_to_playlist()
                input("Press Enter to continue...")
            elif choice == "7":
                self.display_playlist_contents()
                input("Press Enter to continue...")
            elif choice == "8":
                self.display_songs_longer_than()
                input("Press Enter to continue...")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_song(self):
        title = input("\nEnter song title: ")
        artist = input("Enter artist name: ")
        duration = input("Enter song duration: ")
        song_type = input("Enter song type (song/podcast): ")
        song = self.song_factory.create_song(song_type, title, artist, duration)
        self.library.add_song(song)
        print("Song added successfully.")

    def display_music_library(self):
        songs = self.library.songs
        if songs:
            print("\nIterating over Music Library:")
            for song in songs:
                song.play()
        else:
            print("Music library is empty.")

    def create_new_playlist(self):
        name = input("\nEnter playlist name: ")
        playlist = Playlist(name)
        self.library.add_playlist(playlist)
        print("Playlist created successfully.")

    def display_playlists(self):
        playlists = self.library.playlists
        if playlists:
            print("Playlists:")
            for playlist in playlists:
                print(playlist.name)
        else:
            print("No playlists found.")


    def sort_music(self):
        print("\nSort music by:")
        print("1. Title")
        print("2. Artist")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.sort_strategy = SortByTitleStrategy()
        elif choice == "2":
            self.sort_strategy = SortByArtistStrategy()
        else:
            print("Invalid choice. Using default sorting strategy.")

        self.library.songs = self.sort_strategy.sort(self.library.songs)

    def add_component_to_playlist(self):
        playlist_name = input("Enter playlist name: ")
        playlist = self.find_playlist(playlist_name)
        if playlist:
            component_name = input("Enter component name: ")
            component = self.find_component(component_name)
            if component:
                decorated_component = LyricsDecorator(component, "Sample lyrics")
                playlist.add(decorated_component)
                print("Component added to the playlist.")
            else:
                print("Component not found.")
        else:
            print("Playlist not found.")

    def find_component(self, component_name):
        # Search for the component in the library's songs and playlists
        for song in self.library.songs:
            if song.title == component_name:
                return song
        for playlist in self.library.playlists:
            if playlist.name == component_name:
                return playlist
        return None

    def display_playlist_contents(self):
        playlist_name = input("Enter playlist name: ")
        playlist = self.find_playlist(playlist_name)
        if playlist:
            playlist.play()
        else:
            print("Playlist not found.")

    def display_songs_longer_than(self):
        duration_threshold = float(input("Enter duration threshold: "))
        iterator = self.library.get_songs_longer_than(duration_threshold)
        print(f"Songs longer than {duration_threshold}:")
        for song in iterator:
            song.play()

    def find_playlist(self, playlist_name):
        for playlist in self.library.playlists:
            if playlist.name == playlist_name:
                return playlist
        return None

    def create_initial_data(self):
          
            song1 = self.song_factory.create_song("song", "Savior", "Rise Against", 180)
            song2 = self.song_factory.create_song("song", "Bulletproof", "Godsmack", 210)
            song3 = self.song_factory.create_song("song", "Psyhosocial", "Slipknot", 160)
            song4 = self.song_factory.create_song("song", "Out of the Black", "Royal Blood", 230)

        
            podcast1 = self.song_factory.create_song("podcast", "FirstPodcast", "FirstHost", 1800)
            podcast2 = self.song_factory.create_song("podcast", "SecondPodcast", "SecondHost", 2700)

            
            self.library.add_song(song1)
            self.library.add_song(song2)
            self.library.add_song(song3)
            self.library.add_song(song4)
            self.library.add_song(podcast1)
            self.library.add_song(podcast2)