import concurrent.futures
import os
import pprint
import re
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "Arizona State University"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def arizona_state_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=RtyoAMpR_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=DYEmAIfs_v8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=OWxPAeQU__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=sjo3AGg5__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=GoUNAPde__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=TSkCAKlq__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=mk1aAN9-__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Ehw5AJ-K__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=yvk7ABiQ__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=aPI7AFKb__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=pXJAAN2g__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=H_MDADmp__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=16Y0ABGs__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=uLEnAEOv__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=kJp_AKO1__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=bwYBAGy5__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=QM8HAEO7__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ZSxGAGe___8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ROa8AGLC__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=UonlAMXF__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=EnIAAFvJ__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=fvIRAerL__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=JBQBAIjN__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=asAAANHO__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=tBEAAPPP__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=q04BAJjR__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=jabNAfDS__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=YXcGALbV__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=zqyoANXX__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=lyQWAN_Y__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=jQkFAIrZ__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=keVSAG3a__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ffq0ALPb__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=RsAAAOXc__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=d-AOAFre__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Kdq9ACDf__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=VTYCADLg__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=BZ3EADjh__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=nB2EABvi__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=cR24AOri__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=cJsNAHbj__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=JPR9AC3k__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=zkgeABjl__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=mLEvAIDl__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=XlHzAMzl__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=9UsYALzm__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Q48GADzn__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ov8BANPn__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ML8DAEXo__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=vTaFAADp__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=4psRAHLp__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=rDEXAN_p__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=h2cLAC3q__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=QSMCAb3q__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=QxFdADDr__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=rm0cAJ7r__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=oAMZAOjr__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=BNitAD7s__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Ks8HAI3s__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=4HZGAM3s__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=uYSaABHt__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=6viGADjt__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=oOAWAZrt__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=DbcJAATu__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=gScUADbu__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=5Yl5AILu__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=LZhtAMzu__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=xMMCABPv__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Dv4wAI7v__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=fM4AAAjw__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Vs1PACvw__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=aZgfAHPw__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=UOKpAdzw__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=RkhYASPx__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=HeDvAFzx__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=73JuAIHx__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=a90IAbrx__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=i5SdACLy__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=qiCBAGry__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=pTUIAJLy__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=l_3JAOny__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=WMg6AEPz__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=JFccAIzz__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=PwMEAL3z__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Q848AAz0__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=fdrsAHD0__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=l_NmAIr0__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=6fVlAML0__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=KhEEAO30__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=VBdRABr1__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=R4YRAD71__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=fAx0AIL1__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=JgJnALT1__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=cyZJAAT2__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=jklJADD2__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=DlKGAGr2__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=aG_AAKf2__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=YlogAOD2__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=RdBwABf3__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=NEviADn3__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=qRUCAFj3__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=RCg9AHn3__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Ct6ZAJ73__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=2OF2ALv3__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=fkB0Adn3__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=VkgDAAP4__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=4psCAB74__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=LPioAED4__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=YSEAAFv4__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ZmV8AIj4__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=rtspAK34__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=wIugAcX4__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ZSFdAOL4__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=dSHDAAD5__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=vMMhABb5__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=AkhHAD_5__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=cDtDAFT5__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=hLYBAHH5__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=3MUSAJv5__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=HJyNALH5__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=_XU7ANn5__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=rNOfAOr5__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=dl8UAAH6__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=0e7xABT6__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=tOO8AEH6__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=rJkDAFf6__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=pfy9AGf6__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=XxySAHv6__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=x0RnAYv6__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Ex8CAJ36__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Xri8AL76__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=llE0AMn6__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ZPs7ANn6__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=sf0nAPH6__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=62NyAQH7__8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=q71cAAr7__8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=wbyCACv7__8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=7SN-AEP7__8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=_T9MAVL7__8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=kdnVAFf7__8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=gFG9AGL7__8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=dAdkAHb7__8J&astart=1420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=KwqhAIf7__8J&astart=1430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=p6-JAJv7__8J&astart=1440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=z8a4ALT7__8J&astart=1450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=_0bVAMz7__8J&astart=1460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=WwIKANz7__8J&astart=1470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=VR4qAOz7__8J&astart=1480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=CN0PAPj7__8J&astart=1490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=1SMHAAX8__8J&astart=1500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=8It7ABD8__8J&astart=1510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=9LIwARz8__8J&astart=1520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=i_EbACz8__8J&astart=1530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Rt32ADz8__8J&astart=1540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=YQwAAE38__8J&astart=1550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=2nsXAFf8__8J&astart=1560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=K4QUAWL8__8J&astart=1570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=7UEeAHb8__8J&astart=1580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=tdBtAIz8__8J&astart=1590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=tdgNAJ78__8J&astart=1600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=e6HdAKX8__8J&astart=1610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ocIbALT8__8J&astart=1620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=p2emAML8__8J&astart=1630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=_W-BAcr8__8J&astart=1640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=ToNcANb8__8J&astart=1650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=zKF4AOD8__8J&astart=1660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=4hBRAen8__8J&astart=1670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=dHCGAfL8__8J&astart=1680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=nZEnAPn8__8J&astart=1690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=9X18AAH9__8J&astart=1700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=AAUQAAf9__8J&astart=1710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=BeesABP9__8J&astart=1720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=fRP3ABv9__8J&astart=1730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=5QF_ACj9__8J&astart=1740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=MrRSADL9__8J&astart=1750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=2EmpADz9__8J&astart=1760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=W8YQAUL9__8J&astart=1770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=_x0OAE79__8J&astart=1780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=MgWnAFX9__8J&astart=1790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=GXlKAFn9__8J&astart=1800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=lF9ZAWb9__8J&astart=1810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=YByvAG39__8J&astart=1820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=63_cAHn9__8J&astart=1830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=xs0gAIn9__8J&astart=1840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=3199AI_9__8J&astart=1850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=QgIIAJz9__8J&astart=1860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=2AiZAKf9__8J&astart=1870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=smTdALD9__8J&astart=1880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=rKaYAb39__8J&astart=1890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=PESAAMT9__8J&astart=1900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=_zpUAcz9__8J&astart=1910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=zRHvANr9__8J&astart=1920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=Urx7AOH9__8J&astart=1930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=zmc1Aeb9__8J&astart=1940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=UAVTAO_9__8J&astart=1950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=vFoPAPX9__8J&astart=1960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=BpACAfz9__8J&astart=1970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=856495938334247183&after_author=vUl_AAb-__8J&astart=1980',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nArizona State University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    arizona_state_uni()