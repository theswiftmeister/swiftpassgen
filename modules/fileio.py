
import os
import json
import base64


ENCODE_FORMAT = "utf-8"
BYTE_OBJECT_VERSION = 85

class FileIO:
    def __init__(self) -> None:
        pass

    def save(self, file_name, data):
        with open(f"{file_name}", "w", encoding="utf-8") as file:
            file.write(self.data_to_byte_string(data))
            file.close()

    def load(self, path):
        with open(f"{path}", "r", encoding="utf-8") as file:
            _json = json.loads(self.byte_string_to_data(file.read()))
            file.close()
        return _json

    def mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def create_project_files(self, file_names, path, file_type):
        for name in file_names:
            self.create_file(name, path, file_type)

    def create_file(self, file_name, path, file_type):
        file = open(f"{path}/{file_name}{file_type}",
                    "w", encoding="utf-8")
        file.write(self.data_to_byte_string([]))
        file.close()

    def get_project_files(self, path):
        if os.path.isdir(path):
            return os.listdir(path)

    def data_to_byte_string(self, json_data):
        _json = json.dumps(json_data)
        j_bytes = _json.encode("utf-8")
        base_encode = base64.a85encode(j_bytes)
        return base_encode.decode("utf-8")

    def byte_string_to_data(self, byte_string):
        j_bytes = byte_string.encode("utf-8")
        base_decode = base64.a85decode(j_bytes)
        return base_decode