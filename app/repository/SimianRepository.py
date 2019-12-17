import boto3

from app.helper.Helper import Helper
from app.enum.TypeDNA import TypeDNA


class SimianRepository(object):
    resource = boto3.resource(
        'dynamodb',
        region_name="us-east-1"
    )
    table = resource.Table('simian')

    @staticmethod
    def put_simian(dna: str, type_dna: str):
        partition_key = Helper.generate_partition_key(dna)
        response = SimianRepository.table.put_item(
            Item={
                'dna': partition_key,
                'type': str(type_dna)
            }
        )
        return response

    @staticmethod
    def get_stats():
        stats = {'count_mutant_dna': 0, 'count_human_dna': 0, 'ratio': 0.0}
        response = SimianRepository.table.scan()
        items = response['Items']

        for item in items:
            if type(item['type']).__name__ == 'str':
                item_type = item['type']
            else:
                item_type = item['type']['S']

            if item_type == str(TypeDNA.SIMIAN.value):
                stats['count_mutant_dna'] += 1
            elif item_type == str(TypeDNA.HUMAN.value):
                stats['count_human_dna'] += 1

        if stats['count_mutant_dna'] > 0 and stats['count_human_dna'] > 0:
            stats['ratio'] = round(stats['count_mutant_dna'] / stats['count_human_dna'], 2)
        elif stats['count_mutant_dna'] == 0 and stats['count_human_dna'] > 0:
            stats['ratio'] = stats['count_human_dna']
        elif stats['count_human_dna'] == 0 and stats['count_mutant_dna'] > 0:
            stats['ratio'] = stats['count_mutant_dna']

        return stats
