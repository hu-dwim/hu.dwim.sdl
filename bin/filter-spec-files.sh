#!/usr/bin/env bash

# This file is called by generate-spec-files.sh. No need to run it manually.

# https://stedolan.github.io/jq/manual/

patterns=(
    "c2ffi-spec/sdl.*.spec"
    "c2ffi-spec/sdl-gfx.*.spec"
    "c2ffi-spec/sdl-ttf.*.spec"
    "c2ffi-spec/sdl-image.*.spec"
)
# one entry for each pattern above (i.e. this should be a multi
# dimensional array, but this is all the shell fu that i've tolerated
# into my life...)
queries=(
    # it's tempting to do [sort_by(.name) | .[] |... for nice
    # diff'ability, but the lisp generator works in a streaming
    # fashion, i.e. it is sensitive to the order of the definitions
    # (e.g. it filters out struct fields whose type hasn't been seen
    # yet).
    '[.[] | select(.location | contains("/types.h") or contains("/stdint-uintn.h") or contains("/stdint-intn.h") or contains("/stddef.h") or test("SDL2/.+\\.h"))]'
    '[.[] | select(.location | contains("SDL2/SDL2_gfxPrimitives.h") or contains("SDL2/SDL2_framerate.h") or contains("SDL2/SDL2_imageFilter.h") or contains("SDL2/SDL2_rotozoom.h"))]'
    '[.[] | select(.location | contains("SDL2/SDL_ttf.h"))]'
    '[.[] | select(.location | contains("SDL2/SDL_image.h"))]'
)

for i in "${!patterns[@]}"; do
    for file in ${patterns[$i]}; do
        if [ -e ${file} ]; then # avoid creating a 'sdl.*.spec' if it didn't match anything
            echo "Running jq --sort-keys '${queries[$i]}' ${file}"
            jq --sort-keys "${queries[$i]}" ${file} >${file}.filtered &&
                mv ${file}.filtered ${file}
            # This removes the location entries which shrinks
            # the diff size.
            # NOTE: this cannot be done, because cffi/c2ffi uses
            # the location field to decide whether to include the
            # definition or not.
            # Remove from the toplevel entries:
            # jq 'del( .[] .location )' ${file} >${file}.filtered &&
            #     mv ${file}.filtered ${file}
            # Remove from nested entries, too:
            # jq 'map(del(.location))' ${file} >${file}.filtered &&
            #     mv ${file}.filtered ${file}
        fi
    done
done
