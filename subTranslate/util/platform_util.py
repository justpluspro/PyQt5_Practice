import platform


def get_platform() -> str:
    """
    获取系统类型
    :return:  str
    """
    sys_platform = platform.platform().lower()
    if "windows" in sys_platform:
        return "windows"
    elif "macos" in sys_platform:
        return "macos"
    elif "linux" in sys_platform:
        return "linux"
    else:
        return "unknown"
