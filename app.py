from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import argparse
from settings import DATABASE_URL
from storage.base import BaseModel


def initialize() -> None:
    engine = create_engine(
        DATABASE_URL,
        echo=True
    )

    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    BaseModel.set_session(session=session)
    BaseModel.prepare(engine, reflect=True)  # BaseModel.metadata.create_all(engine)


def run() -> None:
    # We will add the argument parser library for python and determine what command is to be run
    # record to start off recorder
    # migrate to migrate sql
    # clean to wipe out all tables and rollback
    pass


# parent_parser = argparse.ArgumentParser(description="The parent parser")
# parent_parser.add_argument("-p", type=int, required=True,
#                            help="set db parameter")
# subparsers = parent_parser.add_subparsers(title="actions")
# parser_create = subparsers.add_parser("create", parents=[parent_parser],
#                                       add_help=False,
#                                       description="The create parser",
#                                       help="create the orbix environment")
# parser_create.add_argument("--name", help="name of the environment")
# parser_update = subparsers.add_parser("update", parents=[parent_parser],
#                                       add_help=False,
#                                       description="The update parser",
#                                       help="update the orbix environment")

def perform_migration():
    pass


def perform_rollback():
    pass


def add_station(name, language, region, url):
    pass


def remove_station(id):
    pass


def list_stations():
    pass


def main() -> None:
    parser = argparse.ArgumentParser(description=" Radio Recorder")
    parser.add_argument("--operation", type=str, required=True, help="operation to run")
    sub_parsers = parser.add_subparsers(title="operations", dest='operation', required=True)
    run_parser = sub_parsers.add_parser(
        "run",
        add_help=False,
        parents=[parser],
        description="run the recorder"
    )
    migrate_parser = sub_parsers.add_parser(
        "migrate",
        add_help=False,
        parents=[parser],
        description="migrate tables in database"
    )
    rollback_parser = sub_parsers.add_parser(
        "rollback",
        add_help=False,
        parents=[parser],
        description="rollback changes to the database"
    )
    add_station_parser = sub_parsers.add_parser(
        "add-station",
        add_help=False,
        parents=[parser],
        description="add station"
    )

    add_station_parser.add_argument(
        "--name",
        help="name of radio station",
        required=True
    )
    add_station_parser.add_argument(
        "--language",
        help="language of station",
        required=True
    )
    add_station_parser.add_argument(
        "--region",
        help="region of the station",
        required=True
    )
    add_station_parser.add_argument(
        "--url",
        help="url of the radio station",
        required=True
    )
    remove_station_parser = sub_parsers.add_parser(
        "remove-station",
        add_help=False,
        parents=[parser],
        description="remove station"
    )
    list_station_parser = sub_parsers.add_parser(
        "list-stations",
        add_help=False,
        parents=[parser],
        description="list stations"
    )

    remove_station_parser.add_argument(
        "--id",
        type=int,
        help="station id",
        required=True
    )

    args = parser.parse_args()

    if args.operation is 'migrate':
        return perform_migration()
    elif args.operation is 'rollback':
        return perform_rollback()
    elif args.operation is 'add-station':
        add_station(name=args.name, language=args.language, region=args.region, url=args.url)
    elif args.operation is 'remove-station':
        remove_station(id=args.id)
    elif args.operation is 'list-stations':
        list_stations()
    elif args.operation is 'run':
        run()
    else:
        print("Unknown operation")
