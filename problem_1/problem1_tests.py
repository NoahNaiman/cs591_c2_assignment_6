import pytest
from url_splitter import url_split
def test1():
    test_string = "https://www.google.com/some-path"
    protocol, domain, path = url_split(test_string)
    assert protocol == "https"
    assert domain == "www.google.com"
    assert path == "some-path"

def test2():
    test_string = ""
    protocol, domain, path = url_split(test_string)
    assert protocol == ""
    assert domain == ""
    assert path == "" 

def test3():
    test_string = "ftp://bu.edu/"
    protocol, domain, path = url_split(test_string)
    assert protocol == "ftp"
    assert domain == "bu.edu"
    assert path == ""

def test4():
    test_string = "https://www.google.com/some-path/more-path/other-stuff"
    protocol, domain, path = url_split(test_string)
    assert protocol == "https"
    assert domain == "www.google.com"
    assert path == "some-path/more-path/other-stuff"

test1()
test2()
test3()
test4()
