@echo off
chcp 65001 > nul

echo "正在切割喵~"
.\venv_audio_slicer\Scripts\python .\audio-slicer.py --output output --input input 10

echo "切割完成...请查看output文件夹..."
pause > nul