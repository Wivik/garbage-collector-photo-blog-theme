---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
photo: "default.png"
draft: false
## Optional additional meta info for resources list
#  description: A sub-title or description for the photo
tags:
  - Album
{{- with getenv "HUGO_TAGS" }}
{{- range split . "," }}
  - {{ . }}
{{- end }}
{{- end }}
---


