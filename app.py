from datetime import datetime
from crontabs import Cron, Tab
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session
import texttable
from recording.models import Station
from settings import RECORDING_HOURS_RANGE, UPLOADING_HOURS_RANGE


class App(object):
    def __init__(self, session: Session) -> None:
        self.__session = session

    @staticmethod
    def __recording_time(timestamp: datetime) -> bool:
        time_range = str(RECORDING_HOURS_RANGE).split("-")
        print("CURRENT RECORDING HOUR {}".format(timestamp.hour))
        return int(time_range[0]) <= timestamp.hour < int(time_range[1])

    @staticmethod
    def __uploading_time(timestamp: datetime) -> bool:
        time_range = str(UPLOADING_HOURS_RANGE).split("-")
        print("CURRENT UPLOADING HOUR {}".format(timestamp.hour))
        return int(time_range[0]) <= timestamp.hour or timestamp.hour < int(time_range[1])

    def __recording_operation(self) -> None:
        print("recording your lordship")
        print(self.__session)

    def __uploading_operation(self) -> None:
        print("uploading your lordship")
        print(self.__session)

    def __create_recording_job(self):
        return Tab(name='recording_job').every(days=1).during(self.__recording_time).run(self.__recording_operation)

    def __create_uploading_job(self):
        return Tab(name='uploading_job').every(days=1).during(self.__uploading_time).run(self.__uploading_operation)

    def run(self):
        Cron().schedule(
            self.__create_recording_job(),
            self.__create_uploading_job()
        ).go(max_seconds=3600 * 24 * 365)

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
            headings = ['Identifier', 'Name', 'Region', 'Language', 'URL']
            table.header(headings)
            for station in stations:
                if station is None:
                    return
                table.add_row([station.id, station.name, station.region, station.language, station.uri])
            s = table.draw()
            print(s)
        except DatabaseError as err:
            print(err)
