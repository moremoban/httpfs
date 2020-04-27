import httpx
from fs.opener import Opener
from fs.memoryfs import MemoryFS

TEXT_FILE_TYPES = ['text/plain']


class HttpFsOpener(Opener):
    protocols = ["http", "https"]

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        r = httpx.get(fs_url)

        content_type, _ = r.headers['content-type'].split(';')

        file_name = parse_result.resource.split('/')[-1]
        mem_fs = MemoryFS()
        if content_type in TEXT_FILE_TYPES:
            mem_fs.writetext(file_name, r.text)
        else:
            mem_fs.writebytes(file_name, r.content)
        return mem_fs
