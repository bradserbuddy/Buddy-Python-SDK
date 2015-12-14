﻿from datetime import datetime
from datetime import timezone
from datetime import timedelta
from unittest import TestCase
import os
from settings import Settings

class TestBase(TestCase):
 
    US_app_id = "bbbbbc.xgjbvPdwkllw"
    US_app_key = "1E9E824E-A3F1-4F34-B4F4-9CC87471A564"
    EU_app_id = "bbbbbc.gfnGlNfJFvFP"
    EU_app_key = "76123a72-4d05-93db-f297-b8a7501fd2f7"

    def setUp(self):
        try:
            os.remove("buddy.cfg")
        finally:
            return

    def setup_with_bad_device_token(self):
        settings = Settings(TestBase.US_app_id)
        settings.set_device_token({"accessToken": "bad device token", "accessTokenExpires": self.past_javascript_access_token_expires()})

    def future_javascript_access_token_expires(self):
        return self.__javascript_access_token_expires(1)

    def past_javascript_access_token_expires(self):
        return self.__javascript_access_token_expires(-1)

    def __javascript_access_token_expires(self, days):
        delta = datetime.now(timezone.utc) + timedelta(days)
        return self.__javascript_access_token_expires_string(delta)

    def __javascript_access_token_expires_string(self, python_datetime):
        return "/Date(" + str(round(self.ticks_from_timestamp(python_datetime.timestamp()))) + ")/"

    def ticks_from_timestamp(self, timestamp):
        return timestamp * 1000