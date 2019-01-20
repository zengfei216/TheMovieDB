import http.client
import json
import time
import sys
import collections

# ************ Q1 part b **************

# **** configurable area *****
API = sys.argv[1]
genre = 'Drama'
retrieve_cnt = 350
# ************************

# method to take a dict and return a query string
def getQueryString(query_dict):
    query_string = []
    for k, v in query_dict.items():
        query_string.append(str(k) + '=' + str(v))
    query_string = '&'.join(query_string)
    return query_string


conn = http.client.HTTPSConnection("api.themoviedb.org")

# # Get all movie genres and genre id
# data = {
#     'api_key': API,
# }
# query_string = getQueryString(data)
# conn.request("GET", '/3/genre/movie/list?'+query_string)
# response_str = conn.getresponse().read().decode()
# # turn response str to dict
# genre_dict = json.loads(response_str)
# # create a lookup table for genre and its id
# genre_id_lookup_dict = {}
# for item in genre_dict['genres']:
#     genre_id_lookup_dict[item['name']] = item['id']
#
# #print(genre_id_lookup_dict)
#
# # create file if not exist
# file = open('movie_ID_name.csv', 'w+')
#
# counter = 0
# page = 1
# while counter < retrieve_cnt:
#     data = {
#         'api_key': API,
#         'with_genres': genre_id_lookup_dict[genre],
#         'sort_by': 'popularity.desc',
#         'primary_release_date.gte': '2004-01-01',
#         'page': page,
#     }
#     query_string = getQueryString(data)
#     conn.request("GET", '/3/discover/movie?' + query_string)
#     response_str = conn.getresponse().read().decode()
#     # turn response str to dict
#     movie_dict = json.loads(response_str)
#
#     movies = movie_dict['results']
#
#     for i in range(20):
#         file.write("%d,%s\n"%(movies[i]['id'], movies[i]['title']))
#         counter += 1
#         if counter == retrieve_cnt:
#             break
#
#     page += 1
#
# file.close()

# ************ Q1 part c **************

with open('movie_ID_name.csv') as file:
    movie_list = file.readlines()
file.close()

# extract movie id
movie_id_list = [int(movie.split(',')[0]) for movie in movie_list]

data = {
    'api_key': API,
}
query_string = getQueryString(data)
similar_movie_dict = {}
request_counter = 0
for movie_id in movie_id_list:

    conn.request("GET", '/3/movie/%s/similar?'%movie_id + query_string)
    request_counter += 1
    response_str = conn.getresponse().read().decode()
    # turn response str to dict
    response_dict = json.loads(response_str)
    similar_movie_id_list = []
    counter = 0
    for item in response_dict['results']:
        similar_movie_id_list.append(item['id'])
        counter += 1
        if counter == 5:
            break

    similar_movie_dict[movie_id] = similar_movie_id_list

    if request_counter == 40:
        time.sleep(60) # sleep 60s





