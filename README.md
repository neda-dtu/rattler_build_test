# Rattler Build Test

This is a small python project setup to test rattler-build for building with meson-python and f2py

This was tested using rattler-build 0.5.2

## build package [noarch]

`rattler-build -r recipe/recipe.yaml`

This recipe uses the `c-compiler` and `fortran-compiler` packages directly, which prevents the noarch compiler check from triggering. The package is built and the tests run successfully.

## Build package [Error]

`rattler-build -r recipe/recipe_error.yaml`

This recipe places the `${{ compiler()}}` Jinja commands in the build section, and removes noarch. 

The error is about patchelf 

```
patchelf for "/tmp/rattler_build_test4tc8NR/lib/python3.11/site-packages/rattler_build_test/fort_add.cpython-311-x86_64-linux-gnu.so": "$ORIGIN/../../..:/home/neil/DTU/repos/tmp/ratter_build_test/output/bld/rattler-build_rattler_build_test_1701707301/build_env/lib"
Error:   × Relink error: Error relinking shared object: failed to read or write elf file: No such file or directory (os error 2)
  ├─▶ Error relinking shared object: failed to read or write elf file: No such file or directory (os error 2)
  ├─▶ failed to read or write elf file: No such file or directory (os error 2)
  ╰─▶ No such file or directory (os error 2)
```
