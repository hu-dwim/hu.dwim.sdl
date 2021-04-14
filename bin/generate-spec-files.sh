#!/bin/sh
#| -*- mode: lisp; coding: utf-8-unix -*-

#set -o xtrace

PROJECT_NAME=hu.dwim.sdl/fancy

SCRIPT_DIR=`dirname "$0"`
SCRIPT_DIR=`readlink -f ${SCRIPT_DIR}`
PROJECT_HOME=`readlink -f ${SCRIPT_DIR}/..`

#LISP=${SCRIPT_DIR}/../../sbcl/run-sbcl.sh
#LISP=`readlink -f ${LISP}`

LISP=sbcl

cd "${PROJECT_HOME}"

echo "*** "`date`" Generating c2ffi spec files for ${PROJECT_HOME}"

BUILD_LOG_FILE="/tmp/${PROJECT_NAME}.build-log"

# TODO reenable source registry override once cffi is fresh enough in ql
#export CL_SOURCE_REGISTRY="(:source-registry (:tree \"${PROJECT_HOME}\") :ignore-inherited-configuration)"
export ASDF_OUTPUT_TRANSLATIONS="(:output-translations (\"${PROJECT_HOME}\" (\"${PROJECT_HOME}/build/fasls/\" :implementation)) :inherit-configuration)"

mkdir --parents build/

# install quicklisp if needed
if [ ! -e "build/quicklisp/setup.lisp" ] ; then
    curl --output build/quicklisp.lisp https://beta.quicklisp.org/quicklisp.lisp
    ${LISP} --noinform --end-runtime-options --no-sysinit --no-userinit \
            --eval "(require :asdf)" --eval "(asdf:load-system :asdf)" \
            --load "build/quicklisp.lisp" \
            --eval '(quicklisp-quickstart:install :path "build/quicklisp/" :dist-url "http://beta.quicklisp.org/dist/quicklisp/2021-04-11/distinfo.txt")' \
            --eval '(quit)'
fi

# "call" the lisp part below.
exec ${LISP} --noinform --end-runtime-options --no-sysinit --no-userinit \
     --eval "(require :asdf)" --eval "(asdf:load-system :asdf)" \
     --load "build/quicklisp/setup.lisp" \
     --eval "(with-open-file (s \"${0}\" :element-type 'character) (read-line s) (load s))" \
     --end-toplevel-options 2>&1 ${PROJECT_NAME} | tee ${BUILD_LOG_FILE}

echo "*** "`date`" Finished generating c2ffi spec files for ${PROJECT_HOME}"

${SCRIPT_DIR}/filter-spec-files.sh

# let's quit the shell part before the shell interpreter runs on the lisp stuff below
exit 0

# and from here follows the lisp part that gets invoked by the above shell part |#

(in-package :cl-user)

(format t "~2&Running on ~A ~A, using Quicklisp dist version ~A~%"
        (lisp-implementation-type)
        (lisp-implementation-version)
        (or #+quicklisp (ql:dist-version "quicklisp")
            "n/a"))

(ql:quickload '(:cffi/c2ffi :cffi/c2ffi-generator :split-sequence))

(defpackage :build-tmp
  (:use :common-lisp
        :alexandria))

(in-package :build-tmp)

(defparameter *project-name* (intern (string-upcase (first uiop:*command-line-arguments*))
                                     (find-package :keyword)))

(defun nix-includes->c2ffi-args ()
  (loop :with str = (or (uiop:getenv "NIX_CFLAGS_COMPILE") "")
        :with pieces = (remove "-isystem"
                               (split-sequence:split-sequence #\Space str :remove-empty-subseqs t)
                               :test 'equal)
        :for el :in pieces
        :collect "--sys-include"
        :collect el))

(appendf cffi/c2ffi::*c2ffi-extra-arguments*
         (nix-includes->c2ffi-args))

;; KLUDGE this is an enormous kludge that is only needed on nixos
;; because there clang is a wrapper script that defines some extra
;; include paths. see https://github.com/rpav/c2ffi/pull/89
(appendf cffi/c2ffi::*c2ffi-extra-arguments*
         (list "--sys-include"
               "/nix/store/kaicsq9mskqvs7ww03rpz7cbjiwamh8i-glibc-2.31-dev/include"))

;; (setf cffi/c2ffi::*trace-c2ffi* t)
;; (trace cffi/c2ffi::ensure-spec-file-is-up-to-date
;;        cffi/c2ffi::generate-spec-with-c2ffi)

(ql:quickload *project-name*)

(asdf:test-system *project-name*)

(uiop:quit)
