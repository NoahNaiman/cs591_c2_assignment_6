import pytest
def test_empty_string():
    test_string = "https://www.google.com/some-path"
    protocol, domain, path = url_splitter.split(test_string)
    assert protocol == "https"
    assert domain == "www.google.com"
    assert path == "some-path"
