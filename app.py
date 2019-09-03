import os
import pickle
from Knnclass import KnnRecommender
import re
from flask import Flask, escape, request , render_template
from flask_restplus import Api, Resource, fields
from flask_assets import Environment,Bundle


app = Flask(__name__)


# CSS && JS

assets = Environment(app)


css = Bundle('css/bootstrap.css', 'css/bootstrap-grid.css', 'css/bootstrap-reboot.css','css/fontawesome.min.css'
             ,'css/style.css','css/all.css',
            filters='cssmin', output='gen/packed.css')
assets.register('css_all', css)



js = Bundle('js/bootstrap.min.js','js/jquery-3.3.1.slim.min.js','js/popper.min.js',
            'js/plugins.js',
            filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)





@app.route('/')
def home():
    ###name = request.args.get("name", "World")
    return render_template('index.html')




@app.route('/visualization')
def visualization():
    ###name = request.args.get("name", "World")
    return render_template('visualization.html')



# @app.route('/recommended', methods=['POST','GET'])
# def recommended():
#     ###name = request.args.get("name", "World")
#       return render_template('recommended.html')

    
     
  
    
    
          
             


       


             




# @app.route('/recommended' , methods=['POST','GET'])
# def recommended():

@app.route('/recommended', methods=['POST','GET'])
def recommended(): 
    thislist = []
    thislist2 = ['mohamed','momk','gffgg']
    
    if(request.method == 'GET'):
        return render_template('recommended.html')
     
        
    if(request.method == 'POST'):
        
        
        movie_name = request.form['movie_name']
        
        rec_num = request.form['Rec_num']

     # the model code 

        movies_filename = 'movies.csv'
        ratings_filename = 'ratings.csv'

        recommender = KnnRecommender(
           os.path.join(movies_filename),
           os.path.join(ratings_filename))


          #load the model
        loaded_model = pickle.load(open('knn_model.sav', 'rb'))

           # get data
        movie_user_mat_sparse, hashmap = KnnRecommender._prep_data(recommender)

        fav_movie = re.sub('[^a-zA-Z]+', '', movie_name)

        n_recom = int(rec_num)

            

        # get recommendations
        raw_recommends = KnnRecommender._inference(recommender, loaded_model, movie_user_mat_sparse,
                                                   hashmap, fav_movie, n_recom)



        # print results
        reverse_hashmap = {v: k for k, v in hashmap.items()}
        print('Recommendations for {}:'.format(fav_movie))

        for i, (idx, dist) in enumerate(raw_recommends):
           ## thislist.append(reverse_hashmap[idx])
            thislist.insert(i+1,reverse_hashmap[idx])
            print('{0}: {1}'.format(i+1, reverse_hashmap[idx])) 
            
            
    print(thislist[1]) 

    #n=thislist2
#    return render_template('recommended.html')

    return render_template('recommended.html' , n=thislist)
 




    

 
if __name__ == '__main__':
    app.run()


