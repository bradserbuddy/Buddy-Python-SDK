import events


class BuddyEvents(object):

    def __init__(self):
        self._service_exception = events.Events()
        self._user_authentication_needed = events.Events()
        self._connection_changed = events.Events()

    @property
    def service_exception(self):
        return self._service_exception

    @property
    def user_authentication_needed(self):
        return self._user_authentication_needed

    @property
    def connection_changed(self):
        return self._connection_changed
