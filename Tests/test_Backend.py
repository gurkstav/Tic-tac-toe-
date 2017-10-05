# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("../UI-Module")
from Backend import *

class TestBackend(unittest.TestCase):
    def setUp(self):
        print("Initialized...", end='')
        self.testBackend = Backend()

    def test_name_process(self):
        """
        Test a null, invalid charater included, over length and usable name
        can be process or not.
        """
        self.assertTrue(self.testBackend._name_process(self.testBackend.main_player)[0])
        self.assertFalse(self.testBackend._name_process('')[0])
        self.assertFalse(self.testBackend._name_process('O bama')[0])
        self.assertFalse(self.testBackend._name_process('Obaaaaaaaama')[0])
        self.assertTrue(self.testBackend._name_process('Obama')[0])

    def testsetMainPlayerName(self):
        """
        Test whether main invalid/usable main player's name can be denied/set.
        """
        self.assertFalse(self.testBackend.setMainPlayerName('Hillary Diane Rodham Clinton')[0])
        self.assertEqual(self.testBackend.main_player,'Player1')
        self.assertTrue(self.testBackend.setMainPlayerName('Trump')[0])
        self.assertEqual(self.testBackend.main_player,'Trump')
        self.assertEqual(self.testBackend.player_list[0][0],'Trump')
        self.assertTrue('Trump' in self.testBackend.player_set)

    def testaddNewPlayerName(self):
        """
        Test whether an existed/usable player name can be denied/set.
        """
        before_add_length = len(self.testBackend.player_list)        
        self.assertFalse(self.testBackend.addNewPlayerName('Player1')[0])
        self.assertEqual(len(self.testBackend.player_list), before_add_length)
        self.assertEqual(len(self.testBackend.player_set), before_add_length)
        self.assertTrue(self.testBackend.addNewPlayerName('Player2')[0])
        self.assertEqual(len(self.testBackend.player_list), before_add_length+1)
        self.assertEqual(len(self.testBackend.player_set), before_add_length+1)

    def testaddNewAIPlayerName(self):
        """
        Test whether an existed/usable name of AI can be denied/set.
        """
        before_add_length = len(self.testBackend.player_list)
        self.assertFalse(self.testBackend.addNewAIPlayerName("Hiro",  playertype.human)[0])
        self.assertFalse(self.testBackend.addNewAIPlayerName("Player1",  playertype.ai_easy)[0])
        self.assertEqual(len(self.testBackend.player_list), before_add_length)
        self.assertTrue(self.testBackend.addNewAIPlayerName("Baymax",  playertype.ai_hard)[0])        
        self.assertEqual(len(self.testBackend.player_list), before_add_length+1)
        self.assertEqual(len(self.testBackend.player_set), before_add_length)
    
    def testgetPlayerName(self):
        """
        Test whether an player's name can be extract in a valid range and also after add a new one.
        """
        self.assertEqual(self.testBackend.getPlayerName(1),self.testBackend.player_list[0][0])
        self.assertFalse(self.testBackend.getPlayerName(2) in self.testBackend.player_set)
        self.assertFalse(self.testBackend.getPlayerName(0) in self.testBackend.player_set)
        self.testBackend.addNewPlayerName('Player2')
        self.assertEqual(self.testBackend.getPlayerName(2),self.testBackend.player_list[1][0])
    
    def testgetPlayerType(self):
        """
        Test whether an player's type can be extract in a valid range and also after add a new one.
        """
        self.assertEqual(self.testBackend.getPlayerType(1),self.testBackend.player_list[0][1])
        self.assertFalse(self.testBackend.getPlayerType(2) in self.testBackend.player_set)
        self.assertFalse(self.testBackend.getPlayerType(0) in self.testBackend.player_set)
        self.testBackend.addNewPlayerName('Player2')
        self.assertEqual(self.testBackend.getPlayerType(2),self.testBackend.player_list[1][1])

    def testgetListOfPlayerNames(self):
        """
        Test whether the list of player's name can be extract in a valid range and also after add a new one.
        """
        user_name_list=[]
        for entity in self.testBackend.player_list:
            user_name_list.append(entity[0])
        self.assertEqual(self.testBackend.getListOfPlayerNames(),user_name_list)
        user_name_list=[]        
        self.testBackend.addNewPlayerName('Player2')
        for entity in self.testBackend.player_list:
            user_name_list.append(entity[0])
        self.assertEqual(self.testBackend.getListOfPlayerNames(),user_name_list)

    def tearDown(self):
        print('Finished!')
    '''
    def test_getName(self): #要測試的功能, 名稱需test開頭
        print 'test getNme', 
        self.assertEqual(self.p.getName(), 'John' ) 
    def test_setAge(self): 
        print 'test setAge', 
        self.assertEqual(self.p.age, 10 ) 
        self.p.setAge(18) 
        self.assertNotEqual(self.p.age, 10 ) 
    def tearDown(self): # 每個測試結束 
        print 'final'
    '''
 
if __name__ == "__main__": 
    unittest.main()
    print('fuck')


