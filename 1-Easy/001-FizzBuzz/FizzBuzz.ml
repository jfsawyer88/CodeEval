(** CodeEval **)
(** FizzBuzz **)


#load "str.cma";;  (** load str module **)

let sep = Str.regexp " ";;  (** string separator **)
let split = Str.split sep;; (** splits line on separator **)

let f = Array.get Sys.argv 1;; (** input file **)
let chan = open_in f;;         (** open file channel **)

(** prints fizzbuzz challenge on one line **)
let fizzbuzz a b n =
  for i = 1 to n do
    if 0 = i mod a then
      if 0 = i mod b then
	print_string "FB"   (** print FB if divisible by a and b **)
      else
	print_string "F"    (** print  F if divisible by a only **)
    else
      if 0 = i mod b then
	print_string "B"    (** print  F if divisible by b only **)
      else
	print_int i;        (** else print the integer **)
    if i <> n then
      print_string " "      (** print whitespace until the end **)
    else
      print_newline ()      (** print newline at the end**)
  done;
;;


(** loop **)
try
  while true do
    let l = input_line chan in            (** get next line **)
    let l = split l in                    (** split line on whitespace **)
    let l = List.map int_of_string l in   (** convert elements to integers **)

    let a = List.nth l 0 in
    let b = List.nth l 1 in
    let n = List.nth l 2 in

    fizzbuzz a b n;
  done
with
  End_of_file -> close_in chan
