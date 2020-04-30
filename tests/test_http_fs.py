from unittest.mock import MagicMock, patch

import fs.errors
from nose.tools import eq_, raises


@patch("httpfs.fs.httpx.get")
def test_get_a_file(fake_get):
    fake_get.return_value = MagicMock(
        headers={"content-type": "text/plain; UTF-8"},
        content=bytes("abc", "utf-8"),
        status_code=200,
    )
    import fs

    with fs.open_fs("https://example.com/_version.py.jj2") as f:
        eq_(f.readtext("/_version.py.jj2"), "abc")


@patch("httpfs.fs.httpx.get")
def test_get_a_binary_file(fake_get):
    fake_get.return_value = MagicMock(
        headers={"content-type": "text/plain; UTF-8"},
        content=bytes("abc", "utf-8"),
        status_code=200,
    )
    import fs

    with fs.open_fs("https://example.com/_version.py.jj2") as f:
        eq_(f.readbytes("/_version.py.jj2"), bytes("abc", "utf-8"))


@raises(fs.errors.CreateFailed)
@patch("httpfs.fs.httpx.get")
def test_failed_to_get_a_file(fake_get):
    fake_get.return_value = MagicMock(
        headers={"content-type": "image/jpeg;"},
        content=bytes("abc", "utf-8"),
        status_code=404,
    )
    import fs

    with fs.open_fs("https://example.com/_version.py.jj2") as f:
        f.readbytes("/_version.py.jj2")
