from sqlient import SQlient


class SQCLI:
    def __init__(self):
        pass


if __name__ == '__main__':
    client_michal = SQlient("michal", "3.121.232.99:9000", "minioadmin", "minioadmin")
    #TODO do the enc while uploading
    client_michal.qrypt.encrypt_file("data/file1.txt")

    client_michal.mount10.put_object(client_michal.buckets[0], "file1", "data/file1.txt")
    client_michal.mount10.get_object(client_michal.buckets[0], "file1", "data/file2")

    client_michal.qrypt.decrypt_file("data/file2")
    print("*******************")
    data = client_michal.qrypt.decrypt_file("data/file1.txt")
    print(open("data/file2").read().encode())
    assert data == open("data/file2").read().encode()



"""
-> Clean up interfaces 
-> decouple encryption decryption and agree on expose hooks
-> 
"""