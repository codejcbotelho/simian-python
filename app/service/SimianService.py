import os
import re
import settings

from app.repository.SimianRepository import SimianRepository
from app.enum.TypeDNA import TypeDNA


class SimianService(object):

    def __init__(self, dna: str):
        self.__dna = dna
        self.__sequences = []
        self.__limit_char = 0
        self.__simian_repository = SimianRepository()

    def is_simian(self) -> bool:
        er_dna_default = r'^[ATCG]{1,}$'
        er_sequence_line = r'[A]{4,}|[T]{4,}|[C]{4,}|[G]{4,}'

        self.__generate_sequence()

        if len(self.__dna) > 0:
            for cell in self.__dna:
                if self.__limit_char == 0 or len(cell) > self.__limit_char:
                    self.__limit_char = len(cell)
                if re.match(er_dna_default, cell):
                    self.__sequences.append(cell)
                else:
                    return False

        simians_list = list(filter(re.compile(er_sequence_line).match, self.__sequences))
        if len(simians_list) > 1:
            self.__simian_repository.put_simian(self.__dna, TypeDNA.SIMIAN.value)
            return True
        else:
            self.__simian_repository.put_simian(self.__dna, TypeDNA.HUMAN.value)
            return False

    def __generate_sequence(self):

        sequence = []
        diagonal1 = []
        diagonal2 = [''] * self.__limit_char

        # vertical values
        for i, f in enumerate(self.__dna):
            for ix, ch in enumerate(f):
                # vertical values
                try:
                    sequence[ix] += str(ch)
                except IndexError:
                    sequence.append(ch)

                # diagonal values 1
                try:
                    diagonal1[ix + i] += str(ch)
                except IndexError:
                    diagonal1.append(ch)

                # diagonal values 2
                try:
                    diagonal2[len(f) + ix - i] += str(ch)
                except IndexError:
                    diagonal2.append(ch)

        self.__sequences += sequence
        self.__sequences += diagonal1
        self.__sequences += diagonal2
