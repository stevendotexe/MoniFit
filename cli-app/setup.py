from cx_Freeze import setup, Executable

modules = [
    'cool', 
    'figletrender', 
    'login', 
    'perhitungan', 
    'rekomendasiMakanan', 
    'vendorselection'
    ]

setup(
    name="YourAppName",
    version="1.0",
    description="Your description",
    options={'build_exe': {'includes':modules}},
    executables=[Executable("main.py")]
)