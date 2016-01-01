(asdf:defsystem :hu.dwim.sdl
  :description "Common Lisp FFI wrapper for libSDL2."
  :author "Attila Lendvai"
  :license "BSD or Bugroff"
  :version "0.1"

  :defsystem-depends-on (:cffi/c2ffi+cl-ppcre)
  :depends-on (:alexandria
               :cffi
               :cffi/c2ffi+cl-ppcre
               :cffi-libffi)
  :components ((:file "package-stage-1"
                :pathname "source/package-stage-1")
               (:file "ffi-prelude"
                :pathname "source/ffi-prelude"
                :depends-on ("package-stage-1"))
               (:module "source"
                :depends-on ("c2ffi-spec" "package-stage-1")
                :serial t
                :components ((:file "package-stage-2")
                             (:file "package-stage-3")
                             (:file "sdl")))
               (:module "c2ffi-spec"
                :depends-on ("ffi-prelude")
                :components ((:cffi/c2ffi-file "sdl.h"
                              :package #:hu.dwim.sdl.ffi
                              :ffi-name-transformer "hu.dwim.sdl::ffi-name-transformer"
                              :ffi-type-transformer "hu.dwim.sdl::ffi-type-transformer"
                              :foreign-library-name "hu.dwim.sdl.ffi::libsdl2"
                              :foreign-library-spec ((:darwin (:or (:framework "SDL2") (:default "libSDL2")))
                                                     (:unix (:or "libSDL2-2.0.so.0" "libSDL2"))
                                                     (:windows "SDL2.dll")
                                                     (t (:default "libSDL2")))
                              :include-sources ("/types.h$"
                                                "SDL2/.+\\.h$")
                              :exclude-sources :all
                              :include-definitions ("^u?int\\d+_t"
                                                    "size_t$"
                                                    "strerror"
                                                    )
                              :exclude-definitions ("^LINE$"
                                                    "^SDL_LINE$"
                                                    ;;"^PRI[xX]"
                                                    ;;"SDL_Log"
                                                    "^SDL_main$"))))))

(asdf:defsystem :hu.dwim.sdl/gfx
  :description "Common Lisp FFI wrapper for libSDL2."
  :author "Attila Lendvai"
  :license "BSD or Bugroff"
  :version "0.1"

  :defsystem-depends-on (:cffi/c2ffi+cl-ppcre)
  :depends-on (:alexandria
               :cffi
               :cffi/c2ffi+cl-ppcre
               :cffi-libffi
               :hu.dwim.sdl)
  :components ((:module "c2ffi-spec"
                :components ((:cffi/c2ffi-file "sdl-gfx.h"
                              :package #:hu.dwim.sdl.ffi
                              :ffi-name-transformer "hu.dwim.sdl::ffi-name-transformer"
                              :ffi-type-transformer "hu.dwim.sdl::ffi-type-transformer"
                              :foreign-library-name "hu.dwim.sdl.ffi::libsdl2/gfx"
                              :foreign-library-spec ((:darwin (:or (:framework "SDL2_gfx") (:default "libSDL2_gfx")))
                                                     (:unix (:or "libSDL2_gfx-1.0.so.0" "libSDL2_gfx"))
                                                     (:windows "SDL2_gfx.dll")
                                                     (t (:default "libSDL2_gfx")))
                              :include-sources ("SDL2/SDL2_gfxPrimitives\\.h$"
                                                "SDL2/SDL2_framerate\\.h$"
                                                "SDL2/SDL2_imageFilter\\.h$"
                                                "SDL2/SDL2_rotozoom\\.h$")
                              :exclude-sources :all
                              :include-definitions ()
                              :exclude-definitions ("^LINE$"
                                                    "^SDL_LINE$"
                                                    ;;"^PRI[xX]"
                                                    ))))))

(asdf:defsystem :hu.dwim.sdl/ttf
  :description "Common Lisp FFI wrapper for libSDL2."
  :author "Attila Lendvai"
  :license "BSD or Bugroff"
  :version "0.1"

  :defsystem-depends-on (:cffi/c2ffi+cl-ppcre)
  :depends-on (:alexandria
               :cffi
               :cffi/c2ffi+cl-ppcre
               :cffi-libffi
               :hu.dwim.sdl)
  :components ((:module "c2ffi-spec"
                :components ((:cffi/c2ffi-file "sdl-ttf.h"
                              :package #:hu.dwim.sdl.ffi
                              :ffi-name-transformer "hu.dwim.sdl::ffi-name-transformer"
                              :ffi-type-transformer "hu.dwim.sdl::ffi-type-transformer"
                              :foreign-library-name "hu.dwim.sdl.ffi::libsdl2/ttf"
                              :foreign-library-spec ((:darwin (:or (:framework "SDL2_ttf") (:default "libSDL2_ttf")))
                                                     (:unix (:or "libSDL2_ttf-2.0.so.0" "libSDL2_ttf"))
                                                     (:windows "SDL2_ttf.dll")
                                                     (t (:default "libSDL2_ttf")))
                              :include-sources ("SDL2/SDL_ttf\\.h$")
                              :exclude-sources :all
                              :include-definitions ()
                              :exclude-definitions ("^LINE$"
                                                    "^SDL_LINE$"
                                                    ;;"^PRI[xX]"
                                                    ))))))

(asdf:defsystem :hu.dwim.sdl/image
  :description "Common Lisp FFI wrapper for libSDL2."
  :author "Attila Lendvai"
  :license "BSD or Bugroff"
  :version "0.1"

  :defsystem-depends-on (:cffi/c2ffi+cl-ppcre)
  :depends-on (:alexandria
               :cffi
               :cffi/c2ffi+cl-ppcre
               :cffi-libffi
               :hu.dwim.sdl)
  :components ((:module "c2ffi-spec"
                :components ((:cffi/c2ffi-file "sdl-image.h"
                              :package #:hu.dwim.sdl.ffi
                              :ffi-name-transformer "hu.dwim.sdl::ffi-name-transformer"
                              :ffi-type-transformer "hu.dwim.sdl::ffi-type-transformer"
                              :foreign-library-name "hu.dwim.sdl.ffi::libsdl2/image"
                              :foreign-library-spec ((:darwin (:or (:framework "SDL2_image") (:default "libSDL2_image")))
                                                     (:unix (:or "libSDL2_image-2.0.so.0" "libSDL2_image"))
                                                     (:windows "SDL2_image.dll")
                                                     (t (:default "libSDL2_image")))
                              :include-sources ("SDL2/SDL_image\\.h$")
                              :exclude-sources :all
                              :include-definitions ()
                              :exclude-definitions ("^LINE$"
                                                    "^SDL_LINE$"
                                                    ;;"^PRI[xX]"
                                                    ))))))

(defsystem :hu.dwim.sdl/fancy
  :description "Fancier API extensions for hu.dwim.sdl in return for more dependencies."
  :author "Attila Lendvai"
  :license "BSD or Bugroff"
  :version "0.1"

  :defsystem-depends-on (:hu.dwim.asdf)
  :class "hu.dwim.asdf:hu.dwim.system"
  :depends-on (:hu.dwim.def+hu.dwim.common
               :hu.dwim.defclass-star+hu.dwim.def
               :hu.dwim.sdl
               :hu.dwim.sdl/gfx
               :hu.dwim.sdl/image
               :hu.dwim.sdl/ttf
               :hu.dwim.syntax-sugar)
  :components ((:module "source"
                :serial t
                :components ((:file "package-fancy")
                             (:file "fancy")))))
