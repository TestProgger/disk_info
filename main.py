from diskinfo import DiskInfo
import json


def get_disk_info():
    with open('result.json', "w", encoding="utf-8") as fw:
        fw.write(
            json.dumps(
                obj=[
                    {key.replace('_Disk__', ''): value for key, value in disk.__dict__.items()}
                    for disk in DiskInfo().get_disk_list()
                ],
                indent=4
            )
        )


if __name__ == "__main__":
    get_disk_info()
