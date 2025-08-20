import requests
import os
from datetime import datetime

# Configuração da API TMDB
TMDB_API_KEY = "demo_key_for_educational_purposes"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Dados de exemplo para demonstração
SAMPLE_MOVIES = [
    {
        "id": 1,
        "title": "O Senhor dos Anéis: A Sociedade do Anel",
        "overview": "Um hobbit recebe uma missão perigosa para destruir um anel mágico.",
        "poster_path": "/poster1.jpg",
        "release_date": "2001-12-19",
        "vote_average": 8.8,
        "genre_ids": [12, 14, 28]
    },
    {
        "id": 2,
        "title": "Matrix",
        "overview": "Um programador descobre que a realidade é uma simulação computadorizada.",
        "poster_path": "/poster2.jpg",
        "release_date": "1999-03-31",
        "vote_average": 8.7,
        "genre_ids": [28, 878]
    },
    {
        "id": 3,
        "title": "Interestelar",
        "overview": "Uma equipe de exploradores viaja através de um buraco de minhoca no espaço.",
        "poster_path": "/poster3.jpg",
        "release_date": "2014-11-07",
        "vote_average": 8.6,
        "genre_ids": [12, 18, 878]
    },
    {
        "id": 4,
        "title": "Vingadores: Ultimato",
        "overview": "Os Vingadores se reúnem para reverter os danos causados por Thanos.",
        "poster_path": "/poster4.jpg",
        "release_date": "2019-04-26",
        "vote_average": 8.4,
        "genre_ids": [12, 28, 878]
    },
    {
        "id": 5,
        "title": "Titanic",
        "overview": "Uma história de amor entre um artista pobre e uma jovem rica no navio Titanic.",
        "poster_path": "/poster5.jpg",
        "release_date": "1997-12-19",
        "vote_average": 7.9,
        "genre_ids": [18, 10749]
    }
]

SAMPLE_GENRES = [
    {"id": 12, "name": "Aventura"},
    {"id": 14, "name": "Fantasia"},
    {"id": 16, "name": "Animação"},
    {"id": 18, "name": "Drama"},
    {"id": 27, "name": "Terror"},
    {"id": 28, "name": "Ação"},
    {"id": 35, "name": "Comédia"},
    {"id": 36, "name": "História"},
    {"id": 37, "name": "Western"},
    {"id": 53, "name": "Thriller"},
    {"id": 80, "name": "Crime"},
    {"id": 99, "name": "Documentário"},
    {"id": 878, "name": "Ficção Científica"},
    {"id": 9648, "name": "Mistério"},
    {"id": 10402, "name": "Música"},
    {"id": 10749, "name": "Romance"},
    {"id": 10751, "name": "Família"},
    {"id": 10752, "name": "Guerra"},
    {"id": 10770, "name": "TV Movie"}
]

def search_movies(query):
    """Busca filmes por nome (usando dados de exemplo)"""
    try:
        # Simular busca nos dados de exemplo
        results = []
        query_lower = query.lower()
        
        for movie in SAMPLE_MOVIES:
            if query_lower in movie["title"].lower():
                results.append(movie)
        
        return {
            'success': True,
            'results': results,
            'total_results': len(results)
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Erro ao buscar filmes: {str(e)}",
            'results': []
        }

def get_popular_movies():
    """Busca filmes populares (dados de exemplo)"""
    try:
        return {
            'success': True,
            'results': SAMPLE_MOVIES,
            'total_results': len(SAMPLE_MOVIES)
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Erro ao buscar filmes populares: {str(e)}",
            'results': []
        }

def get_top_rated_movies():
    """Busca filmes mais bem avaliados (dados de exemplo)"""
    try:
        # Ordenar por avaliação
        sorted_movies = sorted(SAMPLE_MOVIES, key=lambda x: x["vote_average"], reverse=True)
        return {
            'success': True,
            'results': sorted_movies,
            'total_results': len(sorted_movies)
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Erro ao buscar filmes mais avaliados: {str(e)}",
            'results': []
        }

def get_movie_details(movie_id):
    """Busca detalhes completos de um filme (dados de exemplo)"""
    try:
        # Encontrar filme pelo ID
        movie = None
        for m in SAMPLE_MOVIES:
            if m["id"] == int(movie_id):
                movie = m
                break
        
        if not movie:
            return {
                'success': False,
                'error': 'Filme não encontrado',
                'movie': None
            }
        
        # Dados simulados completos
        processed_data = {
            'id': movie["id"],
            'title': movie["title"],
            'original_title': movie["title"],
            'overview': movie["overview"],
            'poster_path': f"https://via.placeholder.com/500x750/333/666?text={movie['title'].replace(' ', '+')}",
            'backdrop_path': f"https://via.placeholder.com/1920x1080/222/555?text={movie['title'].replace(' ', '+')}",
            'release_date': movie["release_date"],
            'runtime': 150,
            'vote_average': movie["vote_average"],
            'vote_count': 1000,
            'genres': ["Ação", "Aventura", "Drama"],
            'status': "Lançado",
            'budget': 100000000,
            'revenue': 500000000,
            'production_companies': [{"name": "Warner Bros."}],
            'cast': [
                {"name": "Ator Principal", "character": "Personagem Principal"},
                {"name": "Atriz Principal", "character": "Personagem Secundário"}
            ],
            'crew': [
                {"name": "Diretor Famoso", "job": "Diretor"},
                {"name": "Roteirista", "job": "Roteiro"}
            ],
            'videos': [
                {"key": "demo1", "name": "Trailer Oficial"},
                {"key": "demo2", "name": "Teaser"}
            ],
            'reviews': [
                {"author": "Crítico 1", "content": "Excelente filme!"},
                {"author": "Crítico 2", "content": "Muito bom!"}
            ]
        }
        
        return {
            'success': True,
            'movie': processed_data
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Erro ao buscar detalhes do filme: {str(e)}",
            'movie': None
        }

def get_movies_by_genre(genre_id):
    """Busca filmes por gênero (dados de exemplo)"""
    try:
        results = []
        for movie in SAMPLE_MOVIES:
            if int(genre_id) in movie["genre_ids"]:
                results.append(movie)
        
        return {
            'success': True,
            'results': results,
            'total_results': len(results)
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Erro ao buscar filmes por gênero: {str(e)}",
            'results': []
        }

def get_genres():
    """Busca lista de gêneros disponíveis (dados de exemplo)"""
    try:
        return {
            'success': True,
            'genres': SAMPLE_GENRES
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Erro ao buscar gêneros: {str(e)}",
            'genres': []
        }

def format_currency(amount):
    """Formata valores monetários"""
    if amount and amount > 0:
        return f"${amount:,}"
    return "N/A"

def format_runtime(minutes):
    """Formata duração do filme"""
    if minutes:
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours}h {mins}min"
    return "N/A"

def get_release_year(date_string):
    """Extrai ano da data de lançamento"""
    if date_string:
        try:
            return datetime.strptime(date_string, '%Y-%m-%d').year
        except:
            return "N/A"
    return "N/A"
