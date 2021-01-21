import spotipy
import pandas as pd
import numpy
import time
import matplotlib
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="56ab3cc7108646a98b183042b661114b",
                                                           client_secret="17fda25e18164fbcb133a6621e453242"))

track_id = '6j4w8O8gEseBUZTOo8vYMK'
feat_results = sp.audio_analysis(track_id)

df = pd.DataFrame(feat_results["segments"])

df.drop(columns=['confidence', 'pitches', 'loudness_start', 'loudness_end', 'loudness_max','loudness_max_time','duration',])

df["average_timbre"] = df["timbre"].apply(numpy.mean)

# min, max, median, std, count
c = df["average_timbre"]


#plotting graph

t = df["start"]
s = df["average_timbre"]

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='timbre (Hertz)',
       title='Side to Side audio analysis')
ax.grid()

fig.savefig("test.png")
plt.show()

# looking up the start time of Nicki's verse

start_verse_timbre = c[424]
#median_verse_timbre = c[453]
end_verse_timbre = c[490]

print(df)

df.to_csv('audio_analysis.csv')

print(c.describe())

print(start_verse_timbre)
#print(median_verse_timbre)
print(end_verse_timbre)

# start time and end time
start_time = 2.14*60
print('Nicki Minajs verse ends at {} seconds'.format(start_time))

end_time = 2.51*60
print('Nicki Minajs verse ends at {} seconds'.format(end_time))




