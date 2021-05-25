stock_exchange = input('Enter the exchange name :')
stock_ticker = input('Enter the ticker name :')
stock_buy_price = float(input('Enter the buying price :'))
stock_sell_price = float(input('Enter the selling price :'))
stock_quantity = float(input('Enter the quantity :'))

end = stock_sell_price - stock_buy_price
total = end * stock_quantity

print('Exhange '+stock_exchange.upper()+' Ticker '+stock_ticker+' Networth '+str(total))