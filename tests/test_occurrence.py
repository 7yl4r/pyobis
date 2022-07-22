"""Tests for occurrences module - search methods"""
import json
import os
import pytest
from unittest.mock import patch

from pyobis import occurrences as occ

@pytest.mark.uses_internet
def test_occurrences_search():
    "occurrences.search - basic test"
    res = occ.search(scientificname = 'Mola mola', size=10100)
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__
    res = occ.search(scientificname="Abra alba",mof=True,size=100, hasextensions="MeasurementOrFact")
    assert "Abra alba"==res.scientificName[0]

@pytest.mark.uses_internet
def test_occurrences_get():
    "occurrences.get - basic test"
    res = occ.get(id = '00023244-457b-48be-8db1-1334d44d6624')
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__

@pytest.mark.uses_internet
def test_occurrences_grid():
    "occurrences.grid - basic test"
    res = occ.grid(5, geojson=True, scientificname='Abra alba')
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__
    res = occ.grid(5, geojson=False, scientificname='Mola mola')

@pytest.mark.uses_internet
def test_occurrences_getpoints():
    "occurrences.getpoints - basic test"
    res = occ.getpoints(scientificname = ['Mola mola','Abra alba'])
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__

@pytest.mark.uses_internet
def test_occurrences_point():
    "occurrences.point - basic test"
    res = occ.point(x=1.77,y=54.22,scientificname = 'Mola mola')
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__

@pytest.mark.uses_internet
def test_occurrences_tile():
    "occurrences.tile - basic test"
    res = occ.tile(x=1.77,y=52.26,z=0.5,mvt=0, scientificname = 'Mola mola')
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__
    res = occ.tile(x=1.77,y=52.26,z=0.5,mvt=1, scientificname = 'Mola mola')

@pytest.mark.uses_internet
def test_occurrences_centroid():
    "occurrences.centroid - basic test"
    res = occ.centroid(scientificname = 'Mola mola')
    assert 'dict' == res.__class__.__name__
    assert 2 == len(res)
    assert list == list(res.keys()).__class__


import example_responses_occurrence
@pytest.mark.parametrize(
    "mock_api_response",
    [example_responses_occurrence.abra_alba, example_responses_occurrence.abra_alba_2]
)
def test_occurrences_search_mof(mock_api_response):
    """
    mock occ.search with MoFs that returns >1 result.
    Demonstrates https://github.com/iobis/pyobis/issues/32.
    """
    with patch('pyobis.occurrences.occurrences.obis_GET') as obis_getter:
        obis_getter.return_value = mock_api_response
        res = occ.search(
            scientificname="Abcdefg", mof=True
        )
        assert len(res > 0)
