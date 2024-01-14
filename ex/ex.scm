((lambda (foo bar)
  (+ foo bar)) 3 (+ 3 2))

(define (waldo lst)
  (define (waldo_add lst index)
    (cond ((null? lst) #f)
	  ((eq? 'waldo (car lst)) index)
	  (else (waldo_add (cdr lst) (+ index 1)))))
  (waldo_add lst 0))
	
(define (fact n)
  (if (= n 0) 1
    (* n (fact (- n 1)))))

(define (fact_exp n)
  (if (= n 0) 1
    (list '* n (fact_exp (- n 1)))))

(define (fib n)
  (if (<= n 1) n
    (+ (fib (- n 1)) (fib (- n 2)))))

(define (fib_exp n)
  (if (<= n 1) n
    (list '+ (fib_exp (- n 1)) (fib (- n 2)))))

(define-macro (twice expr)
	      (list 'begin expr expr))

(define-macro (check expr)
	      (list 'if expr ''passed
		    (list 'quote (list 'failed: expr))))

(define (map fn vals)
  (if (null? vals)
    ()
    (cons (fn (car vals))
	  (map fn (cdr vals)))))

(define-macro (for sym vals expr)
	      (list 'map (list 'lambda (list sym) expr) vals))

(define-macro (check expr)
	      `(if ,expr 'passed '(failed: ,expr)))

(define (replicate x n)
  (if (= n 0) nil
    (cons x (replicate x (- n 1)))))

(define-macro (repeat-n expr n)
	      `(begin ,(car (replicate expr n))
		      ,(replicate expr (- n 1))))


