---
{{ $photo := getenv "HUGO_PHOTO_PAGE" }}
{{ $weight := getenv "HUGO_WEIGHT" }}
photo: "{{ $photo }}"
weight: {{ $weight }}
draft: false
## Optional additional meta info for resources list
#  alt: Image alternative and screen-reader text
#  title: A title for the photo, will be displayed in the album if set
#  description: A sub-title or description for the photo (makdown supported)
#  albumdisplay: Align the album thumbnail according to the CSS background-position property (default is middle)
#  linebreak: true/false, break the album with a new line. If a description is provided in this photo, it will be displayed in the album (default : false)
---
