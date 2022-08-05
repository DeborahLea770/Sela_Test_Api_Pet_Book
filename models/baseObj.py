import json


class baseObj:

    def __init__(self):
        pass

    def to_json(self) -> str:
        # return json.dumps(self.__dict__)
        result = {}
        for key, val in self.__dict__.items():
            if val is not None:
                if key.startswith("_"):
                    result[key[1:]] = val
                else:
                    result[key] = val
        return result

    def __str__(self):
        return json.dumps(self.to_json())
