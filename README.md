# Rattler Build Test

This is a small python project setup to test rattler-build for our use cases

## Issue 1

rattler-build returns a hash based package while mambabuild doesn't.

All packages can be found in conda_env.yml.

There are both meta.yaml and recipe.yaml files in the recipe directory, which are used for mambabuild and rattler-build respectively. The meta.yaml is setup to use a version number of 0.0.2, while the recipe.yaml uses version number of 0.0.1. They should behave the same.


To test I do the following:

```sh
time conda mambabuild -c conda-forge --output-folder ./output/ recipe/
time rattler-build build -c conda-forge -r recipe/
```

Then when I do an `ls output/noarch` I get the files `rattler_build_test-0.0.4-1.tar.bz2` and `rattler_build_test-0.0.4-pyh4616a5c_0.tar.bz2`


## Issue 2 

In the same setup, the package build with mambabuild includes the rattler_build_test site-packages directory, while rattler-build's doesn't. 

This is now resolved by moving the python and other dependencies to host instead of build. 