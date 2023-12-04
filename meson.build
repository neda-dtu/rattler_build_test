project('pywasp', ['c', 'fortran'],
  default_options : ['warning_level=0', 'buildtype=plain', 'c_std=c99', 'fortran_std=legacy'],
  version: run_command('python', '-c', 'from setuptools_scm import get_version; print(get_version())', check : true).stdout().strip()
)

system = build_machine.system()
build_profile = 'release'
#########################################################################################
# Setup compiler information for Python extension modules
#########################################################################################

# Configure python
py_mod = import('python')
py3 = py_mod.find_installation('python3', pure: false)
py3_dep = py3.dependency()
message(py3.path())
message(py3.get_install_dir())

cwd = run_command(py3, ['-c', 'from pathlib import Path; print(Path().cwd())'], check : true).stdout().strip()
message(cwd)

# Get include directories for f2py build
incdir_numpy = run_command(py3,
    ['-c', 'from pathlib import Path; import numpy; inc_path = Path(numpy.get_include()); cwd_path=Path().cwd(); out_path = inc_path.relative_to(cwd_path) if inc_path.is_relative_to(cwd_path) else inc_path; print(out_path)'],
    check : true
).stdout().strip()
message(incdir_numpy)

incdir_f2py = run_command(py3,
    ['-c', 'from pathlib import Path; import numpy.f2py; inc_path = Path(numpy.f2py.get_include()); cwd_path=Path().cwd(); out_path = inc_path.relative_to(cwd_path) if inc_path.is_relative_to(cwd_path) else inc_path; print(out_path)'],
    check : true
).stdout().strip()
message(incdir_f2py)

inc_np = include_directories(incdir_numpy, incdir_f2py)

# Set default options used in all build types
f2py_build_args = [
  '-fno-unsafe-math-optimizations',
  '-frounding-math',
  '-fsignaling-nans',
  '-fopenmp',
  '-cpp',
]
# Add flag for argument mismatch from gfortran > 10
compiler = meson.get_compiler('fortran')
if compiler.has_argument('-fallow-argument-mismatch')
  f2py_build_args += '-fallow-argument-mismatch'
endif
f2py_deps = [py3_dep]

# Add profile dependent optimizations
if build_profile == 'development'
  f2py_build_args += [
    '-O0',
    '-g',
    # '-Wall',
    # '-fcheck=all',
    '-DF2PY_REPORT_ON_ARRAY_COPY=1',
    '-DF2PY_REPORT_ATEXIT'
  ]
  lic_deps = f2py_deps
else
  f2py_build_args += [
    '-O3',
  ]
endif

waspcoredir = 'modules/waspcore/'
lincom_dir = 'pywasp/lincom/'

#########################################################################################
# Process Python extensions
# First build source code using f2py, then compile the extension module
#########################################################################################
## fort_add
message('Building Rvea0279')
fort_add_sources = [
  'rattler_build_test/add.F90'
]
fort_add_f2py = custom_target('fort_addmodule.c',
  input : fort_add_sources, # .f so no F90 wrappers
  output : ['fort_addmodule.c', 'fort_add-f2pywrappers2.f90'],
  command : [ py3, '-m', 'numpy.f2py', '@INPUT@', '-m', 'fort_add', '--lower']
)
fort_add_ext = py3.extension_module('fort_add',
  fort_add_sources,
  fort_add_f2py,
  incdir_f2py + '/fortranobject.c',
  include_directories: inc_np,
  dependencies : f2py_deps,
  fortran_args : f2py_build_args,
  install: true,
  subdir: 'rattler_build_test/'
)

python_root_sources = [
  'rattler_build_test/__init__.py',
  'rattler_build_test/add.py',
]
py3.install_sources(python_root_sources, subdir: 'rattler_build_test')
