from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import DepositProducts, DepositOptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.conf import settings
import requests

API_KEY = settings.API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# 정기예금 상품 목록 및 옵션 목록 저장
@api_view(['GET'])
def save_deposit_products(request):
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(BASE_URL, params=params).json()
    response1 = response['result']['baseList']
    response2 = response['result']['optionList']

    for dict in response1:
        deposit_products = DepositProducts()
        deposit_products.fin_prdt_cd = dict['fin_prdt_cd']   # 금융 상품 코드
        deposit_products.kor_co_nm = dict['kor_co_nm']       # 금융 회사명
        deposit_products.fin_prdt_nm = dict['fin_prdt_nm']   # 금융 상품명
        deposit_products.etc_note = dict['etc_note']         # 금융 상품 설명
        deposit_products.join_deny = int(dict['join_deny'])  # 가입 제한 (1: 제한없음, 2:서민전용, 3:일부제한)
        deposit_products.join_member = dict['join_member']   # 가입 대상
        deposit_products.join_way = dict['join_way']         # 가입 방법
        deposit_products.spcl_cnd = dict['spcl_cnd']         # 우대 조건
        deposit_products.save()

    for dict in response2:
        deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=dict['fin_prdt_cd'])
        
        deposit_options = DepositOptions()
        deposit_options.product = deposit_product                       # 외래 키
        deposit_options.fin_prdt_cd  = dict['fin_prdt_cd']              # 금융 상품 코드
        deposit_options.intr_rate_type_nm  = dict['intr_rate_type_nm']  # 저축금리 유형명
        deposit_options.intr_rate = float(dict['intr_rate'])            # 저축금리
        deposit_options.intr_rate2 = float(dict['intr_rate2'])          # 최고우대금리
        deposit_options.save_trm = int(dict['save_trm'])                # 저축기간 (단위: 개월)
        deposit_options.save()

    return JsonResponse({'message': 'okay'})


# GET: 전체 정기예금 상품 목록 반환 / POST: 상품 데이터 저장
@api_view(['GET', 'POST'])
def deposit_products(request):

    if request.method == 'GET':
        deposit_products = get_list_or_404(DepositProducts)
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = { 'message': '이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.' }
        return Response(data)


# 특정 상품의 옵션 리스트 반환
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options =DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
@api_view(['GET'])
def top_rate(request):
    top_option = DepositOptions.objects.order_by('-intr_rate').first()
    product = top_option.product
    options = product.depositoptions_set.all().order_by('-intr_rate')
    product_serializer = DepositProductsSerializer(product)
    options_serializer = DepositOptionsSerializer(options, many=True)
    response_data = {
        'deposit_product': product_serializer.data,
        'options': options_serializer.data
    }
    return Response(response_data)