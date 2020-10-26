from yoyo import get_backend
from yoyo import read_migrations


class SQLMigrationHandler(object):
    def __init__(self, database_url, migration_folder):
        self.__backend = get_backend(database_url)
        self.__migrations = read_migrations(migration_folder)


def migrate(self) -> None:
    with self.__backend.lock():
        # Apply any outstanding migrations
        self.__backend.apply_migrations(self.__backend.to_apply(self.__migrations))


def rollback(self) -> None:
    with self.__backend.lock():
        # Rollback all migrations
        self.__backend.rollback_migrations(self.__backend.to_rollback(self.__migrations))
