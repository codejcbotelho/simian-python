from app.service.DynamoService import DynamoService
from app.helper.Helper import Helper
from app.enum.TypeDNA import TypeDNA

from flask import g

import os


class SimianRepository(object):

    @staticmethod
    def put_simian(dna: str, type_dna: str):
        partition_key = Helper.generate_partition_key(dna)
        response = g.table.put_item(
            Item={
                'dna': partition_key,
                'type': str(type_dna)
            }
        )
        print('>> response', response)

    @staticmethod
    def get_stats():
        stats = {'count_mutant_dna': 0, 'count_human_dna': 0, 'ratio': 0.0}
        response = g.table.scan()
        items = response['Items']

        for item in items:
            if item['type'] == '1':
                stats['count_mutant_dna'] += 1
            elif item['type'] == '0':
                stats['count_human_dna'] += 1

        if stats['count_mutant_dna'] > 0 and stats['count_human_dna'] > 0:
            stats['ratio'] = round(stats['count_mutant_dna'] / stats['count_human_dna'], 2)
        elif stats['count_mutant_dna'] == 0 and stats['count_human_dna'] > 0:
            stats['ratio'] = stats['count_human_dna']
        elif stats['count_human_dna'] == 0 and stats['count_mutant_dna'] > 0:
            stats['ratio'] = stats['count_mutant_dna']

        return stats
