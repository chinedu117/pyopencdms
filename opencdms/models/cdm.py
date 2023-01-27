# =============================================================================
# MIT License
#
# Copyright (c) 2023, OpenCDMS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================
from dataclasses import dataclass
from datetime import datetime
from typing import NewType, Optional

Geography = NewType("Geography", str)


@dataclass
class ObservationType:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Short name for observation type",  # noqa
        "description": "Description of observation type",  # noqa
        "link": "Link to definition of observation type"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: int, name: str, description: str, link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class FeatureType:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Short name for feature type",  # noqa
        "description": "Description of feature type",  # noqa
        "link": "Link to definition of feature type"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: int, name: str, description: str, link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class User:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Name of user"  # noqa
    }
    _comment = "Placeholder table"  # noqa

    def __init__(self, id: str, name: str):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class ObservedProperty:
    _comments = {
        "id": "ID / primary key",  # noqa
        "short_name": "Short name representation of observed property, e.g. 'at'",  # noqa
        "standard_name": "CF standard name (if applicable), e.g. 'air_temperature'",  # noqa
        "units": "Canonical units, e.g. 'Kelvin'",  # noqa
        "description": "Description of observed property",  # noqa
        "link": "Link to definition / source of observed property"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: int, short_name: str, standard_name: Optional[str], units: str, description: str, link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class ObservingProcedure:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Name of observing procedure",  # noqa
        "description": "Description of observing procedure",  # noqa
        "link": "Link to further information"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: int, name: str, description: str, link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class RecordStatu:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Short name for status",  # noqa
        "description": "Description of the status"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: int, name: str, description: str):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class Host:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Preferred name of host",  # noqa
        "description": "Description of host",  # noqa
        "link": "URI to host, e.g. to OSCAR/Surface",  # noqa
        "location": "Location of station",  # noqa
        "elevation": "Elevation of station above mean sea level",  # noqa
        "wigos_station_identifier": "WIGOS station identifier",  # noqa
        "facility_type": "Type of observing facility, fixed land, mobile sea, etc",  # noqa
        "date_established": "Date host was first established",  # noqa
        "wmo_region": "WMO region in which the host is located",  # noqa
        "territory": "Territory the host is located in",  # noqa
        "valid_from": "Date from which the details for this record are valid",  # noqa
        "valid_to": "Date after which the details for this record are no longer valid",  # noqa
        "version": "Version number of this record",  # noqa
        "change_date": "Date this record was changed",  # noqa
        "user_id": "Which user last modified this record",  # noqa
        "status_id": "Whether this is the latest version or an archived version of the record",  # noqa
        "comments": "Free text comments on this record, for example description of changes made etc"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: str, name: str, description: Optional[str], link: Optional[str], location: Optional[Geography], elevation: Optional[float], wigos_station_identifier: Optional[str], facility_type: Optional[str], date_established: Optional[str], wmo_region: Optional[str], territory: Optional[str], valid_from: Optional[datetime], valid_to: Optional[datetime], version: int, change_date: datetime, user_id: int, status_id: int, comments: str):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class Observer:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Name of sensor",  # noqa
        "description": "Description of sensor",  # noqa
        "link": "Link to further information",  # noqa
        "location": "Location of observer",  # noqa
        "elevation": "Elevation of observer above mean sea level"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: str, name: str, description: str, link: Optional[str], location: Optional[Geography], elevation: Optional[float]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class Collection:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Name of collection",  # noqa
        "link": "Link to further information on collection"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: str, name: str, link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class Feature:
    _comments = {
        "id": "ID / primary key",  # noqa
        "type_id": "enumerated feature type",  # noqa
        "geometry": "",  # noqa
        "elevation": "Elevation of feature above mean sea level",  # noqa
        "parent_id": "Parent feature for this feature if nested",  # noqa
        "name": "Name of feature",  # noqa
        "description": "Description of feature",  # noqa
        "link": "Link to further information on feature"  # noqa
    }
    _comment = "table to contain definition of different geographic features"  # noqa

    def __init__(self, id: str, type_id: int, geometry: Geography, elevation: Optional[float], parent_id: Optional[str], name: Optional[str], description: Optional[str], link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class Source:
    _comments = {
        "id": "ID / primary key",  # noqa
        "name": "Name of source",  # noqa
        "link": "Link to further information on source"  # noqa
    }
    _comment = ""  # noqa

    def __init__(self, id: str, name: str, link: Optional[str]):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)


@dataclass
class Observation:
    _comments = {
        "id": "ID / primary key",  # noqa
        "location": "Location of observation",  # noqa
        "elevation": "Elevation of observation above mean sea level",  # noqa
        "observation_type_id": "Type of observation",  # noqa
        "phenomenon_start": "Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end",  # noqa
        "phenomenon_end": "End time of the phenomenon being observed or observing period",  # noqa
        "result_value": "The value of the result in float representation",  # noqa
        "result_uom": "Units used to represent the value being observed",  # noqa
        "result_description": "str representation of the result if applicable",  # noqa
        "result_quality": "JSON representation of the result quality, key / value pairs",  # noqa
        "result_time": "Time that the result became available",  # noqa
        "valid_from": "Time that the result starts to be valid",  # noqa
        "valid_to": "Time after which the result is no longer valid",  # noqa
        "host_id": "Host associated with making the observation, equivalent to OGC OMS 'host'",  # noqa
        "observer_id": "Observer associated with making the observation, equivalent to OGC OMS 'observer'",  # noqa
        "observed_property_id": "The phenomenon, or thing, being observed",  # noqa
        "observing_procedure_id": "Procedure used to make the observation",  # noqa
        "report_id": "Parent report ID, used to link coincident observations together",  # noqa
        "collection_id": "Primary collection or dataset that this observation belongs to",  # noqa
        "parameter": "List of key/ value pairs in dict",  # noqa
        "feature_of_interest_id": "Feature that this observation is associated with",  # noqa
        "version": "Version number of this record",  # noqa
        "change_date": "Date this record was changed",  # noqa
        "user_id": "Which user last modified this record",  # noqa
        "status_id": "Whether this is the latest version or an archived version of the record",  # noqa
        "comments": "Free text comments on this record, for example description of changes made etc",  # noqa
        "source_id": "The source of this record"  # noqa
    }
    _comment = "table to store observations"  # noqa

    def __init__(self, id: str, location: Geography, elevation: Optional[float], observation_type_id: Optional[int], phenomenon_start: Optional[datetime], phenomenon_end: datetime, result_value: float, result_uom: Optional[str], result_description: Optional[str], result_quality: Optional[dict], result_time: Optional[datetime], valid_from: Optional[datetime], valid_to: Optional[datetime], host_id: Optional[str], observer_id: Optional[str], observed_property_id: int, observing_procedure_id: Optional[int], report_id: Optional[str], collection_id: Optional[str], parameter: Optional[dict], feature_of_interest_id: Optional[str], version: int, change_date: datetime, user_id: int, status_id: int, comments: str, source_id: int):  # noqa
        super().__init__()  # noqa

    def table_info(self) -> str:
        return self._comment

    def column_info(self, column: str) -> str:
        return self._comments.get(column)
