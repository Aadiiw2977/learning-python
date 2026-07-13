import platform
from datetime import datetime

def banner():
    print("╔════════════════════════════════════════════╗")
    print("║          AADIIW SYSTEM INFORMATION         ║")
    print("║      Python • Linux • Android • Termux     ║")
    print("╚════════════════════════════════════════════╝")

def show_info():
    print(f"🖥️  System   : {platform.system()}")
    print(f"📱 Machine  : {platform.machine()}")
    print(f"⚙️  Processor: {platform.processor()}")
    print(f"🐍 Python   : {platform.python_version()}")
    print(f"🕒 Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

banner()
show_info()
