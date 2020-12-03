from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session
import texttable
from recording.models import Station


class App(object):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def run(self):
        pass

    def add_station(self, name, language, region, url):
        try:
            station = Station(
                name=name,
                language=language,
                region=region,
                uri=url
            )
            self.__session.add(station)
            self.__session.commit()
            print("STATION ADDED")
        except DatabaseError as err:
            print(err)

    def remove_station(self, identifier: int) -> None:
        try:
            self.__session.query(Station).filter(Station.id == identifier).delete()
            self.__session.commit()
            print("STATION REMOVED")
        except DatabaseError as err:
            print(err)

    def list_station(self):
        try:
            stations = self.__session.query(Station).all()
            table = texttable.Texttable()
            headings = ['Name', 'Region', 'Language', 'URL']
            table.header(headings)
            for station in stations:
                table.add_row([station.name, station.region, station.language, station.uri])
            s = table.draw()
            print(s)
        except DatabaseError as err:
            print(err)
