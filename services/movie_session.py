import datetime

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int, cinema_hall_id: int):
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None):
    if session_date is not None:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None):
    filtered_movie_session = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        filtered_movie_session.update(show_time=show_time)

    if movie_id is not None:
        filtered_movie_session.update(movie_id=movie_id)

    if cinema_hall_id is not None:
        filtered_movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.get(id=session_id).delete()