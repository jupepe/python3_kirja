# Tiedoston päivittäminen

import datetime


def write_to_file(fname, lines):
    print(f"Kirjoitetaan '{str(lines[1][0])}' jne. txt-tiedostoon '{fname}'")
    with open(fname, 'a+') as f:
        for line in lines:
            current_tstamp = datetime.datetime.now()
            wr_line = f'{current_tstamp};{"--".join(line)}\n'
            if "Login email--" in wr_line:
                continue
            f.write(wr_line)


def read_all_lines(fname):
    rows = []
    with open(fname) as f:
        lines = f.readlines()
    for line in lines:
        arr = line.rstrip().split(";")
        rows.append(arr)
    return rows


file_name = "files/email.csv"
output_fn = "files/output_log.txt"
all_lines = read_all_lines(file_name)
write_to_file(output_fn, all_lines)
