# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ovsdbapp.backend.ovs_idl import fixtures
from ovsdbapp.backend.ovs_idl import vlog
from ovsdbapp.tests import base


class TestOvsdbVlog(base.TestCase):
    def setUp(self):
        super(TestOvsdbVlog, self).setUp()
        self.useFixture(fixtures.OvsdbVlogFixture())

    def test_vlog_patched(self):
        for log_fn in vlog.ALL_LEVELS:
            self.assertTrue(vlog.is_patched(log_fn))

    def test_vlog_reset(self):
        vlog.reset_logger()
        for log_fn in vlog.ALL_LEVELS:
            self.assertFalse(vlog.is_patched(log_fn))

    def test_vlog_patch_all_but_debug(self):
        vlog.reset_logger()
        removed_level = vlog.DEBUG
        levels = set(vlog.ALL_LEVELS) - set([removed_level])
        vlog.use_python_logger(levels)
        for lvl in levels:
            self.assertTrue(vlog.is_patched(lvl))
        self.assertFalse(vlog.is_patched(removed_level))

    def test_vlog_max_level(self):
        vlog.reset_logger()
        max_level = vlog.WARN
        vlog.use_python_logger(max_level=max_level)
        patched_levels = (vlog.CRITICAL, vlog.ERROR, vlog.WARN)
        unpatched_levels = (vlog.INFO, vlog.DEBUG)
        for lvl in patched_levels:
            self.assertTrue(vlog.is_patched(lvl))
        for lvl in unpatched_levels:
            self.assertFalse(vlog.is_patched(lvl))
