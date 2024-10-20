from . import TPriorityBase

import ctypes
from ctypes import wintypes

import warnings


class TPriorityUnix(TPriorityBase):
    def set_priority(self, priority):
        print(f"Setting thread priority to {priority} on Unix")


    def _get_mapped_priority(self, priority):
        if priority < -15:
            warnings.warn("Priority less than -15, setting to -15.", UserWarning)
            priority = -15
        elif priority > 15:
            warnings.warn(f"Priority greater than 15, setting to 15.", UserWarning)
            priority = 15

        unix_priority = int((-priority + 15) * (39 / 30) - 20)

        return unix_priority