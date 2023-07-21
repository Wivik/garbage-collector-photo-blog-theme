#!/usr/bin/env python3

import os
import argparse
import subprocess
import glob

# Setup argument parser
parser = argparse.ArgumentParser(description="Add a new album to the gallery")
parser.add_argument("album", help="Name of the album")
parser.add_argument("-t", "--tags", help="Tags for the album, comma-separated. Example : -t \"tag1,tag2,tag3\"", default="")

args = parser.parse_args()

album = args.album
tags = args.tags

# Define directories
assets_dir = os.path.join("assets", album)
content_dir = os.path.join("content", album)

# Run hugo new command
env_vars = os.environ.copy()
env_vars["HUGO_TAGS"] = tags
subprocess.run(["hugo", "new", os.path.join(content_dir, "_index.md")], check=True, env=env_vars)

# Counter for hugo weight
counter = 1

# Iterate over jpg files in assets_dir
for filename in sorted(glob.glob(os.path.join(assets_dir, "*.jpg"))):
    # Remove directory and extension from filename
    base_name = os.path.basename(filename)
    name_without_ext = os.path.splitext(base_name)[0]

    # Setup environment variables
    env_vars = os.environ.copy()
    env_vars["HUGO_PHOTO_PAGE"] = os.path.join(album, f"{name_without_ext}.jpg")
    env_vars["HUGO_WEIGHT"] = str(counter)

    # Run hugo new command for each photo
    subprocess.run(["hugo", "new", os.path.join(content_dir, f"{name_without_ext.lower()}.md"), "--kind", "photo"], check=True, env=env_vars)

    counter += 1
