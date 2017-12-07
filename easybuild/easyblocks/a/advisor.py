##
# Copyright 2009-2017 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/easybuilders/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for installing the Intel Advisor XE, implemented as an easyblock

@author: Lumir Jasiok (IT4Innovations)
@author: Damian Alvarez (Forschungszentrum Juelich GmbH)
"""

from distutils.version import LooseVersion

from easybuild.easyblocks.generic.intelbase import IntelBase

class EB_Advisor(IntelBase):
    """
    Support for installing Intel Advisor XE
    """

    def __init__(self, *args, **kwargs):
        """Constructor, initialize class variables."""
        super(EB_Advisor, self).__init__(*args, **kwargs)
        if LooseVersion(self.version) < LooseVersion('2017'):
            self.base_path = 'advisor_xe'
        else:
            self.base_path = 'advisor'

    def make_module_req_guess(self):
        """Find reasonable paths for Advisor"""
        return _make_module_req_guess_tools(self)

    def sanity_check_step(self):
        """Custom sanity check paths for Advisor"""
        binaries = ['advixe-cl', 'advixe-feedback', 'advixe-gui', 'advixe-runss', 'advixe-runtrc', 'advixe-runtc']
        custom_paths = _get_custom_paths_tools(self,binaries)
        super(EB_Advisor, self).sanity_check_step(custom_paths=custom_paths)
