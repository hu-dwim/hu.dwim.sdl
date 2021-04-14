{}:

let
  # use c2ffi from the config of your nixos install
  #pkgs = ((import <nixpkgs> {}).nixos /etc/nixos/configuration.nix).pkgs;

  # use a custom built c2ffi
  pkgs = import <nixpkgs> {};
  c2ffi = (pkgs.callPackage "/home/alendvai/workspace/c2ffi/default.nix" {
    #rev = "80a298a9c63f5b05c16a614b309c2414d439388b";
    #sha256 = "17rh1wjvpz9xqm6c8x7j23jsysaw3bdzfkkvlx91mqfblalcy164";
  });
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    sbcl curl cacert
    pkg-config
    jq
    c2ffi
    libffi.dev zlib
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
