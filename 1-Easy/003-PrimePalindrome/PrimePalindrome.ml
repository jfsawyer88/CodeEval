(** CodeEval **)
(** Prime Palindrome **)


(** returns the integer square root of n **)
(** i.e. floor(sqrt(n)) **)
(** rig this up to use pattern matching later? **)
let  isqrt n =
  let rec loop xk = 
    let xk1 = (xk + (n / xk)) / 2 in   (** computs the next x value **)
    if 1 >= (xk - xk1) then  (** compares it with our current x value **)
      xk1
    else loop xk1
  in
  loop n
;;


(** determines if input is prime **)
let is_prime n =
  if n = 2 then true
  else
    if 0 = n mod 2 then         (** false immediately if divisible by 2**)
      false
    else
      let lim = 1 + isqrt n in  (** set limit of loop to ceil(sqrt(n)) **)
      let rec loop i lim =
	if i < lim then
	  if 0 = n mod i then   (** return false if any i divides n **)
	    false
	  else
	    loop (i + 2) lim    (** recurse, incrementing i by 2 **)
	else
	  true                  (** return true if the loop completes **)
      in
      loop 3 lim                (** initialize loop on i=3 **)
;;


(** reverses digits of input **)
let reverse_int n =
  let rec loop n rev =
    if !n = 0 then
      !rev
    else
      begin
	rev := (!rev * 10) + (!n mod 10);
	n := !n / 10;
	loop n rev
      end
  in
  loop (ref n) (ref 0)
;;


(** determines if input is a palindrome **)
let is_palindrome n =
  n = reverse_int n
;;

(** determines if input is a palprime
    that is, a prime palindrome **)
let is_palprime n =
  (is_palindrome n) && (is_prime n)
;;


(** main loop **)
let rec loop n =
  if is_palprime n then n
  else loop (n - 1)
;;

print_int (loop 1000);;
print_newline ()
