#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_eval, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval("1")
        self.assertEqual(v, 3.749542961608775)
        
    def test_eval_2 (self) :
        v = netflix_eval("2")
        self.assertEqual(v, 3.5586206896551724)
    
    def test_eval_3 (self) :
        v = netflix_eval("3")
        self.assertEqual(v, 3.6411530815109345)
    
    def test_eval_4 (self) :
        v = netflix_eval("4")
        self.assertEqual(v, 2.73943661971831)



    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1:\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1:\n200 100\n900 1000\n10 1\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2 2 2\n200 100 125\n900 1000 174\n10 1 20\n")


# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
