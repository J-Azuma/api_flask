from datetime import date
from api.domainlayer.movie.Movie import Movie
from api.usecaselayer.movies.moviedata import MovieData


def test_Movieオブジェクトが変換されること():
    id = 2
    title = "Ariel"
    poster_path = "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg"
    release_date = date(1988, 10, 21)
    runtime = 73
    overview = ""
    genres = [
        {
            "id": 18,
            "name": "ドラマ"
        },
        {
            "id": 80,
            "name": "犯罪"
        },
        {
            "id": 35,
            "name": "コメディ"
        }
    ]
    movie: Movie = Movie(id, title, poster_path, release_date, runtime, overview, genres)
    moviedata: MovieData = MovieData(movie)
    
    assert isinstance(moviedata, MovieData)
    assert moviedata.id == 2
    assert moviedata.title == "Ariel"
    assert moviedata.poster_path == "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg"
    assert isinstance(moviedata.release_date, str)
    assert moviedata.release_date == "1988-10-21"
    assert moviedata.runtime == 73
    assert moviedata.overview == ""        
    
