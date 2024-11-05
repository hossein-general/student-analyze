# region importing

# importings
from typing import Any

# endregion


# region Validater


# This class will do validations for other classes
class Validator:
    # region msg's
    # creating the message dictionary
    msg = {}

    # Default message values
    msg["check_type"] = "The type_check() function found type exceptions"
    msg["is_same_as"] = "The is_same_as() function found non-same exception"

    # check_type messages (these are used automatically by checking given arguments to the function)
    # message: Creating
    msg["parameter-type-creating"] = (
        'the parameter: \n"{field}" should be of type: \n"{the_type}" for creating {creating_class} instance \n(value: "{value}" was given) :)'
    )
    msg["parameter-inner-type-creating"] = (
        'the parameter: \n"{field}" should be of type: \n"{the_type}" and containing values of type: \n"{inner_type}" for creating {creating_class} instance \n(value: "{value}" and inner_value: "{inner_value}" were given) :)'
    )
    msg["parameter-dict-val-type-creating"] = (
        "this message type is not implemented yet :)"
    )

    # message: Normal
    msg["parameter-type"] = (
        'the parameter: \n"{field}" should be of type: \n"{the_type}" \n(value: "{value}" was given) :)'
    )
    msg["parameter-inner-type"] = (
        'the parameter: \n"{field}" should be of type: \n"{the_type}" and containing values of type: \n"{inner_type}" \n(value: "{value}" and inner_value: "{inner_value}" were given) :)'
    )
    msg["parameter-dict-val-type"] = "this message type is not implemented yet :)"

    # message: Short
    msg["parameter-type-simple"] = (
        "expecting value of type {the_type} but got {value_type} :)"
    )
    msg["parameter-inner-type-simple"] = (
        "expecting inner value of type {inner_type} but got {inner_value_type} :)"
    )
    msg["parameter-dict-val-type-simple"] = (
        "expecting dictionary value of type {dict_val_type} but got {dict_val_value_type}"
    )

    # endregion

    # region init_check_type
    # This functions is called whenever classes want to check types using a single dict containing attr-valuetypes
    def init_check_type(self, attrs_and_types: tuple):
        """this method gets multiple attributes and validates them using check_type method
        it gets a tuple containing other tuples, each inner tuple contains data that is needed to be passed to check type
        it will call check_type for each item and unpacks data of inner tuples within each check_type call

        Args:
            attrs_and_types (tuple): a tuple containing other tuples. each inner typle will be unpacked in the order of check_type
            - value: the attributes value (of any type)
            - the_type: the type that the attribute should be
            - inner_type: type of the inner value if the the value was a container
            - dict_val_type: type of values for dict keys if the original value was a dictionary
            - field: the variable name for further help on debugging
            - creating_class: type of the instance that was about to be created with this attribute (if does) for further debug help

        """
        # type checking the given arguments
        self.check_type(attrs_and_types, tuple, inner_type=tuple)

        # calling the check_type() function to validate any new object instance parameters thats inharitted from validation class
        if attrs_and_types is not None:
            for attr in attrs_and_types:
                self.check_type(*attr)

    # endregion

    # region check_type()
    # Mainly check for parameter value validation  (to be of a certain type)
    # NOTE supports multi-types as tuple
    # TODO adding type validation for dict keys and values
    def check_type(
        self,
        value: Any,
        the_type: Any,
        inner_type: Any = None,
        dict_val_type: Any = None,
        *,  # forcing named parameters
        field: str = None,
        creating_class: str = None,
    ):
        # the f-collection dictionary can be used by the caller as a refrence for string formatting and craeting custom messages
        # at this point the f-collect is containing only the function parameters
        fcollection = locals().copy()
        fcollection.pop("self")

        # checking the value and its type

        # region value
        if not isinstance(value, the_type):
            # adding the type of the value
            fcollection["value_type"] = type(value)

            # using the desired message
            if (creating_class is None) and (field is None):
                # if there where no argument else than the value and type
                msg_key = "parameter-type-simple"

            elif field is None:
                # if of normal check type:
                msg_key = "parameter-type"

            else:
                # if of creating instance type:
                msg_key = "parameter-type-creating"
            raise TypeError(self.msg[msg_key].format(**fcollection))
        # endregion

        # region inner-val
        # checking the inner values and their types (if necessary)
        if hasattr(value, "__iter__") and inner_type is not None:
            for inner_value in value:
                if not isinstance(inner_value, inner_type):
                    # adding the 'inner_value' key with its variable value to be able to format the message with it
                    fcollection["inner_value"] = inner_value
                    # adding the type of the inner value
                    # NOTE the inner_type is not the same as inner_value_type
                    # inner_type is the desired type
                    # inner_value_type is the type that is passed
                    fcollection["inner_value_type"] = type(inner_value)

                    # using the desired message
                    if (creating_class is None) and (field is None):
                        # if there where no argument else than the value and type
                        msg_key = "parameter-inner-type-simple"

                    if field is None:
                        # if of normal check type:
                        msg_key = "parameter-inner-type"

                    else:
                        # if of creating instance type:
                        msg_key = "parameter-inner-type-creating"

                    # raising the error and formatting the messgae
                    raise ValueError(self.msg[msg_key].format(**fcollection))

        # endregion

        # region dict-val
        if isinstance(value, dict) and dict_val_type is not None:
            for inner_value in value:
                if not isinstance(value[inner_value], dict_val_type):
                    # adding the 'dict_val_value' key with its variable value to be able to format the message with it
                    fcollection["dict_val_value"] = value[inner_value]
                    # adding the type of the inner value (not the desired one which is dict_val_type)
                    fcollection["dict_val_value_type"] = type(value[inner_value])

                    # using the desired message
                    if (creating_class is None) and (field is None):
                        # if there where no argument else than the value and type
                        msg_key = "parameter-dict-val-type-simple"

                    if field is None:
                        # if of normal check type:
                        msg_key = "parameter-dict-val-type"

                    else:
                        # if of creating instance type:
                        msg_key = "parameter-dict-val-type-creating"

                    # raising the error and formatting the messgae
                    raise ValueError(self.msg[msg_key].format(**fcollection))
        # endregion

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
