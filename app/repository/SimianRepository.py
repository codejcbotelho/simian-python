from app.service.DynamoService import DynamoService
from app.helper.Helper import Helper
from app.enum.TypeDNA import TypeDNA

from flask import g

import os


class SimianRepository(object):

    @staticmethod
    def put_simian(dna: str, type_dna: str):
        partition_key = Helper.generate_partition_key(dna)
        table = DynamoService.table('simian')
        response = table.put_item(
            Item={
                'dna': partition_key,
                'type': str(type_dna)
            }
        )
        #return response

    @staticmethod
    def get_stats():
        stats = {'count_mutant_dna': 0, 'count_human_dna': 0, 'ratio': 0.0}
        table = DynamoService.table('simian')
        response = table.scan()
        print('> response get_stats() >>', response)
        items = response['Items']

        for item in items:
            if item['type'] == TypeDNA.SIMIAN.value:
                stats['count_mutant_dna'] += 1
            elif item['type'] == TypeDNA.HUMAN.value:
                stats['count_human_dna'] += 1

        if stats['count_mutant_dna'] > 0 and stats['count_human_dna'] > 0:
            stats['ratio'] = round(stats['count_mutant_dna'] / stats['count_human_dna'], 2)
        elif stats['count_mutant_dna'] == 0 and stats['count_human_dna'] > 0:
            stats['ratio'] = stats['count_human_dna']
        elif stats['count_human_dna'] == 0 and stats['count_mutant_dna'] > 0:
            stats['ratio'] = stats['count_mutant_dna']

        return stats
