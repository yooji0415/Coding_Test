# 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

# 배열이 필요한 이유
# 1. 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
# 2. 같은 종류의 데이터를 순차적으로 저장

# 배열의 장점 : 빠른 접근 가능 (인덱스를 통한 접근)
# 배열의 단점 : 데이터가 가변적일 경우 (추가/삭제) 시간이 걸린다 / 길이를 지정해야 한다
# 그런데 배열의 단점을 Python 리스트 타입에서 느끼기 힘들다

# 파이썬과 배열
# 리스트 타입을 사용한다

# 1차원 배열
data = [1, 2, 3, 4, 5]
print(data)

# 2차원 배열
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data)
print(data[0])
print(data[0][0])
print(data[0][1])
print(data[2][0])

# 문제 활용
dataset = ['Braund, Mr. Owen Harris',
           'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
           'Heikkinen, Miss. Laina',
           'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
           'Allen, Mr. William Henry',
           'Moran, Mr. James',
           'McCarthy, Mr. Timothy J',
           'Palsson, Master. Gosta Leonard',
           'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
           'Nasser, Mrs. Nicholas (Adele Achem)',
           'Sandstrom, Miss. Marguerite Rut',
           'Bonnell, Miss. Elizabeth',
           'Saundercock, Mr. William Henry',
           'Andersson, Mr. Anders Johan',
           'Vestrom, Miss. Hulda Amanda Adolfina',
           'Hewlett, Mrs. (Mary D Kingcome) ',
           'Rice, Master. Eugene',
           'Williams, Mr. Charles Eugene',
           'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
           'Masselmani, Mrs. Fatima',
           'Fynney, Mr. Joseph J',
           'Beesley, Mr. Lawrence',
           'McGowan, Miss. Anna "Annie"',
           'Sloper, Mr. William Thompson',
           'Palsson, Miss. Torborg Danira',
           'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
           'Emir, Mr. Farred Chehab',
           'Fortune, Mr. Charles Alexander',
           'Dwyer, Miss. Ellen "Nellie"',
           'Todoroff, Mr. Lalio']

m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1
print(m_count)
