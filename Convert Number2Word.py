def number2word(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    l = 100000
    c = 10000000
    if (num < 20):
        return d[num]
    if (num < 100):
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred and ' + number2word(num % 100)

    if (num < l):
        if num % k ==0:
            return number2word(num//k) + ' thousand'
        else:
            return number2word(num//k) + ' thousand and ' + number2word(num % k)
    if (num < c):
        if num % l == 0:
            return number2word(num//l) + ' lakh'
        else:
            return number2word(num//l) + ' lakh and ' + number2word(num % l)
    if (num % c == 0):
        return number2word(num // c) + ' crore'
    else:
        return number2word(num // c) + ' crore and ' + number2word(num % c)

