from mount10 import Mount10
from qrypt import Qrypt
import os


class SQlient:
    def __init__(self, name, server_ip, server_access_key, server_secret_key):
        self.name = name
        self.buckets = [f"bucket-1-{name}"]
        self.mount10 = Mount10(self.name, server_ip, server_access_key, server_secret_key)

        home_dir = os.getenv("HOME")
        self.local_synergy_dir = f"{home_dir}/synergy-quantum"
        self.local_user_dir = f"{self.local_synergy_dir}/{self.name}"
        if not os.path.exists(self.local_synergy_dir):
            os.mkdir(self.local_synergy_dir)
        if not os.path.exists(self.local_user_dir):
            os.mkdir(self.local_user_dir)

        self.key_path = f"{self.local_user_dir}/{self.name}.key"
        if not os.path.exists(self.key_path):
            self.key = Qrypt.generate_key()
            Qrypt.save_key(self.key, self.key_path)
        else:
            self.key = Qrypt.load_key(self.key_path)

        self.qrypt = Qrypt(self.key)

        for bucket in self.buckets:
            try:
                self.mount10.create_bucket(bucket)
            except Exception as err:
                print(err)
