digit_to_letter = {
	0.0 : '',
	0.1 : 'a',
	0.2 : 'aa',
	0.3 : 'e',
	0.4 : 'ee',
	0.5 : 'u',
	0.6 : 'uu',
	0.7 : 'yea',
	0.8 : 'yeaa',
	0.9 : 'i',
	0.10 : 'o',
	0.11 : 'oo',
	0.12 : 'ow',
	1.0 : 'ka',
	1.0 : 'க',
	1.1 : 'kaa',
	1.2 : 'ki',
	1.3 : 'kee',
	1.4 : 'ku',
	1.5 : 'kuu',
	1.6 : 'k',
	1.7 : 'kay',
	1.8 : 'ky',
	1.9 : 'ko',
	1.10 : 'koo',
	1.11 : 'kow',
	2.0 : 'gna',
	2.1 : 'gnaa',
	2.2 : 'gni',
	2.3 : 'gnee',
	2.4 : 'gnu',
	2.5 : 'gnuu',
	2.6 : 'gney',
	2.7 : 'gneey',
	2.8 : 'gny',
	2.9 : 'gno',
	2.10 : 'gnoo',
	2.11 : 'gnow',
	3.0 : 'cha',
	3.1 : 'chaa',
	3.2 : 'chi',
	3.3 : 'chee',
	3.4 : 'chu',
	3.5 : 'chuu',
	3.6 : 'chey',
	3.7 : 'cheey',
	3.8 : 'chy',
	3.9 : 'cho',
	3.10 : 'choo',
	3.11 : 'chow',
	4.0 : 'nya',
	4.1 : 'nyaa',
	4.2 : 'nyi',
	4.3 : 'nyee',
	4.4 : 'nyu',
	4.5 : 'nyuu',
	4.6 : 'nyey',
	4.7 : 'nyeey',
	4.8 : 'ny',
	4.9 : 'nyo',
	4.10 : 'nyoo',
	4.11 : 'nyow',
	5.0 : 'ta',
	5.0 : 'ட',
	5.1 : 'taa',
	5.2 : 'ti',
	5.3 : 'tee',
	5.4 : 'tu',
	5.5 : 'tuu',
	5.6 : 'te',
	5.7 : 'tey',
	5.8 : 'ty',
	5.9 : 'to',
	5.10 : 'too',
	5.11 : 'tow',
	6.0 : 'na',
	6.9 : '	ண',
	6.1 : 'naa',
	6.2 : 'ni',
	6.3 : 'nee',
	6.4 : 'nu',
	6.5 : 'nuu',
	6.6 : 'ney',
	6.7 : 'neey',
	6.8 : 'ny',
	6.9 : 'no',
	6.10 : 'noo',
	6.11 : 'now',
	7.0 : 'tha',
	7.1 : 'thaa',
	7.2 : 'thi',
	7.3 : 'thee',
	7.4 : 'thu',
	7.4 : 'து',
	7.5 : 'thuu',
	7.6 : 'they',
	7.7 : 'theey',
	7.8 : 'thy',
	7.9 : 'tho',
	7.10 : 'thoo',
	7.11 : 'thow',
	8.0 : 'tna',
	8.1 : 'tnaa',
	8.2 : 'tni',
	8.3 : 'tnee',
	8.4 : 'tnu',
	8.5 : 'tnuu',
	8.6 : 'tney',
	8.7 : 'tneey',
	8.8 : 'tny',
	8.9 : 'tno',
	8.10 : 'tnoo',
	8.11 : 'tnow',
	9.0 : 'pa',
	9.1 : 'paa',
	9.2 : 'pi',
	9.3 : 'pee',
	9.4 : 'pu',
	9.5 : 'puu',
	9.6 : 'pey',
	9.7 : 'peey',
	9.8 : 'py',
	9.9 : 'po',
	9.10 : 'poo',
	9.11 : 'pow',
	10.0 : 'ma',
	10.1 : 'maa',
	10.2 : 'mi',
	10.3 : 'mee',
	10.4 : 'mu',
	10.5 : 'muu',
	10.6 : 'mey',
	10.7 : 'meey',
	10.8 : 'my',
	10.9 : 'mo',
	10.10 : 'moo',
	10.11 : 'mow',
	11.0 : 'ya',
	11.1 : 'yaa',
	11.2 : 'yi',
	11.3 : 'yee',
	11.4 : 'yu',
	11.5 : 'yuu',
	11.6 : 'yey',
	11.7 : 'yeey',
	11.8 : 'yy',
	11.9 : 'yo',
	11.10 : 'yoo',
	11.11 : 'yow',
	12.0 : 'ra',
	12.1 : 'raa',
	12.2 : 'ri',
	12.3 : 'ree',
	12.4 : 'ru',
	12.5 : 'ruu',
	12.6 : 'rey',
	12.7 : 'reey',
	12.8 : 'ry',
	12.9 : 'ro',
	12.10 : 'roo',
	12.11 : 'row',
	13.0 : 'la',
	13.1 : 'laa',
	13.2 : 'li',
	13.3 : 'lee',
	13.4 : 'lu',
	13.5 : 'luu',
	13.6 : 'ley',
	13.7 : 'leey',
	13.8 : 'ly',
	13.9 : 'lo',
	13.10 : 'loo',
	13.11 : 'low',
	14.0 : 'va',
	14.0 : 'வ',
	14.1 : 'vaa',
	14.2 : 'vi',
	14.3 : 'vee',
	14.4 : 'vu',
	14.5 : 'vuu',
	14.6 : 'vey',
	14.7 : 'veey',
	14.8 : 'vy',
	14.9 : 'vo',
	14.10 : 'voo',
	14.11 : 'vow',
	15.0 : 'zha',
	15.1 : 'zhaa',
	15.2 : 'zhi',
	15.3 : 'zhee',
	15.4 : 'zhu',
	15.5 : 'zhuu',
	15.6 : 'zhey',
	15.7 : 'zheey',
	15.8 : 'zhy',
	15.9 : 'zho',
	15.10 : 'zhoo',
	15.11 : 'zhow',
	16.0 : 'la',
	16.1 : 'laa',
	16.2 : 'li',
	16.3 : 'lee',
	16.4 : 'lu',
	16.5 : 'luu',
	16.6 : 'ley',
	16.7 : 'leey',
	16.8 : 'ly',
	16.9 : 'lo',
	16.10 : 'loo',
	16.11 : 'low',
	17.0 : 'ra',
	17.1 : 'raa',
	17.2 : 'ri',
	17.3 : 'ree',
	17.4 : 'ru',
	17.5 : 'ruu',
	17.6 : 'rey',
	17.7 : 'reey',
	17.8 : 'ry',
	17.9 : 'ro',
	17.10 : 'roo',
	17.11 : 'row',
	18.0 : 'na',
	18.0 : 'ன',
	18.1 : 'naa',
	18.2 : 'ni',
	18.3 : 'nee',
	18.4 : 'nu',
	18.5 : 'nuu',
	18.6 : 'ney',
	18.7 : 'neey',
	18.8 : 'ny',
	18.9 : 'no',
	18.10 : 'noo',
	18.11 : 'now'
	
	
}

letter_to_digit = { value:key for key, value in digit_to_letter.iteritems() }
