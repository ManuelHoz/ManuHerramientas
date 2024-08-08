import os
from moviepy.editor import AudioFileClip, ColorClip

def audio_to_video(audio_file, output_dir):
    try:
        print(f"Processing file: {audio_file}")
        audio = AudioFileClip(audio_file)
        duration = audio.duration
        max_duration = 20 * 60  # 20 minutes in seconds

        if duration > max_duration:
            parts = int(duration // max_duration) + 1
            for part in range(parts):
                start_time = part * max_duration
                end_time = min((part + 1) * max_duration, duration)
                audio_part = audio.subclip(start_time, end_time)
                
                video = ColorClip(size=(640, 480), color=(0, 0, 0), duration=(end_time - start_time))
                video = video.set_audio(audio_part)

                output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(audio_file))[0]}_part{part + 1}.mp4")
                video.write_videofile(output_file, codec='libx264', fps=24)
                
                print(f"Created video part {part + 1} for {audio_file} at {output_file}")
        else:
            video = ColorClip(size=(640, 480), color=(0, 0, 0), duration=duration)
            video = video.set_audio(audio)

            output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_file))[0] + '.mp4')
            video.write_videofile(output_file, codec='libx264', fps=24)

            print(f"Created video for {audio_file} at {output_file}")

    except Exception as e:
        print(f"Failed to process {audio_file}: {e}")

def process_all_audios_in_directory(directory):
    try:
        print(f"Directory: {directory}")
        for filename in os.listdir(directory):
            print(f"Found file: {filename}")
            if filename.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a')):
                audio_path = os.path.join(directory, filename)
                audio_to_video(audio_path, directory)
            else:
                print(f"Skipped file: {filename} (not an audio file)")
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")

if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the current script
    print(f"Script directory: {directory}")
    process_all_audios_in_directory(directory)
