;; Extra Scheme Questions ;;



; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (cond ((null? lst) '())
	((= item (car lst)) (remove item (cdr lst)))
	(else (cons (car lst) (remove item (cdr lst)))))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((= a b) a)
	(else (gcd (- (max a b) (min a b)) (min a b))))

)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21








