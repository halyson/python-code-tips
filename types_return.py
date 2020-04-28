# Cuidado para retornar sempre o mesmo tipo de dado


User = {}


def get_user(username: str) -> User:
    """Query user by its username.
    :param username: A str holding username
    :returns: User instance
    :raises: UserNotFoundError
    """
    users = User(username=username).select()
    if not users:
        raise UserNotFoundError(f"{username} does not exist.")
    return users.first()
