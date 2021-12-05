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
- 사용자가 웹상에서 사진을 찍으면 그 사진을 S3에 bucket에 올린다. 사진을 Rekognition을 이용하여 분석한 후 Polly를 사용하여 웹상에서 출력해준다.
- JS와 Flask로 웹페이지를 제작하였다. AWS EC2를 이용하여 배포를 하였다. (FileZila와 Git bash 활용)
- AWS의 Machine Learning 서비스인 Rekognition을 활용하였다. Python의 boto3를 이용하여 구현하였다. 영어 번역을 위해서는 Translate을 사용하였다.
- Rekognition을 활용하여 얻은 Request를 문장으로 재조합하였다.
- 그렇게 생긴 문장을 서버에서 받아 웹에 반환해주었다. 반환받은 문장은 웹에서 바로 AWS Polly를 활용하여 음성으로 추출되었다.
<br/> 

# 프로젝트 개발 결과물 소개 (+ 다이어그램)
<img src="https://user-images.githubusercontent.com/73030613/144747169-b0bf9950-1f03-4792-9dbf-0b353ba09978.png" />
<br/>

# 개발 결과물을 사용하는 방법 소개


# 개발 결과물의 필요성 및 활용방안
