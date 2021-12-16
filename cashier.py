class Cashier:
    EMPTY_CART_MSG = "You can't checkout an empty cart"
    
    def checkout(self, cart):
      if cart.is_empty():
        raise Exception(self.EMPTY_CART_MSG)
      
      cart.empty()

      return 10