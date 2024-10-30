# importings
from typing import Any


# region Validater
# This class will do validations for other classes
class Validator:
    def __init__(self) -> None:
        self.msg = {}

        # Default message values
        self.msg["check_type"] = "The type_check() function found type exceptions"
        self.msg["is_same_as"] = "The is_same_as() function found non-same exception"

        # check_type messages
        self.msg["parameter-type-creating"] = (
            'the parameter: "{field}" should be of type: "{type}" for creating {creating_class} instance'
        )
        self.msg["parameter-inner-type-creating"] = (
            'the parameter: "{field}" should be of type: "{type}" and containing values of type: "{inner_value}" for creating {creating_class} instance'
        )
        self.msg["parameter-type"] = (
            'the parameter: "{field}" should be of type: "{type}"'
        )
        self.msg["parameter-inner-type"] = (
            'the parameter: "{field}" should be of type: "{type}" and containing values of type: "{inner_value}"'
        )

    # region check_type()
    # Mainly check for parameter value validation  (to be of a certain type)
    # NOTE supports multi-types as tuple
    def check_type(
        self,
        value: Any,
        type: Any,
        field: str = "-field-",
        creating_class: str = None,
        inner_type: Any = None,
    ):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        # at this point the f-collect is containing only the function parameters
        fcollection = locals().copy()
        fcollection.pop("self")

        # checking the value and its type
        if not isinstance(value, type):

            # using the desired message
            if creating_class is None:
                # if of normal check type:
                msg_key = "parameter-type"
            else:
                # if of creating instance type:
                msg_key = "parameter-type-creating"

            raise TypeError(self.msg[msg_key].format(**fcollection))

        # checking the inner values and their types (if necessary)
        if hasattr(value, "__iter__") and inner_type is not None:
            for inner_value in value:
                if isinstance(inner_value, inner_type):
                    # adding the 'inner_value' key with its variable value to be able to format the message with it
                    fcollection["inner_value"] = inner_value

                    # using the desired message
                    if creating_class is None:
                        # if of normal check type:
                        msg_key = "parameter-inner-type"
                    else:
                        # if of creating instance type:
                        msg_key = "parameter-inner-type-creating"

                    raise ValueError(self.msg[msg_key].format(**fcollection))

    # endregion

    # region is_valid()
    # Checks for Authentication like exceptions, related to boolean values
    def is_valid(self, caller, content):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        # at this point the f-collect is containing only the function parameters
        fcollection = locals().copy()
        fcollection.pop("self")
        fcollection.pop("msg_key")

    # endregion

    # region is_included()
    # Checks for Parent-base Validations, like being within a list
    def is_included(self, caller, content, valid_container):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        # at this point the f-collect is containing only the function parameters
        fcollection = locals().copy()
        fcollection.pop("self")
        fcollection.pop("msg_key")

    # endregion

    # region exists()
    # Checking for Existance of an attribute or item within an instance or a list
    def exists(self, caller, content, container):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        # at this point the f-collect is containing only the function parameters
        fcollection = locals().copy()
        fcollection.pop("self")
        fcollection.pop("msg_key")

    # endregion

    # region is_same_as()
    # This function checks for logical errors that are related to not having same attribute values
    def is_same_as(
        self,
        caller_instance: any,
        content_1: Any,
        content_2: Any,
        attr: str,
        msg_key: str = "is_same_as",
    ):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        # at this point the f-collect is containing only the function parameters
        fcollection = locals().copy()
        fcollection.pop("self")
        fcollection.pop("msg_key")

        # checking if the given content_1 parameter is of an iterable type or not
        if not hasattr(content_1, "__iter__"):
            if getattr(content_1, attr) != content_2:
                # rasing an error with a custom formatted text as a message
                raise ValueError(self.msg[msg_key].format(**fcollection))

        else:
            for each_content in content_1:
                if getattr(each_content, attr) != content_2:
                    # updating the content_1 to each_contetn in the f-collection dict to prevent formatting errors
                    # NOTE there is no need to keep the content_1 and add 'each_content' key to the fcollection (like what we did in type_check) because its desined to be versatile and handle both single argument or container arguments
                    fcollection["content_1"] = each_content
                    # raisng an error with a custom formatted text as a message
                    raise ValueError(self.msg[msg_key].format(**fcollection))

    # endregion
