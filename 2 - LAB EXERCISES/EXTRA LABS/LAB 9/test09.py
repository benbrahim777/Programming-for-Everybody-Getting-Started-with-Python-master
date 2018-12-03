"""
A unit test for module blackjack

Run this test script to make sure everything is working properly.

Authors: L. Lee (LJL2), S. Marschner (SRM2), and W. White (WMW2)
Date:    October 20, 2017 (Python 3 Version)
"""
import cornell
import lab09
import card


def test_init():
    """
    Tests the __init__ method for Blackjack objects
    """
    c1 = card.Card(0, 12)
    c2 = card.Card(1, 10)
    c3 = card.Card(2, 9)
    c4 = card.Card(0, 1)
    
    # Initialize deck and start game.
    deck = [c1, c2, c3, c4]
    game = lab09.Blackjack(deck)
    
    cornell.assert_equals([c1, c2], game.playerHand)
    cornell.assert_equals([c3], game.dealerHand)
    cornell.assert_equals([c4], deck)  # check that cards were removed
    
    deck = card.full_deck()  # non-shuffled deck
    game = lab09.Blackjack(deck)
    c1 = card.Card(0, 1)
    c2 = card.Card(0, 2)
    c3 = card.Card(0, 3)
    c4 = card.Card(0, 4)
    
    cornell.assert_equals([c1, c2], game.playerHand)
    cornell.assert_equals([c3], game.dealerHand)
    
    # check that right cards were removed
    cornell.assert_equals(card.full_deck()[3:], deck)
    
    print('The __init__ tests passed')


def test_str():
    """
    Tests the __str__ function for Blackjack objects
    """
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    cornell.assert_equals('player: 20; dealer: 9', str(game))
    
    game.playerHand=[]
    cornell.assert_equals('player: 0; dealer: 9', str(game))
    game.dealerHand.append(card.Card(2,1))
    cornell.assert_equals('player: 0; dealer: 20', str(game))
    game.dealerHand.append(card.Card(2,5))
    cornell.assert_equals('player: 0; dealer: 25', str(game))
    
    print('The __str__ tests passed')


def test_score():
    """
    Tests the _score method (which is hidden, but we access anyway)
    """
    # need a dummy game object to call its _score function (and test it)
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornell.assert_equals(13, game._score([card.Card(2, 2), card.Card(3, 1)]))
    cornell.assert_equals(13, game._score([card.Card(1, 13), card.Card(0, 3)]))
    cornell.assert_equals(22, game._score([card.Card(1, 1), card.Card(0, 1)]))
    cornell.assert_equals(9, game._score([card.Card(1, 2), card.Card(0, 3), card.Card(3, 4)]))
    cornell.assert_equals(0, game._score([]))
    
    print('The _score tests passed')


def test_dealerScore():
    """
    Tests the dealerScore method for Blackjack objects
    """
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornell.assert_equals(9, game.dealerScore())
    game.dealerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.playerHand = [card.Card(1, 13), card.Card(0, 3)]
    cornell.assert_equals(13, game.dealerScore())
    
    print('The dealerScore tests passed')


def test_playerScore():
    """
    Tests the playerScore method for Blackjack objects
    """
    """Test playerScore function"""
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornell.assert_equals(20, game.playerScore())
    game.playerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.dealerHand = [card.Card(1, 13), card.Card(0, 3)]
    cornell.assert_equals(13, game.playerScore())
    
    print('The playerScore tests passed')


def test_playerBust():
    """
    Tests the playerBust method for Blackjack objects
    """
    # get dummy deck
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornell.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10)]
    cornell.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    cornell.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    cornell.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornell.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    cornell.assert_true(game.playerBust())
    
    print('The playerBust tests passed')


def test_dealerBust():
    """
    Tests the dealerBust method for Blackjack objects
    """
    # get dummy deck
    deck = [card.Card(0, 12),  card.Card(2, 9), card.Card(1, 10),]
    game = lab09.Blackjack(deck)
    
    cornell.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10)]
    cornell.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    cornell.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    cornell.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornell.assert_true(game.dealerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    cornell.assert_true(game.playerBust())
    
    print('The dealerBust tests passed')


# Script code
if __name__ == '__main__':
    test_init()
    test_score()
    test_dealerScore()
    test_playerScore()
    test_dealerBust()
    test_playerBust()
    test_str()

    print('All tests for lab 9 passed')
