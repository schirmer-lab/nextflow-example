#! /usr/bin/env python

import sys


def clean_script(html_file_path: str, output_file_path: str) -> None:
    current_line = ""
    in_scene = False
    with open(output_file_path,'w') as output_file:
        with open(html_file_path, 'r') as html_file:
            for line in html_file.readlines():
                line = line.strip()
                if line.startswith("<H4>Scene"):
                    in_scene=True
                    #write the current line if it is not empty
                    if current_line: output_file.write(f"{current_line}\n--\n")
                    current_line=""
                elif in_scene:
                    if line.startswith("<"):
                        continue
                    #check for new line
                    elif ':' in line:
                        if current_line: output_file.write(f"{current_line}\n")
                        current_line=f" {line}"
                    else:
                        current_line+=f" {line}"
        if current_line: output_file.write(f"{current_line}\n")



if __name__ == "__main__":
    clean_script(sys.argv[1], sys.argv[2])
