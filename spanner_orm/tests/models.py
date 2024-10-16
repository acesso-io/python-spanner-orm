# python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Models used by unit tests."""

from spanner_orm import field, index, model, relationship


class SmallTestModel(model.Model):
    """Model class used for testing."""

    __table__ = "SmallTestModel"
    key = field.Field(field.String, primary_key=True)
    value_1 = field.Field(field.String)
    value_2 = field.Field(field.String, nullable=True)
    index_1 = index.Index(["value_1"])


class SmallTestParentModel(model.Model):
    """Model class used for testing."""

    __table__ = "SmallTestParentModel"
    key = field.Field(field.String, primary_key=True)
    value_1 = field.Field(field.String)
    value_2 = field.Field(field.String, nullable=True)
    index_1 = index.Index(["value_1"])

    children = relationship.Relationship(
        "spanner_orm.tests.models.ChildTestModel", {"key": "key"}
    )


class ChildTestModel(model.Model):
    """Model class for testing interleaved tables."""

    __table__ = "ChildTestModel"
    __interleaved__ = "SmallTestParentModel"

    key = field.Field(field.String, primary_key=True)
    child_key = field.Field(field.String, primary_key=True)


class IndexTestModel(model.Model):
    __table__ = "IndexTestModel"

    key = field.Field(field.String, primary_key=True)
    value = field.Field(field.String)

    value_idx = index.Index(["value"], name="value")
    value_idx2 = index.Index(
        ["value"], name="value_desc", column_ordering={"value": False}
    )


class FieldCustomNameTestModel(model.Model):
    __table__ = "FieldCustomNameTestModel"

    key = field.Field(field.String, primary_key=True, name="key2")


class RelationshipTestModel(model.Model):
    """Model class for testing relationships."""

    __table__ = "RelationshipTestModel"
    parent_key = field.Field(field.String, primary_key=True)
    child_key = field.Field(field.String, primary_key=True)
    parent = relationship.Relationship(
        "spanner_orm.tests.models.SmallTestModel", {"parent_key": "key"}, single=True
    )
    parents = relationship.Relationship(
        "spanner_orm.tests.models.SmallTestModel", {"parent_key": "key"}
    )
    fk_multicolumn = relationship.Relationship(
        "spanner_orm.tests.models.SmallTestModel",
        {"parent_key": "key", "parent_key2": "key2"},
    )


class InheritanceTestModel(SmallTestModel):
    """Model class used for testing model inheritance."""

    value_3 = field.Field(field.String, nullable=True)


class UnittestModel(model.Model):
    """Model class used for model testing."""

    __table__ = "table"
    int_ = field.Field(field.Integer, primary_key=True)
    int_2 = field.Field(field.Integer, nullable=True)
    float_ = field.Field(field.Float, primary_key=True)
    float_2 = field.Field(field.Float, nullable=True)
    string = field.Field(field.String, primary_key=True)
    string_2 = field.Field(field.String, nullable=True)
    string_3 = field.Field(field.String, nullable=True, size=10)
    timestamp = field.Field(field.Timestamp)
    timestamp_2 = field.Field(
        field.Timestamp, nullable=True, allow_commit_timestamp=True
    )
    date = field.Field(field.Date, nullable=True)
    bytes_ = field.Field(field.Bytes, nullable=True)
    bytes_2 = field.Field(field.Bytes, nullable=True, size=2048)
    json = field.Field(field.Json, nullable=True)
    bool_array = field.Field(field.BoolArray, nullable=True)
    int_array = field.Field(field.IntegerArray, nullable=True)
    float_array = field.Field(field.FloatArray, nullable=True)
    date_array = field.Field(field.DateArray, nullable=True)
    string_array = field.Field(field.StringArray, nullable=True)
    string_array_2 = field.Field(field.StringArray, nullable=True, size=50)

    test_index = index.Index(["string_2"])
