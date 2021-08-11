(define-macro (switch expr cases)
  (cons 
        (map (lambda (case)
                        (cons _____ (cdr case)))
             cases)))
