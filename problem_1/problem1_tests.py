import pytest
from url_splitter import url_split
def test_empty_string():
    test_string = "https://www.google.com/some-path"
    protocol, domain, path = url_split(test_string)
    assert protocol == "https"
    assert domain == "www.google.com"
    assert path == "some-path"

test_empty_string()
