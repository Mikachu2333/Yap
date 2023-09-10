def js_dp(obj, path):
    json.dump(obj, open(path, 'w', encoding='utf-8'), ensure_ascii=False)

def js_ld(path):
    return json.load(open(path, 'r', encoding='utf-8'))


def exist_or_create_json(path):
    if not os.path.exists(path):
        js_dp([], path)
        

root_paths = [
    'dumps/',
    'text_dumps/',
    'dumps3',
    'dumps4.0',
    'dumps4.0_tx',
    'dumps4.0_tx2',
    'dumps4.0_tx3',
    'dumps4.0_tx4',
    'dumps4.0_tx5',
    'dumps4.0_tx6',
    'dumps4.0_tx7',
    'dumps4.0_pph',
    'dumps4.0_syfs',
    'dumps4.0_xs',
    'dumps4.0_yjls',
    'dumps4.0_longx',
]

error_paths = set([
    # "dumps/17_raw.jpg",
    # "dumps/1773_raw.jpg",
    # "dumps/2878_raw.jpg",
    # "dumps/3079_raw.jpg",
    # "dumps/3421_raw.jpg",
    # "dumps/9279_raw.jpg",
    # "dumps/13062_raw.jpg",
    # "dumps/14761_raw.jpg",
    # "text_dumps/12_raw.jpg",
    # "text_dumps/13_raw.jpg",
    # "text_dumps/14_raw.jpg",
    # "text_dumps/15_raw.jpg",
    # "text_dumps/25_raw.jpg",
    # "text_dumps/26_raw.jpg",
    # "text_dumps/28_raw.jpg",
    # "text_dumps/29_raw.jpg",
    # "text_dumps/5496_raw.jpg",
    # "text_dumps/5497_raw.jpg",
    # "text_dumps/5498_raw.jpg",
    # "text_dumps/8798_raw.jpg",
    # "text_dumps/8799_raw.jpg",
    # "text_dumps/11261_raw.jpg",
    # "text_dumps/15279_raw.jpg",
    # "text_dumps/23792_raw.jpg",
    # "text_dumps/23794_raw.jpg",
    # "text_dumps/32526_raw.jpg",
    # "dumps3/363_混沌容器_raw.jpg",
    # "dumps3/1198_兽肉_raw.jpg",
    # "dumps3/1379_薄荷_raw.jpg",
    # "dumps3/1661_簇_raw.jpg",
    # "dumps3/1868_教官的怀表_raw.jpg",
    # "dumps4.0/733_3_的_raw.jpg",
    # "dumps4.0/1022_2_浊水的一_raw.jpg",
    # "dumps4.0_tx/542_2_异海凝珠_raw.jpg",
    # "dumps4.0_tx/725_2_游医的怀钟_raw.jpg",
    # "dumps4.0_tx/1001_2_调查_raw.jpg",
    # "dumps4.0_tx/1516_4_的时_raw.jpg",
    
    # "dumps/14777_raw.jpg",
    # "dumps/14789_raw.jpg",
    # "dumps/14810_raw.jpg",
    # "dumps/15004_raw.jpg",
    # "dumps/15163_raw.jpg",
    # "dumps/16059_raw.jpg",
    # "text_dumps/8_raw.jpg",
    # "text_dumps/9_raw.jpg",
    # "text_dumps/10_raw.jpg",
    # "text_dumps/11_raw.jpg",
    # "text_dumps/27_raw.jpg",
    # "text_dumps/4216_raw.jpg",
    # "text_dumps/4401_raw.jpg",
    # "text_dumps/6356_raw.jpg",
    # "text_dumps/23725_raw.jpg",
    # "dumps4.0/1002_2_浊水的一_raw.jpg",
    # "dumps4.0/1007_2_浊水的一_raw.jpg",
    # "dumps4.0/1022_2_浊水的一_raw.jpg",
    # "dumps4.0/1027_2_浊水的一_raw.jpg",
    # "dumps4.0/1268_3_浊水的一_raw.jpg",
    # "dumps4.0_tx/88_2_浊水的一_raw.jpg",
    # "dumps4.0_tx/1943_3_浊水的一_raw.jpg",
    
    # "dumps/563_raw.jpg",
    # "dumps/3713_raw.jpg",
    # "dumps/6703_raw.jpg",
    # "dumps/12515_raw.jpg",
    # "dumps/14750_raw.jpg",
    # "dumps/14760_raw.jpg",
    # "dumps/14761_raw.jpg",
    # "dumps/14777_raw.jpg",
    # "dumps/14789_raw.jpg",
    # "dumps/14808_raw.jpg",
    # "dumps/14810_raw.jpg",
    # "dumps/15135_raw.jpg",
    # "dumps/15192_raw.jpg",
    # "text_dumps/6_raw.jpg",
    # "text_dumps/7_raw.jpg",
    # "text_dumps/9153_raw.jpg",
    # "text_dumps/25105_raw.jpg",
    # "dumps4.0_tx/18_3_浊水的一_raw.jpg",
    # "dumps4.0_tx/54_3_浊水的_raw.jpg",


    # "dumps/16061_raw.jpg",
    # "text_dumps/9153_raw.jpg",
    # "dumps3/227_战脉的枯叶_raw.jpg",
    # "dumps4.0_tx/175_2_浊水的一_raw.jpg",
    # "dumps4.0_tx/535_2_异海凝_raw.jpg",
    

    # "dumps/15006_raw.jpg",
    # "dumps/15018_raw.jpg",
    # "dumps/15111_raw.jpg",
    # "dumps/15198_raw.jpg",
    # "dumps4.0/1477_2_异海凝_raw.jpg",
    # "dumps4.0_tx/87_2_浊水的一_raw.jpg",

    # "dumps/3277_raw.jpg",
    # "dumps/3676_raw.jpg",
    # "dumps/9280_raw.jpg",
    # "dumps/13528_raw.jpg",
    # "dumps/14751_raw.jpg",
    # "dumps/15050_raw.jpg",
    # "dumps/15165_raw.jpg",
    # "dumps/16160_raw.jpg",
    # "dumps/18382_raw.jpg",
    # "dumps/18384_raw.jpg",
    # "dumps/18401_raw.jpg",
    # "dumps/18429_raw.jpg",
    # "dumps/19283_raw.jpg",
    # "dumps/19328_raw.jpg",
    # "text_dumps/21096_raw.jpg",
    # "text_dumps/23793_raw.jpg",
    # "text_dumps/24135_raw.jpg",
    # "dumps3/115_沉重号角_raw.jpg",
    # "dumps3/1765_祥箭_raw.jpg",
    # "dumps4.0_tx/54_3_浊水的_raw.jpg",
    # "dumps4.0_tx/56_2_浊水的一_raw.jpg",
    # "dumps4.0_tx/66_1_出生的浊水_raw.jpg",

    # "dumps4.0_tx4/498_2_「正义」的教_raw.jpg",
    "dumps/15031_raw.jpg",
    "dumps/15049_raw.jpg",
    "text_dumps/1397_raw.jpg",
    "dumps4.0_xs/107_2_蕈兽孢子_raw.jpg",

])
