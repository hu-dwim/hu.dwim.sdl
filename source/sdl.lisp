(in-package :hu.dwim.sdl)

(defun %c-fun/rc/check-error (rc fn-name whole-form)
  (when (minusp rc)
    (error "SDL FFI call failed. Name: ~S, error: ~S (~S), expression: ~S."
           fn-name (|SDL_GetError|) rc whole-form)))

(defmacro c-fun/rc (&whole whole fn-name &rest args)
  (with-unique-names (rc)
    `(let ((,rc (,fn-name ,@args)))
       (%c-fun/rc/check-error ,rc ',fn-name ',whole)
       ,rc)))

(defun %c-fun/not-null/check-error (rc fn-name whole-form)
  (when (minusp rc)
    (error "SDL FFI call failed. Name: ~S returned with NULL, expression: ~S."
           fn-name whole-form)))

(defmacro c-fun/not-null (&whole whole fn-name &rest args)
  (with-unique-names (rc)
    `(let ((,rc (,fn-name ,@args)))
       (%c-fun/not-null/check-error ,rc ',fn-name ',whole)
       ,rc)))
