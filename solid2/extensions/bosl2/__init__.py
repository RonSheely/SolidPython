from ... import config

if config.use_implicit_builtins:
    raise Exception("ExpSolid: unfortunately ImplicitCAD can't handle bosl2...")

from .std import *

from .bosl2_patches import __nothing__
