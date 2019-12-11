class Helper(object):

    @staticmethod
    def generate_partition_key(dna: str) -> str:
        return ':'.join(dna)
