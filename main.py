from diskinfo import DiskInfo
import json


def get_disk_info():
    disk_info = DiskInfo()

    result = []
    for disk in disk_info.get_disk_list():
        result.append({key.replace('_Disk__', ''): value for key, value in disk.__dict__.items() })

    result_json = json.dumps(
        obj=result,
        indent=4
    )

    with open('result.json', "w", encoding="utf-8") as fw:
        fw.write(result_json)



if __name__ == "__main__":
    get_disk_info()