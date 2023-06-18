from lib.slate import *
import unittest


class Test_node(unittest.TestCase):
    def test_basic(self):
        assert True
   # - testing works for N > 5
    def test_v_add_token(self):
        s1=slate()
        s1.add_token(1,Red_turn)
        s1.add_token(1,Red_turn)
        s1.add_token(1,Red_turn)
        self.assertTrue(s1.state == on_going)
        s1.add_token(1,Red_turn)
        self.assertTrue(s1.state == red_won)
   
    def test_h_add_token(self):
        s1=slate()
        s1.add_token(1,Red_turn)
        s1.add_token(2,Red_turn)
        s1.add_token(3,Red_turn)
        s1.add_token(0,Yellow_turn)
        s1.add_token(1,Red_turn)
        self.assertTrue(s1.state == on_going)
        s1.add_token(4,Red_turn)
        self.assertTrue(s1.state == red_won)
   
    def test_d_add_token(self):
        s=slate()
        for i in range(4):
            for j in range(i):
                s.add_token(i,Red_turn)
            self.assertTrue(s.state == on_going)
            s.add_token(i,Yellow_turn)
        self.assertTrue(s.state == yellow_won)