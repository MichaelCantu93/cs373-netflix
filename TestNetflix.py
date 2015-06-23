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
        v = netflix_eval("30878", "1")
        self.assertEqual(v, '3.63')
        
    def test_eval_2 (self) :
        v = netflix_eval("2647871", "1")
        self.assertEqual(v, '3.23')
    
    def test_eval_3 (self) :
        v = netflix_eval("1283744", "1")
        self.assertEqual(v, '3.54')
    
    def test_eval_4 (self) :
        v = netflix_eval("2488120", "1")
        self.assertEqual(v, '4.66')



    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.63\n3.23\n3.54\nRMSE = 0.554\n")

    def test_solve_2 (self) :
        r = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10:\n3.41\n3.15\n1000:\n3.60\n3.29\nRMSE = 0.502\n")


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
