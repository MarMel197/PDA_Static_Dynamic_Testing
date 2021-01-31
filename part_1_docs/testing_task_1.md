### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
    if card.value = 1:                    # This should be - if card.value == 1:
      return True
    else                                  # The else is missing a : after it
      return False
   
#line 26 should start with def not dif
  dif highest_card(self, card1 card2):    # There are commas missing between the parameters
  if card1.value > card2.value:           # The if statement isn't indented
    return card                           # card is not defined, the return should be card1
  else:
    return card2
  


def cards_total(self, cards):             # This is indented incorrectly   
  total                                   # total defined incorrectly it should be total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total  # the return statement is not indented correctly,
                                          # to concatenate the total it needs to be a string  
                                          # it needs to be return "You have a total of " = str(total)
                                          # For readability we need a space between the last word of 
                                          # the closing quotes.
```
