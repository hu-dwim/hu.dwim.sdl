#!/bin/sh
#| -*- mode: lisp; coding: utf-8-unix -*-

#set -o xtrace

SCRIPT_DIR=`dirname "$0"`
SCRIPT_DIR=`readlink -f ${SCRIPT_DIR}`
PROJECT_HOME=`readlink -f ${SCRIPT_DIR}/..`

#LISP=${SCRIPT_DIR}/../../sbcl/run-sbcl.sh
#LISP=`readlink -f ${LISP}`

LISP=sbcl

cd "${PROJECT_HOME}"

echo "*** "`date`" Generating c2ffi spec files for ${PROJECT_HOME}"

BUILD_LOG_FILE="/tmp/hu.dwim.sdl.build-log"

export CL_SOURCE_REGISTRY="(:source-registry (:tree \"${PROJECT_HOME}\") :ignore-inherited-configuration)"
#export ASDF_OUTPUT_TRANSLATIONS="(:output-translations (\"${PROJECT_HOME}\" (\"${DWIM_INSTALL_PATH}/.cache/common-lisp/\" :implementation)) :ignore-inherited-configuration)"

mkdir --parents build/

# "call" the lisp part below.
# TODO copy-pasted, because that goddamn stupid shell variable substitution and splitting makes it near impossible to introduce a QL_SETUP variable for this
if [ -e "build/quicklisp/setup.lisp" ] ; then
  exec ${LISP} --noinform --end-runtime-options --no-sysinit --no-userinit \
    --eval "(require :asdf)" --eval "(asdf:load-system :asdf)" \
    --load "build/quicklisp/setup.lisp" \
    --eval "(with-open-file (s \"${0}\" :element-type 'character) (read-line s) (load s))" \
    --end-toplevel-options 2>&1 | tee ${BUILD_LOG_FILE}
else
  curl --output build/quicklisp.lisp https://beta.quicklisp.org/quicklisp.lisp
  exec ${LISP} --noinform --end-runtime-options --no-sysinit --no-userinit \
    --eval "(require :asdf)" --eval "(asdf:load-system :asdf)" \
    --load "build/quicklisp.lisp" --eval '(quicklisp-quickstart:install :path "build/quicklisp/" :dist-url "http://beta.quicklisp.org/dist/quicklisp/2021-02-28/distinfo.txt")' \
    --eval "(with-open-file (s \"${0}\" :element-type 'character) (read-line s) (load s))" \
    --end-toplevel-options 2>&1 | tee ${BUILD_LOG_FILE}
fi

echo "*** "`date`" Finished generating c2ffi spec files for ${PROJECT_HOME}"

# let's quit the shell part before the shell interpreter runs on the lisp stuff below
exit 0

# and from here follows the lisp part that gets invoked by the above shell part |#

(in-package :cl-user)

(defpackage :build-tmp
  (:use :common-lisp))

(in-package :build-tmp)

(format t "~2&Running on ~A ~A, using Quicklisp dist version ~A~%"
        (lisp-implementation-type)
        (lisp-implementation-version)
        (or #+quicklisp (ql:dist-version "quicklisp")
            "n/a"))

;; KLUDGE for a quicklisp bug: it doesn't download :defsystem-depends-on dependencies,
;; so we need to explicitly quickload it early on, before the project .asd's get loaded.
;; for more details, see: https://github.com/quicklisp/quicklisp-client/pull/122
#+quicklisp
(ql:quickload :hu.dwim.asdf)

(defun load-system* (name)
  #+quicklisp
  (ql:quickload name)
  #-quicklisp
  (asdf:load-system name))

(load-system* :hu.dwim.asdf)
(load-system* :cffi/c2ffi)

(setf cffi/c2ffi::*trace-c2ffi* t)

(trace cffi/c2ffi::ensure-spec-file-is-up-to-date
       cffi/c2ffi::generate-spec-with-c2ffi)

;; TODO replase it once cffi has the commit
;;(cffi/c2ffi:generate-spec :hu.dwim.sdl :force t)
(asdf:operate 'cffi/c2ffi::generate-spec-op :hu.dwim.sdl :force t)

(cl-user::quit)
