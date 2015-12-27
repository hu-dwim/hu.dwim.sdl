# hu.dwim.sdl

## What

It's a Common Lisp [FFI](https://en.wikipedia.org/wiki/Foreign_function_interface)
for http://libsdl.org/ (SDL2).

## Why

The other FFI bindings are partial, while this one already includes the
[CFFI](https://github.com/cffi/cffi) bindings for the various subsystems
of SDL2. Some of the competitors also depend on extra libraries while
some may prefer to stick to using vanilla CFFI.

## Who

Written by [attila@lendvai.name](mailto:attila@lendvai.name). The primary
communication channel is the facilities on [the project GitHub](https://github.com/attila-lendvai/hu.dwim.sdl).

## How

The project uses [CFFI/C2FFI](https://github.com/attila-lendvai/cffi),
a yet to be merged extension of CFFI. Its ASDF extension can do two things:

1. If needed it can invoke https://github.com/rpav/c2ffi to process a C header file
and emit a json spec file that contains everything needed for a given platform
to generate the FFI. (Yours truely has run this phase and checked in the
resulting spec files into the [c2ffi-spec/](c2ffi-spec/) directory, so that
users don't need to have c2ffi and the SDL dev headers installed.)

2. It generates the needed CFFI forms into a temporary lisp file (in the
ASDF fasl cache) and continues as if it was just another lisp file written
by hand.

## Status

It's a young project and requires various, yet to be merged CFFI changes.
There's not much extra lispy functionality added, but the CFFI binding part
is complete, including the TTF, GFX, and IMG subsystems.
