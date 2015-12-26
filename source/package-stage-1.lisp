(defpackage :hu.dwim.sdl
  (:use #:cl
        #:alexandria
        #:cffi)
  (:shadow
   #:listen
   #:hci-filter-clear
   #:hci-filter-set-ptype
   #:hci-filter-set-event
   )

  (:export
   ;; NOTE: it's not possible to re-export stuff from hu.dwim.sdl.ffi by directly referencing the symbols,
   ;; because that changes the behavior of cl:shadow and break things.
   ;; http://paste.lisp.org/+3D97
   ;; 2015-10-19 #sbcl
   ;; (22:12:53) Xof: "If it is accessible as an internal symbol via use-package, it is first imported into package, then exported."
   ;; (22:12:59) Xof: (CLHS EXPORT)
   ;; (22:13:17) Xof: so since the symbol is exported from B, it is present (not inherited) in B, so shadow has no effect
   ;; (22:13:28) stassats: attila_lendvai: you need to use the :shadow option in defpackage
   ;; (22:14:36) attila_lendvai: ooh. managed to code in cl for a decade without having a clue... thanks guys!
   ;; (22:14:54) stassats: yeah, the order is important
   ;; (22:14:56) specbot: http://www.lispworks.com/reference/HyperSpec/Body/m_defpkg.htm
   ;; (22:15:13) stassats: right before the Examples section it lists the order
   ))

(in-package :hu.dwim.sdl)

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
      #+nil
      ((equal context '(:struct "hci_dev_info" "name"))
       (assert (equal type '(:array :char 8)))
       ;; err, no, this dereferences a pointer
       :string)
      (t
       type))))
