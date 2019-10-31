#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
from conans.model.version import Version

if __name__ == "__main__":
    builder = build_template_default.get_builder(pure_c=False, build_policy="missing")
    builder.remove_build_if(lambda build:
                            build.settings["os"] == "Linux"
                            and build.settings["compiler"] == "gcc"
                            and Version(build.settings["compiler.version"]) >= "5"
                            and build.settings["compiler.libcxx"] != "libstdc++11")
    builder.remove_build_if(lambda build:
                            build.settings["compiler"] == "clang" and build.settings["compiler.libcxx"] != "libc++")
    builder.run()
