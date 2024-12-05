import serial
import numpy as np
from PIL import Image

# 시리얼 포트 열기
ser = serial.Serial("COM8", 1000000)

# 이미지 데이터 크기
expected_data_size = 320 * 240  # 76800 bytes

# 데이터를 받을 리스트
image_data = bytearray()

# 데이터 수신 및 처리
while len(image_data) < expected_data_size:
    data = ser.read(expected_data_size - len(image_data))  # 필요한 만큼 데이터 읽기
    image_data.extend(data)

# 수신된 데이터가 예상 크기와 일치하는지 확인
if len(image_data) != expected_data_size:
    print(f"Error: Data size {len(image_data)} is not the expected {expected_data_size}.")
else:
    # raw_data를 numpy 배열로 변환
    img = np.frombuffer(image_data, dtype=np.uint8).reshape(240, 320)

    # 이미지로 변환
    image = Image.fromarray(img)
    image.save("output_image.png")
    print("Image saved successfully.")
