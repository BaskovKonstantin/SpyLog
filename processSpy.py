import wmi

f = wmi.WMI()
print("pid   Process name")

for process in f.Win32_Process():
    print(f"{process.ProcessId:<10} {process.Name}")
