import datetime
from db import getProjections,getMovieDetails


now = datetime.datetime.now()
timeoffset = datetime.timedelta(minutes=30)

fetch_time = now - timeoffset
print(fetch_time)

print(fetch_time.strftime('%Y-%m-%d %H:%M:%S'))
shows = getProjections(fetch_time.strftime('%Y-%m-%d %H:%M:%S'))

moviesSet = set()
for show in shows:
    moviesSet.add(show[1])

listOfMoviesDetails =[]
for movie_id in moviesSet:
    listOfMoviesDetails.extend(getMovieDetails(movie_id)) 
print(moviesSet)
