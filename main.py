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
    def top_songs(self):
        top_5_songs = self.spotify['trackName'].value_counts()[:5]
        top_5_songs.to_csv('/home/aziz/Documents/spotify/top_5_songs.csv')
        with open('/home/aziz/Documents/spotify/top_5_songs.csv' , 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            file.writelines(lines[1:])
        file.close
        with open('/home/aziz/Documents/spotify/top_5_songs.csv', 'r') as original: data = original.read()
        with open('/home/aziz/Documents/spotify/top_5_songs.csv', 'w') as modified: modified.write("trackName,count\n" + data)
    def top_artist():
        pass
    def top_artist_every_3_month():
        pass
if __name__ == '__main__':
    Spotify.top_songs()
    Spotify.top_artist()
    Spotify.top_artist_every_3_month()
