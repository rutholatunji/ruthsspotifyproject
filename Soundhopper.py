#!/usr/bin/env python
# coding: utf-8

# # Using Spotify's audio analysis to find the starting point of Nicki Minaj's verse in Side to Side by Ariana Grande

# ### Step 1: To begin I used pip to install spotipy

# In[3]:


pip install spotipy


# ### Step 2: Then I imported spotipy, and authorised it using my client creditionals.

# #### I imported pandas to make a dataframe to make the data more manageable

# In[2]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="56ab3cc7108646a98b183042b661114b",
                                                           client_secret="17fda25e18164fbcb133a6621e453242"))

track_id = '6j4w8O8gEseBUZTOo8vYMK'
feat_results = sp.audio_analysis(track_id)

import pandas as pd


df = pd.DataFrame(feat_results["segments"])
df


# ### Step 3: I wanted to access the timbre of the audio since that is unique to everyone regardless of the backing track/beat/instrumental
# 
# #### "Vocal Timbre, or as it is described as the quality of that tone utilizing complex overtones, or sound waves, is that unique “something” that gives color and personality to your voice, and how it is recognized."
# 
# #### Every voice has its own distinguished timbre

# In[3]:


df.drop(columns=['confidence', 'pitches', 'loudness_start', 'loudness_end', 'loudness_max','loudness_max_time','duration',])


# ### Step 4: The results returned the timbre in the form of a list so I calculated the average using a for loop

# In[4]:


for feat_results in feat_results["segments"]:
    
    print(sum(feat_results["timbre"]))


# ### Step 5:  I calculated the start of Nicki's verse manually by listening and using some calculations 

# In[9]:


start_time = 2.14*60
print('Nicki Minajs verse ends at {} seconds'.format(start_time))

end_time = 2.51*60
print('Nicki Minajs verse ends at {} seconds'.format(end_time))


# ### Step 6: I extracted the data I needed manually then exported it to csv

# In[7]:


compare_timbre = pd.read_csv("audio_analysis.csv")
compare_timbre


# ### Step 7: Then I did some data analysis to find a trend

# In[8]:


compare_timbre.describe()


# ### Step 8: The maximum and mininum values stood out to me - because Timbre values fluctuate a lot I wanted to find the "outliers" 
# #### Following this I plotted a graph with this data

# <img src="graphproject.png">

# ### Step 9: I calculated the biggest difference in timbre

# In[9]:


(compare_timbre['full_timbre_Hz'] - compare_timbre['nicki_timbre_Hz']).idxmax()


# ### Step 10: Then I found the time stamps greater than or equal to 197 Hz

# In[13]:


compare_timbre[compare_timbre['nicki_timbre_Hz'] >= 197]


# In[10]:


compare_timbre.iloc[424,0]


# #### This timestamp was about 0.6 seconds from the start of nicki's verse that I had calculated prior

# In[24]:


timestamp_cal = compare_timbre.iloc[424,0]
print(timestamp_cal)

difference = timestamp_cal - start_time

print(difference)


# ### Step 11: Then I had a look at the minimum and maximum values

# In[15]:


compare_timbre.groupby(['full_timbre_Hz']).min()


# ### Step 12: On average Nicki had a lower timbre and the minimum timbre of the song was recorded during her verse

# In[62]:


compare_timbre[compare_timbre['nicki_timbre_Hz'] == -419.985]


# In[17]:


compare_timbre.iloc[490,0]


# #### This was approximately 2.6 seconds shorter than the end time I calculated.

# In[33]:


end_time_cal = compare_timbre.iloc[490,0]
end_verse = end_time - end_time_cal
print(end_verse)


# ### Step 13: The median time I calculated was 1 second off the time when the max timbre recorded during Nicki's verse

# In[36]:


median = start_time + end_time
median_time = median/2
print(median_time)


# In[38]:


compare_timbre[compare_timbre['Time_s'] == 138.38992]


# In[37]:


compare_timbre.iloc[453,0]


# In[39]:


print(median_time - compare_timbre.iloc[453,0])


# ### In conclusion:
# 
# #### 1. The biggest difference in timbre was 197Hz, at 129.02150s - where Nicki's verse starts.
# 
# #### 2. The maximum timbre during Nicki's verse was 404.496 Hz - recorded at 138.38992s, in the middle of her verse.
# 
# #### 3. The minimum timbre for the whole song was -419.985 Hz at 148.03810s where Nicki Minajs verse ends.
# 
# #### I wanted to use this data to create a code for a user but I found it quite difficult since the timbre was in a nested list, and the numbers within the list fluctuated.

# ### Instead I created a user led spotify search code.

# In[8]:


user_artist = input('What artist are you looking for? ')

user_track_no = int(input('How many tracks? '))

results = sp.search(q='{}'.format(user_artist), limit='{}'.format(user_track_no))
for idx, track in enumerate(results['tracks']['items']):

    print(idx, track['name'])


# # My spotify developer dashboard

# <img src="spotifydeveloper.png">

# ### The end!
