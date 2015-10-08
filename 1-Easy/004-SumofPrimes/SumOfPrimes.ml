(** CodeEval **)
(** Sum of Primes **)


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


let sum_of_primes n =
  let rec loop i cnt res=
    if cnt = n then res
    else
      if is_prime i then
	loop (i + 1) (cnt + 1) (res + i)
      else
	loop (i + 1) cnt res
  in
  loop 2 0 0
;;

print_int (sum_of_primes 1000);;
print_newline ()
