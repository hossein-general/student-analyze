# importings
from typing import Any

# region Validater
# This class will do validations for other classes
class Validator:
    def __init__(self) -> None:
        self.msg = {}
        
        # Default message values
        self.msg['check_type'] = "The type_check() function found type exceptions" 
        self.msg['is_same_as'] = "The is_same_as() function found non-same exception"

    # def fcollection_adder():
    #     def wrapper(*arg, **args):
    #         pass

    # Mainly check for parameter value validation  (to be of a certain type)
    def check_type(
        self, 
        value: Any, 
        type: Any, 
        field: str,
        msg_key: str = 'check_type'
    ):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        fcollection = {
            'value':value, 
            'type':type, 
            'field':str, 
            'msg_key':msg_key, 
        }
        
        if not isinstance(value, type):
            raise TypeError(self.msg[msg_key].format(**fcollection))

    # Checks for Authentication like exceptions, related to boolean values
    def is_valid(self, caller, content):
        pass

    # Checks for Parent-base Validations, like being within a list 
    def is_included(self, caller, content, valid_container):
        pass

    # Checking for Existance of an attribute or item within an instance or a list
    def exists(self, caller, content, container):
        pass

    # This function checks for logical errors that are related to not having same attribute values
    def is_same_as(
        self, 
        caller: Any, 
        content_1: Any, 
        content_2: Any, 
        attr: str, 
        msg_key: str = 'is_same_as'
    ):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        fcollection = {
            'caller':caller, 
            'content_1':content_1, 
            'content_2':content_2, 
            'attr':attr, 
            'msg_key':msg_key, 
        }

        # checking if the given content_1 parameter is of an iterable type or not
        if not hasattr(content_1, "__iter__"):
            if getattr(content_1, attr) != content_2:
                # rasing an error with a custom formatted text as a message
                raise ValueError(self.msg[msg_key].format(**fcollection))

        else:
            for each_content in content_1:
                if getattr(each_content, attr) != content_2:
                    # updating the content_1 to each_contetn in the f-collection dict to prevent formatting errors
                    fcollection['content_1'] = each_content
                    # raisng an error with a custom formatted text as a message
                    raise ValueError(self.msg[msg_key].format(**fcollection))
