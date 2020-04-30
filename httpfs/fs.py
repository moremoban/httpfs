import logging
from io import BytesIO
from unittest.mock import MagicMock

import httpx
from fs.base import FS
from fs.errors import CreateFailed

LOG = logging.getLogger(__name__)


class HttpFs(FS):
    def __init__(self, url):
        self.base_url = url
        self.cache = {}

    def __enter__(self):
        return self

    def __exit__(self, *_):
        pass

    def getinfo(self, path, namespaces=None):
        LOG.info("getinfo")
        flag = "." not in path
        return MagicMock(is_dir=flag)

    def listdir(self, path):
        return []

    def makedir(self):
        pass

    def openbin(self, a_file, **_):
        LOG.info("openbin")
        try:
            if self.base_url.endswith("/"):
                url = self.base_url + a_file
            else:
                url = self.base_url + "/" + a_file
            content = self.download_file(url)
            return BytesIO(content)
        except NoContentFound:
            raise CreateFailed

    def remove(self):
        pass

    def removedir(self):
        pass

    def setinfo(self):
        pass

    def exists(self, a_file):
        LOG.info("exists")
        if a_file.endswith("/"):
            return True
        try:
            if self.base_url.endswith("/"):
                url = self.base_url + a_file
            else:
                url = self.base_url + "/" + a_file
            self.download_file(url)
            return True
        except NoContentFound:
            return False

    def download_file(self, url):
        LOG.info("download_file")

        if url in self.cache:
            return self.cache[url]

        r = httpx.get(url)

        content = r.content

        if r.status_code == 200:
            self.cache[url] = content
            return content
        else:
            LOG.info(f"status code: {r.status_code}")
            raise NoContentFound()

    def geturl(self, a_file, **_):
        if self.base_url.endswith("/"):
            url = self.base_url + a_file
        else:
            url = self.base_url + "/" + a_file
        return url


class NoContentFound(Exception):
    pass
