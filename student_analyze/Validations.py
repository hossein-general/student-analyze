# region Validater
# This class will do validations for other classes
class Validator:
    def __init__(self) -> None:
        self.msg = {}

    def is_valid(self, caller, content):
        pass

    def is_included(self, caller, content, valid_container):
        pass

    def exists(self, caller, content, container):
        pass

    def is_sameas(self, caller, content_1, content_2, attr, msg_key):
        fcollection = {
            'caller':caller, 
            'content_1':content_1, 
            'content_2':content_2, 
            'attr':attr, 
            'msg_key':msg_key, 
        }

        if hasattr(content_1, "__iter__"):
            for each_content in content_1:
                if getattr(each_content, attr) != getattr(content_2):
                    raise ValueError(self.msg[msg_key].format(**fcollection))

        else:
            if getattr(content_1, attr) != getattr(content_2):
                raise ValueError(msg_key.format(**fcollection))
