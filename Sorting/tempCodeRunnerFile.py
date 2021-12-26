phrases = ['when in rome', 
        'what goes around comes around', 
        'all is fair in love and war'
        ]

phrases.sort(key=lambda x: x.split()[2][1], reverse=True)
print(phrases)
k = lambda x: x.split()[2][1]
print(k)