import pytest
from unittest import TestCase

from pyobis.obisutils import obis_baseurl, obis_GET
import example_responses_occurrence

class Test_obis_GET(TestCase):
    @pytest.mark.uses_internet
    def test_obis_get(self):
        "OBIS API's response for this record is same as when test was written."
        url = f'{obis_baseurl}occurrence/00023244-457b-48be-8db1-1334d44d6624'
        out = obis_GET(url, {}, 'application/json; charset=utf-8')
        self.assertEqual(
            out,
            example_responses_occurrence.abra_alba
        )
