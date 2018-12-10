"""
This module will be used to save configuration related items such as URL, launch mode
"""

import os


class LocatorType(object):
    id = "id"
    name = "name"
    xpath = "xpath"
    link_text = "link_text"
    partial_link_text = "partial_link_text"
    tag = "tag"
    class_name = "class_name"
    css = "css"


class Client(object):
    CHROME = "CHROME"


class LaunchMode(object):
    WEB = "WEB"


DEFAULT_URL = "https://www.dealtap.ca"
DEFAULT_LAUNCH_MODE = LaunchMode.WEB
DEFAULT_CLIENT_NAME = Client.CHROME

URL = os.environ.get("URL", DEFAULT_URL)
LAUNCH_MODE = os.environ.get("LAUNCH_MODE", DEFAULT_LAUNCH_MODE)
CLIENT_NAME = os.environ.get("CLIENT_NAME", DEFAULT_CLIENT_NAME)
