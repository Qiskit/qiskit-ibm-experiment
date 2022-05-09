# This code is part of Qiskit.
#
# (C) Copyright IBM 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Dataclasses for returned results"""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class ExperimentData:
    """Dataclass for experiments"""

    experiment_id: str
    parent_id: Optional[str] = None
    experiment_type: str = None
    backend: Optional[str] = None
    tags: Optional[List[str]] = field(default_factory=lambda: [])
    job_ids: Optional[List[str]] = field(default_factory=lambda: [])
    share_level: Optional[str] = None
    metadata: Optional[Dict[str, str]] = field(default_factory=lambda: {})
    figure_names: Optional[List[str]] = field(default_factory=lambda: [])
    notes: Optional[str] = None
    hub: Optional[str] = None
    group: Optional[str] = None
    project: Optional[str] = None
    owner: Optional[str] = None
    creation_datetime: Optional[datetime] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    updated_datetime: Optional[datetime] = None

    def __str__(self):
        ret = ""
        ret += f"Experiment: {self.experiment_type}"
        ret += f"\nExperiment ID: {self.experiment_id}"
        if self.backend:
            ret += f"\nBackend: {self.backend}"
        if self.tags:
            ret += f"\nTags: {self.tags}"
        ret += f"\nHub\\Group\\Project: {self.hub}\\{self.group}\\{self.project}"
        if self.creation_datetime:
            ret += f"\nCreated at: {self.creation_datetime}"
        if self.start_datetime:
            ret += f"\nStarted at: {self.start_datetime}"
        if self.end_datetime:
            ret += f"\nEnded at: {self.end_datetime}"
        if self.updated_datetime:
            ret += f"\nUpdated at: {self.updated_datetime}"
        if self.metadata:
            ret += f"\nMetadata: {self.metadata}"
        if self.figure_names:
            ret += f"\nFigures: {self.figure_names}"
        return ret

@dataclass
class AnalysisResultData:
    """Dataclass for experiment analysis results"""

    experiment_id: str
    result_id: str
    result_type: str
    result_data: Dict[str, Any]
    device_components: List[str]
    quality: "ResultQuality"
    verified: bool
    tags: List[str]
    backend_name: str
    creation_datetime: datetime
    updated_datetime: Optional[datetime] = None
    chisq: Optional[float] = None

    def __str__(self):
        ret = f"Result {self.result_type}"
        ret += f"\nResult ID: {self.result_id}"
        ret += f"\nExperiment ID: {self.experiment_id}"
        ret += f"\nBackend: {self.backend_name}"
        ret += f"\nQuality: {self.quality}"
        ret += f"\nVerified: {self.verified}"
        ret += f"\nDevice components: {self.device_components}"
        ret += f"\nData: {self.result_data}"
        if self.chisq:
            ret += f"\nChi Square: {self.chisq}"
        if self.tags:
            ret += f"\nTags: {self.tags}"
        if self.creation_datetime:
            ret += f"\nCreated at: {self.creation_datetime}"
        if self.updated_datetime:
            ret += f"\nUpdated at: {self.updated_datetime}"
        return ret

exp1 = ExperimentData()
exp2 = ExperimentData()
exp1.tags.append("foo")
exp2.tags.append("bar")

print(exp1)
print("****")
print(exp2)