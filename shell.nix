{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    sbcl curl cacert
    pkg-config
    # TODO once it's been merged into nixos c2ffi
    libffi.dev
    SDL2 SDL2_gfx SDL2_image SDL2_ttf
  ];

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath (with pkgs; [
    libffi
    SDL2 SDL2_gfx SDL2_image SDL2_ttf
  ]);

  shellHook =
  ''
    alias ..='cd ..'
    alias ...='cd ../..'
  '';
}
