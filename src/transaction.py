# -*- coding: utf-8 -*-
"""
Transaction class.
"""
class Transaction(object):
    def __init__(self, sender, recipient, amount):
        """
        Transaction class constructor.
        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        """          
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        
    def __str__(self):
        return 'transaction[sender: {0}, recipient: {1}, amount: {2}]'.format(
                    self.sender,
                    self.recipient,
                    self.amount)
