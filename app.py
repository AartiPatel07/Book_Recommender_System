from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    # Convert HTTP URLs to HTTPS for secure loading
    images = [url.replace('http://', 'https://') if url.startswith('http://') else url 
              for url in list(popular_df['Image-URL-M'].values)]
    
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=images,
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    
    # Check if the book exists in our dataset
    if user_input not in pt.index:
        # Return to recommend page with error message
        return render_template('recommend.html', error=f"Sorry, '{user_input}' not found in our database. Please try another book title.")
    
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        
        # Convert HTTP URLs to HTTPS for secure loading
        image_url = list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)[0]
        secure_image_url = image_url.replace('http://', 'https://') if image_url.startswith('http://') else image_url
        item.append(secure_image_url)

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)