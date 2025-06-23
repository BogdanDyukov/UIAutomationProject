from config.env_data import EnvData


class ValidLogin:
    USERNAME = EnvData.LOGIN
    PASSWORD = EnvData.PASSWORD

    LOGIN = (USERNAME, PASSWORD)


class InvalidLogin:
    # EMPTY_BOTH = ("", "")
    # EMPTY_USERNAME = ("", ValidLogin.PASSWORD)
    # EMPTY_PASSWORD = (ValidLogin.USERNAME, "")
    #
    # INVALID_BOTH = ("invalid_username", "invalid_password")
    # INVALID_USERNAME = ("invalid_username", ValidLogin.PASSWORD)
    # INVALID_PASSWORD = (ValidLogin.USERNAME, "invalid_password")

    EMPTY_FIELD = ""

    INVALID_USERNAME = "invalid_username"
    INVALID_PASSWORD = "invalid_password"
