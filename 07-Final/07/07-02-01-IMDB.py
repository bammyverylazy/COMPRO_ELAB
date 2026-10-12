#------------------------------------------- IMDB HEADER -------------------------------------------
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"

### do not forget to uncomment the next line to read json data
data = read_json(filename)
### ----------------------------------------------------------
#------------------------------------------- IMDB HEADER -------------------------------------------



def get_directors(movie):
    d = movie.get('director')
    if not d:
        return []
    if isinstance(d, dict):
        name = d.get('name')
        return [name] if name else []
    if isinstance(d, str):
        return [d]
    if isinstance(d, list):
        names = []
        for item in d:
            if isinstance(item, dict) and item.get('name'):
                names.append(item['name'])
            elif isinstance(item, str):
                names.append(item)
        return names
    return []


def is_actor_in_movie(movie, actor_name):
    cast = movie.get('cast')
    if not cast:
        return False
    if isinstance(cast, list):
        for item in cast:
            if isinstance(item, dict) and item.get('name') == actor_name:
                return True
            elif isinstance(item, str) and item == actor_name:
                return True
    elif isinstance(cast, dict) and cast.get('name') == actor_name:
        return True
    elif isinstance(cast, str) and cast == actor_name:
        return True
    return False


def get_rating(movie):
    val = movie.get('ratingValue', 0)
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        val_clean = val.strip()
        if val_clean.replace('.', '', 1).isdigit():
            return float(val_clean)
    return 0.0


# -------------------------------------------------------------------

def q1():
    ford_movies = [
        m for m in data 
        if is_actor_in_movie(m, 'Harrison Ford') 
        and 'Steven Spielberg' not in get_directors(m)
    ]
    
    unique_ratings = {get_rating(m) for m in ford_movies}
    top_5_rating_values = sorted(list(unique_ratings), reverse=True)[:5]
    
    top_movies = [m for m in ford_movies if get_rating(m) in top_5_rating_values]
    
    directors = set()
    for m in top_movies:
        for name in get_directors(m):
            directors.add(name)
            
    for name in sorted(directors):
        print(name)


def q2():
    co_star_movies = []
    excluded = {'George Lucas', 'Steven Spielberg'}
    
    for m in data:
        if is_actor_in_movie(m, 'Harrison Ford') and is_actor_in_movie(m, 'Tommy Lee Jones'):
            dirs = set(get_directors(m))
            if not dirs.intersection(excluded):
                co_star_movies.append(m)
                
    co_star_movies.sort(key=get_rating, reverse=True)
    
    if co_star_movies:
        best_movie = co_star_movies[0]
        print(best_movie.get('name') or best_movie.get('title', ''))
        
        
        
        
#----- driver code
print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
  q1()
elif ans == '2':
  q2()
else:
    print('Nothing to do..')
    
    
    
    

'''
Q1 What are the director names of the top five rating films of the actor Harrison Ford (who had been casted in 'Indiana Jones and the Raiders of the Lost Ark') that have not been directed by Steven Spielberg?
director names no Steven Spielberg
ratingValue top 5
actor Harrison Ford -- specific id as the 'Indiana Jones and the Raiders of the Lost Ark'

Q2 What is the top rated film (not directed either by George Lucas or by Steven Spielberg) in which Harrison Ford and Tommy Lee Jones casting together?


## print(data[0]) ##
{'ImdbId': 'tt0144999', 
'_id': 'tt0144999', 
'name': 'Isaia, horeve', 
'poster_url': 'https://m.media-amazon.com/images/M/MV5BZTE2YTU1ZjAtM2RlNy00ZTJlLTg3ZjEtNmQwZDE0MTBjYzNlXkEyXkFqcGdeQXVyNDE5MTU2MDE@.', 
'year': '1966', 
'certificate': '', 
'runtime': '72 min', 
'genre': ['Comedy'], 
'ratingValue': '4.9', 
'summary_text': "A spirited wife tries to keep her husband's matchmaking and introduction agency afloat--while in the meantime--her daughter is ready to walk down the aisle with an affluent young heir. Have they struck gold or is this a beautiful dream?", 
'ratingCount': '66', 
'director': {'name': 'Kostas Asimakopoulos', 'name_id': 'nm0039350'}, 
'cast': [{'name': 'Vasilis Avlonitis', 'name_id': 'nm0043247'}, {'name': 'Georgia Vasileiadou', 'name_id': 'nm0890522'}, {'name': 'Takis Miliadis', 'name_id': 'nm0587393'}, {'name': 'Giannis Fermis', 'name_id': 'nm0272754'}]}
'''

'''
json -> dict use json.loads()
python -> json use json.dumps()
'''

