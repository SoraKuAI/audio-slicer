import os
from pydub import AudioSegment

def delete_long_audio_files(folder_path, max_duration=20,min_duration=5):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.wav'):
                audio = AudioSegment.from_wav(file_path)
                duration = len(audio) / 1000 
                if duration > max_duration:
                    os.remove(file_path)
                    print(f"删除过长文件 {file_path}")
                elif duration < min_duration:
                    os.remove(file_path)
                    print(f"删除过短文件 {file_path}")

delete_long_audio_files('output', max_duration=20,min_duration=3)
