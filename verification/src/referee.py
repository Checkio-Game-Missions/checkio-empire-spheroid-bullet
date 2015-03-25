from checkio_referee import RefereeCodeGolf
from checkio_referee import covercodes, representations

import settings
import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    BASE_POINTS = 10
    DEFAULT_MAX_CODE_LENGTH = 100
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "spheroid"
    ENV_COVERCODE = {
        "python_2": covercodes.py_unwrap_args,
        "python_3": covercodes.py_unwrap_args,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.unwrap_arg_representation,
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation
    }
