;;; This file is loaded before the generated FFI.

(in-package :hu.dwim.sdl)

(define-condition sdl-error (error)
  ())

(define-condition sdl-error/negative-return-code (simple-error sdl-error)
  ((error-code :initform (error "Must specify ERROR-CODE.")
               :accessor error-code-of
               :initarg :error-code)))

(cffi:define-foreign-type sdl-error-code (cffi::foreign-type-alias)
  ()
  (:default-initargs :actual-type (cffi::parse-type :int))
  (:simple-parser sdl-error-code))

(defmethod cffi:expand-from-foreign (value (type sdl-error-code))
  ;; NOTE: strictly speaking it should be (cffi:convert-from-foreign ,value :int), but not in this case.
  `(let ((return-code ,value))
     (if (< return-code 0)
         (error 'sdl-error/negative-return-code
                :error-code return-code
                :format-control "SDL call failed: ~S ~S"
                :format-arguments (list return-code (hu.dwim.sdl.ffi::|SDL_GetError|)))
         return-code)))

(defun ffi-name-transformer (name kind &key &allow-other-keys)
  (check-type name string)
  #+nil
  (cond
    ((starts-with-subseq "SDL_" name)
     (setf name (subseq name 4))
     #+nil (setf name (cffi/c2ffi:maybe-camelcase-to-dash-separated name)))
    #+nil
    ((or (starts-with-subseq "IMG_" name)
         (starts-with-subseq "TTF_" name))
     (let ((prefix (subseq name 0 4))
           (basename (subseq name 4)))
       (when (cffi/c2ffi:camelcased? basename)
         (setf name (concatenate 'string prefix
                                 (cffi/c2ffi:camelcase-to-dash-separated basename)))))
     (setf name (subseq name 4))))
  (case kind
    #+nil
    ((:constant :member)
     (format nil "+~A+" name))
    (t name)))

(defun ffi-type-transformer (type context &rest args &key &allow-other-keys)
  (let ((type (apply 'cffi/c2ffi:default-ffi-type-transformer type context args)))
    (cond
      ((and (consp context)
            (eq (first context) :function)
            (eq (third context) :return-type)
            (member (second context)
                    ;; TODO this list is by far not complete. see this SDL bug for details:
                    ;; https://bugzilla.libsdl.org/show_bug.cgi?id=3219
                    '("SDL_Init"
                      "TTF_Init"
                      "IMG_Init"
                      "SDL_SetRenderDrawColor"
                      "SDL_RenderClear"
                      "SDL_RenderCopyEx"
                      "SDL_RenderCopyEx"
                      "SDL_RenderDrawLines"
                      "SDL_RenderDrawLines"
                      "SDL_RenderDrawPoint"
                      "SDL_RenderDrawPoints"
                      "SDL_RenderDrawRect"
                      "SDL_RenderDrawRects"
                      "SDL_RenderFillRect"
                      "SDL_RenderFillRects"
                      "SDL_RenderReadPixels"
                      "SDL_RenderSetClipRect"
                      "SDL_RenderSetLogicalSize"
                      "SDL_RenderSetScale"
                      "SDL_RenderSetViewport"
                      )
                    :test 'equal))
       (assert (eq type :int))
       ;; this is a cffi type that automatically signals an error if the return code is negative.
       'sdl-error-code)
      #+nil
      ((equal context '(:struct "hci_dev_info" "name"))
       (assert (equal type '(:array :char 8)))
       ;; err, no, this dereferences a pointer
       :string)
      (t
       type))))
