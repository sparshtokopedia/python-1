list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2):
    merged_list = []
    for d in list_1:
        temp_dict = {k: v for k, v in d.items() if v is not None}
        merged_list.append(temp_dict)
    for d in list_2:
        temp_dict = {k: v for k, v in d.items() if v is not None}
        if temp_dict["id"] not in [d["id"] for d in merged_list]:
            merged_list.append(temp_dict)
        else:
            for md in merged_list:
                if md["id"] == temp_dict["id"]:
                    md.update(temp_dict)
    return merged_list





list_3 = merge_lists(list_1, list_2)
print(list_3)
