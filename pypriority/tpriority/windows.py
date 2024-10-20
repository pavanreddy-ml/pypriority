import ctypes
from ctypes import wintypes
import warnings

class TPriorityWindows:
    THREAD_SET_INFORMATION = 0x0020
    THREAD_QUERY_INFORMATION = 0x0040

    def set_thread_priority(self, priority):
        thread_id = ctypes.windll.kernel32.GetCurrentThreadId()
        windows_priority = self._get_mapped_priority(priority)
        handle = ctypes.windll.kernel32.OpenThread(self.THREAD_SET_INFORMATION | self.THREAD_QUERY_INFORMATION, False, thread_id)
        if not handle:
            raise OSError(f"Failed to open thread {thread_id}")

        try:
            if not ctypes.windll.kernel32.SetThreadPriority(handle, windows_priority):
                raise OSError(f"Failed to set thread priority for thread {thread_id}")
        finally:
            ctypes.windll.kernel32.CloseHandle(handle)

    def _get_mapped_priority(self, priority):
        PRIORITY_MAPPING = {
            -3: -15,  # THREAD_PRIORITY_IDLE
            -2: -2,   # THREAD_PRIORITY_LOWEST
            -1: -1,   # THREAD_PRIORITY_BELOW_NORMAL
             0: 0,    # THREAD_PRIORITY_NORMAL
             1: 1,    # THREAD_PRIORITY_ABOVE_NORMAL
             2: 2,    # THREAD_PRIORITY_HIGHEST
             3: 15    # THREAD_PRIORITY_TIME_CRITICAL
        }
        return PRIORITY_MAPPING[priority]