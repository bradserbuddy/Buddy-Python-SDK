import unittest

import buddysdk
import test_base


class Test1(unittest.TestCase):

    def test_Https(self):
        settings = buddysdk.settings.Settings(test_base.TestBase.US_app_id, test_base.TestBase.US_app_key)
        events = buddysdk.buddy_events.BuddyEvents()
        client = buddysdk.https.Https(events, settings)
        self.assertIsNotNone(client)
        self.assertIs(settings.app_id, test_base.TestBase.US_app_id)
        self.assertIs(settings.app_key, test_base.TestBase.US_app_key)


if __name__ == '__main__':
    unittest.main()
