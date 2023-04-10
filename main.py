
from datetime import datetime, timedelta
def read_file(file_name, nameprod):
    products = {}
    with open(file_name) as file:
        for line in file:

            name, date, price = line.split(' ')
            date = datetime.strptime(date.strip(), '%Y-%m-%d')
            if name not in products:
                products[name] = []
            products[name].append((date, float(price)))

        #return products

        last_date = max(max(product, key=lambda x: x[0])[0] for product in products.values())
        start_date = last_date - timedelta(days=30)

        prices = []
        if nameprod in products:
            for product in products[nameprod]:
                if start_date <= product[0] <= last_date:
                    prices.append(product[1])
        if len(prices) > 0:
            start_price = prices[0]
            end_price = prices[-1]
            price_change = end_price - start_price
            return price_change # "Ціна {nameprod} змінилась на {price_change:.2f} за місяць."
        else:
            return 0 #"нема інформації про  {nameprod} ."
#print(read_file("items1.txt", "Яблуко"))