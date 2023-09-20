def function(card_number, visible_count_char=4):

  hidden_part = '*' * (len(card_number) - visible_count_char)
  visible_part = card_number[-visible_count_char:]

  result = f'{hidden_part}{visible_part}'
  return print(result)

card_number = '5536913768866530'
#visible_count_char = 8
function(card_number)