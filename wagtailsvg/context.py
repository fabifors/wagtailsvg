import os
import pkg_resources
from django.conf import settings

# =======================================
# Context variables passed for javascript
# =======================================

try:
    #  Production part
    VERSION = pkg_resources.get_distribution("wagtailsvg").version
except pkg_resources.DistributionNotFound:
    #  Develop part
    VERSION = "0.0.39"
