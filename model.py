import os
import pickle
import re
from Knnclass import KnnRecommender
    
movies_filename = 'movies.csv'
ratings_filename = 'ratings.csv'


recommender = KnnRecommender(
        os.path.join(movies_filename),
        os.path.join(ratings_filename))

#load the model
loaded_model = pickle.load(open('knn_model.sav', 'rb'))

 # get data
movie_user_mat_sparse, hashmap = KnnRecommender._prep_data(recommender)

fav_movie = re.sub('[^a-zA-Z]+', '', str(input("Enter a movie name: ")))

n_recom = int(input("How many recommendations do you want: "))

# get recommendations
raw_recommends = KnnRecommender._inference(recommender, loaded_model, movie_user_mat_sparse, hashmap, fav_movie, n_recom)

# print results
#reco_list = []
reverse_hashmap = {v: k for k, v in hashmap.items()}
print('Recommendations for {}:'.format(fav_movie.capitalize()))
for i, (idx, dist) in enumerate(raw_recommends):
        #reco_list.append(reverse_hashmap[idx])
        print('{0}: {1}'.format(i+1, reverse_hashmap[idx]))