#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by robbenmu
# Copyright (c) 2015 robbenmu
#
# License: MIT
#

"""This module exports the Fecs plugin class."""

from SublimeLinter.lint import Linter


class Fecs(Linter):

    """Provides an interface to fecs."""

    syntax = ('javascript', 'html', 'javascriptnext', 'javascript (jsx)', 'javascript (babel)')
    cmd = 'fecs --silent --reporter=baidu --format=checkstyle'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'
    regex = (
        r'<error line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?P<warning>error)" '
        r'source="fecs" message="(?P<message>.+?)"'
    )
    multiline = True
    selectors = {'html': 'source.js.embedded.html'}
    tempfile_suffix = 'js'
