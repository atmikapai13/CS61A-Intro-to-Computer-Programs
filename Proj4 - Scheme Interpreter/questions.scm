(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  (if (null? pairs) pairs
  (begin (define first (caar pairs))
    (define second (car (cdr (car pairs))))
    (define rest (zip (cdr pairs)))
    (if (null? rest) (list (list first) (list second))
    (list (cons first (car rest)) (cons second (cadr rest)))))))


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (inner count lst)
      (if (null? lst) lst
      (cons (list count (car lst)) (inner (+ 1 count) (cdr lst)))
    )
  ) (inner 0 s))
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond
      ((null? list1) list2)
      ((null? list2) list1)
      ((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)))
      ((comp (car list2) (car list1)) (cons (car list2) (merge comp list1 (cdr list2))))
  ))
  ; END PROBLEM 16


;; Problem 17

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           (cons form (cons params (map (let-to-lambda body))))
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           (define x (zip values))
           (list (car zip) body (car (cdr zip)))
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         (cons (car expr) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 17
         )))
