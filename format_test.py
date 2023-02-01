#!/usr/bin/env python
#
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import json
import logging
import os
import pkgutil
import re
import subprocess  # nosec
import time
import uuid
from enum import Enum
from shutil import which
from typing import Callable, Dict, List, Optional, Tuple, Type, TypeVar
from urllib.parse import urlparse
from uuid import UUID

import semver
from memoization import cached
from onefuzztypes import (
    enums,
    events,
    models,
    primitives,
    requests,
    responses,
    webhooks,
)
from onefuzztypes.enums import TaskType
from pydantic import BaseModel
from requests import Response
from six.moves import input  # workaround for static analysis

from .__version__ import __version__
from .azcopy import azcopy_sync
from .backend import Backend, BackendConfig, ContainerWrapper, wait
from .ssh import build_ssh_command, ssh_connect, temp_file
