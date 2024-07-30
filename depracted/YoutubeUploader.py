from youtube_uploader_selenium import YouTubeUploader


video_path = 'YoutubeShorts/videos/film.mp4'



uploader = YouTubeUploader(video_path)
was_video_uploaded, video_id = uploader.upload()
assert was_video_uploaded