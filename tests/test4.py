import mock
import unittest

import buddy
from buddysdk.buddy_events import BuddyEvents
from buddysdk.https import Https
from buddysdk.settings import Settings
from test_base import TestBase


class Test4(TestBase):

    @mock.patch("settings.Settings")
    def test_register_device_us(self, settings_mock):
        settings_mock.return_value = Settings(TestBase.US_app_id, TestBase.US_app_key)
        self.setup_with_bad_tokens(settings_mock.return_value)

        self._register_device(self, TestBase.US_app_id, TestBase.US_app_key, "https://api")

    @mock.patch("settings.Settings")
    def test_register_device_eu(self, settings_mock):
        settings_mock.return_value = Settings(TestBase.EU_app_id, TestBase.EU_app_key)
        self.setup_with_bad_tokens(settings_mock.return_value)

        self._register_device(self, TestBase.EU_app_id, TestBase.EU_app_key, "https://api-eu")

    def _register_device(self, test, app_id, app_key, service_root_starts_with):
        client = buddy.https(app_id, app_key)

        access_token_string = client.get_access_token_string()

        settings = Settings(app_id, app_key)
        test.assertEqual(access_token_string, settings.access_token_string)
        test.assertTrue(settings.service_root.startswith(service_root_starts_with))

    @mock.patch.object(Https, "_Https__handle_dictionary_request")
    @mock.patch.object(Https, "_Https__hardware_info_file_name", new_callable=mock.PropertyMock)
    def test_hardware_info(self, hardware_info_file_name_mock, handle_dictionary_request_mock):
        handle_dictionary_request_mock.return_value = {Https.exception_name: Exception()}
        
        # TODO: to run in Python Tools for VS, change to "tests\cpuinfo"
        hardware_info_file_name_mock.return_value = "cpuinfo"

        events = BuddyEvents()

        settings = Settings(TestBase.US_app_id, TestBase.US_app_key)

        client = Https(events, settings)

        client.get_access_token_string()

        cpuinfo = handle_dictionary_request_mock.call_args[0][2]
        self.assertEqual(cpuinfo["model"], "BCM2708-000e")
        self.assertEqual(cpuinfo["uniqueId"], "00000000********")


if __name__ == '__main__':
    unittest.main()
