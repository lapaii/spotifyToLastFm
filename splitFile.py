import json

with open('data.json', encoding='utf-8') as file:
    jsonVer = json.load(file)
    splitSize = 2800
    totalFiles = (len(jsonVer) // splitSize) + 1

    print(f"splitting {len(jsonVer)} objects into {totalFiles} files of {splitSize} objects each...")

    for x in range(totalFiles):
        json.dump(jsonVer[x * splitSize:(x + 1) * splitSize], open(f"blocks/block-{str(x+1)}.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=True)
