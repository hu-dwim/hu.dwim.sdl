# hu.dwim.sdl

## What

It's a Common Lisp [FFI](https://en.wikipedia.org/wiki/Foreign_function_interface)
for http://libsdl.org/ (SDL2).

## Why

The alternative projects are partial, while this one uses
[cffi/c2ffi](https://github.com/cffi/cffi) to automatically generate
the complete CFFI bindings for the various subsystems of
[SDL2](http://libsdl.org/).

It only requires vanilla CFFI when used, no extra dependencies.

## Who

Written by [attila@lendvai.name](mailto:attila@lendvai.name).

## Where

The primary communication channel is the facilities on
[the project's GitHub page](https://github.com/hu-dwim/hu.dwim.sdl).

## How

This project uses [CFFI/C2FFI](https://github.com/cffi/cffi), whose
ASDF extension does two things:

1. When needed, it can invoke [c2ffi](https://github.com/rpav/c2ffi)
to process a C header file and emit a c2ffi spec file (a json file)
that contains every detail needed to generate an FFI for a given
platform. But yours truly has run this phase, and checked in the
resulting spec files into the [c2ffi-spec/](c2ffi-spec/)
directory. This way users don't need to have a working c2ffi
executable, nor the SDL dev headers installed.

2. Based on the above mentioned spec file, it generates the CFFI forms
into a lisp file (placed next to the spec file), and continues as if
it was just another lisp file written by hand. (These lisp files could
also be committed into the repo, but for now they are not, because
their regeneration is automatic and painless.)

### Regenerate the spec files

This should only need to be done by the project maintainer when the
SDL API has some new functionality that is needed on the Lisp
side. Once the `*.spec` files got regenerated, they should be pushed
into the git repo; i.e. the users of `hu.dwim.sdl` don't need to do
this.

Once the necessary dependencies are available (see below):

```
rm -f c2ffi-spec/*.spec &&
  ./bin/generate-spec-files.sh &&
  ./bin/filter-spec-files.sh
```

#### On Debian

```
sudo apt-get install curl sbcl libsdl2-dev jq
```

#### On NixOS

```
$ nix-shell --pure
```

#### On Guix

Just run the script. It should detect that Guix is available and
transparently enter a `guix shell` with the necessary packages.

## Status

It contains a complete FFI for `sdl.h`, `sdl-gfx.h`, `sdl-ttf.h`, and `sdl-image.h`.
Not much has been added yet to lispify the SDL API, but the CFFI binding part is complete.
