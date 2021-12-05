import boto3

# bucket = 'seungwonbucket1'
# name = 'english.png'

def text_extract(bucket : str, name : str, region="ap-northeast-2"):   #이미지 속 텍스트 추출
    client = boto3.client('rekognition', region)
    response = client.detect_text(Image = {'S3Object':{'Bucket':bucket,'Name':name}})
    str = ''
    for i in range(len(response['TextDetections'])):
        if response['TextDetections'][i]['Type'] == 'WORD':   #Type 이 WORD인 것만
            if response['TextDetections'][i]['Confidence'] > 85:   #정확도가 85 초과인 것들만 저장
                str += response['TextDetections'][i]['DetectedText'] + ' '
    return str


# text = text_extract(bucket,name)
#
# print(text)