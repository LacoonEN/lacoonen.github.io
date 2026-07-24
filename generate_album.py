import os
import json

# 設定你的相簿資料夾路徑與輸出的 JSON 檔名
ALBUM_DIR = './album_photos'
OUTPUT_FILE = './photos.json'

def generate_json():
    photos = []
    # 支援的圖片副檔名
    valid_extensions = ('.jpeg', '.jpg', '.png', '.webp')
    
    # 掃描資料夾
    if os.path.exists(ALBUM_DIR):
        for filename in os.listdir(ALBUM_DIR):
            if filename.lower().endswith(valid_extensions):
                # 將圖片資訊加入列表
                photos.append({
                    "src": f"{ALBUM_DIR}/{filename}",
                    "alt": filename.split('.')[0]
                })
    
    # 將清單寫入 JSON 檔案
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(photos, f, ensure_ascii=False, indent=4)
    print(f"✅ 成功生成相簿索引：共 {len(photos)} 張照片")

if __name__ == '__main__':
    generate_json()
