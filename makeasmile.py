
def makeasmile(smilename: str, smilepic: str):
    with open("HTML_pages/welcome.html", "r", encoding="utf-8") as file:
        lines = file.read().split("\n")
        for l in lines:
            if "<span id=\"icon\"" in l:
                optionline = lines.index(l)
        for string in lines:
            if f'<option value="{smilename}">' in string:
                print(f"Smile {smilename} already exists.")
                return
            elif "let formattedElement =" in string:
                replaceline = lines.index(string) + 1
                break
        print(f"replaceline: {replaceline}")
    lines[optionline + 1] += f'\n            <span aria-valuenow="{smilename}">{smilepic}</span>'
    lines[replaceline - 1] += f'.replace(/{smilename}/g, "{smilepic}")'
    with open("HTML_pages/welcome.html", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
