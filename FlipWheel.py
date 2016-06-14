import winreg
def MyEnumKeys(key):
    _i = 0
    _devnames = []
    try:
        while 1:
            _keyname = winreg.EnumKey(key, _i)
            _devnames.append(_keyname)
            _i += 1
    except WindowsError:
        pass
    return _devnames
HIDKey =  winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Enum\HID")
DevNames = MyEnumKeys(HIDKey)
for keyname in DevNames:
    DevKey = winreg.OpenKey(HIDKey, keyname)
    DevDesc = MyEnumKeys(DevKey)
    for devdesc in DevDesc:
        DevDescKey = winreg.OpenKey(DevKey, devdesc)
        try:
            value, type = winreg.QueryValueEx(DevDescKey, "Service")
            if value == "mouhid":
                DevPara = winreg.OpenKey(DevDescKey, "Device Parameters",0, winreg.KEY_WRITE)
                winreg.SetValueEx(DevPara, "FlipFlopWheel", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(DevPara)
        except WindowsError:
            pass
        winreg.CloseKey(DevDescKey)
    winreg.CloseKey(DevKey)
winreg.CloseKey(HIDKey)
