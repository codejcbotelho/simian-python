import hashlib


class Helper(object):

    @staticmethod
    def generate_partition_key(dna: str) -> str:
        h = hashlib.sha1()
        h.update(":".join(dna).encode('utf-8'))
        return h.hexdigest()
