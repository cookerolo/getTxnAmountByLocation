import requests

def getTxnAmountByLocation(locationId, txnType):
    # Write your code here
    r = requests.get('https://jsonmock.hackerrank.com/api/transactions/search?txnType='+ txnType)
    results = r.json()
    output = []
    pages = int(results['total_pages'])
    for i in range(1,pages+1):
        r = requests.get('https://jsonmock.hackerrank.com/api/transactions/search?txnType='+ txnType + "&page="+ str(i))
        results = r.json()
        output.extend(list(filter(lambda x: x['location']['id'] == locationId, results['data'])))
    output2 = []
    for i in output:
            output2.append([i['userId'], float(i['amount'][1:].replace(',',''))])    
    final = []
    a = set([x for x,y in output2])
    for i in a:
        addition = list(filter(lambda x: x[0] == i, output2))
        sum_addition = round(sum([x[1] for x in addition]),2)
        final.append([i, sum_addition])
    return final
