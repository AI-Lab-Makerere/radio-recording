from datetime import datetime
from threading import Thread


class RecordingWorker(Thread):
    def __init__(self, region: str, station: str, language: str, uri: str):
        self.__region = region
        self.__station = station
        self.__language = language
        self.__uri = uri

    def start(self):
        pass

    def stop(self):
        pass

    def run(self) -> None:
        pass

    def __record_audios(self, time_limit: int):
        while self.__is_running:
            start_time = datetime.now()
            generated_content = self.__record_audio_files(start_time=start_time, time_limit=time_limit)
            for content in generated_content:
                tag_details = self.__tag_file(content=content)
                self.__persist_file_information(information=tag_details)