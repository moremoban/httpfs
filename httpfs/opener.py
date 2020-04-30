from fs.opener import Opener

from httpfs.fs import HttpFs


class HttpFsOpener(Opener):
    protocols = ["http", "https"]

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        http_fs = HttpFs(fs_url)
        return http_fs
