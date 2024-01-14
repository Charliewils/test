(define (map f s)
  (if (null? s)
    nil
    (cons (f (car s))
	  (map f (cdr s)))))

(define (filter f s)
  (if (null? s)
    nil
    (if (f (car s))
      (cons (car s)
	    (filter f (cdr s)))
      (filter f (cdr s)))))

(define (reduce f s start)
  (if (null? s)
    start
    (reduce f
	    (cdr s)
	    (f start (car s)))))

(define (range a b)
  (if (>= a b) nil 
    (cons a (range (+ a 1) b))))

(define (sum s)
  (reduce + s 0))

(define (prime? x)
  (if (<= x 1)
    #f
    (null? (filter (lambda (y) (= 0 (remainder x y)))
		   (range 2 x)))))

(define (sum-prime a b)
  (sum (filter prime? (range a b))))

(define (range-stream a b)
  (if (>= a b) nil
    (cons-stream a (range-stream (+ 1 a) b))))

(define (int-stream x)
  (cons-stream x (int-stream (+ x 1))))

(define (prefix s k)
  (if (= 0 k)
    nil
    (cons (car s) (prefix (cdr-stream s) (- k 1)))))

(define onse (cons-stream 1 ones))

(define (add-stream s t)
  (cons (+ (car s) (car t))
	(add-stream (cdr-stream s)
		    (cdr-stream t))))

(define ints (cons-stream 1 (add-stream ones ints)))
