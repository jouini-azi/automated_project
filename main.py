import pandas as pd
class Spotify():
    def __init__(self):
        self.spotify = pd.read_csv('Spotify_data.csv' , encoding="ISO-8859-1")
        print(self.spotify.columns)
        self.spotify.drop(columns=['segPlayed' , 'minPlayed','mesAño'] , inplace= True)
        self.spotify['time'] = ''
        self.spotify = self.spotify[['endTime','time','artistName','trackName','msPlayed']]
        for i in range(self.spotify.shape[0]):
            pos = self.spotify.loc[i,'endTime'].rfind(' ') 
            self.spotify.loc[i,'time'] = self.spotify.loc[i,'endTime'][pos+1:]
            self.spotify.loc[i,'endTime'] = self.spotify.loc[i,'endTime'][:pos]
    def delete_the_first_line_in_file(self,ch):
        with open('/home/aziz/Documents/spotify/'+ch+'.csv' , 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            file.writelines(lines[1:])
        file.close
    def top_songs(self):
        top_5_songs = self.spotify['trackName'].value_counts()[:5]
        top_5_songs.to_csv('/home/aziz/Documents/spotify/top_5_songs.csv')
        self.delete_the_first_line_in_file('top_5_songs')
        with open('/home/aziz/Documents/spotify/top_5_songs.csv', 'r') as file: data = file.read()
        with open('/home/aziz/Documents/spotify/top_5_songs.csv', 'w') as file: file.write("trackName,count\n" + data)
    def the_most_listned_song_artist(self):
        maximum =  self.spotify['msPlayed'].max()
        most_listened_music = self.spotify[self.spotify['msPlayed']==maximum]['trackName']
        most_listened_music.to_csv('/home/aziz/Documents/spotify/the_most_listned_song_artist.csv')
        self.delete_the_first_line_in_file('the_most_listned_song_artist')
        with open('/home/aziz/Documents/spotify/the_most_listned_song_artist.csv', 'r') as file: data = file.read()
        with open('/home/aziz/Documents/spotify/the_most_listned_song_artist.csv', 'w') as file: file.write("msPlayed,trackName\n" + data)
    def top_artist_every_3_month(self):
        pass
if __name__ == '__main__':
    top_songs = Spotify().top_songs()
    the_most_listned_song_artist = Spotify().the_most_listned_song_artist()
    top_artist_every_3_month = Spotify().top_artist_every_3_month()
