from diskinfo import DiskInfo
import json


def get_disk_info():
    result = [
        {key.replace('_Disk__', ''): value for key, value in disk.__dict__.items() }
        for disk in DiskInfo().get_disk_list()
    ]
    result_json = json.dumps(
        obj=result,
        indent=4
    )

    with open('result.json', "w", encoding="utf-8") as fw:
        fw.write(result_json)



if __name__ == "__main__":
    get_disk_info()