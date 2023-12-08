
from Scanner import Scanner

def test_p1():
    file = open('p1.txt', 'r')
    scanner = Scanner(file.read())


def test_p1error():
    file = open('p1_error.txt', 'r')
    scanner = Scanner(file.read())


def test_p2():
    file = open('p2.txt', 'r')
    scanner = Scanner(file.read())


def test_p3():
    file = open('p3.txt', 'r')
    scanner = Scanner(file.read())

test_p1()