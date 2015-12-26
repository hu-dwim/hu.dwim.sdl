(in-package :hu.dwim.sdl)

(hu.dwim.def:def hu.dwim.def:package :hu.dwim.sdl/fancy
  (:use :hu.dwim.common
        :hu.dwim.def
        :metabang-bind)
  (:import-from :hu.dwim.sdl
                c-fun
                c-fun/rc)
  (:local-nicknames
   (#:sdl :hu.dwim.sdl)
   (#:sdl.ffi :hu.dwim.sdl.ffi))
  ;; To use C-c C-c in slime: (asdf:load-systems :hu.dwim.def+swank :hu.dwim.sdl/fancy)
  (:readtable-setup
   (hu.dwim.syntax-sugar:enable-sharp-boolean-syntax)
   (hu.dwim.syntax-sugar:enable-feature-cond-syntax)
   (hu.dwim.syntax-sugar:enable-case-preserving-syntax :packages '(:hu.dwim.sdl.ffi))))
