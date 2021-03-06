# hu.dwim.sdl

## What

It's a Common Lisp [FFI](https://en.wikipedia.org/wiki/Foreign_function_interface)
for http://libsdl.org/ (SDL2).

## Why

The alternative projects are partial, while this one uses
[cffi/c2ffi](https://github.com/cffi/cffi) to automatically generate the
CFFI bindings for the various subsystems of [SDL2](http://libsdl.org/).

It only requires vanilla CFFI when used, no extra dependencies.

## Who

Written by [attila@lendvai.name](mailto:attila@lendvai.name).

## Where

The primary communication channel is the facilities on
[the project's GitHub page](https://github.com/hu-dwim/hu.dwim.sdl).

## How

The project uses [CFFI/C2FFI](https://github.com/cffi/cffi).
Its ASDF extension does two things:

1. If needed it can invoke [c2ffi](https://github.com/rpav/c2ffi) to process a C header file
and emit a c2ffi spec file (a json file) that contains every detail needed for a given platform
to generate its FFI. Yours truely has run this phase and checked in the
resulting spec files into the [c2ffi-spec/](c2ffi-spec/) directory, so that
users don't need to have a working c2ffi executable and the SDL dev headers
installed.

2. Based on the spec file it generates the CFFI forms into a lisp file (placed next to the spec file)
and continues as if it was just another lisp file written by hand. (These lisp files
could also be checked in the repo, but for now they are not.)

## Status

It contains a complete FFI for ```sdl.h```, ```sdl-gfx.h```, ```sdl-ttf.h```, and ```sdl-image.h```.
Not much has been added yet to lispify the SDL API, but the CFFI binding part is complete.
