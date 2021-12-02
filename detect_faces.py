import boto3
from collections import Counter

# bucket = 'seungwonbucket1'
# name = 'actor.jpg'


def photo_analysis(bucket, name, region="ap-northeast-2"):
    s3 = boto3.resource('s3',
                        aws_access_key_id='AKIA57X6PIL2LKEGNZRM',
                        aws_secret_access_key='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')
    client = boto3.client('rekognition', region)
    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': name}}, Attributes=['ALL'])

    age_list = []
    gender_list = []
    emotion_list = []
    num_humans = 0
    out = ''
    for i in range(len(response['FaceDetails'])):
        low = response['FaceDetails'][i]['AgeRange']['Low']
        high = response['FaceDetails'][i]['AgeRange']['High']  # 나이 최소, 최대값 저장
        age = (low + high) / 2  # 최소, 최대값의 중간값을 저장
        age_list.append(int(age))  # age 리스트에 중간값을 저장
        gender_list.append(response['FaceDetails'][i]['Gender']['Value'])  # 각 인물 별 성을 저장

        if gender_list[i] == 'Male':
            gender_list[i] = '남자'
        elif gender_list[i] == 'Female':
            gender_list[i] = '여자'  # 영어 -> 한국어

        emo_conf = []
        for j in range(len(response['FaceDetails'][i]['Emotions'])):
            emo_conf.append(response['FaceDetails'][i]['Emotions'][j]['Confidence'])  # 8개의 감정의 Confidence값 저장

        max_index = emo_conf.index(max(emo_conf))
        emotion_list.append(
            response['FaceDetails'][i]['Emotions'][max_index]['Type'])  # 각 사람 별로 Confidence값이 가장 높은 감정을 리스트에 저장

        if emotion_list[i] == 'HAPPY':
            emotion_list[i] = '행복한'
        elif emotion_list[i] == 'SURPRISED':
            emotion_list[i] = '놀란'
        elif emotion_list[i] == 'ANGRY':
            emotion_list[i] = '화난'
        elif emotion_list[i] == 'FEAR':
            emotion_list[i] = '두려운'
        elif emotion_list[i] == 'CONFUSED':
            emotion_list[i] = '혼란스러운'
        elif emotion_list[i] == 'DISGUSTED':
            emotion_list[i] = '역겨운'
        elif emotion_list[i] == 'SAD':
            emotion_list[i] = '슬픈'
        elif emotion_list[i] == 'CALM':
            emotion_list[i] = '침착한'  # 영어 -> 한국어

        num_humans = len(response['FaceDetails'])  # 사진 속 인물의 숫자

    # print(emotion_list)
    # print(gender_list)
    # print(age_list)
    if num_humans == 1:  # 사진 속 인물이 1명일 때
        out = "약 " + str(age_list[0]) + "살 처럼 보이는 한명의 " + gender_list[0] + "가 " + emotion_list[0] + " 표정을 짓고 있습니다 "
    elif num_humans > 1:
        gender_set = set(gender_list)
        gender_list = list(gender_set)  # 중복 제거

        emotion_set = set(emotion_list)
        emotion_list_ded = list(emotion_set)  # 중복 제거

        if len(gender_list) == 2:
            genders = '남녀'
        elif len(gender_list) == 1:
            genders = gender_list[0]

        if len(emotion_list_ded) == 1:
            emotions = emotion_list[0]
            out = str(num_humans) + "명의 " + genders + "들이 " + emotions + " 표정을 짓고 있습니다."
            print(out)
            exit(0)

        counter = Counter(emotion_list)
        print(counter[0])

        out = str(num_humans) + "명의 " + genders + "들이 있습니다."
        # return out
    # print(out)
    return out

# photo_analysis(bucket,name)
