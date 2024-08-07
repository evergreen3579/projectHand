from flask import Blueprint, render_template, request
import requests

# 블루프린트 생성
maps_bp = Blueprint('maps', __name__)

client_id = "0eons4vk5g"  # 네이버 지도 API 클라이언트 ID
client_secret = "uGSGQw715PW5xBJaHsvACqdR3jYv1ChEqxLCqfEg"  # 네이버 지도 API 클라이언트 시크릿 (여기에 입력)

# 지도 페이지 및 검색 기능
@maps_bp.route('/maps', methods=['GET', 'POST'])
def maps():
    lat = None
    lng = None
    address = None
    
    if request.method == 'POST':
        search_query = request.form.get('search_query')

        # 네이버 지도 API 요청 URL
        url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

        # API 요청 헤더 설정
        headers = {
            'X-NCP-APIGW-API-KEY-ID': client_id,
            'X-NCP-APIGW-API-KEY': client_secret,
        }

        # 요청 파라미터 설정
        params = {'query': search_query}

        # 요청 보내기
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            json_data = response.json()
            if json_data['addresses']:
                location = json_data['addresses'][0]
                lat = location.get('y')
                lng = location.get('x')
                address = location.get('roadAddress', location.get('jibunAddress'))

    return render_template('maps.html', lat=lat, lng=lng, address=address)
