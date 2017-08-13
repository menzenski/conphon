#!/usr/bin/env python3

import conphon


def test_version_number():
    package_version = conphon.__version__
    print("package version is {}".format(package_version))
    assert package_version and isinstance(package_version, str)
