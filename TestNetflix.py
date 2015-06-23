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
        self.assertEqual(v, '3.71')
        
    def test_eval_2 (self) :
        v = netflix_eval("2647871", "1")
        self.assertEqual(v, '3.31')
    
    def test_eval_3 (self) :
        v = netflix_eval("1283744", "1")
        self.assertEqual(v, '3.62')
    
    def test_eval_4 (self) :
        v = netflix_eval("2488120", "1")
        self.assertEqual(v, '4.73')



    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.71\n3.31\n3.62\nRMSE = 0.529\n")

    def test_solve_2 (self) :
        r = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10:\n2.92\n2.66\n1000:\n3.21\n2.90\nRMSE = 0.440\n")


# ----
# main
# ----

if __name__ == "__main__" :
    main()

