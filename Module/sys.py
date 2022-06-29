import platform


# built-in modules platform.system
x = platform.system()
print(x)

y = platform.machine()
print(y)

z = platform.processor()
print(z)

dir1 = dir(platform)
print("built-in function: ", dir1)

# Windows
# AMD64
# Intel64 Family 6 Model 165 Stepping 5, GenuineIntel
# built-in function:  ['_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES',
#  '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__',
#  '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re',
#  '_default_architecture', '_follow_symlinks', '_ironpython26_sys_version_parser',
#  '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml',
#  '_node', '_norm_version', '_platform', '_platform_cache', '_pypy_sys_version_parser',
#  '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname',
#  '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 
# 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor',
#  'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 
# 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias',
#  'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']