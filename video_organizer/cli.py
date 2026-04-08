import argparse
import os
import sys

from video_organizer.core.organizer import Organizer

def parse_args():
    parser = argparse.ArgumentParser(
        description="Video Organizer – sorts and moves video files into structured folders."
    )
    parser.add_argument(
        "--src",
        required=True,
        help="Source directory containing the video files to organize.",
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Destination root directory where organized files will be placed.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    src = os.path.abspath(args.src)
    dest = os.path.abspath(args.dest)

    if not os.path.isdir(src):
        print(f"[ERROR] Source path does not exist or is not a directory: {src}")
        return 1

    print(f"Source : {src}")
    print(f"Destination: {dest}")

    organizer = Organizer(src=src, dest=dest)
    organizer.run()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
