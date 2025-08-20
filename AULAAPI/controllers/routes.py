import json
from flask import render_template, request
from controllers import getMovieData

def init_app(app):
    @app.route("/")
    def home():
        # Buscar filmes populares para a página inicial
        popular_movies = getMovieData.get_popular_movies()
        top_rated = getMovieData.get_top_rated_movies()
        genres = getMovieData.get_genres()
        
        return render_template("index.html", 
                             popular_movies=popular_movies,
                             top_rated=top_rated,
                             genres=genres)
    
    @app.route("/search", methods=['POST', 'GET'])
    def search():
        if request.method == 'POST':
            query = request.form.get("searchQuery")
            
            if query:
                search_results = getMovieData.search_movies(query)
                return render_template("search.html", results=search_results, query=query)
        
        # Se for GET, mostrar página de busca vazia
        return render_template("search.html", results=None, query="")
    
    @app.route("/movie/<int:movie_id>")
    def movie_details(movie_id):
        """Página de detalhes do filme"""
        movie_data = getMovieData.get_movie_details(movie_id)
        
        if movie_data['success']:
            return render_template("movie_details.html", movie=movie_data['movie'])
        else:
            return render_template("error.html", error=movie_data['error'])
    
    @app.route("/popular")
    def popular_movies():
        """Página de filmes populares"""
        movies = getMovieData.get_popular_movies()
        return render_template("popular.html", movies=movies)
    
    @app.route("/top-rated")
    def top_rated_movies():
        """Página de filmes mais bem avaliados"""
        movies = getMovieData.get_top_rated_movies()
        return render_template("top_rated.html", movies=movies)
    
    @app.route("/genre/<int:genre_id>")
    def movies_by_genre(genre_id):
        """Página de filmes por gênero"""
        movies = getMovieData.get_movies_by_genre(genre_id)
        genres = getMovieData.get_genres()
        
        # Encontrar o nome do gênero atual
        current_genre = None
        if genres['success']:
            for genre in genres['genres']:
                if genre['id'] == genre_id:
                    current_genre = genre
                    break
        
        return render_template("genre.html", 
                             movies=movies, 
                             current_genre=current_genre,
                             all_genres=genres)
    
    @app.route("/genres")
    def all_genres():
        """Página com todos os gêneros disponíveis"""
        genres = getMovieData.get_genres()
        return render_template("genres.html", genres=genres)
    
