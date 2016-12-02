import pytest

from puzzles import day1
import pdb

class TestDirectionParser(object):
    def test_correctly_parses_direction(self):
        parser = day1.DirectionParser('L1')
        assert parser.direction == 'L'

    def test_correctly_parsers_distance(self):
        parser = day1.DirectionParser('L1')
        assert parser.distance == 1

    def test_raises_error_when_direction_string_is_bad(self):
        with pytest.raises(day1.DirectionParser.BadDirectionStringError):
            parser = day1.DirectionParser('some bogus string')

class TestGridNavigator(object):
    def 
