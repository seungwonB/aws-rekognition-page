# 프로젝트 명
<h3> ✔️From the Picture✔️ </h3>
<br/>

# 프로젝트 멤버
- 방승원(팀장) : 웹 사이트 제작(Front, Back) 및 배포(AWS), 생성한 API를 서버에서 받고 반환, AWS Polly를 활용하여 웹상에서 음성 즉각 출력, Github 관리, PPT 제작
- 이영빈(팀원) : AWS Rekognition 활용(S3버킷에 저장된 이미지 활용-인물 분석, 유명 인사 탐지, 글자 추출, 응답을 문장으로 재구성), AWS Translate 활용(유명 인사 한글로 번역), 보고서 작성
<br/>

# 프로젝트 소개
- 저시력자들, 시각장애인 분들을 위해 <b>사진을 설명</b>해주는 프로그램이다. <br>
이미지에서 <b>인물을 분석</b>하여 또는 <b>글자를 추출</b>하여 <b>음성으로 출력</b>한다. 드라마 '스타트업'에서 영감을 얻어 시작하였다.
<br/>

# 개발 내용
- 사용자가 웹상에서 사진을 찍으면 그 사진을 S3의 bucket에 올린다. 사진을 Rekognition을 이용하여 분석한다.
- 그 후 Polly를 사용하여 웹상에서 음성을 출력해준다.
- JS와 Flask로 웹페이지를 제작하였다. 
- AWS EC2를 이용하여 배포를 하였다. (FileZila와 Git bash 활용)
- AWS의 Machine Learning 서비스인 Rekognition을 활용하였다. 
- Python의 boto3를 이용하여 Rekognition을 구현하였다. 
- 영어 번역을 위해서는 Translate을 사용하였다.
- Rekognition을 활용하여 얻은 Response를 문장으로 재조합하였다.
- 그렇게 생긴 문장을 서버에서 받아 웹에 반환해주었다. 반환받은 문장은 웹에서 바로 AWS Polly를 활용하여 음성으로 추출되었다.
<br/> 

# 프로젝트 개발 결과물 소개 (+ 다이어그램)
<img src="https://user-images.githubusercontent.com/73030613/144747169-b0bf9950-1f03-4792-9dbf-0b353ba09978.png" />
<br/>

# 개발 결과물을 사용하는 방법 소개
- 초기화면에서 음성으로 안내가 나온다.
- 사진을 촬영하고 인물, 글자 버튼 중 하나를 누르면 된다.
- 잠시 기다리면 텍스트와 함께 음성이 출력된다.
- 연예인을 정확히 인식하고 인물을 분석해주었다.
<img src="https://user-images.githubusercontent.com/73030613/144747467-45ff1845-221b-4a56-b9bc-c0137fc12283.gif" />

- 일반인도 닮은 유명인사가 출력되고 안경 쓴 디테일까지 잡아준다.
<img width="250px" src="https://user-images.githubusercontent.com/73030613/144747534-f472a1db-4c05-4144-91dd-243d7c5bf775.png" />

- 다수의 인물도 분석해준다.
<img width="250px" src="https://user-images.githubusercontent.com/73030613/144747601-d748dbf3-c2fc-409c-8242-ecfd1c58f52e.png" />

- 이미지에서 텍스트를 추출한다.
<img width="250px" src="https://user-images.githubusercontent.com/73030613/144747628-ae891052-a9e8-4ebb-9bf9-c766ef4b76a5.png" />
<br/>

# 개발 결과물의 필요성 및 활용방안
- 저시력자, 시각장애인들이 보지 못하거나 보기 힘든 세상을 조금이나마 볼 수 있게 도와준다. 때문에 그들에게 소소한 즐거움이나 도움이 될 것이다.
- 현재 개발 결과물은 그래도 버튼을 보고 눌러야하기 때문에 시력이 아예 없으신 분들은 이용하기가 힘들다. 그들의 몸에 소형카메라를 부착하여 실시간으로 앞의 영상을 몇 초 단위로 이미지로 전달한 후 이어폰을 통해 음성으로 인식하는 방법도 있을 것이다. 또한 음성인식 API를 이용하여 '사진 찍어줘'와 같이 그들이 보면서 클릭하지 않아도 사용할 수 있는 방법들도 후에 개발해보면 더욱 많은 사용자들이 이용할 수 있을 것이다.

<h3>AWS Detail 설정 정리</h3>
https://velog.io/@swbang/AWS-s3-bucket에-이미지-올리기
<br/>
https://velog.io/@swbang/AWS-Polly
<br/>
https://velog.io/@swbang/AWS-EC2를-이용한-웹사이트-배포
