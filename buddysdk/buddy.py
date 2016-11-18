import mprop

import buddysdk


https_client = None
mqtt_client = None
settings = None
events = None
mqtt_events = None


@property
def https(module):
    if module.https_client is None:
        def init_https(app_id_value, app_key_value):
            objects = buddysdk.https.Https.init(app_id_value, app_key_value)

            module.events = objects[0]
            module.settings = objects[1]
            module.https_client = objects[2]

            return module.https_client

        return init_https
    else:
        return module.https_client


@property
def mqtt(module):
    if module.mqtt_client is None:

        def init_mqtt(app_id_value, app_key_value):
            objects = buddysdk.mqtt.Mqtt.init(app_id_value, app_key_value)

            module.events = objects[0]
            module.mqtt_events = objects[1]
            module.settings = objects[2]
            module.https_client = objects[3]
            module.mqtt_client = objects[4]

            return module.mqtt_client

        return init_mqtt
    else:
        return module.mqtt_client


@property
def app_id(module):
    return module.settings.app_id


@property
def current_user_id(module):
    return module.https_client.current_user_id


@property
def last_location(module):
    return module.settings.last_location


@last_location.setter
def last_location(module, value):
    module.settings.last_location = value


@property
def service_exception(module):
    return module.events.service_exception


@property
def connection_changed(module):
    return module.events.connection_changed


@property
def user_authentication_needed(module):
    return module.events.user_authentication_needed


@property
def connection_changed(module):
    return module.events.connection_changed


@property
def user_authentication_needed(module):
    return module.events.user_authentication_needed


def init(module, app_id_value, app_key):
    # mqtt depends on https, so leverage mqtt's init
    module.mqtt(app_id_value, app_key)


mprop.init()
