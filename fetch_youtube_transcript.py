"""
Script sederhana untuk mengambil transcript YouTube.
Cara pakai:
1. pip install youtube-transcript-api
2. Ganti VIDEO_ID di bawah dengan ID video YouTube yang mau diambil
   (ID ada di URL, contoh: youtube.com/watch?v=H2O9Hpaksv8 -> ID-nya "H2O9Hpaksv8")
3. Jalankan: python3 fetch_youtube_transcript.py
4. Transcript akan otomatis disimpan jadi file .md di folder research/youtube-transcripts/
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os

# ====== UBAH BAGIAN INI ======
VIDEO_ID = "QhhbOHi9apM"
VIDEO_TITLE = "Introducing Marketing Against the Grain Podcast"
AUTHOR_NAME = "Kipp Bodnar and Kieran Flanagan"
OUTPUT_FOLDER = "research/youtube-transcripts"
# ==============================

def fetch_and_save():
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(VIDEO_ID)

        full_text = " ".join([snippet.text for snippet in transcript])

        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        filename = f"{AUTHOR_NAME.lower().replace(' ', '-')}-{VIDEO_ID}.md"
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {VIDEO_TITLE}\n\n")
            f.write(f"- Author: {AUTHOR_NAME}\n")
            f.write(f"- Video URL: https://www.youtube.com/watch?v={VIDEO_ID}\n\n")
            f.write("## Transcript\n\n")
            f.write(full_text)

        print(f"Berhasil! Transcript disimpan di: {filepath}")

    except Exception as e:
        print(f"Gagal mengambil transcript: {type(e).__name__} - {e}")
        print("Kemungkinan video tidak punya transcript, atau diblokir YouTube.")

if __name__ == "__main__":
    fetch_and_save()